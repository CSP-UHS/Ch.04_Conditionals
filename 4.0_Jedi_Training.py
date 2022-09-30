# # Sign your name:_Tommy Hensley_
#
#   #1. Make the following program work. (3 mistakes)

midichlorians = float(input("Enter midichlorian count: "))
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)

x = input("Enter a number: ")
if x == 3:
    print("You entered 3")


  # 3. Make the following program work. (4 mistakes)

answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)

jedi = input("Name one of the top 3 greatest Jedi.")
if jedi.lower() == "yoda" or jedi.lower() == "luke skywalker" or jedi.lower() =="obi-wan kenobi":
    print("That is correct!")
else:
    print("That is incorrect!")


 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "jedi master":
         sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "sith lord":
         sensitivity = 900
elif user_input.lower() == "c" or user_input.lower() == "droid":
         sensitivity = 0
else:
    sensitivity = "Not a Choice"
print("sensitivity:", sensitivity)
