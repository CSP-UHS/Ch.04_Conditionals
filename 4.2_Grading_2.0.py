'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sem= int(input("Please enter your semester grade: "))
final= int(input("Please enter your final exam grade: "))
worth= int(input("Please enter your exam worth: "))
overall= (sem*((100-worth)/100))+(final*(worth/100))
if overall > 92:
    letter = "A"
elif overall > 87:
    letter = "A-"
elif overall > 85:
    letter = "B+"
elif overall > 82:
    letter = "B"
elif overall > 77:
    letter = "B-"
elif overall > 75:
    letter = "C+"
elif overall > 72:
    letter = "C"
elif overall > 67:
    letter = "C-"
elif overall > 65:
    letter = "D+"
elif overall > 62:
    letter = "D"
elif overall > 50:
    letter = "D-"
else:
    letter = "F"
    overall = "Transfer to Johnston!"
print("This is your overall final grade:",letter, "" ,overall,)