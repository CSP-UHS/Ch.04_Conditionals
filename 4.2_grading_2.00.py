'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("Hey! calculate your Overall exam score!!")
S=int(input("Sem Grade:"))
F=int(input("Final Exam:"))
E=int(input("Exam worth in %:"))
E=E/100
overal=S*(1-E)+F*(E)

if overal >= 100:
    A= "You are smart"
elif overal >= 93:
    A = "A"
elif overal >= 90:
    A = "A-"
elif overal >= 87:
    A = "B+"
elif overal >= 83:
    A = "B"
elif overal >= 80:
    A = "B-"
elif overal >= 77:
    A = "C+"
elif overal >= 73:
    A = "C"
elif overal >= 70:
    A = "C-"
elif overal >= 67:
    A = "D+"
elif overal >= 65:
    A = "D"
else:
    A = "Transfer to Johnston!"
print(overal, A)
