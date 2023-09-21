from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from ...utils.Motors import ClampSpeed


default_motor_configuration = [
    (Port.A, Direction.CLOCKWISE),
    (Port.B, Direction.CLOCKWISE),
    (Port.C, Direction.CLOCKWISE),
    (Port.D, Direction.CLOCKWISE),
]


class MotorModule:
    """Master class for motor related actions."""

    def __init__(self, motor_configuration=default_motor_configuration, debug=False):
        self.motorReferences = []
        self.motorPorts = []
        for port, motorDirection in motor_configuration:
            try:
                m = Motor(port, motorDirection)
                self.motorPorts.append(port)
                self.motorReferences.append(m)
            except Exception as e:
                raise Exception(
                    "Error initializing motor on port {port}: {error}".format(
                        port=port, error=e
                    )
                )

        self.defaultMotorValues = [float(0)] * len(self.motorReferences)

        self.finalMotorValues = self.defaultMotorValues
        self.debug = debug

        if self.debug:
            print("Base Motor Modules are online.")

    def __HandleInterrupt(function):
        def wrapper(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except Exception as e:
                for key, motor in enumerate(self.motorReferences):
                    try:
                        motor.stop()
                        self.finalMotorValues[key] = 0
                    except:
                        raise Exception(
                            "Error stopping motor {key} on port {port}".format(
                                key=key, port=self.motorPorts[key]
                            )
                        )
                print("Error: {error}".format(error=e))

        return wrapper

    @__HandleInterrupt
    def isStalled(self):
        """Returns True if any of the motors are stalled"""
        return any([motor.stalled() for motor in self.motorReferences])

    @__HandleInterrupt
    def ResetMotorValues(self):
        """Sets all motors to run at 0 speed"""
        self.finalMotorValues = self.defaultMotorValues

    @__HandleInterrupt
    def RunMotors(self, speed=100):
        """Runs the output motors of computed values to the motors"""
        self.finalMotorValues = ClampSpeed(self.finalMotorValues, speed)
        for motor, value in zip(self.motorReferences, self.finalMotorValues):
            motor.stop() if value == 0 else motor.dc(value)

        if self.debug:
            print(
                "Running motors at {motorValues}".format(
                    motorValues=self.finalMotorValues
                )
            )

    @__HandleInterrupt
    def StopMotors(self):
        for motor in self.motorReferences:
            motor.brake()

        self.ResetMotorValues()
