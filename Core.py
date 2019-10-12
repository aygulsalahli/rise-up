#!/usr/bin/env python3
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import GyroSensor

from time import sleep

# TODO: Add code here
left_motor = OUTPUT_B
right_motor = OUTPUT_C
tank_drive = MoveTank(left_motor, right_motor)
gyro = GyroSensor()

def move_forward():
    speed = 75
    rotations = 2
    # Turn on left and right motor with defined speed for defined rotations
    tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations)


def turn(direction):
    speed = 75
    rotations = 1
    GyroSensor.mode = GyroSensor.MODE_GYRO_CAL
    sleep (1)
    if gyro.angle == 0:
        GyroSensor.mode = GyroSensor.MODE_GYRO_ANG
        print('Gyro calibrated ')

    # Turn on left and right motor with defined speed for defined rotations
    if direction == 'left' and GyroSensor.mode == GyroSensor.MODE_GYRO_ANG:
        while gyro.angle <= -90:
            tank_drive.on(SpeedPercent(0), SpeedPercent(speed))
            print('turning left', gyro.angle)
    elif direction == 'right'and GyroSensor.mode == GyroSensor.MODE_GYRO_ANG:
        while gyro.angle >= 90:
            tank_drive.on(SpeedPercent(speed), SpeedPercent(0))
            print('turning right', gyro.angle)
    else:
        tank_drive.on(SpeedPercent(0), SpeedPercent(0))
def follow_line:
    try:
        # Follow the line for 4500ms
        tank_drive.follow_line(
            kp=11.3, ki=0.05, kd=3.2,
            speed=SpeedPercent(30),
            follow_for = 'follow_for_ms',
            ms=4500
        )
    except Exception:
        tank_drive.stop()
        raise

#Cycle
#move_forward()

turn('left')

turn('right')
