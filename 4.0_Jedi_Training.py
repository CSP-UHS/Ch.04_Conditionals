# Sign your name: Tanner Evitts

  #1. Make the following program work. (3 mistakes)

midichlorians = float(input("Enter midichlorian count: "))
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)
     
x = int(input("Enter a number: ")) #set input to int
if x == 3: #added colon and another equal sign
    print("You entered 3")


  # 3. Make the following program work. (4 mistakes)
     
answer = str(input("What is the name of Poe Dameron's Droid? "))  #set input type to string
if answer == "BB8":   #changed the variable
    print("Correct!")
else:   #undid one indent and added colon
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)
     
jedi = input("Name one of the top 3 greatest Jedi.") #changed variable and input type to string
if jedi.lower() == "yoda" or jedi.lower() =="luke skywalker" or jedi.lower() == "obi-wan kenobi":
    print("That is correct!")
else:
    print("Incorrect! YOU HAD THREE CHOICES.")



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "jedi master":
    sensitivity = 1000
elif user_input.lower() == "b":
    sensitivity = 900
elif user_input.lower() == "c":
    sensitivity = 0

print("Sensitivity: ",sensitivity)