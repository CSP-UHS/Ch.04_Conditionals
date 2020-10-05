'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sem_grade = float(input("Semester Grade: "))
fin_grade = float(input("Final Exam Grade: "))
weight = float(input("Exam Weight: "))
sem_grade = sem_grade*(100-weight)  # Multiplies semester grade by semester weight
fin_grade = fin_grade*weight  # Multiplies final grade by final weight
overall = float(sem_grade+fin_grade)  # Adds semester grade and final grade
overall = overall/100  # Turns the value into tens values
print()
if 93 <= overall:  #
    print("Overall Grade: ",overall," (A)")
elif 90 <= overall < 93:
    print("Overall Grade: ",overall," (A-)")
elif 83 <= overall < 90:
    print("Overall Grade: ",overall," (B)")
elif 80 <= overall < 83:
    print("Overall Grade: ",overall," (B-)")
elif 73 <= overall < 80:
    print("Overall Grade: ",overall," (C)")
elif 70 <= overall < 73:
    print("Overall Grade: ",overall," (C-)")
elif 63 <= overall < 70:
    print("Overall Grade: ",overall," (D)")
elif 60 <= overall < 63:
    print("Overall Grade: ",overall," (D-)")
else:
    print("Overall Grade: ",overall," (F)")