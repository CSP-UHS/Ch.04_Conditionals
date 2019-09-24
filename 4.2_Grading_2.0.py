'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("Hi, I hope you are not too worried about your overall grades!\nHere's something to help, though.")
sem_grade=int(input("What is your semester grade? "))
fin_grade=int(input("What is your final exam grade? "))
fin_worth=float(input("What is your final exam worth written as a decimal? "))
sem_worth=1-fin_worth
ovr_grade=(sem_grade*sem_worth)+(fin_grade*fin_worth)
if ovr_grade >=90:
    print("Your overall grade is an A and",ovr_grade)
elif ovr_grade <90 and ovr_grade >=80:
    print("Your overall grade is a B and",ovr_grade)
elif ovr_grade <80 and ovr_grade >=70:
    print("Your overall grade is a C and",ovr_grade)
elif ovr_grade <70 and ovr_grade >=60:
    print("Your overall grade is a D and",ovr_grade)
else:
    print("Your overall grade is a F and",ovr_grade)
    print("Transfer to Johnston!")