'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
sem = int(input("What is your semester grade?"))
final = int(input("What is your final exam grade?"))
worth = int(input("What is the exam worth?"))
second_worth = 100 - worth
worth2 = worth * .01
second_worth2 = second_worth * .01
final_grade = (second_worth2*sem) + (worth2*final)
print(final_grade)

if final_grade <= 100 and final_grade >= 90:
    print("A")
elif final_grade < 90 and final_grade >= 80:
    print("B")
elif final_grade < 80 and final_grade >= 70:
    print("C")
elif final_grade < 70 and final_grade >= 60:
    print("D")
else:
    print("F")
    print("Transfer to Johnston!!!!!!")
