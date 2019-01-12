# Assignment01 ---> sum of first n numbers

userInput = int(input("Enter a number:"))

sum = 0
i = 0

while i < userInput:
    i+=1
    sum = sum + i
print(sum)