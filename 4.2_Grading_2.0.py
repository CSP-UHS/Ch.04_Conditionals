'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''


semester = int(input('Please Enter Semester Grade: '))  #take variables and turn them into integers
final = int(input('Please Enter Final Exam Grade: '))
weight = int(input('Please Enter Final Exam Weight: '))

overall = ((semester*(100-weight))+(final*weight))/100  #calculate
text = 'Your final grade would be '                     #Added a text variable so I wouldn't have to type as much

if overall >= 90:                                       #Dont make me comment the if/else because you and I both know how they work
    print('\nCongratulations! '+text+'an A, '+str(overall)+'%')

elif overall < 90 and overall >= 80:
    print('\n'+text+'a B, '+str(overall)+'%')

elif overall < 80 and overall >= 70:
    print('\n'+text+'a C, '+str(overall)+'%')

elif overall <70 and overall >= 60:
    print('\n'+text+'a D, '+str(overall)+'%')

else:
    print('\n'+text+str(overall)+'%, Please transfer to Johnston')

