'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semgrade = input("What was your semester grade? ")
finalgrade = input("What was your Final Exam grade? ")
weight = input("What is the weight of the exam? (ex: 20% would be 20) ")

semweight = (100 - int(weight)) * 0.01
semweightgrade = int(semgrade) * semweight

finalweightgrade = int(finalgrade) * int(weight) *0.01

overall = semweightgrade + finalweightgrade
overall = round(overall,1)
print ("Your overall grade is " +str(overall))

if overall >= 90:
    print("Letter Grade: A")
elif overall >= 80:
    print("Letter Grade: B")
elif overall >= 70:
    print("Letter Grade: C")
elif overall >= 60:
    print("Letter Grade: D")
elif overall <= 60:
    print("Letter Grade: F")
    print("Transfer to Johnston!")
else:
    print("Woah, How did you break this?")