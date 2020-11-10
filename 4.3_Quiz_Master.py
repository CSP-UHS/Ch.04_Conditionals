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

