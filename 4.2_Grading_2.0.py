'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("This is a final grade calculator")
sem=float(input("What is your semester grade?"))
fin=float(input("What did you get on your final exam?"))
wor=float(input("How much is your exam worth"))
print("Your final grade is:",(sem*((100-wor)/100)+fin*(wor/100)))
x=(sem*((100-wor)/100)+fin*(wor/100))
if x<60:
    print("You failed")
    print("Transfer to Johnston")
elif x>=90:
    print("You got an A")
elif x<90 and x>=80:
    print("You got an B")
elif x<80 and x>=70:
    print("You got an C")
elif x<70 and x>=60:
    print("You got a D")