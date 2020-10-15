# Sign your name:________________

  #1. Make the following program work. (3 mistakes)

midichlorians = int(input("Enter midichlorian count: "))
if midichlorians > 10000:
         print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)
     
x = int(input("Enter a number: "))
if x == 3:
    print("You entered 3")


  # 3. Make the following program work. (4 mistakes)

answer = input("What is the name of Poe Dameron's Droid? ").upper()
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)
     
jedi = input("Name one of the top 3 greatest Jedi.").upper()
if jedi == "YODA" or jedi == "LUKE SKYWALKER" or jedi == "OBI-WAN KENOBI":
    print ("That is correct!")



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

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

