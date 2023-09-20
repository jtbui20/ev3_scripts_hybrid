from typing import List
import math
from utils.Motors import ClampSpeed
from utils.Math import AngleBetween


def RadialMove(
    angle: int,
    speed: int = 100,
    motor_count: int = 4,
    motor_order_offset: int = 1,
) -> List[float]:
    """Takes an angle that you want to travel in and sets the current direction to it"""
    values = [float(0)] * motor_count
    # If speed is 0, set values to 0
    if speed != 0:
        theta = math.radians(angle)
        values = [
            math.sin(theta - ((i + motor_order_offset) * math.pi / 2) - math.pi / 4)
            for i in range(0, motor_count)
        ]

        values = ClampSpeed(values, speed)

    return values


def RadialTurn(
    currentAngle: int,
    targetAngle: int,
    spread: int = 30,
    speed: float = 10,
    motor_count: int = 4,
    motor_order_offset: int = 1,
) -> List[float]:
    """Takes an angle that you want to turn towards and sets motor values to it"""
    differenceAngle = AngleBetween(currentAngle, targetAngle)[0]

    values = [float(0)] * motor_count
    if differenceAngle < -spread:
        values = [speed, 0, speed, 0]
    elif spread < differenceAngle:
        values = [0, -speed, 0, -speed]
    return values
