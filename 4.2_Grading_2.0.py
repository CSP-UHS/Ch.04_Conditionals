'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
semG = float(input("What is the semester grade"))
FE = float(input("what did you get on the Final exam"))
EW = float(input("how much is the exam worth"))
semw = 100-EW
OG = (semG*semw/100)+(FE*EW/100)
print("your overall grade is", OG)
if OG >= 90:
    print("You got an A")
elif OG >= 80:
    print("You got a B")
elif OG >= 70:
    print("You got a C")
else:
    print("Transfer to Johnston!")