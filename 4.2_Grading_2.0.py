'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

SemesterGrade=float(input("What is your semester grade?"))
FinalExamScore=float(input("What did you score on the final?"))
FinalExamWorth=float(input("What percent of your grade is the final worth?"))

FinalWeighted=FinalExamWorth/100
GradeThatCounts = SemesterGrade*(1-FinalWeighted)+FinalExamScore*(FinalWeighted)
print("Your grade that counts is", GradeThatCounts)

If GradeThatCounts>= 90:
    print("Thats an A!")
elif GradeThatCounts>= 80:
    print("Thats an B!")
elif GradeThatCounts>= 70:
    print("Thats an C!")
elif GradeThatCounts>= 60:
    print("Thats an B!")
else:
    print("You failed, transfer to Johnston you clown!")