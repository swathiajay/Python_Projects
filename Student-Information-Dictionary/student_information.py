student = {}
n = int(input("Enter number of student:"))
for i in range(n):
    print("\nEnter details of the student")
    reg = input("Register number:")
    name = input("Student name:")
    python = int(input("Python marks:"))
    maths = int(input("Maths marks:"))
    english = int(input("English marks:"))
    total = python+maths+english
    average = round(total / 3, 2)
    if average>=90:
        grade = "A"
    elif average>=80:
        grade = "B"
    elif average>=70:
        grade = "C"
    elif average>=60:
        grade = "D"
    else:
        grade = "F"
    student[reg] = {"name":name,
                    "marks":{
                        "Python":python,
                        "Maths":maths,
                        "English":english
                    },
                    "total":total,
                    "average":average,
                    "grade":grade
    }
    print("\n---Student Information---")
    for reg,details in student.items():
        print("\nRegister Number:",reg)
        print("Name:",details["name"])
        print("Python:",details["marks"]["Python"])
        print("Maths:",details["marks"]["Maths"])
        print("English:",details["marks"]["English"])
        print("Total:",details["total"])
        print("Average:",details["average"])
        print("Grade:",details["grade"])
highest_average = 0
top_student = ""
for reg,details in student.items():
    if details["average"]>highest_average:
        highest_average = details["average"]
        top_student = details["name"]
print("\n--Highest Average---")
print("Student:",top_student)
print("Average:",highest_average)
class_total = 0
for reg,details in student.items():
    class_total+=details["average"]
class_average = class_total / len(student)
print("\nClass Average:",class_average)
print("\n---Students Above Class Average---")
for reg,details in student.items():
    if details["average"]>class_average:
        print(details["name"],"-",details["average"])
search_reg = input("\nEnter register number of search:")
if search_reg in student:
    details = student[search_reg]
    print("\n---Student Found---")
    print("Register Number:",search_reg)
    print("Name:",details["name"])
    print("Total:",details["total"])
    print("Average:", details["average"])
    print("Grade:",details["grade"])
else:
    print("Student not found")

        



















    
