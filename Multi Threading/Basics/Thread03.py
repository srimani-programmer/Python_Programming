# Working with classes without extending the thread class.

from threading import *

class Show:

    def display(self):
        for i in range(10):
            print('This is my own method to work with thread.')

obj = Show()
thread_obj = Thread(target=obj.display)

thread_obj.start()

# thread_obj.join() ===> join() is used to wait the main thread until child threads are executing.

for i in range(10):
    print('My main thread is executing.')