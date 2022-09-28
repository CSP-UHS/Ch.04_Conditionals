'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
s=0
t=0
print("Welcome to my quiz, lets see how smart you really are.")
print()

print("What villager in the Animal Crossing series, not from the original Animal Crossing,")
print("got cut from an installment after appearing in a previous installment?")
questionOne = input("")
if questionOne.lower() == "champ" or questionOne.lower() == "kaitlin":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect, the correct answer was Champ or Kaitlin.")
    t += 1

print()
print("What generation of Animal Crossing is New Horizons considered to be?")
print("A: First Generation")
print("B: Second Generation")
print("C: Third Generation")
print("D: Fourth Generation")
questionTwo = input("")
if questionTwo.lower() == "d":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect, the correct answer was D.")
    t += 1

print()
print("How many villagers are there is Animal Crossing New Horizons?")
questionThree = input("")
if questionThree == "397":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect, the correct answer was 397")
    t += 1

print()
print("How many villager species are there in Animal Crossing New Horizons?")
print("A: 32")
print("B: 35")
print("C: 36")
print("D: 38")
questionFour = input("")
if questionFour.lower() == "b":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect, the correct answer was B")
    t += 1

print()
print("Which of the following is not a personality type in Animal Crossing?")
print("A: Jock")
print("B: Lazy")
print("C: Friendly")
print("D: Snooty")
questionFive = input("")
if questionFive.lower() == "c":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect, the correct answer was C")
    t += 1

print()
print("What was the first console Animal Crossing was on in the US?")
questionSix = input("")
if questionSix.lower() == "gamecube":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect, the correct answer was GameCube")
    t += 1

print()
print("How many cat villagers are there in New Horizons?")
questionSeven = input("")
if questionSeven == "23":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect, the correct answer is 23")
    t += 1

print()
print("How many octopus villagers are there in New Horizons")
questionEight = input("")
if questionEight == "3":
    print("Correct")
    s += 1
    t += 1
else:
    print("Incorrect the correct answer is 3")
    t += 1
print()

o = (s/t)*100

if o >= 93:
    letter = "A"
elif o >= 90:
    letter = "A-"
elif o >= 87:
    letter = "B+"
elif o >= 83:
    letter = "B"
elif o >= 80:
    letter = "B-"
elif o >= 77:
    letter = "C+"
elif o >= 73:
    letter = "C"
elif o >= 70:
    letter = "C-"
elif o >= 67:
    letter = "D+"
elif o >= 65:
    letter = "D"
else:
    letter = "F"

print("Your overall grade is",o,",", letter)