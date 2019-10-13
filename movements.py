#!/usr/bin/env python3
from ev3dev2.motor import Motor, MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, follow_for_forever
from ev3dev2.sensor.lego import ColorSensor

lifting_motor = MediumMotor('outA')
left_motor = OUTPUT_B
right_motor = OUTPUT_C
tank_drive = MoveTank(left_motor, right_motor)

# Setpoints
speed = 15
tank_drive.cs = ColorSensor()


def move(move_dir):
    if move_dir == 'forward':
        tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))
    if move_dir == 'reverse':
        tank_drive.on(SpeedPercent(-speed), SpeedPercent(-speed))
    elif move_dir == '':
        tank_drive.off()


def turn(turn_dir, custom_turn_degree=0):
    left_turn_degree = 420
    right_turn_degree = 420
    u_turn_degree = 360
    # Turn on left and right motor with defined speed for defined rotations
    if turn_dir == 'left':
        tank_drive.on(SpeedPercent(0), SpeedPercent(speed))
    elif turn_dir == 'right':
        tank_drive.on(SpeedPercent(speed), SpeedPercent(0))
    elif turn_dir == 'u_turn':
        tank_drive.on_for_degrees(SpeedPercent(-speed), SpeedPercent(speed), u_turn_degree)
    elif turn_dir == 'custom':
        tank_drive.on_for_degrees(SpeedPercent(-speed), SpeedPercent(speed), custom_turn_degree)
    elif turn_dir == '':
        tank_drive.off()


def lift(direction):
    lifting_motor.reset()
    if direction == 'up':
        lifting_motor.run_to_rel_pos(position_sp=20, speed_sp=300, stop_action=)
    if direction == 'down':
        lifting_motor.run_to_rel_pos(position_sp=-20, speed_sp=300, stop_action="coast")


