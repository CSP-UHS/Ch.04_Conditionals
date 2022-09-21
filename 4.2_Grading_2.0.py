'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
g = float(input("What is your grade?"))

if g > 90:
    print("You got an A.")
elif g > 80:
    print("You got a B.")
elif g > 70:
    print("You got a C.")
else:
    print("Transfer to Johnston!")