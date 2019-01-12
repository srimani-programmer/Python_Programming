# Assignment03 ---> print n even and odd numbers

userInput = int(input("Enter a number:"))

print("The even numbers are:")
for value in range(0,userInput+1):
    if value % 2 == 0:
        print(value)

print("The odd numbers are:")
for value in range(0,userInput+1):
    if value % 2 != 0:
        print(value)