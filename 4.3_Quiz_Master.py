'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
c = 0
w = 0

print("        Welcome to the Minecraft quiz!")
print("Enter the right answer to prove you are an")
print("                    EPIC GAMER                ")
print("               Ready? Let's start")
print()
print("What was the original name of the game?")
print()
print("A.  Cave Game")
print("B.  Craft and Mine")
print("C.  Square Spelunking")
print()
a = str(input("Your answer: "))
if a.lower() == ("a") or a.lower() == ("cave game"):
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: A. Cave Game")
print()
print("When was the game released?")
print()
print("A.  2009")
print("B.  2005")
print("C.  2007")
print()
a = str(input("Your answer: "))
if a.lower() == ("a") or a.lower() == ("2011"):
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: A. 2009")
    w += 1
print()
print("How many dyes are in the game?")
print()
a = str(input("Your answer: "))
if a.upper() == "20":
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: 20")
    w += 1
print()
print("What is the rarest ore to get while mining?")
a = str(input("Your answer: "))
if a.lower() == ("emeralds") or a.lower() == ("emerald ore") or a.lower() == ("emerald"):
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: Emeralds")
    w += 1
print()
print("What is the final boss of the game?")
print()
print("A.  The Wither")
print("B.  Steve")
print("C.  The Ender Dragon")
print()
a = str(input("Your answer: "))
if a.lower() == ("c") or a.lower() == ("the ender dragon"):
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: C. The Ender Dragon")
    w += 1
print()
print("What is the best food source in the game?")
print()
print("A.  Golden Apples")
print("B.  Golden Carrots")
print("C.  Steak")
print()
a = str(input("Your answer: "))
if a.lower() == ("b") or a.lower() == ("golden carrots"):
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: B. Golden Carrots")
    w += 1
print()
print("Which portal requires obsidian to work?")
print()
a = str(input("Your answer: "))
if a.lower() == ("the nether portal") or a.lower() == ("nether") or a.lower() == ("the nether") or a.lower() == ("nether portal"):
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: The Nether Portal")
    w += 1
print()
print("What does the observer do?")
print()
print("A.  Watches for entity movement")
print("B.  Watches for block updates")
print("C.  Watches for redstone signals")
print()
a = str(input("Your answer: "))
if a.lower() == ("b") or a.lower() == ("watches for block updates"):
    print()
    print("Correct!")
    c+=1
else:
    print()
    print("Incorrect")
    print("The correct answer was: B. Watches for block updates")
    w+= 1

grade = 100*(c/(c+w))
grade//=1


if grade == 80:
    print("Your score is: ", grade, "%")
    print("You are a true")
    print(" EPIC GAMER")
elif grade > 80 and grade < 100:
    print("Your score is: ", grade, "%")
    print("You are close, Steve.")
else:
    print()
    print()
    print()
    print("             You     died!")
    print()
    print()
    print("              Score:",int(grade))
    print()
    print()
    print("               Respawn")
    print()
    print("             Title screen")
