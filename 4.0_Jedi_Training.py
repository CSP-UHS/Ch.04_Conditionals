# # Sign your name: Lily Burkhead

# # # 1. Make the following program work. (3 mistakes)

midichlorians = int(input("Enter midichlorian count: "))
number=10000
if midichlorians >= number:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")


#  2. Make the following program work. (3 mistakes)

x = int(input("Enter a number: "))
y=3
if x==y:
    print("You entered 3")
else:
    print("Enter a different number")

#   # 3. Make the following program work. (4 mistakes)

answer = str(input("What is the name of Poe Dameron's Droid? "))
if answer.lower() == "bb8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")


#  # 4. Make the following program work. (4 mistakes)

Jedi = input('Name one of the top 3 greatest Jedi.')
if Jedi.lower() == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi":
    print("That is correct!")
else:
    print("Try again. The jedi council would be disappointed.")


 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = (input("Choose a character?"))

if user_input.lower() == "a" or "jedi master":
    print ("sensitivity = 1000")
elif user_input.lower() == "b" or "sith lord":
    print("sensitivity = 900")
elif user_input.lower() == "c" or "droid":
    print("sensitivity = 0")
else:
    print("Not a choice!")
    print("sensitivity = ")

