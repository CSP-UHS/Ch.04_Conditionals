# Sign your name:Matthew Flyr

  #1. Make the following program work. (3 mistakes)

     midichlorians = float(input("Enter midichlorian count: ")) #add a second closing parathenthesis
     if midichlorians > 10000:  #add a colon at the end of the if statement
         print("You have serious Jedi potential")
     else:
         print("Jedi, you will never be.")  #change the elif to an else, because it is an if/else statement and needs an else.


 # 2. Make the following program work. (3 mistakes)

     x = int(input("Enter a number: ")) #you are using an integer value and will need to specify else it will assume its a string.
     if x == 3:        #ADD COLONS THEY SAVE LIVES, you also need two equal signs, because one is used for assigning variables
         print("You entered 3")


  # 3. Make the following program work. (4 mistakes)

     a = input("What is the name of Poe Dameron's Droid? ") #Variables need to match
     if a == "BB8": #Double equal sign for comparsion
         print("Correct!")
     else: #COLONS MY GUY COLONS!!! And indentation is off.
         print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)

     jedi = input("Name one of the top 3 greatest Jedi.") #Make sure the variables match
     if jedi == "Yoda" or jedi == "Luke Skywalker" or jedi == "Obi-Wan Kenobi": #Add quotes around strings, super tricky error add jedi == to every one
         print("That is correct!") #Parenthesis



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input == "A" or user_input == "a" or user_input == "Jedi Master" or user_input == "jedi master":
         sensitivity = 1000
     elif user_input == "B" or user_input == "b" or user_input == "Sith Lord" or user_input == "sith lord":
         sensitivity = 900
     elif user_input == "C" or user_input == "c" or user_input == "Droid" or user_input == "droid":
        sensitivity = 0
     print("Sensitivity: " + str(sensitivity))
