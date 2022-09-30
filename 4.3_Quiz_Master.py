'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
points = 0
question1 = int(input("What is the square root of 49? "))
if question1 == 7:
    print("7 is correct!")
    points += 1
else:
    print("Incorrect. The answer is 7.")
print()

question2 = input("What does Mr. Carver say at the end of every announcement? ")
if question2.lower() == "go jhawks" or question2 == "Go Jhawks":
    print("That is correct! GO JHAWKS!!!")
    points += 1
else:
    print("Incorrect. The answer is Go Jhawks!")
print()

print("Which US state has the largest land mass?")
print("A. Texas")
print("B. California")
print("C. Alaska")
print("D. Montana")
question3 = input("")
if question3 == "c" or question3 == "C":
    print("That is correct!")
    points += 1
else:
    print("Incorrect. The answer is Alaska.")
print()

question4 = input("What is the capital of France? ")
if question4.lower() == "Paris" or question4 == "Paris":
    print("That is correct!")
    points += 1
else:
    print("Incorrect. The answer is Paris.")
print()

question5 = int(input("How much is a bakers dozen? "))
if question5 == 13:
    print("That is correct!")
    points += 1
else:
    print("Incorrect. The answer is 13.")
print()

question6 = int(input("How many weeks are in a year? "))
if question6 == 52:
    print("52 is correct!")
    points += 1
else:
    print("Incorrect. There are 52 weeks in a year.")
print()

print("What is the longest river in the world?")
print("A. The Nile River")
print("B. The Amazon River")
print("C. The Mississippi River")
print("D. The Yellow River")
question7 = input("")
if question7 == "A" or question7 == "a":
    print("That is correct.")
    points += 1
else:
    print("Incorrect. The answer is the Nile River.")

print()
percent = round(((points/7)*100), 1)

if percent >= 90:
    print("Your score is ", percent, "%. That is an A which means you passed! Congratulations!")
elif percent >= 80:
    print("Your score is ", percent, "%. That is an B which means you passed! Congratulations!")
elif percent >= 70:
    print("Your score is ", percent, "%. That is an C which means you passed! Congratulations!")
elif percent >= 60:
    print("Your score is ", percent, "%. That is an D which means you passed! Congratulations!")
else:
    print("Your final score is", percent, "% which is a F. That means you failed the test. Better luck next time.")
