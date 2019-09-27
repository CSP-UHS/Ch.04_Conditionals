'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
S = int(input("enter semester grade"))
F = int(input("enter final exam percentage"))
W = int(input("enter the weight of the final exam"))
x = W/100
y = 1-x
grade = print("your overall grade is",((S*y)+(x*F)))

if grade < 59
    print("you have an F.  Move to Johnston!!")

