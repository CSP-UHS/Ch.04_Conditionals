'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
run = True
while run is True:
    # Takes relevant input to calculate the users final grade
    sem_grade = float(input("What is your semester grade? "))
    fin_grade = float(input("What is your final exam grade? "))
    fin_worth = float(input("What % is your final exam worth? "))
    sem_worth = 100 - fin_worth

    # Sets the grading scale
    A = range(90, 101)
    B = range(80, 90)
    C = range(70, 80)
    D = range(60, 70)
    F = range(0, 60)

    # Calculates the users final grade
    sem_grade = sem_grade * (sem_worth/100)
    fin_grade = fin_grade * (fin_worth/100)
    grade = int(round(sem_grade + fin_grade, 1))

    # Calculates and set's the letter grade based on percentage
    if grade in A:
        letter = 'A'
    elif grade in B:
        letter = 'B'
    elif grade in C:
        letter = 'C'
    elif grade in D:
        letter = 'D'
    elif grade in F:
        letter = 'F'

    # prints the users final grade
    if letter != 'F':
        print("Your final grade is: " + str(grade) + " That's a " + letter + "!\n")
    else:
        print("You failed! Transfer to Johnston!")

    again = input("Would you like to calculate another grade? y/n")
    if again.lower() == 'y':
        continue
    else:
        break
