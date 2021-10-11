'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print("Welcome to grading software v1.1 (Unstable build, may explode upon error")
SG = float(input("What is your semester grade"))
TS = float(input("What is the score of the test"))
TW = float(input("How much is the test worth?"))

endscore = SG*(100-TW) + TS * TW
endscore /=100

if endscore >=90:
    print("Good job, you got an A (A- is basically a knock off A)")
elif endscore >=80:
    print("good job, you got a B")
elif endscore >=70:
    print("Sadly, you got a C")
elif endscore >=60:
    print("Can't even compete with that D grade ")
else:
    print("Transfer to Johnston")
print("The overall grade is", endscore,)
