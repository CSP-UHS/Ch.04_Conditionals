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

print("Just a quiz with 1 math question mostly about Twitch streamers and Youtubers.")

score = 0

name = input(print("What is your name? "))
print(name, "")
print("")
print("")
print("")
answerONE = input("")

if answerONE.lower() == 'a':
    print("")
    score = score+
    print("", score)
elif answerONE.lower() == 'b':
    print("")
    score = score+
    print("", score)
elif answerONE.lower() == 'c':
    print("")
    score = score+
    print("", score)
else:
    print("")
    print("", score)

print(name, "")
print("")
print("")
print("")
answerDOS = input("")

if answerDOS.lower() == 'a':
    print("")
    score = score +
    print("", score)
elif answerDOS.lower() == 'b':
    print("")
    score = score+
    print("", score)
elif answerDOS.lower() == 'c':
    print("")
    score = score + 0
    print("", score)
else:
    print("")
    score = score +
    print("", score)

print(name, "")
answerTRES = input(" ")

if answerTRES.lower() == '' or answerTRES.lower() == '':
    print("")
    score = score+
    print("", score)
else:
    print("")
    print("", score)

print(name, "")
answerCuatro = int(input(""))

if answerCuatro == '':
    print("")
    score = score+
    print("", score)
else:
    print("")
    print("")

print("Joji is a fairly known artist who used to be a Youtuber.")
answerCinco = input("Name one of his Aliases when he was a Youtuber")

