'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''


print()
semester=int(input("What is your current semester grade: "))
Test=int(input("What is your Test Grade: "))
Worth=int(input("What is the Test worth: "))
Worth=(Worth/100)
Final=semester*(1-Worth) + Test*(Worth)
print()
if Final>=93:
    print("you got an A Great Job!")
elif Final>=90:
    print("You got an A- Great Job.")
elif Final>=87:
    print("you got a B+ Great Job.")
elif Final>=83:
    print("you got a B Great.")
elif Final>=80:
    print("you got a B- Great.")
elif Final>=77:
    print("you got a C+ Might wanna retake")
elif Final>=73:
    print("you got a C Might wanna retake")
elif Final>=70:
    print("you got a C- Might wanna retake")
elif Final>=67:
    print("you got a D+ your gonna need to retake")
elif Final>=63:
    print("you got a D your gonna need to retake")
elif Final>=60:
    print("you got a D- your gonna need to retake")
elif Final<60:
    print("you got a F you better transfer to Johnston!")
print("This is your final grade",Final)
