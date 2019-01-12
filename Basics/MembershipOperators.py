# Membership operators in Strings
# in and not in

mainStr = input("Enter Main String:")
subStr = input("Enter Sub String:")

if (subStr in mainStr):
    print(subStr, "is present in main String")
else:
    print(subStr, "is not present in MainString")