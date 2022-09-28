'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
grade = int(input("What is your number grade for the class?"))
if grade>=97 and grade<=100:
    print("You have an A+ great job!")
elif grade>100:
    print("That's not a valid number.")
elif grade<=96 and grade>=93:
    print("Nice! You have an A")
elif grade<=92 and grade>=90:
    print("Cool! You're at an A-")
elif grade<=89 and grade>=87:
    print("You're at a B+")
elif grade<=86 and grade>=83:
    print("You're getting there! You're at a B")
elif grade<=82 and grade>=80:
    print("Keep trying! You're at a B-")
elif grade<=79 and grade>=77:
    print("Seems like you should study more, you're at a C+")
elif grade<=76 and grade>=73:
    print("You're at a C, do better.")
elif grade<=72 and grade>=70:
    print("You have a C-, really?")
elif grade<=69 and grade>=67:
    print("You have a D+, get help.")
elif grade<=66 and grade>=65:
    print("You have a D, how did this even happen?")
elif grade<=64 and grade>=63:
    print("You have a D-, you're clearly gonna fail this class.")
elif grade<=62 and grade>=1:
    print("You have failed this class.")
elif grade<1:
    print("That's not a valid number.")