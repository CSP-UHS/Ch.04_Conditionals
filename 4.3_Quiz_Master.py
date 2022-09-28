'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
total = 0
print("Welcome to Owen's test thing!")
print()
ready = input("Are you ready to start the test?")
if ready.upper()=="NO":
    print("Too bad you're gonna do it anyway.")
elif ready.upper()=="YES":
    print("Okay, let's get started.")
else:
    print("It's a yes or no question, try again.")
print()
print("Question 1: How much wood would a woodchuck chuck if a woodchuck could chuck wood?")
print()
print("A: None")
print("B: 5,349 Tons")
print("C: 700 Pounds")
print("D: Idk")
print()
quest1 = input("Answer: ")
print()
if quest1.upper()=="A":
    print("You are wrong, the woodchuck can actually chuck a decent amount of wood.")
elif quest1.upper()=="B":
    print("You are wrong, that's a little too much wood to chuck.")
elif quest1.upper()=="C":
    print("You are correct! In 2017, researchers determined that a woodchuck could chuck roughly 700 pounds of wood.")
    total = total+1
elif quest1.upper()=="D":
    print("You are wrong, at least try to answer the question.")
else:
    print("Please choose one of the provided answers.")
print()
print("Question 2: If you dig a six foot hole, how deep is that hole?")
print()
print("A: 7 Decimeters")
print("B: 6 Feet")
print("C: 2 Miles")
print("D: Probably like 20 Feet")
print()
quest2 = input("Answer: ")
print()
if quest2.upper()=="A":
    print("You are wrong, you really had to pick the most random answer?")
elif quest2.upper() == "B":
    print("You are correct, in theory, if you dug a hole that was 6 feet deep, the hole would be 6 feet deep.")
    total = total + 1
elif quest2.upper() == "C":
    print("You are wrong, if you managed to dig a 2 mile hole that would be pretty impressive though.")
elif quest2.upper() == "D":
    print("You are wrong, I guess if you took away 14 it would be right, but you didn't.")
else:
    print("Please choose one of the provided answers.")
print()
print("Question 3: What is 3+3?")
print()
print("A: 10-4.0000001")
print("B: 2+29/3")
print("C: 1+2(3)-(5-4)")
print("D: 1+2(5)-(5-2)/2")
print()
quest3 = input("Answer: ")
print()
if quest3.upper()=="A":
    print("You are wrong, you had the right idea, but its a little more complicated.")
elif quest3.upper()=="B":
    print("You are wrong, get better at math.")
elif quest3.upper()=="C":
    print("You are correct, you'll probably do well on your next math test.")
    total = total + 1
elif quest3.upper()=="D":
    print("You are wrong, we all know you picked it because it was the longest answer.")
else:
    print("Please enter one of the provided answers.")
print()
print("Question 4: What month of the year has 28 days?")
print()
quest4 = input("Answer: ")
print()
if quest4.upper()=="FEBRUARY":
    print("Wow, you really fell for that one, unbelieveable. Every month has 28 days.")
elif quest4.upper()=="ALL" or quest4.upper()=="ALL OF THEM":
    print("You are correct, good job thinking outside the box.")
    total = total + 1
else:
    print("You are wrong, every month has 28 days.")
print()
print("Question 5: True or False. In the hit game Fortnite, there is a Black Widow skin.")
print()
quest5 = input("Answer: ")
print()
if quest5.upper()=="TRUE":
    print("You are correct, it is a very rare skin, but it still is in the game.")
    total = total + 1
elif quest5.upper()=="FALSE":
    print("You are wrong, it actually was a skin.")
else:
    print("Please enter either TRUE or FALSE.")
print()
print("Question 6: David's parents have three sons. Snap, Crackle, and what's the third son's name?")
print()
quest6 = input("Answer: ")
if quest6.upper()=="POP":
    print("You are wrong, I really got you with that one. The answer was David.")
elif quest6.upper()=="DAVID":
    print("You are correct, nice job actually reading the question.")
    total = total + 1
else:
    print("You are wrong, the correct answer was David.")
print()
print("Question 7: If you're running in a race and you pass the person in 2nd Place, what place are you in?")
print()
print("A: 1st Place")
print("B: 3rd Place")
print("C: 2nd Place")
print("D: Last Place")
print()
quest7 = input("Answer: ")
print()
if quest7.upper()=="A":
    print("You are wrong, you had the right idea, but think again, the right answer was C.")
elif quest7.upper()=="B":
    print("You are wrong, why would you even think this. The answer was C.")
elif quest7.upper()=="C":
    print("You are correct, nice job.")
    total = total + 1
elif quest7.upper()=="D":
    print("You are wrong, stop overthinking everything. The correct answer was C.")
else:
    print("Please enter one of the provided answers.")
print()
print("Question 8: If there are 3 apples and you take away 2, how many apples do you have?")
print()
quest8 = input("Answer: ")
if quest8.upper()=="1":
    print("You are wrong, you really thought it would be that easy? The correct answer was 2.")
elif quest8.upper()=="2":
    print("You are correct, nice job!")
    total = total + 1
else:
    print("You are wrong, the correct answer was 2.")
print()
print("Question 9: What 4 letter word can be written forward, backward or upside down, and can still be read left to right?")
print()
quest9 = input("Answer: ")
if quest9.upper()=="NOON":
    print("Nice job, you are correct!")
    total = total + 1
else:
    print("You are wrong, the correct answer was NOON.")
print()
print("Question 10: What can you hold in your right hand, but never in your left hand?")
print()
quest10 = input("Answer: ")
print()
if quest10.upper()=="LEFT HAND":
    print("You are correct, good thinking!")
    total = total + 1
else:
    print("You are wrong, the correct answer was your left hand.")
print()
print("Congratulations! You finished the quiz!")
print()
if total==0:
    percent=0
elif total==1:
    percent=10
elif total==2:
    percent=20
elif total==3:
    percent=30
elif total==4:
    percent=40
elif total==5:
    percent=50
elif total==6:
    percent=60
elif total==7:
    percent=70
elif total==8:
    percent=80
elif total==9:
    percent=90
elif total==10:
    percent=100
if percent==0:
    letter = "a F."
elif percent==10:
    letter = "a F."
elif percent==20:
    letter = "a F."
elif percent==30:
    letter = "a F."
elif percent==40:
    letter = "a F."
elif percent==50:
    letter = "a F."
elif percent==60:
    letter = "a D."
elif percent==70:
    letter = "a C."
elif percent==80:
    letter = "a B."
elif percent==90:
    letter = "an A."
elif percent==100:
    letter = "an A."
print("You got",total,"out of 10 questions correct.")
print("Your score is",percent,"percent, which translates to",letter,)