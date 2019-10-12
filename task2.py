#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from color_sensor import on_line
from Core import move, turn

# Connect ultrasonic and touch sensors to any sensor port
ts = TouchSensor()

while not on_line():
    move('forward')
turn('left')

while not ts.value():
    move('forward')

while on_line():
    move('reverse')

turn('left')

while not on_line():
    move('forward')

turn('left')
