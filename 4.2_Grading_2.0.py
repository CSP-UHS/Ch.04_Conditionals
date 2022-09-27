'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
SG = float(input("What is your Semester Grade? "))
FE = float(input("What is your final Exam Grade? "))
EX = float(input("What is your Exam Worth? "))
FR = (EX/100)
WO = ((100-EX)/100)
OA = ((SG*WO)+(FE*FR))
print("Your overall grade is: ",OA,)

if OA>89:
    print("Numerical Grade: A+")
elif OA>79 and OA<90:
    print("Numerical Grade: A")
elif OA>74 and OA<80:
    print("Numerical Grade: B+")
elif OA>69 and OA<75:
    print("Numerical Grade: B")
elif OA>64 and OA<70:
    print("Numerical Grade: C+")
elif OA>59 and OA<65:
    print("Numerical Grade: C")
elif OA>54 and OA<60:
    print("Numerical Grade: D+")
elif OA>49 and OA<55:
    print("Numerical Grade: D")
elif OA>39 and OA<50:
    print("Numerical Grade: E")
elif OA>-1 and OA<40:
    print("Numerical Grade: F")

if OA<51:
    print("Transfer to Johnston!")
