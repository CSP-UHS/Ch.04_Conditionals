# Sign your name:Denis Toric

  #1. Make the following program work. (3 mistakes)
     #Forgot Colons, forgot the variable in elif and forgot extra ) in the end of the first line for the input
     midichlorians = float(input("Enter midichlorian count: "))
     if midichlorians > 10000:
         print("You have serious Jedi potential")
     elif midichlorians:
         print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)
     #Forgot to put input in (), didn't put int or float behind input and didn't do the double equals(also didn't put the colon)
     x = int(input("Enter a number: "))
     if x == 3:
         print("You entered 3")


  # 3. Make the following program work. (4 mistakes)
     #Didn't put string as the input, didn't put the full varaible in the if, didn't do the double equals, and the else statement needs to be at 0 spaces with the colon aswell
     answer = str(input("What is the name of Poe Dameron's Droid? "))
     if answer == "BB8":
         print("Correct!")
     else:
         print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)
     # between the or's you must put the variable and == again, the print string must be in (), instead of "jedi" it should be "x" and the acceptable jedis must be in "". (Optional, to optimize this code the x can be made to accept lower and upper case if the .lower() command is used also must enter the accpetable string as lowercase)
     x = input("Name one of the top 3 greatest Jedi.")
     if x.lower() == "yoda" or x.lower()=="luke skywalker" or x.lower()=="obi-wan kenobi":
         print ("That is correct!")



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
     #change else if to elif, in last print line change the capital s to lower case, accepteable answers must be put into "" and double equals,
print("Welcome to the Jedi Academy!")
print()
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")
print()
user_input = str(input("Choose a character?"))

if user_input.lower() == "a" or user_input.lower()=="jedi master":
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower()=="sith lord":
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower()=="droid":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity=("")

print("Sensitivity:",sensitivity,)
#a