# Sign your name:________________

  #1. Make the following program work. (3 mistakes)
'''
     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians > 10000
         print("You have serious Jedi potential")
     elif:
         print("Jedi, you will never be.")
'''
midichlorians = float(input("Enter midichlorian count: "))
if midichlorians >= 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")

 # 2. Make the following program work. (3 mistakes)
'''
     x = input("Enter a number: ")
     if x = 3
         print("You entered 3")
'''
x = float(input("Enter a number:"))
if x == 3:
    print("You entered 3")
else:
    print("That's not a 3")

  # 3. Make the following program work. (4 mistakes)
'''
     answer = input("What is the name of Poe Dameron's Droid? ")
     if a = "BB8":
         print("Correct!")
         else
         print("Incorrect! It is BB8.")
'''
answer = input("What is the name of Poe Dameron's Droid? ")
if answer.upper() == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")

  # 4. Make the following program work. (4 mistakes)
'''
     x = input("Name one of the top 3 greatest Jedi.")
     if jedi == Yoda or Luke Skywalker or Obi-Wan Kenobi:
         print "That is correct!"
'''
jedi = input("Name one of the top 3 greatest Jedi:")
if jedi.lower() == "yoda" or jedi.lower() == "luke skywalker" or jedi.lower() == "obi-wan kenobi":
    print("That is correct!")
else:
    print("Wrong")

# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
# Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
'''
     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input = A:
         sensitivity = 1000
     else if user_input = B:
         sensitivity = 900
     else if user_input = C:
         sensitivity = 0

     print("Sensitivity: ",Sensitivity)
'''
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character:")
sensitivity = int
if user_input.upper() == "A":
    sensitivity = 1000
elif user_input.upper() == "B":
    sensitivity = 900
elif user_input.upper() == "C":
    sensitivity = 0
else:
    print("Not valid, please enter A,B or C")
print("Sensitivity:", sensitivity)
