from pybricks.ev3devices import Motor as baseMotor
from pybricks.parameters import Port, Direction, Stop
from ...generic.Motors import Motor
from time import sleep

default_motor_configuration = [
    {"Port": Port.A, "Direction": Direction.CLOCKWISE},
    {"Port": Port.B, "Direction": Direction.CLOCKWISE},
    {"Port": Port.C, "Direction": Direction.CLOCKWISE},
    {"Port": Port.D, "Direction": Direction.CLOCKWISE},
]


class PyBricksMotor(Motor):
    def __init__(self, config):
        self.port = config.get("Port", None)
        self.__motorDirection = config.get("Direction", Direction.CLOCKWISE)
        self.__motor = None
        self.__error = False

        self.CreateMotorAdapter()

    def CreateMotorAdapter(self):
        try:
            self.__motor = baseMotor(self.port, self.__motorDirection)
            return self
        except Exception as e:
            raise e

    def HandleErrorStop(self):
        try:
            self.Off(True)
        except:
            self.__error = True
            print("Motor {port} has disconnected".format(port=self.port))

            while self.__error:
                try:
                    self.Off(self)
                    self.__error = False
                except Exception as e:
                    print("Please reconnect motor {port}".format(port=self.port))
                    sleep(1)
                    continue

    def On(self, speed):
        self.__motor.dc(speed)

    def Off(self, mode):
        if mode in [1, "BRAKE", True, Stop.BRAKE]:
            self.__motor.brake()
        else:
            self.__motor.stop()

    @property
    def isStalled(self):
        return self.__motor.stalled()
