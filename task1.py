import movements
import color_sensor
from time import sleep
# start point, move to the line
movements.move('forward')
# start following the line until yellow button is detected
while color_sensor.is_white():
    movements.follow_line()
# Turn to the left
movements.turn('left')
# Wait until turning is finished
sleep(1)
# Turn left once again
movements.turn('left')
# Move one block forward
movements.move('forward')
movements.turn('right')
while color_sensor.is_white():
    movements.follow_line()

