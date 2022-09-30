# Sign your name:________________

# 1. Make the following program work. (3 mistakes)

# midichlorians=float(input("Enter midichlorian count: "))
# if midichlorians>10000:
#     print("You have serious Jedi potential")
# else:
#     print("Jedi, you will never be.")


# # 2. Make the following program work. (3 mistakes)

# x = float(input("Enter a number  :"))
# if x == 3:
#     print("The number is 3!")
#

# 3. Make the following program work. (4 mistakes)
# answer = input("What is the name of Poe Dameron's Droid? ")
# if answer == "BB8":
#     print("Correct!")
# else:
#     print("Incorrect! It is BB8.")


#  # 4. Make the following program work. (4 mistakes)
# x = input("Name one of the top 3 greatest Jedi.")
# if x == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi":
#     print("That is correct!")
#

#
# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
#    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")
print("------------------------------")
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")
print("------------------------------")
inp=(input("Choose a character?: "))

if inp.lower()==("a"):
        sensitivity = 1000
elif inp.lower()==("b"):
        sensitivity = 900
elif inp.lower()==("c"):
        sensitivity = 0
else:
        print("NOT A CHOICE")
        sensitivity = 0
print("------------------------------")
print("Sensitivity: ",sensitivity)
