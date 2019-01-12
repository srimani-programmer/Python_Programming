# In this program we are going to deal with for-else loop

userInput = eval(input("Enter some list values:"))

for val in range(userInput):
    print(val)
    if val == 50: break

# break  --> if we use break then else block will not execute
# This else block will execute iff loop execute completely
else:
    print("Yur list values are completely printed")

