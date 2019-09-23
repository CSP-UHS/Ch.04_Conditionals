'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semester_grade=float(input("whats your semester grade?"))
final_exam_grade=float(input("whats your final exam grade?"))
final_exam_worth=float(input("whats your final exam worth?"))
final_exam_worth=final_exam_worth/100
semester_grade_worth=1-final_exam_worth
avg=semester_grade*semester_grade_worth+final_exam_grade*final_exam_worth
print(avg)

if avg > 93:
    print("You got an A.")
elif avg < 89 and avg > 80:
    print("You got a B")
elif avg < 70 and avg > 60:
    print("You got a C")
elif avg < 60 and avg > 40:
    print("You got a D")
else:
    print("You failed. Transfer to Johnston!")
