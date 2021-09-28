'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
correct = 0
total = 0
number_correct = float(input("Question 1: What is 25*5"))
total += 1
if number_correct == 125:
    print("You are correct")
    correct += 1
else:
    print("You are incorrect it was 125")
print()
name = input("Question 2: What is my middle name")
total += 1
if name.lower() == "thomas":
    print("You are correct")
    correct += 1
else:
    print("you are incorrect my middle name is Thomas")
print()
mario = input("Question 3: Who is my favorite Mario character A. Mario B. Luigi C. Bowser D. Donkey Kong")
total += 1
if mario.lower() == "c" or mario.lower() == "bowser":
    print("you are correct")
    correct += 1
else:
    print("That is incorrect the answer is Bowser")
print()
number = float(input("Question 4: What is 10*(4+6)*0"))
total += 1
if number == 0:
    print("That is correct")
    correct += 1
else:
    print("That is incorrect the answer is zero")
print()
mario_galaxy = input("Question 5: What are the humanoid stars in Mario galaxy called")
total += 1
if mario_galaxy.lower() == "luma" or mario_galaxy.lower() == "lumas":
    print("You are correct")
    correct += 1
else:
    print("You are incorrect it was Luma")
print()
ganondorf = input("Question 6: Who is the main villain of the Legend of Zelda")
total += 1
if ganondorf.lower() == "ganondorf" or ganondorf.lower() == "ganon":
    print("You are correct")
    correct += 1
else:
    print("You are incorrect it is Ganondorf")
print()
Majora = input("Question 7: Who is the villain of the Legend of Zelda Majora's Mask")
total += 1
if Majora.lower() == "majora" or Majora.lower() == "majora's mask" or Majora.lower() == "majoras mask":
    print("you are correct")
    correct += 1
else:
    print("You are incorrect it was Majora")
TG = correct/total*100
print("You got", TG, "percent")
if TG >= 90:
    print("You got an A")
elif TG >= 80:
    print("You got a B- or higher")
elif TG >= 70:
    print("You got a C- or higher")
else:
    print("You got a D+ or less")
