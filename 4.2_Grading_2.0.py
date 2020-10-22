'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semester_grade=int(input("Semester Grade:"))
final_exam_grade=int(input("Final Exam Grade:"))
worth=int(input("Final Exam Worth:"))
print()
final_grade=(semester_grade*(100-worth)+(final_exam_grade*worth))/100
print("Overall:" ,final_grade)

if final_grade >=89:
    print("The grade is an A")
elif final_grade>=79:
    print("The grade is a B")
elif final_grade>=69:
    print("The grade is a C")
elif final_grade>=59:
    print("The grade is a D")
else:
    print("Transfer to Johnston!")