from ...generic.Motors import Motor
from ev3dev2.motor import (
    LargeMotor,
    OUTPUT_A,
    OUTPUT_B,
    OUTPUT_C,
    OUTPUT_D,
)

default_motor_configuration = [
    {"Port": OUTPUT_A, "Class": LargeMotor},
    {"Port": OUTPUT_B, "Class": LargeMotor},
    {"Port": OUTPUT_C, "Class": LargeMotor},
    {"Port": OUTPUT_D, "Class": LargeMotor},
]


class EV3Motor(Motor):
    def __init__(self, config):
        self.port = config.get("Port", None)
        self.__motorClass = config.get("Class", LargeMotor)
        self.__motor  # type: Motor
        self.__error = False

        self.CreateMotorAdapter()

    def CreateMotorAdapter(self):
        try:
            self.__motor = self.__motorClass(self.port)
            return self
        except Exception as e:
            return None

    def HandleErrorStop(self):
        try:
            self.Off(True)
        except:
            self.__error
            raise Exception(
                "Motor {port} has disconnected".format(port=self.port), self
            )
        pass

    def On(self, speed):
        self.__motor.on(speed)

    def Off(self, mode):
        mode = True if mode in [1, "BRAKE", True] else False
        self.__motor.off(brake=mode)

    @property
    def isStalled(self):
        return self.__motor.is_stalled
