'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sem_grade=float(input("Enter Semester Grade here: "))
final_exam=float(input("Enter Final Exam here: "))
exam_worth=float(input("Enter Percent value of final exam here: "))
final_exam_worth=(exam_worth/100)
sem_grade_worth=((100-exam_worth)/100)
overall=(sem_grade*sem_grade_worth+final_exam*final_exam_worth)
print(overall)
if overall>=90:
    print("A")
elif overall>=80:
    print("B")
elif overall>=70:
    print("C")
elif overall>=60:
    print("D")
else:
    print("Transfer to Johnston!")