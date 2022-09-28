'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
# if __ is greater than 95, then print a
# # # if __ is between __ and __, then print ___
# Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
# Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
# Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6

semGrade = float(input("What is the semester grade?"))
finExam = float(input("What is the final exam's grade?"))
examW = float(input("What is the exam worth?"))
Percent = float(examW/100)
Overall = ((finExam*Percent)+((1-Percent)*semGrade))
if Overall >= 97:
    print("A+")
elif 90 < Overall < 97:
    print("A")
elif 80 < Overall < 90:
    print("B")
elif 70 < Overall < 80:
    print("C")
elif 60 < Overall < 70:
    print("D")
elif 92 < Overall < 95:
    print("F")
    print("Transfer to Johnston!")
