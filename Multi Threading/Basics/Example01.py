# Implementing a simple program without multithreading

import time

def cube(value):
    result = list()
    for i in value:
        result.append(i ** 3)
    
    return result

def square(value):
    result = list()
    for i in value:
        result.append(i ** 2)

    return result

values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Starting the program execution
begin_time = time.time()

print('Cubes Result is: {}'.format(cube(values)))
print('Squares Result is: {}'.format(square(values)))

end_time = time.time()

print('The total time taken by the program to execute the task is: {}'.format(end_time - begin_time))
