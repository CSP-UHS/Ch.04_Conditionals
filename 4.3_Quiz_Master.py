'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print ("Thanks for taking my quiz about Minecraft.")
print("This won't be easy, only Minecraft pros will get a perfect score.")

NumberOfQuestionsAnswered = 0
NumberOfQuestionsCorrect = 0

print("Here is an easy one, who created Minecraft?")
print("A, Notch. B, Steve. C, Pewdiepie. D, George Lucas")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered + 1
if UserInput.lower() == "a" or UserInput.lower() == "notch":
    NumberOfQuestionsCorrect + 1
    print("Good job, but its only gonna get harder.")
else:
    print("Wrong, the right answer was A, Notch")

print("What version is Java Minecraft on as of October 3, 2019?")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered + 1
if UserInput == "1.14" or UserInput == "1.14.4" or UserInput == "Release 1.14.4" or UserInput == "Release 1.14" or UserInput == "19w40a":
    NumberOfQuestionsCorrect + 1
    print("Correct.")
else:
    print("Incorrect, the right answer was 1.14 or 1.14.4")

print("What is the name of the Mob that explodes?")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered + 1
if UserInput.lower() == "creeper" or UserInput.lower() == "charged creeper":
    NumberOfQuestionsCorrect + 1
    print("Good job..")
else:
    print("Wrong, the right answer was Creeper or Charged Creeper.")



