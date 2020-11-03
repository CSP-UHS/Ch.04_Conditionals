'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
'''Create your own quiz with 7 or more questions. Ask at least one of each of the following types of questions:
a number as an answer (e.g., What is 1+1?)
text as an answer (e.g. Who created C3PO?)
a multiple choice (Which of these choices are correct? A, B, or C?)
When the user enters non-numeric answers, think and cover the different ways a user could enter a correct answer. For example, if the answer is "a", would "A" also be acceptable?
Let the user know if he or she gets the question correct. Print the correct answer if the user gets it wrong.
You need to keep track of how many questions they get correct.
At the end of the program print the percentage of questions the user gets right and their letter grade.
Keep the following in mind when creating the program:
Variable names should start with a lower case letter. Upper case letters work, but it is not considered proper.
To create a running total of the number correct, create a variable to store this score. Set it to zero. With an if statement, add one to the variable each time the user gets a correct answer. (How do you know if they got it correct? Remember that if you are printing out "correct" then you have already done that part. Just add a line there to add 1 to the number correct.)
Calculate the percentage by using a formula at the end of the game. Don't just add a certain percentage for each question the user gets correct. If you add a certain percentage each time, then you have to change the program in all of those places if some day you want to add another question. With a formula, you only need 1 change.
To print a blank line so that all the questions don't run into each other, use the following code:'''

print("Welcome to the Slappening Quiz")

score = 0

name = input(print("Enter your name "))
print(name, "What is the velocity required to cook a chicken with one slap")
print("A. 3725.95 mph.")
print("B. Really fast.")
print("C. 4327.88 m/s.")
answerONE = input("Answer by entering the corresponding letter that represents the answer: ")

if answerONE.lower() == 'a':
    print("Correct, how'd you know?")
    score = score+20
    print("Your current score is", score)
elif answerONE.lower() == 'b':
    print("Incorrect, the right answer was A")
    score = score+0
    print("Your current score is", score)
elif answerONE.lower() == 'c':
    print("Incorrect, the right answer was A.")
    score = score+0
    print("Your current score is", score)
else:
    print("You have greatly disappointed me.")
    print("Your current score is", score)

print(name, "What is the difference between a punch and a slap?")
print("A. No difference.")
print("B. When you punch your hand is closed and when you slap it's wide open.")
print("C. Real man only punch real man.")
answerDOS = input("Enter your answer: ")

if answerDOS.lower() == 'a':
    print("Incorrect, the correct answer was B.")
    score = score + 0
    print("Your current score is", score)
elif answerDOS.lower() == 'b':
    print("Ez credit bro.")
    score = score+10
    print("Your current score is", score)
elif answerDOS.lower() == 'c':
    print("Do you think you're still an edgy teenager? Grow up buddy!")
    score = score + 0
    print("Your current score is", score)
else:
    print("Smooth brain.")
    score = score +0
    print("Your current score is", score)

print("How many slaps do YOU think it takes to cook a chicken on average")
answerTRES = int(input("Enter the amount without commas: "))

if answerTRES >= 10000:
    print("Multiple sources state on average around 23034 but, gotta make this test easier.")
    score = score+10
    print("Your current score is", score)
else:
    print("Incorrect, the right answer was at least 10000")
    print("Your current score is", score)

print("Is it possible to die from a sudden slap on the external genitalia?")
answerCuatro = input("True or false: ")

if answerCuatro.lower() == 'true' or answerCuatro.lower() == 't':
    print("Well one way or another I guess.")
    score = score+10
    print("Correct, your current score is", score)
else:
    print("Although a low chance it could potentially stop the heart beat")
    print("Incorrect, your current score is", score)

print("Who is generally credited as the inventor of slap on electric bass?")
answerCinco = input("Thumpin' and pluckin': ")

if answerCinco.lower() == 'larry graham' or answerCinco.lower() == 'graham larry':
    print("Correct!")
    score = score+10
    print("Your current score is", score)
else:
    print("I don't blame you but... The correct answer was Larry Graham")
    print("Your current score is", score)

print("Who is the Russian slap champion?")
answerSeis = input("Be sure to correctly spell it: ")

if answerSeis.lower() == 'vasiliy khamotiskiy':
    print("You get extra points for this!")
    score = score+20
    print("Your current score is", score)
else:
    print("Better luck next time? The correct answer was Vasiliy Khamotiskiy")
    print("Your current score is", score)

print("Vasiliy Khamotiskiy was knocked out for the first time by who?")
answerSeis = input("Be sure to correctly spell it: ")

if answerSeis.lower() == 'vyacheslav zezulya':
    print("Nicely done!")
    score = score+20
    print("Your current score is", score)
else:
    print("Incorrecto. The correct answer was Vasiliy Khamotiskiy")
    print("Your current score is", score)
