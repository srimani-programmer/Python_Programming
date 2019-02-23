# Implementing the same example program with multithreading

from threading import *
import time

def cube(value):
    result = list()
    for i in value:
        result.append(i ** 3)
    
    print('The Cubes Result is: {}'.format(result))

def square(value):
    result = list()
    for i in value:
        result.append(i ** 2)

    print('The Squares Result is: {}'.format(result))

values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
square_thread = Thread(target=square,args=(values,))
cube_thread = Thread(target=cube, args=(values,))

begin_time = time.time()

square_thread.start()
cube_thread.start()

end_time = time.time()

print('The total time taken by the program is: {}'.format(end_time - begin_time))