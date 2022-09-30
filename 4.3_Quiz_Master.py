'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
# multiple choice, number as answer, text as answer
# add score variable

bg_red = '\u001b[41;1m\u001b[30m'
END = '\033[0m'
bg_green = '\u001b[42;1m\u001b[30m'
bg_yellow = '\u001b[43;1m\u001b[30m'
bg_orange = '\033[48;2;255;165;0m\u001b[30m'

score = 0
print("\n \nHopefully you know Urbandale...\n")
print("1.) Which Urbandale sport has the most state championships?: ")
print("    A. Baseball")
print("    B. Soccer")
print("    C. Softball")
user_input = input("Your Answer: ")
if user_input.lower() == "a" or user_input.lower() == "baseball":
    print()
    print(bg_green + "Correct! You're a genius." + END)
    score = score + 1
else:
    print(bg_red + "Incorrect, It was baseball." + END)
    print()
answer = input("\n2.) How many State Championships does the baseball team have?: ")
if answer == "4":
    print()
    print(bg_green + "Yes! Nice job." + END)
    score = score + 1
else:
    print(bg_red + "Wrong, it was 4" + END)
    print()
answer = input("\n3.) Boys Bowling, Cross Country, and Soccer all have the same number of state titles, How many?: ")
print()
if answer == "2":
    print(bg_green + "Wow! Correct!" + END)
    print()
    score = score + 1
else:
    print(bg_red + "Nope,  the answer was 2" + END)
    print()
print("4.) What are the school colors?")
print("    A. White and Red")
print("    B. Red and Blue")
print("    C. Blue and white\n")
user_input = input("Your answer: ")
print()
if user_input.lower() == "c" or user_input.lower() == "blue and white":
    print(bg_green + "You got it!" + END)
    print()
    score = score + 1
else:
    print(bg_red + "Nope... it was Blue and White" + END)
    print()
answer = input("5.) When was the Urbandale High school founded?: ")
print()
if answer == "1889":
    print(bg_green + "Correct!" + END)
    print()
    score = score + 1
else:
    print(bg_red + "Wrong, The high school was built and founded in 1889" + END)
    print()
answer = input("6.) What conference is Urbandale in?: \n")
if answer == "CIML" or answer == "ciml":
    print(bg_green + "Right!" + END)
    score = score + 1
else:
    print(bg_red + "Incorrect, Urbandale is in the CIML" + END)
print()
print("You scored" ,score, "out of 6!\n")
if score >= 6:
    print(bg_green + "A, 100%" + END)
elif score >= 5:
    print(bg_yellow + "B, 83%" + END)
elif score >= 4:
    print(bg_orange + "D, 67%" + END)
elif score == 3:
    print(bg_red + "F, 50% Transfer to Johnston" + END)
elif score == 2:
    print(bg_red + "F, 33% Transfer to Johnston" + END)
elif score == 1:
    print(bg_red + "F, 17% Transfer to Johnston" + END)
else:
    print(bg_red + "You should probably transfer to Johnston..." + END)
    print(bg_red + "You got an F, 0%" + END)
