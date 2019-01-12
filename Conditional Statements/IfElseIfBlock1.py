# Assignment01 --> Student Grade system

subject1 = float(input("Enter subject1 marks:"))
subject2 = float(input("Enter subject2 marks:"))
subject3 = float(input("Enter subject3 marks:"))
subject4 = float(input("Enter subject4 marks:"))
subject5 = float(input("Enter subject5 marks:"))
subject6 = float(input("Enter subject6 marks:"))

total = (subject1 + subject2 + subject3 + subject4 + subject5 + subject6)

totalMarks = total / 6

if totalMarks >= 90 and totalMarks < 100:
    print("Grade : O")
elif totalMarks >= 80 and totalMarks < 90:
    print("Grade : A1")
elif totalMarks >=70 and totalMarks < 80:
    print("Grade : A2")
elif totalMarks >= 60 and totalMarks < 70:
    print("Grade : B1")
elif totalMarks >= 50 and totalMarks < 60:
    print("Grade : B2")
elif totalMarks >= 40 and totalMarks < 50:
    print("Grade : C1")
else:
    print("Fail : F")

print(totalMarks)