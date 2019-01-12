# In this program we are going to deal with while-else loop

userInput = int(input("Enter a value for upperBound of n:"))

# By using the user input we are going to calculate sum of n natural numbers

i = 0
sum = 0

while i < userInput :
    i+=1
    sum = sum + i
    if(sum == userInput):
        print("The answer is coincide with userInput value while iterating")
        break

# this below else block is going to execute when there is a complete execution of loop
else:
    print(sum)