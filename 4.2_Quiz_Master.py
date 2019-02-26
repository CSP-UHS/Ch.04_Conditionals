'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("Welcome to the hardest quiz of your life! To begin, enter your name.")
playername=input("")
rightanswers=0

print("Okay, first question. What is 2 times 3?")
firstanswer=input("")
if firstanswer == str(6) or firstanswer == str("six"):
    print("Absolutely. Great job!")
    rightanswers+=1
    print()
else:
    print("Sorry, that's incorrect. The correct answer was 6.")
    print()

print("Okay, second question.")
print("Who is Harry Potter's nemesis?")
secondanswer=input("")
if secondanswer.lower() == "voldemort" or secondanswer.lower() == "lord voldemort":
    print("Absolutely. Great job!")
    rightanswers+=1
    print()
else:
    print("Sorry that's incorrect. The correct answer is Voldemort.")
    print()

print("Third question. Which of these characters has green skin? (Just put in the corresponding letter)")
print("A. Mace Windu")
print("B. Obi Wan Kenobi")
print("C. Anakin Skywalker")
print("D. Yoda ")
thirdanswer=input("")
if thirdanswer == str("D") or thirdanswer == str("d"):
    print("Absolutely. Great job!")
    rightanswers+=1
    print()
else:
    print("Sorry, that's incorrect. The correct answer is A. Mace Windu.")
    print()

print("Fourth question. I had 3 cookies, but ate 2 of them. How many do I have now?")
fourthanswer=input("")
if fourthanswer == str("1") or fourthanswer == str("one"):
    print("Absolutely. Great job!")
    rightanswers+=1
    print()
else:
    print("Sorry, that's incorrect. The correct answer is 1.")
    print()

print("Final question. What is the name of Mickey Mouse's dog?")
fifthanswer=input("")
if fifthanswer == str("Pluto") or fifthanswer == str("pluto"):
    print("Absolutely. Great job!")
    rightanswers+=1
    print()
else:
    print("Sorry, that's incorrect. The correct answer is Pluto.")
    print()

print("Okay " + str(playername)+ ", here's your score:")
percentage=(int(rightanswers)/5)*100
print(str(percentage)+ "%")
