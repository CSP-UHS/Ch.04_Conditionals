'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

SG=float(input("What's your grade?"))
TG=float(input("What is your score?"))
EW=float(input("How much is your test worth?"))
EW=EW/100
GW=1-EW
FG=SG*GW+TG*EW
if 93<= FG and FG <= 100:
    print("Your grade is an A",FG)
elif 90<=FG and FG<93:
    print("Your grade is an A-",FG)
elif 80<=FG and FG<=89:
    print("Your grade is a B",FG)
elif 70<=FG and FG<=79:
    print("Your grade is a C",FG)
else:
    print("Falure, Transfure to Johnston")
