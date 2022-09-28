'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sg = float(input("What is your grade of the semester? "))
fe = float(input("What did you get on the final exam? "))
ew = float(input("What is the final exam worth? "))
ew = ew/100
sw = 1-ew
o = (sg*sw)+(fe*ew)

if o >= 93:
    letter = "A"
elif o >= 90:
    letter = "A-"
elif o >= 87:
    letter = "B+"
elif o >= 83:
    letter = "B"
elif o >= 80:
    letter = "B-"
elif o >= 77:
    letter = "C+"
elif o >= 73:
    letter = "C"
elif o >= 70:
    letter = "C-"
elif o >= 67:
    letter = "D+"
elif o >= 65:
    letter = "D"
else:
    letter = "F"

print("Your overall grade is",o,",", letter)

if letter == "F":
    print("Transfer to Johnston")