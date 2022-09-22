'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("Hey I know you suck at your classes but everything will be ok. Let's take a look at your grades.")
semGrade = float(input("What is your grade for this semester?"))
finExam = float(input("What did you get on your final exam?"))
examWorth = float(input("How much was the final worth?"))
overall = (finExam*(examWorth/100))+(semGrade*((100-examWorth)/100))

print("Your final grade for the year is" ,overall,"%. Good Job")
if overall>=93:
    print("Your letter is an A. Fantastic work!")
elif overall>=90:
    print("Your letter is an A-. Great work.")
elif overall>=87:
    print("Your letter is an B+. Good work.")
elif overall>=83:
    print("Your letter is an B. Good Job.")
elif overall>=80:
    print("Your letter is an B-. Good work.")
elif overall>=77:
    print("Your letter is an C+. Good work.")
elif overall>=73:
    print("Your letter is an C. Good work.")
elif overall>=70:
    print("Your letter is an C-. Okay work.")
elif overall>=67:
    print("Your letter is an D+. Did you try.")
elif overall>=63:
    print("Your letter is an D. It's alright.")
elif overall>=60:
    print("Your letter is an D-. Feel bad about yourself.")
else:
    print("How dumb are you? Maybe Johnston will take you idiotic self. LEAVE!")