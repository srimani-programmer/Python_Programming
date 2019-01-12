# Difference between is and == operator
# == is used for content comparison
# is operator is used for reference comparison

list1 = [10,20,30,40,'a',3-4j]
list2 = [10,20,30,40,'a',3-4j]

print(id(list1))
print(id(list2))

print(list2 is list1) # False

print(list1 == list2) # True

list3 = list2

print(list3 is list2) # True