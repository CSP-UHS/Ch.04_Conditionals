'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
total = 0
# First question
print("What letter comes after F in the english alphabet? \nA.Z \nB.G \nC.D \nD.W")
a = str(input("answer: "))
total += 1
if a.lower() == "b" or a.lower() == "g":
    print("You are correct!")
    score += 1
elif a.lower() == "c":
    print("c deez nutz")
    score -= 1
else:
    print("you are incorrect. the correct answer is B")

# second question
print("What is the square root of 256")
b = float(input("answer: "))
total += 1
if b == 16:
    print("You are correct!")
    score += 1
else:
    print("you are incorrect the answer was 16")
# third question
print("How many seconds are in one week? \n A. 604800 \n B. 781800 \n C. 0.5 \n D. 601938760")
c = str(input("answer: "))
total += 1
if c.lower() == "a" or c.lower() == "604800":
    print("You are correct!")
    score += 1
else:
    print("You are incorrect, the answer was 604800")
# fourth question
print("What is the 9th largest pyramid in the world \nA. Pyramid of Giza \nB. The pyramid of snow I made in my "
      "backyard \nC. Bass Pro Shop Pyramid \nD. Red Pyramid of Dahshur, Egypt")
d = str(input("answer: "))
total += 1
if d.lower() == "c" or d.lower() == "bass pro shop pyramid" or d.lower() == "bass pro shop":
    print("You are correct")
    score += 1
else:
    print("You are incorrect. The correct answer is the Bass Pro Shop Pyramid in Memphis")
# fifth question
print("What is 5 + 5 - 5 * 5 / 5")
e = int(input("answer: "))
total += 1
if e == 5:
    print("You got it right!")
    score += 1
else:
    print("Incorrect, the answer is 5")
# sixth question
print("What's 9+10? ")
f = float(input("answer: "))
total += 1
if f == 21 or f == 19:
    print("You are correct")
    score += 1
else:
    print("Incorrect, the answer is 21. 19 would have also been acceptable")
# seventh question
print("Who is Joe?")
g = str(input("answer: "))
total += 1
if g.lower() == "joe mama" or g.lower() == "joemama":
    print("Correct")
    score += 1
else:
    print("ITS JOE MAMA LOL")
# score
print("Congratulations on finishing the test you ended with", score, "questions correct out of", total, "questions")
if score >= 0:
    o = round((score/total)*100, 1)
    print("That is a ", o, "%")
else:
    print("deez nutz")
