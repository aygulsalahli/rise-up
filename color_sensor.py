#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor

# Connect ultrasonic and touch sensors to any sensor port
cs = ColorSensor()

# In this mode the sensor will return a value between 0 and 100
cs.mode = 'COL-REFLECT'


def on_line():
    return is_white()

def is_white():
    return cs.value() >= 50 and cs.value()<=60


def is_yellow():
    return cs.value() <= 70 and cs.value() >= 65


def is_gray():
    return cs.value() <= 15 and cs.value() > 6


def is_black():
    return cs.value() > 0 and cs.value() <= 6
