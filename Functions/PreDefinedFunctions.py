# using the predefined functions in python for strings

# To find length of the string

str = "sriManiKantaPalakollu"

print(len(str))
# printing the length manually

i = 0
for val in str:
    i+=1
print(i)

# Converting the String to UpperCase

print(str.upper())

# Converting the String into lowerCase

print(str.lower())

# Capitalize the Given String
# The capitalize() function returns a string with first letter capitalized.
# It doesn't modify the old string.

print(str.capitalize())

print(str)

# Boolean functions in strings concept

print(str.isalpha())

print(str.islower())

print(str.isupper())

name = "1234mani"

print(name.isalnum())

print(name.isalpha())

decimalString = "123456"
# The isdecimal() returns:
#
# True if all characters in the string are decimal characters.
# False if at least one character is not decimal character.
print(decimalString.isdecimal())

# The casefold() method is removes all case distinctions present in a string. It is used for caseless matching,
# i.e. ignores cases when comparing.
#
# For example, German lowercase letter ß is equivalent to ss.
# However, since ß is already lowercase, lower() method does nothing to it.
# But, casefold() converts it to ss.

print(str.casefold())

# encode() is used to change utf-8 conversion

print(str.encode())

# The isdigit() returns:
#
# True if all characters in the string are digits.
# False if at least one character is not a digit.

digitString = "1232443"

print(digitString.isdigit())

digitString1 = "13234AB"

print(digitString1.isdigit())