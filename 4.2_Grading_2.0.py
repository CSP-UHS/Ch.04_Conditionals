'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

semesterGrade = float(input("What was your semester grade?"))
finalExam = float(input("What did you get on your final exam?"))
examWorth = float(input("What was your final exam worth?"))/100
semesterWorth = 1-examWorth
overall = semesterWorth*semesterGrade+finalExam*examWorth
print(overall)
if overall >= 90:
    print("Congratulations you got an A")
elif 89 >= overall >= 80:
    print("Congratulations you got a B, you could do better though")
elif 79 >= overall >= 70:
    print("Really a C are you proud of that?")
elif 69 >= overall >= 60:
    print("Cmon a D you should be ashamed, go home and eat some oatmeal")
else:
    print("F, Leave go to Johnston")