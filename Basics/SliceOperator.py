# working with slice operator

str1 = 'Sri Manikanta palakollu'

# printing all string value

# slice operator syntax----> [beginIndex : endIndex : step]

print(str1[0:len(str1):1])

# printing the all characters of a string without beginIndex,endIndex and step value

print(str1[::])

# printing the required character set in a string

print(str1[0:len(str1):2]) # it will skip every 2 characters

# printing the all characters of a string without endIndex and step value

print(str1[0::])

# printing the all characters of a string without beginIndex and step value

print(str1[:len(str1):])

# reverse the string in python

print(str1[::-1])

# Playing games with slice operator

s = "0123456789"

print(s[-3:-2:-1]) # Ans-->Empty string

print(s[-6:1:-5])  #4

print(s[2:1:-1])  # 2

print(s[-7:3:-6])  # Ans-->Empty string

print(s[2:-3:-1]) # Ans-->Empty string

print(s[3:6:6])  # 3

print(s[-3:-1:-2]) # Ans-->Empty string

print(s[8:-4:-4])   # 8

print(s[-4:-3:-6]) # Ans-->Empty string

print(s[2:-5:-1])  # Ans-->Empty string

print(s[4:0:-1])  # 4321

# In any case while computing slice operator
# if begin value is +ve and endIndex value is <=0  then the output is empty string..
# if begin index value is -ve and end indexValue is == 0 then the output is empty string..

print(s[4:-3:-1])
