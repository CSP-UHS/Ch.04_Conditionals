'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
S = int(input("enter semester grade"))
F = int(input("enter final exam percentage"))
W = int(input("enter the weight of the final exam"))
x = W/100
y = 1-x
grade = (S*y)+(x*F)
print("your overall grade is",grade)

if grade < 59:
    print("you have an F.  Move to Johnston!!")
elif grade > 59 and grade <= 66:
    print("you have a D in your class.")
elif grade >= 67 and grade <=69:
    print("you have a D+ in your class")
elif grade >=70 and grade <=72:
    print("you have a C- in your class")
elif grade >= 73 and grade <=76:
    print("you have a C in your class")
elif grade >= 77 and grade <=79:
    print("you have a C+ in your class")
elif grade >= 80 and grade <=83:
    print("you have a B- in your class")
elif grade >= 83 and grade <=86:
    print("you have a B in your class")
elif grade >= 87 and grade <=89:
    print("you have a B+ in your class")
elif grade >= 90 and grade <=93:
    print("you have an A- in your class")
elif grade >= 94 and grade <=100:
    print("you have an A in your class")

