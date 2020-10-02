print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character. ")

if user_input.lower() == "a" or user_input.lower() == "a. jedi master" or user_input.lower() == "jedi master" or user_input.lower() == "a jedi master":
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "b. sith lord" or user_input.lower() == "sith lord" or user_input.lower() == "b sith lord":
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower() == "c. droid" or user_input.lower() == "droid" or user_input.lower() == "c droid":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity = ""

print("Sensitivity: ",sensitivity,)