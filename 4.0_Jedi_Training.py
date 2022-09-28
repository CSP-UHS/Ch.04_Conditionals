# Sign your name: Rachel Linthicum

# 1. Make the following program work. (3 mistakes)

midichlorians = int(input("Enter midichlorians count: "))
m = 10000
if midichlorians > m:
    print('You have serious Jedi potential')
else:
    print("Jedi, you will never be.")
print()
# Corrections:
# made 10000 a variable;
# changed float to int;
# added colons to if and else (which I changed from elif)

# 2. Make the following program work. (3 mistakes)

x = int(input("Enter a number: "))
if x == 3:
    print("You entered 3")
else:
    print("The number you entered is not 3")
print()
# Corrections:
# Int instead of float;
# 2 equal signs instead of 1;
# no indention on if and else

# 3. Make the following program work. (4 mistakes)

answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")
print()
# corrections:
# add colon after else;
# changes "A" to answer;
# 2 equal signs instead of 1;
# used proper indentations

# 4. Make the following program work. (4 mistakes)

jedi = str("Name one of the top 3 greatest Jedi.")
if jedi == "Yoda" or "Luke Skywalker" or "Obi-wan Kenobi":
    print("That is correct!")
print()
# Corrections:
# jedi insteadof x;
# str instead of int;
# put names in quotes, not parenthesis;
# parenthesis for "That is correct!"

# 5. Make the following program work whether they enter "a", A, Jedi Master or jedi master
#  Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.


print("Welcome to the Jedi Academy!")
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")
Sensitivity = 0

if user_input.upper() == "A":
    Sensitivity = 1000
elif user_input.upper() == "JEDI MASTER":
    Sensitivity = 1000
elif user_input.upper() == "B":
    Sensitivity = 900
elif user_input.upper() == "SITH LORD":
    Sensitivity = 900
elif user_input.upper() == "C":
    Sensitivity = 0
elif user_input.upper() == "DROID":
    Sensitivity = 0
else:
    print("Not a choice!")
    Sensitivity = "___"
print("Sensitivity: ", Sensitivity)
# Corrections:
# added an equal sign after the inputs
# elif not else if
# added Sensitivity = 0
# added .upper() after input to allow the answer to be lowercase when inputted and still have the correct answer
# added "Jedi Master", "Sith Lord", and "Droid"
