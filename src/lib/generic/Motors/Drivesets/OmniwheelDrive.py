from ...Motors import MotorModule
from ....utils.Math import AddMatrix
from ....generic.logic.Motors.OmniwheelLogic import RadialMove, RadialTurn


class OmniWheelDrive(MotorModule):
    def __init__(self, motorType, motor_configuration, debug=False):
        super().__init__(motorType, motor_configuration, debug)

    def RadialMove(self, angle, speed=100, motor_order_offset=1):
        """Takes an angle that you want to travel in and sets the current direction to it"""
        values = RadialMove(angle, speed, len(self.motorReferences), motor_order_offset)

        self.finalMotorValues = AddMatrix(self.finalMotorValues, values)

        return values

    def RadialTurn(self, currentAngle, targetAngle, spread=30, speed=10):
        """Takes an angle that you want to turn towards and sets motor values to it"""
        values = RadialTurn(
            currentAngle, targetAngle, spread, speed, len(self.motorReferences)
        )

        self.finalMotorValues = AddMatrix(self.finalMotorValues, values)

        return values
