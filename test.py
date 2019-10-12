from color_sensor import is_black, is_white
from movements import turn, move
from motor_a import lift
from ultrasonic_sensor import is_blocked
from time import sleep
from threading import Thread

white = False
black = False


def colorCheck():
    while True:
        white = is_white()
        black = is_black()
        sleep(2)


t = Thread(target=colorCheck)
t.start()


while True:
    sleep(2)
    print("test me here")
    if not is_blocked() and not black:
        move('forward')
    elif black:
        turn("custom", 100)
        lift('up')
        move('forward')
        lift('down')
