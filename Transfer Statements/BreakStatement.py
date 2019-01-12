# In this program we are going to deal with break statement

cartItemPrice = eval(input("Enter the cart item prices list:"))

sum = 0
myCartAccountBalance = 10000

for price in cartItemPrice:
    sum = sum + price
    if price < 500 and sum < 500:
        print("Delivery charges are applicable because itemprice and totalAmount", price,"and",sum,"is lessthan 500")

    if sum > myCartAccountBalance :
        print("No sufficient money to shop this session will logging out "
              "for further information please check your mail")
        break
else:
    print("The total bill of current shopping is",sum)

