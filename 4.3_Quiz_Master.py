'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("Welcome to the Minecraft quiz!")
print("A. Kill the Ender Dragon")
print("B. Punch a Tree")
print("C. Find a Pet")
print("D. Find a Village")
question1 = input("1.What is the first thing you should always do when you start a world? ")
if question1.lower() == "a" or question1.lower() == "kill the ender dragon":
    print("Incorrect, the correct answer was B")
    answer1 = 0
elif question1.lower() == "b" or question1.lower() == "punch a tree":
    print("Correct")
    answer1 = 100
elif question1.lower() == "c" or question1.lower() == "find a pet":
    print("Incorrect, the correct answer was B")
    answer1 = 0
elif question1.lower() == "d" or question1.lower() == "find a village":
    print("Incorrect, the correct answer was B")
    answer1 = 0
else:
    print("That was not a Choice")
    answer1 = 0

print("A. 1")
print("B. 7")
print("C. 3")
print("D. 5")
question2 = input("2.What is the max level of sharpness on a sword? ")
if question2.lower() == "a" or question2.lower() == "1":
    print("Incorrect, the correct answer was D")
    answer2 = 0
elif question2.lower() == "b" or question2.lower() == "7":
    print("Incorrect, the correct answer was D")
    answer2 = 0
elif question2.lower() == "c" or question2.lower() == "3":
    print("Incorrect, the correct answer was D")
    answer2 = 0
elif question2.lower() == "d" or question2.lower() == "5":
    print("Correct")
    answer2 = 100
else:
    print("That was not a Choice")
    answer2 = 0

print("A. Cat")
print("B. Parrot")
print("C. Dog")
print("D. Pig")
question3 = input("3.What is the main pet that everybody wants? ")
if question3.lower() == "a" or question3.lower() == "cat":
    print("Incorrect, the correct answer was C")
    answer3 = 0
elif question3.lower() == "b" or question3.lower() == "parrot":
    print("Incorrect, the correct answer was C")
    answer3 = 0
elif question3.lower() == "c" or question3.lower() == "dog":
    print("Correct")
    answer3 = 100
elif question3.lower() == "d" or question3.lower() == "pig":
    print("Incorrect, the correct answer was C")
    answer3 = 0
else:
    print("That was not a Choice")
    answer3 = 0

question4 = input("4.What is the max amount of most items you can hold in one inventory slot? ")
if question4 == "64":
    print("Correct")
    answer4 = 100
else:
    print("Incorrect, the correct answer was 64")
    answer4 = 0

question5 = str(input("5.What is the name of one of the two starting characters? "))
if question5.lower() == "steve" or question5.lower() == "alex":
    print("Correct")
    answer5 = 100
else:
    print("Incorrect, the correct answer was Steve or Alex")
    answer5 = 0

print("A. Ender Dragon")
print("B. The Wither")
print("C. The Warden")
print("D. Stewie Griffin")
question6 = input("6.What is known as the final boss of Minecraft? ")
if question6.lower() == "a" or question6.lower() == "ender dragon":
    print("Correct")
    answer6 = 100
elif question6.lower() == "b" or question6.lower() == "the wither":
    print("Incorrect, the correct answer was A")
    answer6 = 0
elif question6.lower() == "c" or question6.lower() == "the warden":
    print("Incorrect, the correct answer was A")
    answer6 = 0
elif question6.lower() == "d" or question6.lower() == "stewie griffin":
    print("Incorrect, the correct answer was A")
    answer6 = 0
else:
    print("That was not a Choice")
    answer6 = 0

question7 = str(input("7.True or False - There is a point where you can't do anything else in the game "))
if question7.lower() == "true" or question7.lower() == "t":
    print("Incorrect, there is always something to do")
    answer7 = 0
elif question7.lower() == "false" or question7.lower() == "f":
    print("Correct")
    answer7 = 100
else:
    print("That was not a Choice")
    answer7 = 0

finalScore = (answer1 + answer2 + answer3 + answer4 + answer5 + answer6 + answer7) / 7
print("your final score was",finalScore,"%")
if finalScore >= 90:
    print("Congratulations you got an A")
elif 89 >= finalScore >= 80:
    print("Congratulations you got a B, you could do better though")
elif 79 >= finalScore >= 70:
    print("Really a C are you proud of that?")
elif 69 >= finalScore >= 60:
    print("Cmon a D you should be ashamed, go home and eat some oatmeal")
else:
    print("F, Leave, go to Johnston")

