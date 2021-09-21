'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
# NO PEEKING
print("THE ULTIMATE QUIZ!  You must score a 93% or better to win!.\n\n")
mhermons = int(input("\nQuestion 1: How many times can Marc Hermon be seen in Placeholder Team Name's Rube Goldberg Machine?\nAnswer: "))

correct = 0

if mhermons == 4:
    print("\n\n\"Correct!\" - Plankton, Sept. 7th 2001\n\n")
    correct += 1
else:
   print("\n\nIncorrect! It was 4, not" + str(mhermons) + "\n\n")

position_three = input("\nQuestion 2: Where was the third Marc Hermon Photo located?\n\nA. In the laundry Chute\nB. On the fridge\nC. In the LifeTouch folder\n\nYour answer: ")

if position_three == 'B' or position_three == 'b':
    print("\n\nCorrect! It was on the fridge!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was on the fridge.\n\n")

book_nine = input("What was the ninth book in the domino effect?\n\nA. Wacky Wednesday\nB. Green Eggs and Ham\nC. Fox in Socks\nD. Go Dog Go!\n\nAnswer: ")

if book_nine == 'C' or book_nine == 'c':
    print("\n\nCorrect! It was Fox in Socks!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was Fox in Socks.\n\n")

sweatshirts = int(input("How many students are seen wearing their property of physics sweatshirts during the explanation?\n\nAnswer: "))

if sweatshirts == 3:
    print("\n\nCorrect! It was 3 students!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was 3 students.\n\n")

chopsticks = int(input("How many chopsticks were required for \"The chopstick battering ram\"?\n\nAnswer: "))

if chopsticks == 10:
    print("\n\nCorrect! It was 10 chopsticks!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was 10 chopsticks.\n\n")

year = int(input("What year was this Rube Goldberg Machine done?\n\nAnswer: "))

if year == 2018:
    print("\n\nCorrect! It was 2018!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was 2018.\n\n")

videos = int(input("How many videos were in the 2018 Rube Goldberg Playlist?\n\nAnswer: "))

if videos == 11:
    print("\n\nCorrect! It was 11 videos!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was 11 videos.\n\n")

remote_object = input("What is the object on the TV Remote that helps the Jenga pieces to be able to press the button?\n\nAnswer: ")

if remote_object == "Marble" or remote_object.lower() == "marble" or remote_object.upper() == "MARBLE" or remote_object == "A Marble" or remote_object.lower() == "a marble" or remote_object.upper() == "A MARBLE":
    print("\n\nCorrect! It was a marble\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was a marble\n\n")

jengas = int(input("How many Jenga blocks were used in the Jenga tower?\n\nAnswer: "))

if jengas == 12:
    print("\n\nCorrect! It was 12!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was 12.\n\n")

plot = input("If \"Play YouTube\" didn't have much of a storyline behind it, then what was \"Cat Catcher\" about?\n\nAnswer: ")

if "cat" in plot:
    print("\n\nCorrect! It had to do with cats!\n\n")
    correct += 1
elif "Cat" in plot:
    print("\n\nCorrect! It had to do with cats!\n\n")
    correct += 1
elif "CAT" in plot:
    print("\n\nCorrect! It had to do with cats!\n\n")
    correct += 1
else:
    print("\n\nIncorrect! It was about cats.\n\n")

percent = correct * 10

print("You had a total score of " + str(correct) + "/10 possible points. ")
print("You got a " + str(percent) + "%! \n\n")

if correct < 10:
    print("You lost! You got less than 93%!")
else:
    print("You win! You got a 93% or better!")
