'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
SG=int(input("What is the Semester Grade?"))
FE=int(input("What was your Final Exam Grade?"))
EW=int(input("What Weight is the Exam Worth?"))
p=EW/100
s=1-p
OG=(SG*s)+(p*FE)
print("Your Overall grade is",OG)
if OG>=90:
    print("Your Letter Grade is A")
elif OG>=80:
    print("Your Letter Grade is B")
elif OG>=70:
    print("Your Letter Grade is C")
elif OG>=60:
    print("Your Letter Grade is D")
else:
    print("Your Letter Grade is F, Transfer to Johnston!!")