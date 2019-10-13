import getch
from threading import Thread, Lock

lock = Lock()
user_input = ''
done = False


def get_user_input():
    global done
    global user_input
    while not done:
        char = getch.getch()
        if char == ' ':
            lock.acquire()
            user_input = char
            done = True
            lock.release()
        else:
            char = char.lower()
        lock.acquire()
        user_input = char
        lock.release()


def execute_user_input():
    global done
    global user_input
    while not done:
        lock.acquire()
        input = user_input
        lock.release()
        if input == 'w':
            print(user_input)


thread_reader = Thread(target=get_user_input)
thread_executer = Thread(target=execute_user_input)

thread_reader.start()
thread_executer.start()
thread_reader.join()
thread_executer.join()
