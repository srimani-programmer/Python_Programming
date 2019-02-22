# Creating thread extensding the thread class

from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('MyThread is extending the Thread class.')

thread_obj = MyThread()
thread_obj.start()

for i in range(10):
    print('Main thread is working fine.')



