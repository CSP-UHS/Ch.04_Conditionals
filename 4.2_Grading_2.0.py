'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
sg=int(input("What's your semester grade?: "))
fe=int(input("What did you get on your final exam?: "))
ew=int(input("How much was the final exam worth?: "))
ew=ew/100
overall=sg*(1-ew)+fe*(ew)


if overall >= 90:
    print("You got an A")
elif overall >= 80:
    print("You got a B")
elif overall >=70:
    print("You got a C")
elif overall >=60:
    print("You got a D")
else:
    print("Transfer to Johnston")