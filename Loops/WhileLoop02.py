# Assignment02 --> Password validation

userPassword = int(input("Enter Your Password:"))

while userPassword != 123456789 :
    print("Invalid Password")
    userPassword = int(input("please Enter your Password again:"))
print("you are sucessfully logged in..!")