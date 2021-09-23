'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
sem= float(input("What's your grade for this semester?"))
exa= float(input("What's did you get on finals?"))
exv= float(input("How much did the exam impact your grade?"))
exv/=100
overall= (exa*exv)+(sem)*(1-exv)
print ("Your overall grade for the class was",overall,"!")
if overall >=93:
    print ("Your letter grade is a A! Congrats!")
elif overall >=90:
    print ("Your letter grade is a A-! Congrats!")
elif overall >=87:
    print ("Your letter grade is a B+! Congrats!")
elif overall >=83:
    print ("Your letter grade is a B!Congrats!")
elif overall >=80:
    print ("Your letter grade is a B-, You passed!")
elif overall >=77:
    print ("Your letter grade is a C+, You passed!")
elif overall >=73:
    print ("Your letter grade is a C, You passed!")
elif overall >=70:
    print ("Your letter grade is a C-, You passed!")
elif overall >=67:
    print ("Your letter grade is a D+, You barley passed")
elif overall >=65:
    print ("Your letter grade is a D, You barley Passed")
else:
    print ("Yikes! Seems that you failed, try to study next time!")