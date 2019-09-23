'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
Sem_Grade=float(input("What is the semester grade?"))
Final_Exam=float(input("What is the final exam?"))
Exam_Worth=float(input("What is the exam worth?"))
Exam_Worth=Exam_Worth/100
x=1-Exam_Worth
Final_Grade=(Sem_Grade* x)+(Final_Exam*Exam_Worth)
print(Final_Grade)