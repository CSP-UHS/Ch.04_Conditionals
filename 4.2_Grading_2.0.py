'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print()
print("Welcome to the grade calculator")
print()
sem_g = float(input("What is your Semester Grade:"))
print()
final_g = float(input("What is your Final Exam Grade:"))
print()
final_w = float(input("What is your Final Exam Worth (decimal):"))
sem_w = 1-final_w
over = (sem_g*sem_w)+(final_g*final_w)
print()
print("Your final grade will be", over)
print()
if over >= 90:
    print("A")
elif over >= 80:
    print("B")
elif over>= 70:
    print("C")
elif over >= 60:
    print("D")
else:
    print("Your transfer notice to johnston has been sent")
