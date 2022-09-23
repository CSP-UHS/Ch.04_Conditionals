'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
z=0
print("Video Game Trivia")

print()

#Question 1
print("A. The Leviathan")
print("B. Mjolnir")
print("C. Godslayer")
print("D. Bone Reaver")

print()

user_input = input("What is Kratos's axe called")

print()

if user_input.upper() == "A":
    x=1
elif user_input.upper() == "B":
    x=2
elif user_input.upper() == "C":
    x=2
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was The Leviathan")

print()

#Question 2
print("A. 3 stone, 5 iron")
print("B. 4 stone, 2 iron")
print("C. 4 wood, 2 iron")
print("D. 3 wood, 5 iron")

print()

user_input = input("What materials are needed to make a smithing table in Minecraft")

print()

if user_input.upper() == "A":
    x=2
elif user_input.upper() == "B":
    x=2
elif user_input.upper() == "C":
    x=1
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 4 wood, 2 iron")

print()

#Question 3
print("A. Cursed Captain")
print("B. Gold Hoarder")
print("C. Pirate King")
print("D. Pirate Lord")

print()

user_input = input("What is the name of the final boss in Sea of Thieves, Tall Tales")

print()

if user_input.upper() == "A":
    x=2
elif user_input.upper() == "B":
    x=1
elif user_input.upper() == "C":
    x=2
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was the Gold Hoarder")

print()

#Question 4
print("A. 8")
print("B. 10")
print("C. 12")
print("D. 15")

print()

user_input = input("How much boost does a small boost pad give you in Rocket League")

print()

if user_input.upper() == "A":
    x=2
elif user_input.upper() == "B":
    x=2
elif user_input.upper() == "C":
    x=1
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 12")

print()

#Question 5
print("A. 5")
print("B. 10")
print("C. 15")
print("D. 20")

print()

user_input = input("How long does it take for a large boost pad to respawn in Rocket League")

print()

if user_input.upper() == "A":
    x=2
elif user_input.upper() == "B":
    x=1
elif user_input.upper() == "C":
    x=2
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 10")

print()

#Question 6
print("A. 3")
print("B. 5")
print("C. 7")
print("D. 10")

print()

user_input = input("How many generators are needed to open the escape doors in Dead by Daylight")

print()

if user_input.upper() == "A":
    x=2
elif user_input.upper() == "B":
    x=1
elif user_input.upper() == "C":
    x=2
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 5")

print()

# Question 7
print("A. 11")
print("B. 14")
print("C. 16")
print("D. 19")

print()

user_input = input("How many Call of Duty games are there")

print()

if user_input.upper() == "A":
    x = 2
elif user_input.upper() == "B":
    x = 2
elif user_input.upper() == "C":
    x = 2
elif user_input.upper() == "D":
    x = 1

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 19")

print()

# Question 8
print("A. The Black Lotus")
print("B. Company of Onyx")
print("C. Trevor and Kids")
print("D. The Black Hand")

print()

user_input = input("What is the name of the enemies in Just Cause 4")

print()

if user_input.upper() == "A":
    x = 2
elif user_input.upper() == "B":
    x = 2
elif user_input.upper() == "C":
    x = 2
elif user_input.upper() == "D":
    x = 1

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was The Black Hand")

print()

# Question 9
print("A. 24 Story Levels")
print("B. 36 Story Levels")
print("C. 43 Story Levels")
print("D. 52 Story Levels")

print()

user_input = input("How many levels are there in Lego Star Wars, The Complete Saga")

print()

if user_input.upper() == "A":
    x = 2
elif user_input.upper() == "B":
    x = 1
elif user_input.upper() == "C":
    x = 2
elif user_input.upper() == "D":
    x = 2

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 36")

print()

# Question 10
print("A. Spyro")
print("B. Echo")
print("C. Whirlwind")
print("D. Phoenix")

print()

user_input = input("What is the name of the first dragon in Skylanders")

print()

if user_input.upper() == "A":
    x = 1
elif user_input.upper() == "B":
    x = 2
elif user_input.upper() == "C":
    x = 2
elif user_input.upper() == "D":
    x = 2

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was Spyro")

print()

print("Your score is",z/10*100,"%")