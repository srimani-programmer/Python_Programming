# Working with var-arg functions as key value pairs

def details(**values):
    for keys,valuePairs in values.items():
        print(keys,":",valuePairs)

details(name = 'sriManikanta',age = 18,DOB = '18-may-1999',nativePlace = 'HanumanJunction')
details(name = 'naveen',age = 20 , DOB = '24-sep-1997',hobbies = '''playing cricket,watchin
g tv,betting and many more''',profession = "Enterpenuer")