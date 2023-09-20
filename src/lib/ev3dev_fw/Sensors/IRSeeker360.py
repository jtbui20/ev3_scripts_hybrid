#!/usr/bin/env python3
from smbus import SMBus
from ev3dev2.sensor import I2cSensor


class IRSeeker360:
    def __init__(self, port: str | int):
        if type(port) == str:
            port = StringToPort(port)

        self.i2c_address = 0x08
        self.port = port

        self.create_bus()

    def value(self):
        return self.bus.read_i2c_block_data(self.i2c_address, 0, 2)

    def create_bus(self):
        self.bus = SMBus(self.port + 0x2)

    def close(self):
        self.bus.close()


def StringToPort(port: str) -> int:
    """Converts the literal in1 to the number port it is on."""
    return port[2:]
