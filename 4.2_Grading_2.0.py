'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sem= float(input("Enter your Semester Grade:"))
final= float(input("Enter your Final Exam results:"))
worth= float(input("Enter your Exam Worth:"))
worth= .01* worth
worth2 = 1-worth
grade = sem*worth2+final*worth
print("Your overall grade is:", sem*worth2+final*worth )
if grade >= 92:
    print("A")
elif grade >= 90:
    print("A-")
elif grade >= 88:
    print("B+")
elif grade >= 82:
    print("B")
elif grade >= 80:
    print("B-")
elif grade >= 78:
    print("C+")
elif grade >= 72:
    print("C")
elif grade >= 70:
    print("C-")
elif grade >= 65:
    print("D")
else:
    print("F")
    print("Transfer to Johnston!")