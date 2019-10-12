#!/usr/bin/env python3

import movements
import color_sensor
from time import sleep
line_detected = False
# start point, move to the line
print (1)
while not line_detected:
    line_detected = color_sensor.is_white()
    movements.move('forward')
    print(2)
movements.move('stop')
# start following the line until yellow button is detected
movements.follow_line()
print(3)
movements.turn('left')
print(4)
# Turn to the left
movements.turn('left')
print(5)
movements.follow_line()
print(6)
movements.turn('left')
print(7)
movements.follow_line()
print(8)
movements.turn('right')
print(9)
movements.follow_line()
print(10)
movements.turn('right')
print(11)
movements.follow_line()
print(12)
if color_sensor.is_yellow():
    movements.move('backwards')
    sleep(2)
    movements.turn('left')
    sleep(2)

# Wait until turning is finished
sleep(1)
# Turn left once again
movements.turn('left')
# Move one block forward
movements.move('forward')
movements.turn('right')
while color_sensor.is_white():
    movements.follow_line()

