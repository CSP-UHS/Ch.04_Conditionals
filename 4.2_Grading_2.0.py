'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
SemesterGrade=float(input("what is your semester grade?"))
FinalExamGrade=float(input("what is your Final Exam Grade?"))
FinalExamWorth=float(input("How heavily was your test Weighted?"))
FinalExamWorth/=100
Average=SemesterGrade*(1-FinalExamWorth)+FinalExamGrade*(FinalExamWorth)
print("Your Overall Is",Average)

if Average >=90:
    print("That happens to be an A")
elif Average>=80:
    print("That's a B")
elif Average>=70:
    print("That's a C bud")
elif Average>=60:
    print("That's a D Sadly")

else:
    print("that's an F and a free transfer to Johnston")