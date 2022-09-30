'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

#use this one a lot (if answer.lower()== "answer") etc.
#multiple choice variables

score = 0
questions = 7

print("We will now begin the greatest quiz of all time.")
print("Please remember that spelling matters during this quiz. However, capitalization does not.")
print("Question 1: What is seven squared?")
answer = int(input("What is your answer?"))
if answer == 49:
    print("Correct. On to question 2.")
    score = score + 1
else:
    print("Incorrect. The correct answer was 49.")
print()
print("Question 2: What is the capitol of Arizona?")
answer = input("What is your answer?")
if answer.lower().strip() == "phoenix":
    print("Correct. On to question 3.")
    score = score + 1
else:
    print ("Incorrect. The correct answer was Phoenix.")
print()
print("Question 3. This ones multiple choice. Of the following countries, "
      "which has the greatest land mass?")
print("A) The United States of America")
print("B) Brazil")
print("C) China")
answer = input("What is your choice?")
if answer.lower().strip() == "a":
    print("Correct. On to question 4.")
    score = score + 1
else:
    print("Incorrect. The correct choice was option A.")
print()
print("Question 4: In Mojang's hit game, Minecraft, what is the name of the "
      "default player character?")
answer = input("What is your answer?")
if answer.lower().strip() == "steve" or answer.lower().strip() == "alex":
    print("Correct. On to question 5.")
    score = score + 1
else:
    print("Incorrect. The correct answer was; Steve. An alternate answer could have been Alex as well.")
print()
print("Question 5: Name one of the noble gasses in chemistry.")
answer = input("What is your answer?")
if answer.lower().strip() == "helium" or answer.lower().strip() == "neon" or answer.lower().strip() == "argon" or answer.lower().strip() == "krypton" or answer.lower().strip() == "xenon" or answer.lower().strip() == "radon" or answer.lower().strip() == "Oganesson":
    print("Correct. On to question 6.")
    score = score + 1
else:
    print("Incorrect, you should consider utilizing a search engine.")
print()
print("Question 6: How do you say hello in French?")
answer = input("What is your answer?")
if answer.lower().strip() == "bonjour":
    print("Correct. On to the final question.")
    score = score + 1
else:
    print("Incorrect.")
print()
print("Question 7: What English word becomes shorter when you add two letters to it?")
answer = input("What is your answer?")
if answer.lower().strip() == "short":
    print("Correct. End sequence initiated.")
    score = score + 1
    print()
else:
    print("Incorrect. End sequence initiated.")
    print()

print("The quiz is now over, your judgement will arrive soon,")
print("...")
print("...")

grade = score/questions
letter = "blank"
if grade > 0.90:
    letter = "A"
elif grade > 0.80:
    letter = "B"
elif grade > 0.79:
    letter = "C"
elif grade > 0.5:
    letter = "D"
else:
    letter = "F"
percent = grade*100
print("Calculations are complete.")
print("Your percentage score was:",percent,"%.")
print("That correlates to a letter grade of",letter,". We hope you are happy "
      "with this outcome.")
if letter == "A" or letter == "B" or letter == "C":
    print("You received a passing score. Congratulations, you will live to see "
          "another day.")
else:
    print("You did not pass the quiz. The council will now decide your fate.")