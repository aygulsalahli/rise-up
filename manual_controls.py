import getch
from threading import Thread, Lock
from movements import *
from time import sleep

lock = Lock()
user_input = ''
done = False


def get_user_input():
    global done
    global user_input
    while not done:
        reading_input = getch.getch()
        if reading_input == ' ':
            lock.acquire()
            done = True
            lock.release()
        else:
            reading_input = reading_input.lower()
        lock.acquire()
        user_input = reading_input
        lock.release()


def execute_user_input():
    global done
    global user_input
    while not done:
        lock.acquire()
        executing_input = user_input
        user_input = ''
        lock.release()
        print('user input executer')
        print(executing_input)
        if executing_input == 'w':
            print(executing_input)
        if executing_input == 'w':
            move('forward')
        elif executing_input == 's':
            move('reverse')
        elif executing_input == 'a':
            turn('left')
        elif executing_input == 'd':
            turn('right')
        elif executing_input == 'u':
            turn('u_turn')
        elif executing_input == 'r':
            lift('up')
        elif executing_input == 'f':
            lift('down')
        elif executing_input == '':
            lift('')
            move('')
            turn('')
        sleep(0.1)
        executing_input = ''
thread_reader = Thread(target=get_user_input)
thread_executer = Thread(target=execute_user_input)

thread_reader.start()
thread_executer.start()
thread_reader.join()
thread_executer.join()
