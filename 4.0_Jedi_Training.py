# # Sign your name:________________
#
#   #1. Make the following program work. (3 mistakes)
# #
# midichlorians = float(input("Enter midichlorian count: "))    #add close parenthesis
# if midichlorians > 10000:   # needs :
#     print("You have serious Jedi potential")
# else:       #let it be else
#     print("Jedi, you will never be.")

#
#  # 2. Make the following program work. (3 mistakes)
#
# x = float(input("Enter a number: "))   #add float or int before
# if x == 3:     # == not just =    # add :
#      print("You entered 3")

#
#   # 3. Make the following program work. (4 mistakes)
#
# answer = input("What is the name of Poe Dameron's Droid? ")
# if answer.upper() == "BB8":     #change = to ==   # change 'a' to 'answer'   # add .upper()
#     print("Correct!")
# else:   #add :
#      print("Incorrect! It is BB8.")


#   # 4. Make the following program work. (4 mistakes)
#
# jedi = input("Name one of the top 3 greatest Jedi.")
# if jedi.lower == "yoda" or jedi.lower == "luke skywalker" or jedi.lower == "obi-wan kenobi":
#     print("That is correct!")



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character: ")

if user_input.lower() == "a":
    sensitivity = 1000
    print("Sensitivity:", sensitivity)
elif user_input.lower() == "b":
    sensitivity = 900
    print("Sensitivity:", sensitivity)
elif user_input.lower() == "c":
    sensitivity = 0
    print("Sensitivity:", sensitivity)
else:
    print("not an option")


