#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor

# Connect ultrasonic and touch sensors to any sensor port
us = UltrasonicSensor()

# Put the US sensor into distance mode.
us.mode = 'US-DIST-CM'
# reports 'cm' even though the sensor measures 'mm'
units = us.units


def get_distance():
    return us.value()/10


def is_blocked():
    return (us.value()/10) < 6  # convert mm to cm
