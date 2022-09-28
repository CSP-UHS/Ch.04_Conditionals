'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''


sg = int(input("What was your Semester grade?"))
fg = int(input("What was your Final grade?"))
w= int(input("What was your Final Exam worth?"))/100
r = (1-w)
FinalGrade=float((sg*r+fg*w))
print(FinalGrade)

if FinalGrade >= 90:
    print("Good Job! It's an A")
elif FinalGrade >= 80:
    print("You got a B!")
elif FinalGrade >= 70:
    print("You got a C")
elif FinalGrade >= 60:
    print("You can do better than a D!")
elif FinalGrade < 60:
    print("F. Transfer to Johnston!")