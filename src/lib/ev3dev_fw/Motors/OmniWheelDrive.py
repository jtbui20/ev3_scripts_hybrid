#!/usr/bin/env python3
from Motors import MotorModule, default_motor_configuration
from typing import List
from utils.Math import AddMatrix
from generic.logic.Motors.OmniwheelLogic import RadialMove, RadialTurn


class OmniWheelDrive(MotorModule):
    """Class that defines how an omni wheel robot should move."""

    def __init__(self, motor_configuration=default_motor_configuration, debug=False):
        super().__init__(motor_configuration, debug)

    def RadialMove(
        self,
        angle: int,
        speed: int = 100,
        motor_order_offset: int = 1,
    ) -> List[float]:
        """Takes an angle that you want to travel in and sets motor values to it"""
        values = RadialMove(angle, speed, len(self.motorReferences), motor_order_offset)

        if self.debug:
            print(values)

        self.finalValues = AddMatrix(self.finalValues, values)
        return values

    def RadialTurn(
        self, currentAngle: int, targetAngle: int, spread: int = 30, speed: int = 10
    ) -> List[float]:
        """Takes an angle that you want to turn towards and sets motor values to it"""
        values = RadialTurn(
            currentAngle, targetAngle, spread, speed, len(self.motorReferences)
        )

        self.finalMotorValues = AddMatrix(self.finalMotorValues, values)

        return values
