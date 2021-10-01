'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
tscore = 0
#Question #1
answer1 = int(input("Question #1: What is 137 plus 79? "))
if answer1 == 216:
    print("You are correct!!!")
    tscore += 1
else:
    print("You are incorrect!, the answer is: 216")
print()
#Question #2
answer2 = input("Question #2: What did Marc Hermon Tweet on November 26, 2013? \n A) I love mayonnaise!! #uhschemistryqed \n B) I'm feeling a green sticker today #uhschemistryqed \n C) Yep....we're taking 4.1 and 4.2 again today! #uhschemistryqed \n")
if answer2.lower() == "b":
    print("You are correct!!!")
    tscore += 1
elif answer2.lower() == "a":
    print("Sorry, although Mr. Hermon is a mayonnaise goblin, he did not tweet this.")
else:
    print("You are incorrect!, the answer is B")
print()
#Question #3
answer3 = str(input("Question #3: What college did Marc Hermon attend? \n "))
if answer3.lower() == "university of iowa":
    print("You are correct!!!")
    tscore += 1
else:
    print("You are incorrect!!! The correct answer is the University of Iowa")
print()
#Question #4
answer4 = input("Question #4: Kanye is the most influential music artist of our generation \n True? \n or \n False? \n")
if answer4.lower() == "true":
    print("You are correct!!!")
    tscore += 1
elif answer4.lower() == "false":
    print("You are a certified moron!!!")
else:
    print("You meant to type True right?!?!?!?!??!?!")
print()
#Question #5
answer5 = input("Question #5: What is Mr. Hermon's most viral Youtube Video? \n A) 'Shoot the Cat'  \n B) '2019 Cable Cars' \n C) '3D Printed iPhone Sound Amplifier' \n D) 'Compound Gears' \n")
if answer5.lower() == "d":
    print("You are correct!!!")
    tscore += 1
else:
    print("You are incorrect!!! The correct answer is D.")
print()
#Question #6
answer6 = input("Question #6: What date does the Star Wars show 'The book of Boba Fett' drop on Disney+? \n A) December 29th \n B) October 30th \n C) January 7th \n ")
if answer6.lower() == "a":
    print("You are correct!!!")
    tscore += 1
else:
    print("You are incorrect!!! The correct Answer is December 29th")
print()
#Question #7
answer7 = input("Question #7: How many season are there of 'The Mandalorian'? \n A) 3 \n B) 2 \n C) 6 \n D) 1 \n")
if answer7.lower() == "b":
    print("You are correct!!!")
    tscore += 1
else:
    print("You are incorrect!!! The correct answer is B.")
print()
#Total Score
quotient = tscore/7
totalp = round(quotient * 100)
if totalp >= 90:
    letter = "A"
elif totalp >=80:
    letter = "B"
elif totalp >= 70:
    letter = "C"
elif totalp >= 60:
    letter = "D"
else:
    letter = "F!!! You failed!!! You moron!!!"
print("You got", totalp,"% of the answers correct!!! \n Your letter grade is:", letter)


