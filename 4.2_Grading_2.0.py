'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
sem_Grade = int(input("Enter your semester grade:"))
final_Exam = int(input("Enter your score for your final exam:"))
exam_Worth = int(input("Enter the % of your grade the exam is worth:"))
exam_Worth: float = exam_Worth/100
overall_Grade = sem_Grade*(1-exam_Worth)+final_Exam*exam_Worth
if overall_Grade < 65:
    print("This is your overall grade:", overall_Grade, "which is a F")
elif overall_Grade >= 90:
    print("This is your overall grade:", overall_Grade, "which would be an A")
elif overall_Grade >= 80 and overall_Grade < 90:
    print("This is your overall grade:", overall_Grade, "which is a B")
elif overall_Grade >= 70 and overall_Grade < 80:
    print("This is your overall grade:", overall_Grade, "which would be a C")
elif overall_Grade >= 65 and overall_Grade <70:
    print("This is your overall grade:", overall_Grade, "which is a D")