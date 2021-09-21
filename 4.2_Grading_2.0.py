'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"

Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''

'''
sem_grade: the overall semester grade
sem_value: how much the semester was worth
exam_grade: the overall exam grade
exam_value: how much the exam was worth
'''
sem_grade = float(input("Please input your semester grade excluding the final exam: "))  # Asks for the semester grade
exam_grade = float(input("Please input your overall exam grade: "))  # Asks for the exam grade
exam_value = float(input("Please input your overall exam worth: "))  # Asks how much the exam was worth

# Checks is the user's exam value is a decimal, or not.
if 1 <= exam_value <= 100:  # Checks if 'exam_value' is > 1 and < 100
    exam_value = exam_value * 0.01  # If it is, change it to decimal form
# If none of this applies, it just moves on #

sem_value = 1.00 - exam_value  # Find how much the semester was worth based on the exam value
sem_average = sem_grade * sem_value + exam_grade * exam_value  # Calculate the average

print("Your semester average is " + str(sem_average))  # Prints the average

if sem_average >= 98:
    print("You got an A+!")
elif 94 <= sem_average <= 97:
    print("You got an A!")
elif 90 <= sem_average <= 93:
    print("You got an A-!")
elif 87 <= sem_average <= 89:
    print("You got a B+!")
elif 83 <= sem_average <= 86:
    print("You got a B!")
elif 80 <= sem_average <= 82:
    print("You got a B-!")
elif 77 <= sem_average <= 79:
    print("You got a C+!")
elif 73 <= sem_average <= 76:
    print("You got a C!")
elif 70 <= sem_average <= 72:
    print("You got a C-! Transfer to Johnston!")
elif 67 <= sem_average <= 69:
    print("You got a D+! Transfer to Johnston")
elif 63 <= sem_average <= 66:
    print("You got a D! Transfer to Johnston")
elif 60 <= sem_average <= 62:
    print("You got a D-! Transfer to Johnston")
else:
    print("You got a F! Transfer to Johnston")
