'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
sgrade = float(input("What was your Semester Grade? "))
fegrade = float(input("What was your Final Exam Grade? "))
feworth = float(input("What % is the Final Exam worth? "))
og = sgrade * (100 - feworth) + fegrade * feworth
og/=100
if og >= 90:
    letter = "A"
elif og >=80:
    letter = "B"
elif og >= 70:
    letter = "C"
elif og >= 60:
    letter = "D"
else:
    letter = "F!!! You should transfer to johnston you moron!!!"

print("Your Overall Grade is:", letter)
