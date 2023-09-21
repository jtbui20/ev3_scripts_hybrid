from ev3dev2.motor import LargeMotor, Motor, SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ...utils.Motors import ClampSpeed


default_motor_configuration = [
    (OUTPUT_A, LargeMotor),
    (OUTPUT_B, LargeMotor),
    (OUTPUT_C, LargeMotor),
    (OUTPUT_D, LargeMotor),
]


class MotorModule:
    """Master class for motor related actions."""

    def __init__(self, motor_configuration=default_motor_configuration, debug=False):
        self.motorReferences = []
        self.motorPorts = []
        for port, motorType in motor_configuration:
            try:
                m = motorType(port)
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
            print("Motors are online")

    def __HandleInterrupt(function):
        def wrapper(self, *args, **kwargs):
            try:
                return function(*args, **kwargs)
            except:
                for key, motor in enumerate(self.motorReferences):
                    try:
                        motor.off()
                        self.finalMotorValues[key] = 0
                    except:
                        raise Exception(
                            "Error stopping motor {key} on port {port}".format(
                                key=key, port=self.motorPorts[key]
                            )
                        )

                raise Exception(
                    "Error in motor module. Check motor connections and try again."
                )

        return wrapper

    @__HandleInterrupt
    def isStalled(self):
        """Returns True if any of the motors are stalled"""
        return any([motor.is_stalled for motor in self.motorReferences])

    @__HandleInterrupt
    def ResetMotorValues(self):
        """Sets all motors to run at 0 speed"""
        self.finalMotorValues = self.defaultMotorValues

    @__HandleInterrupt
    def RunMotors(self, speed=100):
        """Runs the output motors of computed values to the motors"""
        self.finalMotorValues = ClampSpeed(self.finalMotorValues, speed)
        for motor, value in zip(self.motorReferences, self.finalMotorValues):
            motor.off() if value == 0 else motor.on(value)

        if self.debug:
            print(
                "Running motors at {motorValues}".format(
                    motorValues=self.finalMotorValues
                )
            )

    @__HandleInterrupt
    def StopMotors(self):
        for motor in self.motorReferences:
            motor.stop()

        self.ResetMotorValues()
