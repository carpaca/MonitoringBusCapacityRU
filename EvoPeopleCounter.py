#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import crcmod.predefined
import serial.tools.list_ports
import threading
import struct
from ruamel.yaml import YAML
yaml = YAML()


class EvoPeopleCounter(object):
    TEXT_MODE = b"\x00\x11\x01\x45"
    BINARY_MODE = b"\x00\x11\x02\x4C"
    BIDIRECTIONAL_MODE = b"\x00\x21\x0A\x8D"
    RESET_BIDIRECTIONAL_COUNTER = b"\x00\x55\x08\x00\x00\x00\x00\x7C"
    GET_SENSOR_PARAMETERS = b"\x00\x61\x01\xE7"

    def __init__(self, portname=None):
        if portname is None:
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                if ":5740" in p[2]:
                    print("Evo Swipe Plus found on port {}".format(p[0]))
                    portname = p[0]
            if portname is None:
                print("Sensor not found. Please Check connections.")
                exit()
        self.portname = portname
        self.baudrate = 115200

        # Configure the serial connections
        self.port = serial.Serial(
            port=self.portname,
            baudrate=self.baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        self.port.isOpen()
        self.crc8 = crcmod.predefined.mkPredefinedCrcFun('crc-8')
        self.serial_lock = threading.Lock()

        self.filename = "config.yaml"
        self.yaml_dict = {}

    def get_ranges(self):
        # Read one byte
        data = []
        header = self.port.read(2)

        if header == b'DD':
            # After DD read D1(2) + D2(2) + CRC (1) bytes
            frame = header + self.port.read(5)  # Try a two-range frame
            if frame[-1] != self.crc8(frame[:-1]):
                print("CRC mismatch. Check connection or make sure only one program accesses the sensor port.")
                return header, []

            rng = struct.unpack(">hh", frame[2:6])
            rng = list(rng)
            data = rng
            sensor_id = 0
            self.check_ranges(data)

        elif header == b'PC':
            # After PC read 13 bytes (Bytes N°: Sensor ID (4), Inside(4), In(2), Out(2) + CRC(1))
            frame = header + self.port.read(13)  # Try a Bidirectional frame
            # print("FRAME:", frame)
            if frame[-1] != self.crc8(frame[:-1]):
                return header, "CRC mismatch."
            sensor_id = struct.unpack(">l", frame[2:6])
            counts = struct.unpack(">lhh", frame[6:14])
            data = counts

        else:
            return "Waiting for frame header", header

        return header, sensor_id, data

    def get_parameters_values(self):

        sensor_parameters = {}
        header = self.port.read(2)

        # Frame is: BPXXXX
        if header == b'BP':
            frame = header + self.port.read(4)
            sensor_parameters["bidirectional_max_threshold"] = struct.unpack(">H", frame[2:4])
            sensor_parameters["bidirectional_min_threshold"] = struct.unpack(">H", frame[4:6])

        return sensor_parameters

    def check_ranges(self, range_list):
        for i in range(len(range_list)):
            # Checking error codes
            if range_list[i] == 65535:  # Sensor measuring above its maximum limit
                range_list[i] = float('inf')
            elif range_list[i] == 1:  # Sensor not able to measure
                range_list[i] = float('nan')
            elif range_list[i] == 0:  # Sensor detecting object below minimum range
                range_list[i] = -float('inf')
            else:
                # Convert frame in meters
                range_list[i] /= 1000.0

        return range_list

    def send_command(self, command):
        with self.serial_lock:  # This avoid concurrent writes/reads of serial
            self.port.write(command)
            ack = self.port.read(1)
            # This loop discards buffered frames until an ACK header is reached
            while ack != b"\x12":
                ack = self.port.read(1)
            else:
                ack += self.port.read(3)

            # Check ACK crc8
            crc8 = self.crc8(ack[:3])
            if crc8 == ack[3]:
                # Check if ACK or NACK
                if ack[2] == 0:
                    return True
                else:
                    print("Command not acknowledged")
                    return False
            else:
                print("Error in ACK checksum")
                return False

    def yaml_config(self):

        try:
            with open(self.filename, 'r') as ymlfile:
                self.yaml_dict = yaml.load(ymlfile)
                max_range = self.yaml_dict["thresholds"]["max_range"]
                min_range = self.yaml_dict["thresholds"]["min_range"]

        except IOError:
            print("Config file not found. ", "Using default parameters")

        return max_range, min_range

    def set_bidirectional_mode(self):
        if self.send_command(EvoPeopleCounter.BIDIRECTIONAL_MODE):
            print("Bidirectional traffic detection mode set")

    def reset_bidirectional_counter(self):
        if self.send_command(EvoPeopleCounter.RESET_BIDIRECTIONAL_COUNTER):
            print("Reset Bidirectional counter")

    def get_sensor_parameters(self):
        if self.send_command(EvoPeopleCounter.GET_SENSOR_PARAMETERS):
            print("Get Parameters")
            return self.get_parameters_values()

    def set_bidirectional_range(self, bidirectional_max_limit, bidirectional_min_limit):
        crc8_command_bidirectional = b"\x00\x55\x03"
        crc8_command_bidirectional += struct.pack(">H", bidirectional_max_limit)
        crc8_command_bidirectional += struct.pack(">H", bidirectional_min_limit)
        crc8_command_bidirectional += bytes(bytearray([self.crc8(crc8_command_bidirectional)]))
        if self.send_command(crc8_command_bidirectional):
            print("Changed Bidirectional Limits")

    def run(self):
        self.port.flushInput()
        while ranges is not None:
            ranges, new_counter_value, movement = self.get_ranges()
        else:
            print("No data from sensor")


if __name__ == '__main__':
    sensor = EvoPeopleCounter()
    #sensor.run()
    while True:
        header, sensor_id, data = sensor.get_ranges()
        if header == b'PC':
            print(data)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import crcmod.predefined
import serial.tools.list_ports
import threading
import struct
from ruamel.yaml import YAML
yaml = YAML()


class EvoPeopleCounter(object):
    TEXT_MODE = b"\x00\x11\x01\x45"
    BINARY_MODE = b"\x00\x11\x02\x4C"
    BIDIRECTIONAL_MODE = b"\x00\x21\x0A\x8D"
    RESET_BIDIRECTIONAL_COUNTER = b"\x00\x55\x08\x00\x00\x00\x00\x7C"
    GET_SENSOR_PARAMETERS = b"\x00\x61\x01\xE7"

    def __init__(self, portname=None):
        if portname is None:
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                if ":5740" in p[2]:
                    print("Evo Swipe Plus found on port {}".format(p[0]))
                    portname = p[0]
            if portname is None:
                print("Sensor not found. Please Check connections.")
                exit()
        self.portname = portname
        self.baudrate = 115200

        # Configure the serial connections
        self.port = serial.Serial(
            port=self.portname,
            baudrate=self.baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        self.port.isOpen()
        self.crc8 = crcmod.predefined.mkPredefinedCrcFun('crc-8')
        self.serial_lock = threading.Lock()

        self.filename = "config.yaml"
        self.yaml_dict = {}

    def get_ranges(self):
        # Read one byte
        data = []
        header = self.port.read(2)

        if header == b'DD':
            # After DD read D1(2) + D2(2) + CRC (1) bytes
            frame = header + self.port.read(5)  # Try a two-range frame
            if frame[-1] != self.crc8(frame[:-1]):
                print("CRC mismatch. Check connection or make sure only one program accesses the sensor port.")
                return header, []

            rng = struct.unpack(">hh", frame[2:6])
            rng = list(rng)
            data = rng
            sensor_id = 0
            self.check_ranges(data)

        elif header == b'PC':
            # After PC read 13 bytes (Bytes N°: Sensor ID (4), Inside(4), In(2), Out(2) + CRC(1))
            frame = header + self.port.read(13)  # Try a Bidirectional frame
            # print("FRAME:", frame)
            if frame[-1] != self.crc8(frame[:-1]):
                return header, "CRC mismatch."
            sensor_id = struct.unpack(">l", frame[2:6])
            counts = struct.unpack(">lhh", frame[6:14])
            data = counts

        else:
            return "Waiting for frame header", header

        return header, sensor_id, data

    def get_parameters_values(self):

        sensor_parameters = {}
        header = self.port.read(2)

        # Frame is: BPXXXX
        if header == b'BP':
            frame = header + self.port.read(4)
            sensor_parameters["bidirectional_max_threshold"] = struct.unpack(">H", frame[2:4])
            sensor_parameters["bidirectional_min_threshold"] = struct.unpack(">H", frame[4:6])

        return sensor_parameters

    def check_ranges(self, range_list):
        for i in range(len(range_list)):
            # Checking error codes
            if range_list[i] == 65535:  # Sensor measuring above its maximum limit
                range_list[i] = float('inf')
            elif range_list[i] == 1:  # Sensor not able to measure
                range_list[i] = float('nan')
            elif range_list[i] == 0:  # Sensor detecting object below minimum range
                range_list[i] = -float('inf')
            else:
                # Convert frame in meters
                range_list[i] /= 1000.0

        return range_list

    def send_command(self, command):
        with self.serial_lock:  # This avoid concurrent writes/reads of serial
            self.port.write(command)
            ack = self.port.read(1)
            # This loop discards buffered frames until an ACK header is reached
            while ack != b"\x12":
                ack = self.port.read(1)
            else:
                ack += self.port.read(3)

            # Check ACK crc8
            crc8 = self.crc8(ack[:3])
            if crc8 == ack[3]:
                # Check if ACK or NACK
                if ack[2] == 0:
                    return True
                else:
                    print("Command not acknowledged")
                    return False
            else:
                print("Error in ACK checksum")
                return False

    def yaml_config(self):

        try:
            with open(self.filename, 'r') as ymlfile:
                self.yaml_dict = yaml.load(ymlfile)
                max_range = self.yaml_dict["thresholds"]["max_range"]
                min_range = self.yaml_dict["thresholds"]["min_range"]

        except IOError:
            print("Config file not found. ", "Using default parameters")

        return max_range, min_range

    def set_bidirectional_mode(self):
        if self.send_command(EvoPeopleCounter.BIDIRECTIONAL_MODE):
            print("Bidirectional traffic detection mode set")

    def reset_bidirectional_counter(self):
        if self.send_command(EvoPeopleCounter.RESET_BIDIRECTIONAL_COUNTER):
            print("Reset Bidirectional counter")

    def get_sensor_parameters(self):
        if self.send_command(EvoPeopleCounter.GET_SENSOR_PARAMETERS):
            print("Get Parameters")
            return self.get_parameters_values()

    def set_bidirectional_range(self, bidirectional_max_limit, bidirectional_min_limit):
        crc8_command_bidirectional = b"\x00\x55\x03"
        crc8_command_bidirectional += struct.pack(">H", bidirectional_max_limit)
        crc8_command_bidirectional += struct.pack(">H", bidirectional_min_limit)
        crc8_command_bidirectional += bytes(bytearray([self.crc8(crc8_command_bidirectional)]))
        if self.send_command(crc8_command_bidirectional):
            print("Changed Bidirectional Limits")

    def run(self):
        self.port.flushInput()
        while ranges is not None:
            ranges, new_counter_value, movement = self.get_ranges()
        else:
            print("No data from sensor")


if __name__ == '__main__':
    sensor = EvoPeopleCounter()
    #sensor.run()
    while True:
        header, sensor_id, data = sensor.get_ranges()
        if header == b'PC':
            print(data)


