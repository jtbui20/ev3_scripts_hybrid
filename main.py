#!/usr/bin/env pybricks-micropython
from src.lib.generic.Motors.Drivesets import OmniWheelDrive
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Port, Direction
from src.lib.pybricks_fw.Motors import PyBricksMotor
from time import sleep

drive = OmniWheelDrive(
    motorType=PyBricksMotor,
    motor_configuration=[{"Port": Port.A, Direction: Direction.CLOCKWISE}],
    debug=True,
)

state = False

while True:
    buttonsPressed = EV3Brick().buttons.pressed()
    if Button.CENTER in buttonsPressed:
        state = not state
        sleep(1)

    if state:
        drive.RadialMove(0, 100)

        drive.RunMotors()
    else:
        drive.StopMotors()
