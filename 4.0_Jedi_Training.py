# Sign your name:Zachary Blum
  #1. Make the following program work. (3 mistakes)
midichlorians = float(input("Enter midichlorians count: "))
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")
 # 2. Make the following program work. (3 mistakes)
x = input("Enter a number: ")
if x == 3:
    print("You entered 3")
  # 3. Make the following program work. (4 mistakes)
answer = input("What is the name of Poe Dameron's Droid? ")
a = "name of droid"
if a == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")
  # 4. Make the following program work. (4 mistakes)
x = input("Name one of the top 3 greatest Jedi.")
jedi = "name of jedi"
if jedi == input("Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi"):
    print("That is correct!")
 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.
print("Welcome to the Jedi Academy!")
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")
user_input = input("Which side do you want to be")
if user_input.upper() == "A" or "Jedi Master":
    x = 1000
elif user_input.upper() == "B" or "SITH LORD":
    x = 900
elif user_input.upper() == "C":
    x = 0
else:
    print("Not a Choice")
print("Sensitivity:equals", x)
#finished
