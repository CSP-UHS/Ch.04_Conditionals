# Sign your name:Oded

  #1. Make the following program work. (3 mistakes)
     
# midichlorians = float(input("Enter midichlorian count:")) #added parenthesis
# if midichlorians > 10000: #added colon
#     print("You have serious Jedi potential")
# else: #changed to else
#     print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)
#
# x = float(input("Enter a number: ")) #Added float
# if x == 3: #added colon #added another = sign
#     print("You entered 3")
#

 # 3. Make the following program work. (4 mistakes)

# answer = input("What is the name of Poe Dameron's Droid? ")
# if answer == "BB8": #added another = sign #changed undefine "a" to variable "answer"
#     print("Correct!")
# else: #added colon
#     print("Incorrect! It is BB8.")



 # 4. Make the following program work. (4 mistakes)

# jedi = input("Name one of the top 3 greatest Jedi.") #Changed undefined "x" to variable "jedi"
# if jedi == "Yoda" or jedi == "Luke Skywalker" or jedi== "Obi-Wan Kenobi":  # Added quotations #Added jedi==
#     print("That is correct!") #Added parenthesis
# else:
#     print("That is incorrect!") #Added Else for incorrect answers

 # # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 # #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")


user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "jedi master":
    #added lower command #added quotations #added = sign #added or
    print("sensitivity = 1000")
elif user_input.lower() == "b" or user_input.lower() == "sith lord":
    #added lower command #added quotations #shortened to elif #added = sign #added or
    print("sensitivity = 900")
elif user_input.lower() == "c" or user_input.lower() == "droid":
    #added lower command #added quotations #shortened to elif #added = sign added or
    print("sensitivity = 0")
else:
    print("Not a choice!")
    print("Sensitivity:")
    #added else line for all other options


#print("Sensitivity: ",Sensitivity)


#NOTE TO SELF - I ADDED PRINT TO EACH SENSITIVITY SO IT JUST PRINTS WHAT THE SENSTITIVITY IS.
# NOT SURE IF THE SENSITITY IS SUPPOSED TO DO SOMETHING AND NOT BE JUST PRINTED