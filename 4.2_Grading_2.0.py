'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sem_grade = int(input("please enter your semester grade:"))
final_exam = int(input("please enter your final exam score:"))
exam_worth = int(input("please enter what the exam is worth:"))
grade_worth = 100-exam_worth
overall = (sem_grade*grade_worth*.01)+(final_exam*exam_worth*.01)
print("your overall grade in the class is",overall,"%")

if overall>=93.0:
    print("Your letter grade is an A")
    print("Amazing Job!")
elif overall>=90.0 and overall<=92.9:
    print("Your letter grade is an A-")
    print("Great Job!")
elif overall>=87.0 and overall<=89.9:
    print("Your letter grade is a B+")
    print("Good Job!")
elif overall>=83.0 and overall<=86.9:
    print("Your letter grade is a B")
    print("Nice Job!")
elif overall>=80.0 and overall<=82.9:
    print("Your letter grade is a B-")
    print("Pretty good.")
elif overall>=77.0 and overall<=79.9:
    print("Your letter grade is a C+")
    print("You did ok.")
elif overall>=73.0 and overall<=76.9:
    print("Your letter grade is a C")
    print("Average.")
elif overall>=70.0 and overall<=72.9:
    print("Your letter grade is a C-")
    print("Just enough.")
elif overall>=67.0 and overall<=69.9:
    print("Your letter grade is a D+")
    print("Barely enough.")
elif overall>=65.0 and overall<=66.9:
    print("Your letter grade is a D")
    print("At least you passed.")
elif overall<65.0:
    print("FAILED!!!!!! YOU STINK")
    print("TRANSFER TO JOHNSTON!!!")
