'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.

10 question quiz about whatever I have on my mind
'''

count = 0

def correct():
    print('That is the correct answer')
    global count
    count = count + 1

def incorrect():
    print('That is not the correct answer')

answer = int(input('Enter 3: '))
if answer == 3:
    correct()

answer = int(input('Enter 4: '))
if answer == 4:
    correct()

print(count)