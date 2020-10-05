'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
question_one = int(input("1. How many letters are there in the alphabet? "))
if question_one == 26:
    print("\nCorrect\n")
    score = score+1
else:
    print("\nIncorrect")
    print("Correct Answer: 26\n")
question_two = input("2. What is the capital of Scotland?\nA: London\nB: Glasgow\nC: Edinburgh\nPlease enter a letter: ")
if question_two.lower() == "c":
    print("\nCorrect\n")
    score = score+1
else:
    print("\nIncorrect")
    print("Correct Answer: C\n")
question_three = input("What is political efficacy?\nA: Citizen's trust in their government and their ability to influence the government.\nB: One's political beleifs.\n Please enter a letter: ")
if question_three.lower() == "a":
    print("\nCorrect\n")
    score = score + 1
else:
    print("\nIncorrect\n")
    print("Correct Answer: A\n")
question_four = input("What is the main color of Joe's water bottle? ")
if question_four.lower() == "green":
    print("\nCorrect\n")
    score = score + 1
else:
    print("\nIncorrect\n")
    print("Correct Answer: Green\n")
question_five = float(input("What does sin30 equal? (Please enter a decimal): "))
if question_five == "0.5" or ".5":
    print("\nCorrect\n")
    score = score + 1
else:
    print("\nIncorrect\n")
    print("Correct Answer: 0.5\n")
question_six = input("What is the largest country in North America by land area? ")
if question_six.lower() == "canada":
    print("\nCorrect\n")
    score = score + 1
else:
    print("\nIncorrect\n")
    print("Correct Answer: Canada")
question_seven = input("How many words are in this question? (Spell out the number) ")
if question_seven.lower() == "seven":
    print("\nCorrect\n")
    score = score + 1
else:
    print("\nIncorrect\n")
    print("Correct Answer: Seven\n")
print("Final Score: ", score, "/ 7")
score = score/7
score = int(score*100)
print(score,"%")



