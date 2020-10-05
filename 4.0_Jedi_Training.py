# Sign your name:Tom Dau

  #1. Make the following program work. (3 mistakes)

midichlorians = float(input("Enter midichlorian count: "))            #Add ) at the end
if midichlorians>10000:                                               #Add : at the end
    print("You have serious Jedi potential")
else:                                                                 #Change elif to else
    print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)

x = float(input("Enter a number: "))                                  #Add float( before input, and ) at the end
if x == 3:                                                            # Add = and :
    print("You entered 3")


  # 3. Make the following program work. (4 mistakes)

answer = str(input("What is the name of Poe Dameron's Droid? "))      # Add str( before input
if answer.upper() == "BB8":                                           # Add = and .upper to fix casing
    print("Correct!")
else:                                                                 # Add :
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)

jedi = input("Name one of the top 3 greatest Jedi.  ")                                              # Replace x for jedi
if jedi.upper() == "YODA" or jedi.upper() == "LUKE SKYWALKER" or jedi.upper() == "OBI-WAN KENOBI":  # put jedi.upper() == in front of all naems
    print("That is correct!")                                                                       # Put () around "That is correct



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "jedi master":                    # .lower to make a or A accessible, add or ~~~~~~ for same effect
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "sith lord":                    # replace else with elif
    sensitivity = 900
elif user_input.lower() == "C" or user_input.lower() == "droid":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity = "blank text"                                                          # Add sens = "blank text" (i know how to actually leave it blank don't worry)
print("Sensitivity: ", sensitivity)
