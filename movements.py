#!/usr/bin/env python3
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, follow_for_forever

# TODO: Add code here
left_motor = OUTPUT_B
right_motor = OUTPUT_C
tank_drive = MoveTank(left_motor, right_motor)
# Setpoints
speed = 75


def move(move_dir):
    if move_dir == 'forward':
        rotations = 1
        # Turn on left and right motor with defined speed for defined rotations
        tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations)
    if move_dir == 'reverse':
        rotations = 1
        # Turn on left and right motor with defined speed for defined rotations
        tank_drive.on_for_rotations(SpeedPercent(-speed), SpeedPercent(-speed), rotations)


def turn(turn_dir):
    left_turn_degree = 360
    right_turn_degree = 360
    u_turn_degree = 360
    # Turn on left and right motor with defined speed for defined rotations
    if turn_dir == 'left':
        tank_drive.on_for_degrees(SpeedPercent(0), SpeedPercent(speed), left_turn_degree)
    elif turn_dir == 'right':
        tank_drive.on_for_degrees(SpeedPercent(speed), SpeedPercent(0), right_turn_degree)
    elif turn_dir == 'u_turn':
        tank_drive.on_for_degrees(SpeedPercent(-speed), SpeedPercent(speed), u_turn_degree)

#TODO Buggy part
def follow_line(active):
    try:
        MoveTank.follow_line(
            kp=11.3, ki=0.05, kd=3.2,
            speed=SpeedPercent(30),
            follow_for_ms=follow_for_forever)
        if not active:
            tank_drive.stop()
    except Exception:
        tank_drive.stop()
        raise


# Cycle
while True:
    move('forward')
    follow_line()
    break
