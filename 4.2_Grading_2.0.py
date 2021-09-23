'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
grade=float(input("What is your current grade?"))
test=float(input("What do you hope to score on the test?"))
worth=float(input("How much is the test worth?"))

overall=grade*(100-worth)+test*worth
overall/=100
print("Your overall grade is:   ",overall)
if overall>89:
    print("Your letter grade is an A, good job")
if overall>79 and overall<90:
    print("Your letter grade is a B, keep going")
if overall>69 and overall<80:
    print("Your letter grade is a C, keep studying")
if overall>59 and overall<70:
    print("Your letter grade is a D, try to keep up")
if overall>0 and overall<60:
    print("You failed, great job")


