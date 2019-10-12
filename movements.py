#!/usr/bin/env python3
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, follow_for_forever
from ev3dev2.sensor.lego import ColorSensor
# TODO: Add code here
left_motor = OUTPUT_B
right_motor = OUTPUT_C
tank_drive = MoveTank(left_motor, right_motor)
# Setpoints
speed = 75
tank_drive.cs = ColorSensor()


def move(move_dir):
    if move_dir == 'forward':
        rotations = 1
        # Turn on left and right motor with defined speed for defined rotations
        tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations)
    if move_dir == 'reverse':
        rotations = 1
        # Turn on left and right motor with defined speed for defined rotations
        tank_drive.on_for_rotations(SpeedPercent(-speed), SpeedPercent(-speed), rotations)


def turn(turn_dir, custom_turn_degree=0):
    left_turn_degree = 420
    right_turn_degree = 420
    u_turn_degree = 360
    # Turn on left and right motor with defined speed for defined rotations
    if turn_dir == 'left':
        tank_drive.on_for_degrees(SpeedPercent(0), SpeedPercent(speed), left_turn_degree)
    elif turn_dir == 'right':
        tank_drive.on_for_degrees(SpeedPercent(speed), SpeedPercent(0), right_turn_degree)
    elif turn_dir == 'u_turn':
        tank_drive.on_for_degrees(SpeedPercent(-speed), SpeedPercent(speed), u_turn_degree)
    elif turn_dir == 'custom':
        tank_drive.on_for_degrees(SpeedPercent(-speed), SpeedPercent(speed), custom_turn_degree)


def follow_line():
    try:
        tank_drive.follow_line(
            kp=5.3, ki=0.05, kd=3.2,
            speed=SpeedPercent(30))
        print(ColorSensor.COLOR_WHITE)
    except Exception:
        tank_drive.stop()
        raise
    print(ColorSensor.COLOR_WHITE)


# Cycle
while True:
    move('forward')
    follow_line()
    break
