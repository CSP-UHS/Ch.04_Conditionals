'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("Hello there student!")
sg = int(input("What was your Semester Grade?"))
fg = int(input("Nice! What was your Final grade?"))
w = int(input("What was your Final Exam worth?"))/100
r = (1-w)
FinalGrade = float((sg*r+fg*w))
print(FinalGrade)

if FinalGrade >= 90:
    print("A")
elif FinalGrade >= 80:
    print("B")
elif FinalGrade >= 70:
    print("C")
elif FinalGrade >= 60:
    print("D")
else:
    print("Transfer to Johnston")
    print("You got an F")
