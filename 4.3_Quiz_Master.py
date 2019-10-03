'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

score=0
print("Welcome to my Hallows Eve Quiz")
print("Miss too many and you'll get caught by the dark spirits")
print()
print("1. In what countries was the tradition of dressing up and going door to door for food or coins for Halloween most popular?")
print("A. Scotland and Ireland")
print("B. United States of America and Canada")
print("C. Scotland and United States of America")

answer=str(input("Which answer is correct: "))
if answer.lower()=="a" or answer.lower()=="scotland and ireland":
    print("Correct")
    print("This has been going on since the 16th century.  Also known as souling has thought to be the origin of trick-or-treat.")
    score+=1
else:
    print("Incorrect")
    print("Scotland and Ireland is correct")
print()
print("2. In what country was the first written account of children saying Trick-or-Treat?")
print("A. England")
print("B. France")
print("C. Canada")

answer=str(input("What answer is correct: "))
if answer.lower()=="c" or answer.lower()=="canada":
    print("Correct, on November 4th 1927 it was printed that kids had demanded candy by saying trick-or-treat")
    score+=1
else:
    print("Incorrect, C. Canada was correct.")
print()
print("3. How many american States produce a major amount of pumpkins?")
answer=int(input("Enter the number of how many states: "))
right=6
if answer==right:
    print("Correct")
    score+=1
else:
    print("Incorrect, 6 is the correct answer")
print()
answer=str(input("4. Name the person who first made the Jak-O-Lantern: "))
if answer.lower()=="jack":
    print("Correct")
    score+=1
else:
    print("Incorrect, the correct answer is Jack")
print()

print("5. In Hollywood, California during Halloween which item is banned from 12am October 31st to 12pm November 1st?")
print("A. Confetti Poppers")
print("B. Silly String")
print("C. Sparklers")
answer=str(input("Which answer is correct: "))
if answer.lower()=="b" or answer.lower()=="silly string":
    print("Correct")
    score+=1
else:
    print("Incorrect, Silly String was correct")
print()
print("6. What does Dracula mean?")
print("A. Son of Evil")
print("B. Man of Darkness")
print("C. Evil Night")
answer=str(input("Which answer is correct? "))
if answer.lower()=="a" or answer.lower()=="son of evil":
    print("Correct")
    score+=1
else:
    print("Incorrect, Son of Evil is correct")
print()
print("7. In medieval Europe what were owls believed to be?")
answer=str(input("Enter which common halloween person that owls were believed to be: "))
if answer.lower()=="witches" or answer.lower()=="witch":
    print("Correct")
    score+=1
else:
    print("Incorrect, owls were believed to be witches")
print()
print("Your score is", score)
if score>=4:
    print("You escaped the dark spirits congratulation. Enjoy your spooky season.")
else:
    print("Oh No, the dark spirits caught up. You lost.")