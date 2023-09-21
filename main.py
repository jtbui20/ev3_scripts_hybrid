#!/usr/bin/env pybricks-micropython
from src.lib.pybricks_fw.Motors import OmniWheelDrive
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Port, Direction
from time import sleep

drive = OmniWheelDrive(
    motor_configuration=[(Port.A, Direction.CLOCKWISE)],
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
