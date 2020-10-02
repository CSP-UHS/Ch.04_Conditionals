sensitivity = 0
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = str(input("Choose a character?"))

if user_input.upper() == "A" or user_input.upper() == "JEDI MASTER":
    sensitivity = 1000
elif user_input.upper() == "B" or user_input.upper() == "SITH LORD":
    sensitivity = 900
elif user_input.upper() == "C" or user_input.upper() == "DROID":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity = -1
if sensitivity != -1:
    print("Sensitivity: ", sensitivity)