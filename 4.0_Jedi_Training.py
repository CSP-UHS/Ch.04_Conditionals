# Sign your name:________________

  #1. Make the following program work. (3 mistakes)

midichlorians=float(input("Enter midichlorian count: ")) #parentheses and make it float
if midichlorians > 10000:
         print("You have serious Jedi potential")
else: #change to else
         print("Jedi, you will never be.")

 # 2. Make the following program work. (3 mistakes)
     
     x = float(input("Enter a number: ")) #put in float
     if x == 3: #colon and double equals
         print("You entered 3")


  # 3. Make the following program work. (4 mistakes)
     
     answer = input("What is the name of Poe Dameron's Droid? ")
     if answer == "BB8": #make a answer and double equals
         print("Correct!")
     else:
         print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)
     
     x = input("Name one of the top 3 greatest Jedi.")
     if x == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi": #need to use x and add quotation marks
         print("That is correct!")# Paranthases



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?").lower()

if user_input == "A" or "Jedi Master":
    sensitivity=1000
elif user_input == "B" or "Sith Lord":
    sensitivity=900
elif user_input == "C" or "Droid":
    sensitivity=0
else:
    sensitivity=""

print("Sensitivity: ", sensitivity)
