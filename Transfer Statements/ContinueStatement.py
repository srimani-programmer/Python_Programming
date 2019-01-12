# In this program we are going to deal with continue statement

userInput = int(input("Enter a number:"))

for val in range(userInput):
    if val%2 != 0:
        continue
    print(val)

userInput = int(input("Enter a number:"))

for val in range(userInput):
    if val%2 == 0:
        continue
    print(val)