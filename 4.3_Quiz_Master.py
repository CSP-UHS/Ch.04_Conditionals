'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
number_correct =0

print("Welcome to the Quake Champion's Quiz")
print()
print("*note that ups means units per second also units in you answer*")
print()

#question 1
print("1. What is Ranger's max ups when strafe jumping?")
print(" a. 400 ups")
print(" b. 640 ups")
print(" c. 310 ups")
print(" d. 320 ups")
print()
one=input("ANSWER: ")
if one.lower() == "b" or one.lower() == "640 ups":
    print("Correct now go keep fragging")
    number_correct += 1
else:
    print("YOU DIED!!! Should have pick up a power item")
print()

#question 2
print("2. What is Doom Slayer's passive ability?")
print(" a. Charring")
print(" b. Wall Jump")
print(" c. Double Jump")
print(" d. Full Sprint")
print()
two=input("ANSWER: ")
if two.lower() == "c" or two.lower() == "double jump":
    print("Correct now go keep fragging")
    number_correct += 1
else:
    print("YOU DIED!!! Should have pick up a power item")
print()

#question 3
print("3. What is the Unholy Trinity")
print(" a. Heavy Machine Gun, Super Shotgun, and Super Nailgun")
print(" b. Rocket Launcher, Lightning Gun, and Railgun")
print(" c. Tri-Bolt, Railgun, and Heavy Machine Gun")
print(" d. Machine Gun, Shotgun, Nailgun")
print()
three=input("ANSWER: ")
if three.lower() == "b" or three.lower() == "rocket Launcher, lightning Gun, and railgun":
    print("Correct now go keep fragging!")
    number_correct += 1
else:
    print("YOU DIED!!! Should have pick up a power item")
print()

#question 4
print("4. What is Nyx's active ability?")
print(" a. Plasma Trail")
print(" b. Barriar Sheild")
print(" c. Dire Orb")
print(" d. Ghost Walk")
print()
four=input("ANSWER: ")
if four.lower() == "d" or four.lower() == "ghost walk":
    print("Correct now go keep fragging")
    number_correct += 1
else:
    print("YOU DIED!!! Should have pick up a power item")
print()

#question 5
print("5. When did Quake Champions enter early acess")
print()
five=input("ANSWER: ")
if five.lower() == "2017":
    print("Correct now go keep fragging")
    number_correct += 1
else:
    print("YOU DIED!!! Should have pick up a power item")
print()

#question 6
print("6. What type of shooter is Quake Champions considered")
print()
six=input("ANSWER: ")
if six.lower() == "arena shooter" or six.lower() == "arena":
    print("Correct now go keep fragging")
    number_correct += 1
else:
    print("YOU DIED!!! Should have pick up a power item")
print()

#question 7
print("7. True or False: Is Quake Champions still in early acess?")
print()
seven=input("ANSWER: ")
if seven.lower() == "true" or seven.lower() == "t":
    print("Correct now go keep fragging")
    number_correct += 1
else:
    print("YOU DIED!!! Should have pick up a power item")
print()

#score
ave = (number_correct/7) * 100
print("Your score is: ",number_correct)
print("Here is your letter grade: ",ave,)
if ave>90:
    print("Here is your letter grade: A!")
    print("How are those 6 minute wait times for comp nerd.")
elif ave>80:
    print("Here is your letter grade: B!")
    print("Try comp pubstomper.")
elif ave>70:
    print("Here is your letter grade C")
    print("I thought you were the best.")
elif ave>60:
    print("Here is your letter grade D")
    print("Welcome to Quake Champions!!!")
else:
    print("Here is your letter grade F")
    print("Go back to Call of Duty!!")