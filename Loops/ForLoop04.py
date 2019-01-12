# Assignment04 ---> print 1 to user_input value of prime numbers

userInput = int(input("Enter a number:"))

for num in range(0,userInput+1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)