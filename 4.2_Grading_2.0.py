'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print("Would you like to know how your grades will end up? Look no further than right here!")


sgrade=int(input("What is your Semester Grade?"))
fgrade=int(input("What is your Final Grade?"))
exworth=int(input("What is your Exam worth?"))
exworth/=100

overall=sgrade*(1-exworth)+(fgrade*exworth)

print("Your Overall grade is",overall)

if overall>=90.0:
    print("Your grade is an A")
elif overall>80.0:
    print("Your grade is a B")
elif overall>70.0:
    print("Your grade is a C")
elif overall>60.0:
    print("Your grade is a D")
else:
    print("Your grade is an F. Transfer to Johnston!")