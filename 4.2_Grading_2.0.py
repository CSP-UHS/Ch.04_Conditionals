'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
Sem_Grade = float(input("sem grade:"))
Final_Exam = float(input("Final Exam"))
Exam_worth = float(input("Exam_Worth"))
Answer = ((Sem_Grade*(100-Exam_worth)+(Final_Exam*Exam_worth))/100)
Grade_Percent = Answer

if Grade_Percent >= 100:
    Msg = "Awesome Job you got all questions correct for an A+"
elif  Grade_Percent > 90:
    Msg = "Great Job you Got an A"
elif  Grade_Percent >= 80:
    Msg = "Great Job you Got an B"
elif  Grade_Percent >= 70:
    Msg = "Great Job you Got an C"
elif  Grade_Percent >= 60:
    Msg = "You barely passed with an D"
else:
    Msg = "You failed you loser!! don't get a F again loser"

print(Msg)
