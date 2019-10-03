'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print("Welcome to Smith's Final Overall Grade Calculator")
SG=int(input("What is your current semester grade?"))
FE=int(input("What did you score on the final exam?"))
EW=int(input("What percentage is your exam worth?"))
GW=((EW/100)*FE)
RP=(1-(EW/100))
OG=(SG*RP)
NG=(GW+OG)
print("Your new overall grade is....", NG)
if NG<=60:
    print("You failed, Transfer to Johnston!")
elif NG>=93:
    print("You've got an A")
elif NG>=80:
    print("You've got a B")
elif NG>=70:
    print("You've got a C")
else:
    print("You've got a D")