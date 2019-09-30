'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print("Welcome to the Grading Calculator!")
SG=int(input("What is your semester grade?"))
FE=int(input("What is your final exam grade?"))
EW=int(input("What is the exam worth?"))
EW=EW/100
overall=SG*(1-EW)+FE*(EW)
print("This is your Final Grade",overall)
if overall>70:
    PF="Passing"
else:
    PF="Failing, Transfer to Johnston!"

if overall>=93:
    G="A"
elif overall>=90 and overall<=92:
    G="A-"
elif overall>=87 and overall<=89:
    G="B+"
elif overall>=83 and overall<=86:
    G="B"
elif overall>=80 and overall<=82:
    G="B-"
elif overall>=77 and overall<=79:
    G="C+"
elif overall>=73 and overall<=76:
    G="C"
elif overall>=70 and overall<=72:
    G="C-"
elif overall>=67 and overall<=69:
    G="D+"
elif overall>=65 and overall<=66:
    G="D"

print(G,PF)

