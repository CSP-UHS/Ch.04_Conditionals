'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Hey you are here to take a quiz \n Keep in mind that the quiz is about a million page long.")
p=0

print("1. There once was a horse in a barn and it died. \n How many legs does the horse have? ")
print("a. 1 \nb. 3 \nc. 4 ")
a=input("Type one of the letters")   #answer stuff abc Q1
if a.lower() == "a":
    p+=10
    print("Good job! Points:",p)
elif a.lower() == "b":
    p+=5
    print("Close enough..They ate three of the legs Points:",p)
elif a.lower() == "c":
    print("What a twist!! They ate three of the legs")
else:
    print("Come on! not a choice, no second chance.")
print(".\n.\n.\n.\n.\n.\n.")


print("2. Now, real questions! When did WW1 Start?? ")
print("a. June 4, 1919 \nb. September 1, 1939 \nc. July 28, 1914 ")
a=input("Type one of the letters")   #answer stuff abc Q2
if a.lower() == "a":
    print("sorry, wrong answer. It started in July 28, 1914. Points:",p)
elif a.lower() == "b":
    print("Sorry, wrong answer. It started in July 28, 1914. Points:",p)
elif a.lower() == "c":
    p+=10
    print("Correct!! Points:",p)
else:
    print("Come on! not a choice.")
print(".\n.\n.\n.\n.\n.\n.")


print("3. When was the first computer invented? ")
print("a. 1960 \nb. 2000 \nc. 1936 ")
a=input("Type one of the letters")   #answer stuff abc Q3
if a.lower() == "a":
    p+=5
    print("Sorry.\nThe first computer was made in 1936\nThe first small computer was made in 1960 Points:",p)
elif a.lower() == "b":
    print("Sorry, wrong answer. It was invented in 1936:",p)
elif a.lower() == "c":
    p+=10
    print("Correct!! Points:",p)
else:
    print("Come on! not a choice.")
print(".\n.\n.\n.\n.\n.\n.")


a=input("4. If there are 10 normal cows in a farm,\nhow many legs do they have in total? ") #answer stuff ##
if a=="40":
    p+=10
    print("That is correct! Points:",p)
else:
    print("10*4=40")
print(".\n.\n.\n.\n.\n.\n.")

a=input("5. What is the substance that human needs to live? ")
if a.lower()=="water" or a.lower()=="h2o":
    p+=10
    print("Correct! Points:",p)
else:
    print("You should know this! Water!")
print(".\n.\n.\n.\n.\n.\n.")


a=input("6.What does >  PC  < mean? ")
if a.lower()=="personal computer":
    p+=10
    print("Correct! Points:",p)
else:
    print("It's Personal computer")
print(".\n.\n.\n.\n.\n.\n.")


a=input("7. What is six times six and divided by six? ")  #answer stuff ##
if a=="6":
    p+=10
    print("Good job! Points:",p)
else:
    print("Its six, sorry")


##Score stuff
score=int((p/70)*100)


if score >= 100:
    A= "You are smart"
elif score >= 93:
    A = "A"
elif score >= 90:
    A = "A-"
elif score >= 87:
    A = "B+"
elif score >= 83:
    A = "B"
elif score >= 80:
    A = "B-"
elif score >= 77:
    A = "C+"
elif score >= 73:
    A = "C"
elif score >= 70:
    A = "C-"
elif score >= 67:
    A = "D+"
elif score >= 65:
    A = "D"
else:
    A = "Transfer to Johnston!"


print("Score:",score,"%",A)