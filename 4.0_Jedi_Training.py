# Sign your name:________________

  #1. Make the following program work. (3 mistakes)
midichlorians = int(input("Enter midichlorian count:"))# should be integer not float and forgot to put end parenthesis for input
if midichlorians > 10000:
         print("You have serious Jedi potential")
else:    #should be else
  print("Jedi, you will never be.")



 # 2. Make the following program work. (3 mistakes)
     
x = int(input("Enter a number: "))   #forgot to put integer for what the input will be
if x==3:           #it's x==3 because you are not trying to reassign a variable, forgot colon as well
   print("You entered 3")


  # 3. Make the following program work. (4 mistakes)

answer = input("What is the name of Poe Dameron's Droid? ")
if answer.upper() =="BB8":     #you're asking if answer equals BB8 not a, and its supposed to answer=="BB8"
         print("Correct!")
else: #no colon, no indent on else
         print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes)
     
x = input("Name one of the top 3 greatest Jedi.")
if x.lower()== "yoda" or x.lower()=="luke skywalker" or x.lower()=="obi-wan kenobi":
#x==Yoda not Jedi==Yoda, also Yoda, Luke Skywalker and Obi-Wan Kenobi should all be in quotes because they are answers and not assigned variables and forgot to put x.lower for each one
     print("That is correct!") #forgot paranthesis in print



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower()=="jedi master":
         print("sensitivity = 1000")
elif user_input.lower() == "b" or user_input.lower()=="sith lord" :
         print("sensitivity = 900")
elif user_input.lower() == "c" or user_input.lower()=="droid":
         print("sensitivity= 0")
else:
    print("Not a choice!")



