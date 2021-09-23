'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.

Things to add:
- Total grade by somehow adding up the total points

'''
# quiz that tests people qbout quizzes
print("Hello! This is a quiz about quizzes in school!")
score = int(0)
studentname = input("What is your name?")
print("Hello", studentname, "! get ready to take the quiz!")

q1 = int(input("What is the passing grade of Urbandale High School? (Do NOT include % because that was too much work to code)"))
if q1 == 80:
    print("Good job", studentname, "You got the question right!")
    score  += 1
else:
    print("Lmao", studentname, "You suck how did you even pass school?")

print("Enough of that, now its time for True or False questions.")

q2 = input("Are you able to use your phone to search for answers on google while taking a test?")
if q2 == 'False' or 'false':
    print("Good job,", studentname, "clearly you are a good person.")
    score += 1
else:
    print("Wow... currently reporting you to your teachers right now.")

q3 = input("Should you study for a test?")
if q3 == 'true' or 'True' or "yes" or 'Yes':
    print("Good job", studentname)
    score += 1
else:
    print("Makes sense, considering that you are failing this.")

q4 = int(input("What is the range for getting an A grade? (Don't includd % sign")
if q4 == 93-100 or 93 - 100 or 93- 100 or 93 -100:
    print("Good job,", studentname)
    score += 1
else:
    print("Eh, that's alright. Tough question.")

finalscore = score /5
print("Your final score is", finalscore)