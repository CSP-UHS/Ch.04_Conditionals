'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

number_correct = 0


print("Hello! Thank you for taking my quiz.")

#Question 1#

ans1 = input("Which goes first? Milk or Cereal?").lower()

if ans1 == "milk":
    print("You disgust me.")

if ans1 == "cereal":
        print("Correct.")
if ans1 == "cereal":
    number_correct = number_correct + 1

#Question 2#

ans2 = int(input("What is 2+2?"))

if ans2 < 4 or ans2 > 4:
    print("How did you get that wrong?")

if ans2 == 4:
    print("Correct.")
if ans2 == 4:
    number_correct = number_correct + 1

#Question 3#

print("Is Wyoming:")
print("A: A state in the United States of America.")
print("B: A country in South America.")
print("C: A myth created by the US Government.")
ans3 = input("Answer here:").lower()

if ans3 == "a" or ans3 == "b":
    print("Incorrect.")
if ans3 == "c":
    print("Correct.")
if ans3 == "c":
    number_correct = number_correct + 1

#Question 4#

ans4 = input("What is the capital of the State of Iowa?").lower()

if ans4 != "des moines":
    print("Incorrect.")

if ans4 == "des moines":
        print("Correct.")
if ans4 == "des moines":
    number_correct = number_correct + 1


#Question 5#

ans5 = input("Is country music good?").lower()

if ans5 != "yes":
    print("Incorrect.")

if ans5 == "no":
        print("Correct.")
if ans5 == "no":
    number_correct = number_correct + 1

#Question 6#

ans6 = int(input("What is 11+14?"))

if ans6 < 25 or ans6 > 25:
    print("Wrong.")

if ans6 == 25:
    print("Correct.")
if ans6 == 25:
    number_correct = number_correct + 1

#Question 7#

ans7 = int(input("What is 9 x 9?"))

if ans7 < 81 or ans7 > 81:
    print("Wrong.")

if ans7 == 81:
    print("Correct.")
if ans7 == 81:
    number_correct = number_correct + 1

#Question 8#

ans8 = int(input("What is 15 / 3?"))

if ans8 < 5 or ans8 > 5:
    print("Wrong.")

if ans8 == 5:
    print("Correct.")
if ans8 == 5:
    number_correct = number_correct + 1

#Question 9#

ans9 = int(input("What is 50 - 32?"))

if ans9 < 18 or ans9 > 18:
    print("Wrong.")

if ans9 == 18:
    print("Correct.")
if ans9 == 18:
    number_correct = number_correct + 1

#Question 10#

ans10 = int(input("What is 72 + 38?"))

if ans10 < 110 or ans10 > 110:
    print("Wrong.")

if ans10 == 110:
    print("Correct.")
if ans10 == 110:
    number_correct = number_correct + 1

print("You are finished!")
print("Your score is", number_correct, "correct!")