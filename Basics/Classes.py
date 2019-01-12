# Creating class and object

class Student:

    def __init__(self,name,roll):
        self.sname = name
        self.sno = roll

    def display(self):
        print("My Name is:",self.sname)
        print("My roll number is:",self.sno)

obj1 = Student("Sri Manikanta",'16D41A05F0')
obj1.display()