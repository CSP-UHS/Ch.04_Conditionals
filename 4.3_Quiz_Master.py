'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.

Things to add:
- Total grade by somehow adding up the total points

'''

# quiz that tests people about random things
'''print("Hello! This is a quiz about quizzes in school!")
score = int(0)
studentname = input("What is your name?")
print("Hello", studentname, "! get ready to take the quiz!")
'''
score = int(0)

q1 = input("What is the passing grade of Urbandale High School? (Do NOT include % because that was too much work to code)")
if q1 == '80':
    print("Good job You got the question right!")
    score  += 1
else:
    print("How did you not know that it was 80%?")

print("You did good on the first one... how here's some hard ones ")

q2 = input("How many cores and threads do the IMACs have?(Bryce)")
if q2 == '2 cores and 4 threads':
    print("Good job, clearly did research")
    score += 1
else:
    print("Wow Bryce, I'd expect you to know that one. (2 cores and 4 threads) ")

q3 = input("Should you study for a test?")
if q3 == 'true' or q3 == 'True' or q3 =="yes" or q3 == 'Yes':
    print("Good job")
    score += 1
else:
    print("It's Yes cmon man")

q4 = input("What is the range for getting an A grade? (Don't include % sign)")
if q4 == '93-100':
    print("Good job, satisfactory performance ")
    score += 1
else:
    print("93-100 is that beautiful A grade")
q5 = input("How do you use a projector? \n A: Slap it until it works \n B: Plug the HDMI into the computer and put it on the right input \n C: Scream at it \n D: Put in a tech support ticket")
if q5 == 'B':
    print("Good Job! You did it! Now tell Mr. Hermon your wise words.")
    score += 1
else:
    print("Wow, did I give Mr. Hermon this test by accident? It's B")

q6 = input("Can fire have a shadow?")
if q6 == 'Yes' or 'yes':
    print("I don't even know that answer either so good job")
    score += 1
else:
    print("Yes... somehow ")

print("Time for the hard one.")

q7 = input("Is Mr. Hermons first name Mark or Marc? NO CHEATING!")
if q7 == 'Marc':
    score += 1
    print("Good one.")
else:
    print("Marc... good try though")

print("Thanks for taking this test!")

finalscore = (score /7)*100
if finalscore >= 90:
    print("Good job, you got an A (A- is basically a knock off A")
elif finalscore >= 80:
    print("good job, you got a B")
elif finalscore >= 70:
    print("Sadly, you got a C")
elif finalscore >= 60:
    print("Can't even compete with that D grade ")
else:
    print("You're a failure")


print("Your final score is", finalscore)

