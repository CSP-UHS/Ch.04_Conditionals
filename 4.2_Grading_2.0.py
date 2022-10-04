'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semester = float(input("What is your semester grade?"))
final = float(input("What was your final grade in the class?"))
tw = float(input("What is the weight of the test?"))
tw=tw/100
gw=1-tw
ave = (gw*semester + tw*final)

# over = semester+final+tw/3


print("Your overall grade was", ave, "for the class!")

if ave <= 59:
    print("Failed! Transfer to Johnston!")
if ave >= 60 and ave <=69:
    print("D")
if ave >=70 and ave<=79:
    print("C")
if ave >=80 and ave <=89:
    print("B")
if ave >=90 and ave <=100:
    print("A")

