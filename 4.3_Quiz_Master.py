'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
print("1. What kind of eclipse happened earlier this week?")

print("A. Lunar Eclipse")
print("B. Solar Eclipse")
print("C. A total eclipse of the heart")


user_input = input("Choose a character?")

if user_input.lower() == "c" or user_input.lower() == "a total eclipse of the heart":
    print("Correct!")
    score+=1
else:
    print("Incorrect! It was a total eclipse of the heart!")

print("2. How many total minutes of silence are there in all the twilight movies.")

print("A. 32")
print("B. 26")
print("C. A total eclipse of the heart")
print("D. What movie?")


user_input = input("Choose a character?")

if user_input.lower() == "b" or user_input.lower() == "26":
    print("Correct!")
    score+=1
else:
    print("Incorrect! It was 26 minutes!")

print("3. What is the 30th Digit Past the Decimal of Pi?")

print("A. 9")
print("B. 4")
print("C. 3.143.14")


user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "9":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It is 9")


print("4. Playstation or Xbox?")

print("A. Playstation")
print("B. Xbox")
print("C. Wii U")
print("D. PC Master Race")



user_input = input("Choose a character?")

if user_input.lower() == "c" or user_input.lower() == "wii u":
    print("Correct!")
    score += 1
else:
    print("Wii U Wii U Wii U, the ambulance is coming to help you recover from that incorrect response!")

print("5. Define what the word \"Forgetting\" Means")

print("A. To Strive")
print("B. To Run")
print("C. Winning")
print("D. Sorry, I can't remember")


user_input = input("Choose a character?")

if user_input.lower() == "d" or user_input.lower() == "sorry, I can't remember":
    print("Correct!")
    score += 1
else:
    print("Incorrect! I can't remember what the answer was.")

print("6. What do Americans do 15-20 Times a day")

print("A. Open the Fridge")
print("B. Unlock their phones")
print("C. Breath")
print("D. Drink Water")


user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "open the fridge":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was open the fridge!")

print("7. Type Your Answer!")

apple = input("If Apple made a car, what would it not have?")


if apple.lower() == "windows" or user_input.lower() == "non-proprietary charging":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the answer was Windows! HAHAHA!")

print("THANKS FOR PLAYING!")
total = (score*100)/7
print(total)

if total >= 90:
    print("You just won Million Dollars! It's an A!")
elif total >= 80:
    print("Nice, you got a B!")
elif total >= 70:
    print("You got a C")
elif total >= 60:
    print("You can do better than a D!")
elif total < 60:
    print("F. That's just unfortunate.")