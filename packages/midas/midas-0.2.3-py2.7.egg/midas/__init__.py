#!/usr/bin/python
"""
A Python driver for Honeywell's Midas gas detector, using TCP/IP modbus.

Distributed under the GNU General Public License v2
Copyright (C) 2015 NuMat Technologies
"""
import csv
import os
from struct import pack
import logging

from pymodbus.client.async import ModbusClientProtocol
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder

from twisted.internet import reactor, protocol

# Map register bits to sensor states
# Further information can be found in the Honeywell Midas technical manual
alarm_level_options = ['none', 'low', 'high']
concentration_unit_options = ['ppm', 'ppb', '% volume', '% LEL', 'mA']
monitor_state_options = ['Warmup',
                         'Monitoring',
                         'Monitoring with alarms inhibited',
                         'Monitoring with alarms and faults inhibited',
                         'Monitoring every response inhibited',
                         'Alarm or fault simulation',
                         'Bump test mode',
                         '4-20 mA loop calibration mode',
                         'Non-analog calibration mode']
fault_status_options = ['No fault',
                        'Maintenance fault',
                        'Instrument fault',
                        'Maintenance and instrument faults']

root = os.path.normpath(os.path.dirname(__file__))
with open(os.path.join(root, 'faults.csv')) as in_file:
    reader = csv.reader(in_file)
    next(reader)
    faults = {row[0]: {'description': row[1], 'condition': row[2],
                       'recovery': row[3]} for row in reader}


class GasDetector(object):
    """Python driver for [Honeywell Midas Gas Detector](http://www.honeywell
    analytics.com/en/products/Midas).

    This driver uses twisted to asynchronously read from the sensor. The `get`
    method supports a `callback` argument. When specified, it is called when
    the device response comes through. If unspecified, this class blocks until
    a response is received.
    """
    def __init__(self, address):
        """Connects to modbus on initialization."""
        self.client = None
        self.ip = address
        self._connect()

    def get(self, callback=None, *args, **kwargs):
        """Returns the current state through Modbus TCP/IP."""
        if callback:
            if self.client is None:
                callback(self._on_error("Not connected"), *args, **kwargs)
            else:
                d = self.client.read_holding_registers(address=0, count=16)
                d.addCallbacks(self._process, self._on_error)
                d.addCallbacks(lambda r: callback(r, *args, **kwargs))
        else:
            try:
                with ModbusTcpClient(self.ip) as client:
                    res = client.read_holding_registers(address=0, count=16)
                return self._process(res)
            except Exception as e:
                return self._on_error(e)

    def _connect(self):
        """Initializes modbus connection through twisted framework."""
        deferred = protocol.ClientCreator(reactor, ModbusClientProtocol
                                          ).connectTCP(self.ip, 502)
        deferred.addCallbacks(self._on_connection, self._on_error)

    def _on_connection(self, client):
        """Saves reference to client on connection."""
        self.client = client

    def _on_error(self, error):
        logging.log(logging.ERROR, error)
        self._connect()
        return {'ip': self.ip, 'connected': False}

    def _process(self, response):
        """Parses the response, returning a dictionary."""
        result = {'ip': self.ip, 'connected': True}

        register_bytes = ''.join(pack('<H', x) for x in response.registers)
        decoder = BinaryPayloadDecoder(register_bytes)

        # Register 40001 is a collection of alarm status signals
        reg_40001 = decoder.decode_bits() + decoder.decode_bits()
        # Bits 0-3 map to the monitor state
        monitor_integer = sum(1 << i for i, b in enumerate(reg_40001[:4]) if b)
        result['state'] = monitor_state_options[monitor_integer]
        # Bits 4-5 map to fault status
        fault_integer = sum(1 << i for i, b in enumerate(reg_40001[4:6]) if b)
        result['fault'] = {'status': fault_status_options[fault_integer]}
        # Bits 6 and 7 tell if low and high alarms are active
        low, high = reg_40001[6:8]
        result['alarm'] = alarm_level_options[low + high]
        # Bits 8-10 tell if internal sensor relays 1-3 are energized. Skipping.
        # Bit 11 is a heartbeat bit that toggles every two seconds. Skipping.
        # Bit 12 tells if relays are under modbus control. Skipping.
        # Remaining bits are empty. Skipping.

        # Register 40002 has a gas ID and a sensor cartridge ID. Skipping.
        decoder._pointer += 2

        # Registers 40003-40004 are the gas concentration as a float
        result['concentration'] = decoder.decode_32bit_float()

        # Register 40005 is the concentration as an int. Skipping.
        decoder._pointer += 2

        # Register 40006 is the number of the most important fault.
        fault_number = decoder.decode_16bit_uint()
        if fault_number != 0:
            code = ('m' if fault_number < 30 else 'F') + str(fault_number)
            result['fault']['code'] = code
            result['fault'].update(faults[code])

        # Register 40007 has info related to 40005 in the first byte. Skipping.
        decoder._pointer += 1

        # Register 40007 holds the concentration unit in the second byte
        # Instead of being an int, it's the position of the up bit
        unit_bit = decoder.decode_bits().index(True)
        result['units'] = concentration_unit_options[unit_bit]

        # Register 40008 holds the sensor temperature in Celsius
        result['temperature'] = decoder.decode_16bit_int()

        # Register 40009 holds number of hours remaining in cell life
        result['life'] = decoder.decode_16bit_uint() / 24.0

        # Register 40010 holds the number of heartbeats (16 LSB). Skipping.
        decoder._pointer += 2

        # Register 40011 is the sample flow rate in cc / min
        result['flow'] = decoder.decode_16bit_uint()

        # Register 40012 is blank. Skipping.
        decoder._pointer += 2

        # Registers 40013-40016 are the alarm concentration thresholds
        result['low-alarm threshold'] = decoder.decode_32bit_float()
        result['high-alarm threshold'] = decoder.decode_32bit_float()

        # Despite what the manual says, thresholds are always reported in ppm.
        # Let's fix that to match the concentration units.
        if result['units'] == 'ppb':
            result['concentration'] *= 1000
            result['low-alarm threshold'] *= 1000
            result['high-alarm threshold'] *= 1000

        return result


def command_line():
    import argparse
    import json
    from time import time

    parser = argparse.ArgumentParser(description="Read a Honeywell Midas gas "
                                     "detector state from the command line.")
    parser.add_argument('address', help="The IP address of the gas detector.")
    parser.add_argument('--stream', '-s', action='store_true',
                        help="Sends a constant stream of detector data, "
                             "formatted as a tab-separated table.")
    args = parser.parse_args()

    detector = GasDetector(args.address)

    if args.stream:
        try:
            print('time\tconcentration\tunits\talarm\tstate\tfault\t'
                  'temperature (C)\tflow rate (cc/min)\tlow alarm threshold\t'
                  'high alarm threshold')
            t0 = time()
            while True:
                d = detector.get()
                if d['connected']:
                    print(('{time:.2f}\t{concentration:.1f}\t{units}\t'
                           '{alarm}\t{state}\t{fault}\t{temperature:.1f}'
                           '\t{flow:.1f}\t{low-alarm threshold:.1f}\t'
                           '{high-alarm threshold:.1f}'
                           ).format(time=time()-t0, **d))
                else:
                    print("Not connected")
        except KeyboardInterrupt:
            pass
    else:
        print(json.dumps(detector.get(), indent=2, sort_keys=True))


if __name__ == '__main__':
    command_line()
