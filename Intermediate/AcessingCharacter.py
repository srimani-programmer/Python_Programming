# Accessing a string character by character ----> It can be done in 2ways
'''By using
 1. indexes
 2. slice operator'''

# By index method we can access the string by character by character only
str = input("Enter String:")

i=0

for val in str:
    print("The string at positive index:{} and negative index:{} is:{}".format(i,i-len(str),val))
    i+=1

for val in str:
    print('The char value is:',val)
