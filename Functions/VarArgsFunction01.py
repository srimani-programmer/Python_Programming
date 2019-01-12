# Working with var-arg methods

def sample(*var):
    print("Var-Arg Function")
'''
sample()
sample(10)
sample(10,20)
sample('Manikanta',10)
sample(10,20,'Manikanta',40)
'''

def sumFunction(*val):
    sum = 0
    for result in val:
        sum = sum + result
    return sum

print(sumFunction(10,20,30,40,50))

def sumFunction1(*val,name):
    sum = 0
    for result in val:
        sum = sum + result
    print("The Sum by",name,":",sum)
sumFunction1(10,20,30,40,50,name = 'Manikanta')

def sumFunction2(name,*val):
    sum = 0
    for result in val:
        sum = sum + result
    print("The sum by",name,":",sum)
sumFunction2('Manikanta',10,20,30,40,506,60)