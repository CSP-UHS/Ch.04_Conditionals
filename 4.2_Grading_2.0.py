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
if overall>=90:
    print("Amazing! You managed to not disappoint your parents or the world!")
    print("A")
elif overall>=80:
    print("You can live, for now...")
    print("B")
elif overall>=70:
    print("You're so... average")
    print("C")
elif overall>=60:
    print("Everyone is disappointed in you but we still have hope")
    print("D")
else:
    print("Transfer to Johnston!")
    print("F")
print("\nHere's your overall grade:")
print(math.floor(overall))
