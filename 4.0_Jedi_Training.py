# Sign your name: Ryan Muetzel

  #1. Make the following program work. (3 mistakes)

midichlorians = float(input("Enter midichlorian count: ")) #was missing end parenthesis, also removed unexpected indentation
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:  #else instead of elif
    print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)
     
x = int(input("Enter a number: "))  #needed to change variable into integer
if x == 3:          # use ==    ,    added colon
    print("You entered 3")


  # 3. Make the following program work. (4 mistakes)
     
answer = input("What is the name of Poe Dameron's Droid? ")  #indentation errors
if answer.upper() == "BB8" or answer.upper() == "BB-8":                 # use ==, change to correct variable, add colon
    print("Correct!")
else:
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)
     
jedi = input("Name one of the top 3 greatest Jedi. ")       # change variable from x to jedi so they match
if jedi.upper() == 'YODA' or jedi.upper() == 'LUKE SKYWALKER' or jedi.upper() == 'OBI-WAN KENOBI':  # ==, make the answers strings
    print("That is correct!")      #put print statement in parenthesis



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
     
print("Welcome to the Jedi Academy!")
print("Please enter of the following letters to choose!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("\nPlease choose a character: ")

if user_input.upper() == 'A':
    sensitivity = 1000
elif user_input.upper() == 'B':
    sensitivity = 900
elif user_input.upper() == 'C':
    sensitivity = 0
else:
    sensitivity = ' '

if type(sensitivity) == int:
    print("Sensitivity: "+str(sensitivity))
else:
    print('Not a choice!')