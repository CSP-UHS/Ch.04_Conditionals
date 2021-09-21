# Sign your name: Jarman

# This is absolute indent hell, because Python does those types of things.

  #1. Make the following program work. (3 mistakes)
     
midichlorians = float(input("Enter midichlorian count: ")) # Forgot second parenthesis
if midichlorians > 10000: # Forgot the colon
    print("Serious Jedi potential, you have young padawan.")
else: # Had elif, elif could work, but you'd need a circumstance to execute the code, and an else statement after that, so else makes the most sense
    print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)
     
x = float(input("Enter a number: ")) #Takes it as a string by default
if x == 3: # Forgot the Colon & need the 'double-equals'
    print("You entered 3")


  # 3. Make the following program work. (4 mistakes)
     
answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8": # Double equals, and instead of "a" it has to be "answer"
    print("Correct!")
else: # Incorrect indent, and colon
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)

jedi = input("Name one of the top 3 greatest Jedi.")  # x should be jedi (jedi on the next line could also be x instead)
if jedi == "Yoda" or jedi == "Luke Skywalker" or jedi == "Obi-Wan Kenobi":  # need quotes and jedi == every or
    print("That is correct!")  # You had Python 2 syntax, but python3 has parenthesis


 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input == "A": # Double-equals and quotes around A because it is a string
    sensitivity = 1000
elif user_input == "B": # elif not else if # Double-equals and quotes around B because it is a string
    sensitivity = 900
elif user_input == "C": # elif not else if # Double-equals and quotes around C because it is a string
    sensitivity = 0
else:
    sensitivity = ""
    print("Not a Choice!")

print("Sensitivity: ", str(sensitivity)) # sensitivity, not Sensitivity and don't forget to convert it to a string!
