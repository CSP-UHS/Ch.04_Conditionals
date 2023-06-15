# Sign your name:________________

  #1. Make the following program work. (3 mistakes)
     
midichlorians = float(input("Enter midichlorian count: "))
if midichlorians > 10000:
         print("You have serious Jedi potential")
else:
         print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)
     
x = float(input("Enter a number: "))
if x == 3:
         print("You entered 3")


  # 3. Make the following program work. (4 mistakes)
     
answer = str(input("What is the name of Poe Dameron's Droid?: "))
if answer.lower() == "bb8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)
     
jedi = input("Name one of the top 3 greatest Jedi.")
if jedi.upper() == "YODA" or jedi.upper() == "LUKE SKYWALKER" or jedi.upper() == "OBI-WAN KENOBI":
     print ("That is correct!")
else:
     print("Wrong!")

 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")
sensitivity = 0
if user_input.upper() == "A" or user_input.upper() == "JEDI MASTER":
         sensitivity = 1000
elif user_input.upper() == "B" or user_input.upper() == "SITH LORD":
         sensitivity = 900
elif user_input.upper() == "C" or user_input.upper() == "DROID":
         sensitivity = 0
else:
         print("Not a choice!")
         sensitivity = ""


print("Sensitivity: ",sensitivity)
