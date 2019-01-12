# In this program we are going to deal with pass statement

'''
 pass Statement is nothing but an empty statement or null statement
 it is like a abstract method in java..!
 if we don't know about the implementation of certain block then we can happily use this
 statement...!
 To avoid syntactical error in a program
'''

userInput = int(input("Enter a value:"))

sum = 0
for val in range(userInput):
    if val % 2 == 0:
        sum = sum + val
    else:pass
print("The sum of all Even numbers in a given range is:",sum)