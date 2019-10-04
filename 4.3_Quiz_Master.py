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
NumberOfQuestionsAnswered = NumberOfQuestionsAnswered + 1
if UserInput.lower() == "a" or UserInput.lower() == "notch":
    NumberOfQuestionsCorrect = NumberOfQuestionsCorrect + 1
    print("Good job, but its only gonna get harder.")
else:
    print("Wrong, the right answer was A, Notch")

print("What version is Java Minecraft on as of October 3, 2019?")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered = NumberOfQuestionsAnswered + 1
if UserInput == "1.14" or UserInput == "1.14.4" or UserInput == "Release 1.14.4" or UserInput == "Release 1.14" or UserInput == "19w40a":
    NumberOfQuestionsCorrect = NumberOfQuestionsCorrect + 1
    print("Correct.")
else:
    print("Incorrect, the right answer was 1.14 or 1.14.4")

print("What is the name of the Mob that explodes?")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered = NumberOfQuestionsAnswered + 1
if UserInput.lower() == "creeper" or UserInput.lower() == "charged creeper":
    NumberOfQuestionsCorrect = NumberOfQuestionsCorrect + 1
    print("Good job.")
else:
    print("Wrong, the right answer was Creeper or Charged Creeper.")

print("How many different ores are in Minecraft? (count the two technically different kinds of gold a one).")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered = NumberOfQuestionsAnswered + 1
if UserInput == "7" or UserInput.lower() == "seven":
    NumberOfQuestionsCorrect = NumberOfQuestionsCorrect + 1
    print("Good job.")
else:
    print("Wrong, the right answer was seven.")

print("True or False, all platforms where Minecraft has been released are able to do cross platform play.")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered = NumberOfQuestionsAnswered + 1
if UserInput.lower() == "false" or UserInput.lower() == "no" or UserInput.lower() == "f":
    NumberOfQuestionsCorrect = NumberOfQuestionsCorrect + 1
    print("Good job.")
else:
    print("Wrong, While pc, xbox, and mobile are able to do cross platform play, it is not availible on ps4, old gen console, ps vita, rasberry pie, 3ds, wii u. .")

print("How much does a three player realm cost for a one month subscription on Minecraft bedrock edition?")
print("Do not include tax.")
UserInput = str(input("Choose an answer: $"))
NumberOfQuestionsAnswered = NumberOfQuestionsAnswered + 1
if UserInput == "3.99" or UserInput == "4":
    NumberOfQuestionsCorrect = NumberOfQuestionsCorrect + 1
    print("Good job.")
else:
    print("Wrong, the right answer was $3.99.")

print("Which java edition mod improves performance, adds dynamic lighting, and allows all players using that mod to see each others capes?")
UserInput = str(input("Choose an answer: "))
NumberOfQuestionsAnswered = NumberOfQuestionsAnswered + 1
if UserInput.lower() == "optifine":
    NumberOfQuestionsCorrect = NumberOfQuestionsCorrect + 1
    print("Good job.")
else:
    print("Wrong, the right answer was Optifine.")

PercentCorrect = NumberOfQuestionsCorrect / NumberOfQuestionsAnswered
print("Thanks for taking the quiz.")
print("You scored an", PercentCorrect)
if PercentCorrect >= .90:
    print("Thats an A.")
elif PercentCorrect >= .80:
    print("Thats an B.")
elif PercentCorrect >= .70:
    print("Thats an C.")
elif PercentCorrect >= .60:
    print("Thats an D.")
else:
    print("Thats an F.")