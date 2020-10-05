import math
'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
examgrade=float(input("What is your Final exam grade?"))
examworth=float(input("How much is the Final worth?"))
semgrade=float(input("What is your Semester grade?"))
examworth=examworth/100
examworthe=1-examworth
examgrade=examgrade*examworth
semgrade=semgrade*examworthe
overall=examgrade+semgrade

print()
if overall<60:
    print("Transfer to Johnston!")
elif overall>90:
    print("Wow! Your parents aren't disappointed at you that much than I thought")
else:
    print("You can live, for now...")
print("\nHere's your overall grade:")
print(math.floor(overall))
