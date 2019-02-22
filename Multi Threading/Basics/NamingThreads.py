# Getting and Setting names

# To create our own name to the thread

from threading import *

print('My current working thread is: {}'.format(current_thread().name))

# changing my thread name

current_thread().setName('SriMani')

print('Now My thread name is: {}'.format(current_thread().getName()))
