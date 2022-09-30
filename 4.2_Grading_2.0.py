'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
smgrd=float(input("what is your semester grade?: "))
fnlexm=float(input("what is your final exam grade?: "))
exmwght=float(input("what is your final exam worth?: "))
smwght=(100-exmwght)
ovrall=((smgrd*smwght)+(fnlexm*exmwght))/100
print("-----")
print("your overall grade is",ovrall,)
print("-----")
if ovrall >= 94:
    print("YOU DID AMAZING AHHHHHH GOOD JOBB AHHHH You got an A!")
if 94 > ovrall >= 90:
    print("you did good!! You got an A-")
if 90 > ovrall >= 87:
    print("Good job!!! You got a B+")
if 87 > ovrall >= 84:
    print("Woooooo!! You got a B")
if 84 > ovrall >= 80:
    print("Ayyy! You got a B-")
if 80 > ovrall >= 77:
    print("okayyy purr You got a C+")
if 77 > ovrall >= 74:
    print("you got a C bruh")
if 74 > ovrall >= 70:
    print("you got a C- you're on the brink of failing WHEW")
if ovrall < 70:
    print("YOU FAILED GO TO JOHNSTON HAHAHHAHAH AHHHHHHH")
