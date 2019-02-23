# Thread Identification number

from threading import *

def display():
    print('Hello from display')

thread_obj = Thread(target=display)
thread_obj.start()  # Once python thread is created then identification number is assigned.
# printing the identification number
# ident is an implicit variable.
print('My main thread Identification number is: {}'.format(current_thread().ident))
print('My child thread Identification number is: {}'.format(thread_obj.ident))