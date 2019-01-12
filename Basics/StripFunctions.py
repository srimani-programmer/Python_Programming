# Working with removal of spaces

cityList = ["Delhi","Hyderabad","Bangalore","goa","Gujarat","Kerala","Chennai"]

# Strip functions
# strip() --> used to remove all spaces in left and right
# lstrip()  ---> used to remove all spaces present in left
# rstrip() ----> used to remove all spaces present in right

userCityName = input("please enter your city name:")

if userCityName.strip() in cityList:
    print("available service centers are at xyz location")
else:
    print("please enter valid city name")