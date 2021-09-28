'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
examy= float(input("What did you get on the final"))
semy= float(input("What's your grade for this semester?"))
exvis= float(input("How much did the exam change your grade"))
exvis/=100
overall= (examy*exvis)+(semy)*(1-exvis)
print("your final grade for the class was" ,overall,"%")
if overall >= 90:
    print("you have an A")
elif overall <= 89 and overall >=80:
    print("you have a B")
elif overall <=79 and overall >=70:
    print("you have a C")
elif overall <= 69 and overall >= 60:
    print("you have a D")
else:
    print("Your grade sucks,transfer to johnston")
