'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

letterGrades = \
    {"A": 93, "A-": 90, "B+": 87, "B": 83, "B-": 80, "C+": 77, "C": 73, "C-": 70, "D+": 67, "D": 63, "D-": 60, "F": 0}

def overallGrade(sem,final,worth) :
    return sem*(1-worth/100) + final*(worth/100)

def toLetterGrade(percent) :
    for i in letterGrades :
        if percent >= letterGrades.get(i) :
            return i


userSemesterGrade = float(input("What is your semester grade? (%)\n"))
userFinalGrade = float(input("What is your final grade? (%)\n"))
userFinalWorth = float(input("How much is your final worth? (%)\n"))

userOverall = overallGrade(userSemesterGrade,userFinalGrade,userFinalWorth)

print("Your final grade is {}% ({})!{}".format(userOverall,toLetterGrade(userOverall),(userOverall < 60) and " Transfer to Johnston!" or ""))
