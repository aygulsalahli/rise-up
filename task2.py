#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from color_sensor import on_line
import movements

# Connect ultrasonic and touch sensors to any sensor port
ts = TouchSensor()
# Move to the line
while not on_line():
    movements.move('forward')
# Turn left to face the button
movements.turn('right')
# Move towards the button until button butt first
while not ts.value():
    movements.move('reverse')
# After button is pressed move to end of the line
while on_line():
    movements.move('forward')
# Turn right and face the ramp
movements.turn('right')
# Move towards the line
while not on_line():
    movements.move('forward')
# Turn left after line has reached
movements.turn('left')
# Go up from lamp
while not on_line():
    movements.move('forward')

