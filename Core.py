#!/usr/bin/env python3
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank

from time import sleep

# TODO: Add code here
left_motor = OUTPUT_B
right_motor = OUTPUT_C
tank_drive = MoveTank(left_motor, right_motor)


def move_forward():
    speed = 75
    rotations = 2
    # Turn on left and right motor with defined speed for defined rotations
    tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations)


def turn(direction):
    speed = 75
    rotations = 2
    # Turn on left and right motor with defined speed for defined rotations
    if direction == 'left':
        tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(speed), rotations)
    elif direction == 'right':
        tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(0), rotations)

#Cycle
move_forward()

turn('left')

turn('right')