# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
#    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "jedi master":                    #.lower to make a or A accessible, add or ~~~~~~ for same effect
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "sith lord":                    #replace else with elif
    sensitivity = 900
elif user_input.lower() == "C" or user_input.lower() == "droid":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity = "blank text"                                                          #Add sens = "blank text" (i know how to actually leave it blank don't worry)
print("Sensitivity: ", sensitivity)
