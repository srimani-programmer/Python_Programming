# Working with threads
# Creating threads without classes

from threading import *

def sayMessage():
    for i in range(10):
        print('Hello from {} thread'.format(current_thread().getName()))

def sayGoodBye():

    for i in range(10):
        print('Good Bye message from {} thread'.format(current_thread().getName()))


def main():
    for i in range(10):
        print("Good bye from : {}".format(current_thread().getName()))

# creating the thread object.
thread_obj1 = Thread(target=sayMessage)
thread_obj2 = Thread(target=sayGoodBye)

# Starting the thread

thread_obj1.start()
thread_obj2.start()

main()

