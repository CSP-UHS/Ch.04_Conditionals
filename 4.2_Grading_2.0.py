'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sem = float(input("Enter your semester grade as an integer: "))
final = float(input("Enter your final exam grade as an integer: "))
fw = float(input("Enter your final exam grade weight as a decimal: "))
sw = 1.00-fw
overall = sem*sw+final*fw
print("Your overall grade is",overall,)

if overall <=100 and overall >=94:
    print("Your final grade is and A, GOOD JOB")
elif overall <94 and overall >=90:
    print("Your final grade is an A-, GOOD JOB")
elif overall <90 and overall >=87:
    print("Your final grade is an B+, IVE SEEN BETTER")
elif overall <87 and overall >=83:
    print("Your final grade is an B, IVE SEEN BETTER")
elif overall <83 and overall >=80:
    print("Your final grade is an B-, NOT THE WORST IVE SEEN")
elif overall <80 and overall >=77:
    print("Your final grade is an C+, STILL A GOOD GRADE I GUESS")
elif overall <77 and overall >=73:
    print("Your final grade is an C, STILL A GOOD GRADE I GUESS")
elif overall <73 and overall >=70:
    print("Your final grade is an C-, YOU CAN STILL RETAKE RIGHT?")
elif overall <70 and overall >=67:
    print("Your final grade is an D+, YOU CAN STILL RETAKE RIGHT?")
elif overall <67 and overall >=60:
    print("Your final grade is an D, WOW I ACTUALY THOUGHT YOU WOULD FAIL")
else :
    print("Your final grade is an F, YOUR TERRIBLE AND ARE DOOMED TO FAIL GO TO JOHNSTON NERD")

