'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

score = 0

cat = int(input("1. If there's 2 cats in a room and 1 leaves, how many are left? "))
if cat == 1:
    print("Correct!")
    score += 1
else:
    print("Incorrect. There would be 1 left.")

print()

sound = input("2. What sound does a cat make? ")
if sound.lower() == "meow" or sound.lower() == "purr":
    print("Correct!")
    score += 1
else:
    print(" Incorrect. The sound makes the sound 'meow' or 'purr'. ")

print()

print("3. Which of these is true about cats?")
print("A. Cats spend 70% of their lives sleeping.")
print("B. Cats walk like camels and giraffes.")
print("C. The oldest known pet cat existed 9,500 years ago.")
print("D. All of the above.")
facts = input("")
if facts.lower() == "d" or facts.lower() == "d. all of the above" or facts.lower() == "d all of the above" or facts.lower() == "all of the above" or facts.lower() == "d.":
    print("Correct!")
    score += 1
else:
    print("Incorrect. D. All of the above was the correct answer.")

print()

bones = int(input("4. How many bones do cats have? "))
if bones == 230:
    print("Correct!")
    score += 1
else:
    print("Incorrect. Cats have 230 bones.")

print()

inside = input("5. True or false, indoor cats live longer. ")
if inside.lower() == "true" or inside.lower() == "true." or inside.lower() == "t":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The statement is true.")

print()

print("6. Which of these is correct?")
print("A. Cats must be at least a year old to get pregnant.")
print("B. Grapes/raisins are fine for cats to eat.")
print("C. Many cats are lactose intolerant.")
print("D. Cats only have 10 different vocalizations.")
lactose = input("")
if lactose.lower() == "c" or lactose.lower() == "c. many cats are lactose intolerant" or lactose.lower() == "c many cats are lactose intolerant" or lactose.lower() == "many cats are lactose intolerant" or lactose.lower() == "c.":
    print("Correct!")
    score += 1
else:
    print("Incorrect. C. Many cats are lactose intolerant was the correct answer.")

print()

lincoln = int(input("7. How many cats did Abraham Lincoln have with him in the White House? "))
if lincoln == 4:
    print("Correct!")
    score += 1
else:
    print("Incorrect. He had 4 cats living with him in the White House.")

print()

print("Score:" ,score,"/7")
final_score = (score/7)*100
print("This is your final score percent: %0.2f"%(final_score,), "%")