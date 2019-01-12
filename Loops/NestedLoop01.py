# Assignment01 ---> print a pattern as shown below
'''
    if noOfRows = 5 then print as follows
    *
    * *
    * * *
    * * * *
    * * * * *
'''

userInput = int(input("Enter a number:"))

for pat in range(userInput):
    for i in range(pat+1):
        print("*", end = " ")
    print("\r")
