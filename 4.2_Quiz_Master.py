'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Please answer all questions as best as possible")
print()

score = 0

q1 = int(input("Question #1: What is the square root of 529? "))
if q1 == 23:
    print("That is correct")
    score += 1
else:
    print("Wrong, the correct answer is 23")
print()

q2 = input("Question #2: What is the name of Spongbob's pet snail? ")
if q2.lower() == "gary":
    print("That is correct")
    score += 1
else:
    print("Wrong the correct answer is Gary")
print()

q3 = input("Question #3: What is the highest grossing movie of all time? ")
if q3.lower() == "avatar":
    print("That is correct")
    score += 1
else:
    print("Wrong, the correct answer is Avatar")
print()

q4 = input("Question #4: What color is the sky? ")
if q4.lower() == "blue":
    print("That is correct")
    score += 1
else:
    print("Wrong, the correct answer is blue")
print()

q5 = input("Question #5: What is H2O? ")
if q5.lower() == "water":
    print("That is correct")
    score += 1
else:
    print("Wrong, the correct answer is water")
print()

print(score)


