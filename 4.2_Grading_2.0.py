'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
grade = int(input("What is your current grade? "))
exam = int(input("What do you want to get on the exam? "))
examWorth = int(input("How much of your grade is the exam worth? "))
gradeWorth = (100-examWorth)/100
newGrade = round(((grade*gradeWorth)+(exam*(examWorth/100))),1)

if newGrade <= 100 and newGrade >= 90:
    print("Your grade will be "+str(newGrade)+"%. That's an A.")
elif newGrade < 90 and newGrade >=80:
    print("Your grade will be "+str(newGrade)+"%. That's a B.")
elif newGrade < 80 and newGrade >= 70:
    print("Your grade will be "+str(newGrade)+"%. That's a C.")
elif newGrade < 70 and newGrade >= 60:
    print("Your grade will be "+str(newGrade)+"%. That's a D.")
else:
    print("Your grade is so bad I don't want to tell you. Go transfer to Johnston!! >:(")