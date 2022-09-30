'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("WELCOME TO THE QUIZ, NERD")
print()
print("WHICH LETTER IS BEST?")

answer = input("ANSWER:")
if answer.lower() == "a":
    print("CORRECT")
    score = 1
else:
    print("WRONG, THE CORRECT ANSWER WAS 'A' ARE YOU TRYING TO GET A BAD GRADE?")
    score = 0
print()
print("WAS MACHE ICH IN MEINER FREIZEIT?")
print("A) POSAUNE SPIELEN")
print("B) HAUSAUFGABEN MACHEN")
print("C) LAUFEN")
print("D) JAPANISCH SPRECHEN")
answer = input("ANSWER:")
if answer.lower() == "a":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT, ICH SPIELE POSAUNE IN MEINER FREIZEIT")
print()
print("HOW MANY MINUTES DID I SPEND MAKING THIS QUESTION?")
answer = input("ANSWER:")
if answer == "0":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT, IT WAS 0")
print()
print("WHAT IS THE MEANING OF LIFE?")
print("A) THERE IS NO MEANING")
print("B) FORTY TWO")
print("C) TAKING QUIZZES")
print("D) BEING NICE")
answer = input("ANSWER: ")
if answer.lower() == "b":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT, ITS FORTY TWO. DID YOU NOT READ THE GUIDE?")
print()
print("WHERE DO BIRDS GO IN THE WINTER?")
print("A) CANADA")
print("B) EUROPE")
print("C) SOUTH")
print("D) THE GOVERNMENT SENDS THEM TO AUSTRALIA TO RECHARGE SO THEY CAN COME BACK AND SPY ON US")
answer = input("ANSWER: ")
if answer.lower() == "c":
    print("CORRECT")
    score += 1
elif answer.lower() == "d":
    print("CORRECT, THEY ARE HIDING SOMETHING FROM US")
    score += 1
else:
    print("INCORRECT, THEY GO SOUTH")
print()
print("WHICH ONE IS A NAVAJO FOLK MONSTER?")
print("A) BIGFACE")
print("B) ma'ii")
print("C) BIGFOOT")
print("D) SKINWALKER")
answer = input("ANSWER: ")
if answer.lower() == "d":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT, ITS THE SKINWALKER A SHAPE-SHIFTING WITCH")
print()
print("WHAT IS THE FLATTEST STATE IN THE USA?")
print("A) KANSAS")
print("B) FLORIDA")
print("C) IOWA")
print("D) NEBRASKA")
answer = input("ANSWER: ")
if answer.lower() == "b":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT, ITS FLORIDA")





print()
hpgh = score/7
overall = score/7*100
print("Your score is",f"{hpgh:.2%}")
if overall <=100 and overall >=94:
    print("Your final grade is and A, GOOD JOB")
elif overall <94 and overall >=90:
    print("Your final grade is an A-, GOOD JOB")
elif overall <90 and overall >=87:
    print("Your final grade is an B+, IVE SEEN BETTER")
elif overall <87 and overall >=83:
    print("Your final grade is an B, IVE SEEN BETTER")
elif overall <83 and overall >=80:
    print("Your final grade is an B-, NOT THE WORST IVE SEEN")
elif overall <80 and overall >=77:
    print("Your final grade is an C+, STILL A GOOD GRADE I GUESS")
elif overall <77 and overall >=73:
    print("Your final grade is an C, STILL A GOOD GRADE I GUESS")
elif overall <73 and overall >=70:
    print("Your final grade is an C-, YOU CAN STILL RETAKE RIGHT?")
elif overall <70 and overall >=67:
    print("Your final grade is an D+, YOU CAN STILL RETAKE RIGHT?")
elif overall <67 and overall >=60:
    print("Your final grade is an D, WOW I ACTUALY THOUGHT YOU WOULD FAIL")
else:
    print("Your final grade is an F, YOUR TERRIBLE AND ARE DOOMED TO FAIL GO TO JOHNSTON NERD")
