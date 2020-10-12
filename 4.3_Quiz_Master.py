'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score=0
print("Himbo Quiz")
print("Correct answers are based off what is said in the video (If you know you know)")

print()

print("1: Who painted the Mona Lisa?")
print("A: Mona Lisa")
print("B: Da Vinci")
print("C: Da Vinky")

answerone = input("Your answer:  ")
if answerone.lower() == "a" or answerone.lower() == "mona lisa":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("2: How many days are in a year?")

answertwo = int(input("Your answer:  "))
if answertwo == 324:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("3: What is the fiery liquid that flows from a volcano?")

answerthree = input("Your answer:  ")
if answerthree.lower() == "sriracha":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("4: What money is used in Germany?")
print("A: Euros")
print("B: Dollars")
print("C: Cash")

answerfour = input("Your answer:  ")
if answerfour.lower() == "c" or answerfour.lower() == "cash":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("5: Which star is at the center is at the center of our Solar System?")

answerfive = input("Your answer:  ")
if answerfive.lower() == "the north star" or answerfive.lower() == "north star":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("6: A yellow fruit")

answersix = input("Your answer:  ")
if answersix.lower() == "orange" or answersix.lower() == "a yellow apple" or answersix.lower() == "yellow apple":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("7: How many hours are in 2 days?")

answerseven = int(input("Your answer:  "))
if answerseven == 32:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("8: When did the Cold War end?")
print("A: 1989")
print("B: Summer")
print("C: Winter")

answereight = input("Your answer:  ")
if answereight.lower() == "b" or answereight.lower() == "summer":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("9: On which continent is the South Pole?")

answernine = input("Your answer:  ")
if answernine.lower() == "south america":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("")

print("10: What do tadpoles turn into?")

answerten = input("Your answer:  ")
if answerten.lower() == "butterflies":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print()

grade = score*10
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade>= 60:
    print("D")
elif grade<60:
    print("F")

print("You got", score, "out of 10 correct")
print("Your grade is", grade,"%")
print("Congrats!")
print("Here is the video the answers are based off of:")
print("https://www.youtube.com/watch?v=CMnLDhph5Cc")