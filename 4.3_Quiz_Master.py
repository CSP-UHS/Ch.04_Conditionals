'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.

7-10 question quiz about whatever I have on my mind
'''

count = 0

def correct():      #subroutine for when the user gets the question correct, so I dont have to type everything out every single time
    print('\nThat is the correct answer.')
    global count
    count = count + 1

def incorrect():    #subroutine for when the user gets the question incorrect
    print('\nThat is not the correct answer.')

print('\nWhich of the following is my least favorite class?\nA) AP Government\nB) Advanced Composition\nC) Both')
answer = input('Enter answer HERE: ')                   #question 1
if answer.upper() == 'C' or answer.upper() == 'BOTH':
    correct()
else:
    incorrect()

print('\nWhat is the name of my favorite robot?')       #question 2
answer = input('Enter answer HERE: ')
if answer.upper() == 'TOM' or answer.upper() == 'TOM 2.0':
    correct()
else:
    incorrect()

print('\nYES/NO: Is League of Legends a fun game?')     #question 3
answer = input('Enter answer HERE: ')
if answer.upper() == 'NO' or answer.upper() == 'ABSOLUTELY NOT':
    correct()
else:
    incorrect()

print('\nYES/NO: Is it easy to think of these questions?')      #question 4
answer = input('Enter answer HERE: ')
if answer.upper() == 'NO':
    correct()
else:
    incorrect()

print('\nWhat are the derived units (mks) of length?')          #question 5
answer = input('Enter answer HERE: ')
if answer.upper() == 'M' or answer.upper() == 'METERS':
    correct()
else:
    incorrect()

print('\nWhat is 2+2*4?')
answer = int(input('Enter answer HERE: '))                  #question 6
if answer == 10:
    correct()
else:
    incorrect()

print('\nWhich of the following colors is the most sus?\nA) Cyan\nB) Red\nC) Green\nD) Yellow')
answer = input('Enter answer HERE: ')                       #question 7
if answer.upper() == 'B' or answer.upper() == 'RED':
    correct()
else:
    incorrect()

print('\nWhich of the following is superior?\nA) PC\nB) Mac')   #question 8
answer = input('Enter answer HERE: ')
if answer.upper() == 'A' or answer.upper() == 'PC':
    correct()
else:
    incorrect()

percentage = (count/8)*100

text = 'Your quiz grade is '
if percentage >= 90:                                       #Dont make me comment the if/else because you and I both know how they work
    print('\nCongratulations! '+text+'an A, '+str(percentage)+'%')

elif percentage < 90 and percentage >= 80:
    print('\n'+text+'a B, '+str(percentage)+'%')

elif percentage < 80 and percentage >= 70:
    print('\n'+text+'a C, '+str(percentage)+'%')

elif percentage <70 and percentage >= 60:
    print('\n'+text+'a D, '+str(percentage)+'%')

else:
    print('\n'+text+str(percentage)+"%.  I honestly don't know how you got here either.")
