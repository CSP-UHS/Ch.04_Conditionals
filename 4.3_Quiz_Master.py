'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print()
final = 0
print("Welcome to a Test made by someone who isnt crative enough to")
print("think of his own questions so got his friends to think of some for him.")
print()
input("Are you ready to begin? ")
print()
print("Question 1")
a1 = int(input("What is 80+70 "))
if a1 == 150:
    final = final+1
    print("Correct!")
else:
    print("Wrong the correct answer is 150? ")
print()
print("Question 2")
a2 = int(input("12*12"))
if a2 == 144:
    final = final+1
    print("Correct!")
else:
    print("Wrong the correct answer is 144? ")
print()
print("Question 3")
a3 = (input("What console was the first Super Smash Bros on? "))
if a3.lower() == ("nintendo 64"):
    final = final+1
    print("Correct!")
else:
    print("Wrong the correct answer was Nintendo 64")
print()
print("Question 4")
a4 = (input("Who was the second released DLC in Super Smash Bros Ultimate"))
if a4.lower() == ("joker"):
    final = final+1
    print("Correct")
else:
    print("Wrong the correct answer is Joker")
print()
print("Question 5")
a5 = (input("Who invented the first Car? A.Carl Benz B.Aaron Fetcher C.Milton Reeves D.All of the above"))
if a5.lower == "d":
    final=final+1
    print("Correct... google says its an opinion on who actually invented the first car.")
else:
    print("Wrong the correct answer is D")
print()
print("Question 6")
a6 = int(input("Whats 37+26"))
if a6 == 63:
    final=final+1
    print("Correct")
else:
    print("Wrong the correct answer is 63")
print()
print("Question 7")
a7 = int(input("Whats 2+48"))
if a7 == 50:
    final=final+1
    print("Correct")
else:
    print("Wrong the correct answer is 50")
print()
Final=(final/7)*100
print("You got",Final)
if Final>=93:
    print("you got an A Great Job!")
elif Final>=90:
    print("You got an A- Great Job.")
elif Final>=87:
    print("you got a B+ Great Job.")
elif Final>=83:
    print("you got a B Great.")
elif Final>=80:
    print("you got a B- Great.")
elif Final>=77:
    print("you got a C+")
elif Final>=73:
    print("you got a C")
elif Final>=70:
    print("you got a C-")
elif Final>=67:
    print("you got a D+")
elif Final>=63:
    print("you got a D")
elif Final>=60:
    print("you got a D-")
elif Final<60:
    print("you got a F")
