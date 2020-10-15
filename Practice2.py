print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?").lower()

if user_input == "A" or user_input == "jedi master":
    sensitivity = 1000
if user_input == "B" or user_input == "sith lord":
    sensitivity = 900
if user_input == "C" or user_input == "droid":
    sensitivity = 0

print("Sensitivity: ", sensitivity)
