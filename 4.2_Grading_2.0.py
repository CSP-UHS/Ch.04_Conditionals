'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
og = int(input("Enter your current grade: "))
fg = int(input("Enter the final grade: "))
worth = int(input("Enter the final worth: "))
worthperc = worth/100
ogperc = 1-worthperc
total = (og*ogperc) + (fg*worthperc)
if total >= 90:
    print("Your grade is an A!")
if total < 90 and total >= 80:
    print("Your grade is a B!")
if total < 80 and total >= 70:
    print("Your grade is a C.")
if total < 70 and total >= 60:
    print("Your grade is a D.")
if total < 60:
    print("Transfer to Johnston!")
print("Your percentage is:" ,total,end='')