'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print(" _____                         _____       _              __  ______ _____  ________  ___  _")
print("/  ___|                       |  _  |     (_)            / _| |  _  \  _  ||  _  |  \/  | | |")
print("\ `--. _   _ _ __   ___ _ __  | | | |_   _ _ ____   ___ | |_  | | | | | | || | | | .  . | | |")
print(" `--. \ | | | '_ \ / _ \ '__| | | | | | | | |_  /  / _ \|  _| | | | | | | || | | | |\/| | | |")
print("/\__/ / |_| | |_) |  __/ |    \ \/' / |_| | |/ /  | (_) | |   | |/ /\ \_/ /\ \_/ / |  | | |_|")
print("\____/ \__,_| .__/ \___|_|     \_/\_\.\__,|_/___| \____/|_|   |___/  \___/  \___/\_|  |_/ (_)")
print("            | |")
print("            |_|")
print()

qzero = input("Are you ready? (yes or no) ")
quiz = 0
numcorrect = 0
numincorrect = 0
if qzero.lower() == "yes":
    quiz = 1
    print("")
else:
    print("I see")

if quiz == 1:

#Question 1
    print("Question One:")
    ans1 = input("What is 69+420? ")
    if (ans1) == "489":
        print("Correct")
        print("")
        numcorrect = int(numcorrect) + 1
    else:
        print("Incorrect!")
        print("Correct answer: 489")
        print("")
        numincorrect = int(numincorrect) + 1


#Question 2
    print("Question Two:")
    ans2 = input("What is tyler one? ")
    if ans2.lower() == "built different":
        print("Correct")
        print("")
        numcorrect = int(numcorrect) + 1
    else:
        print("Incorrect!")
        print("Correct answer: built different")
        print("")
        numincorrect = int(numincorrect) + 1


#Question 3
    print("Question Three:")
    print()
    print("A. Dual")
    print("B. Bisolar")
    print("C. Binary")
    print()

    ans3 = input("What is a solar system with two stars called? ")
    if ans3.lower() == "binary" or ans3.lower() =="c":
        print("Correct")
        print("")
        numcorrect = int(numcorrect) + 1
    else:
        print("Incorrect!")
        print("Correct answer: C")
        print("")
        numincorrect = int(numincorrect) + 1

#Question 4
    print("Question Four:")
    print()
    print("A. The person who wrote this code")
    print("B. Your Mom")
    print("C. Some coffee adict")
    print("")

    ans4 = input("Who gets nowhere near enough sleep ever? ")

    if ans4.lower() == "The person who wrote this code" or ans4.lower() == "a":
        print("Correct")
        print("")
        numcorrect = int(numcorrect) + 1
    else:
        print("Incorrect!")
        print("Correct answer: A")
        print("")
        numincorrect = int(numincorrect) + 1

#Question 5
    print("Question Five, Complete the quote:")
    print()
    ans5 = input("The Dark Side of the Force is a pathway to many abilities some consider to be _________. ")

    if ans5.lower() == "unnatural":
        print("Correct")
        print("")
        numcorrect = int(numcorrect) + 1
    else:
        print("Incorrect!")
        print("Correct answer: unnatural")
        print("")
        numincorrect = int(numincorrect) + 1

#Question 6
    print("Question Six:")
    print()
    print("A. Prequels (I-III)")
    print("B. Original Trilogy (IV-VI)")
    print("C. Sequels (VII-IX)")
    print()
    ans6 = input("What is the best StarWars trilogy? ")
    print("In my opinion the Prequels are the best but you are allowed to have your own opinion :) (no incorrect answers)")
    print()
    print("Correct")
    print()
    numcorrect = int(numcorrect) + 1


#Question 7
    print("Question Seven:")
    print("")
    print("A. Daniel Mitchell")
    print("B. Daniel Mitchell")
    print("C. Daniel Mitchell")
    print("")
    ans7 = input("Who cant think of any more questions? ")

    if ans7.lower() == "a" or ans7.lower() == "b" or ans7.lower() == "c" or ans7.lower() == "daniel mitchell":
        print("Correct")
        print("")
        numcorrect = int(numcorrect) + 1
    else:
        print("Incorrect!")
        print("Correct answer: LITERALLY ANY OF THEM HOW DID YOU GET THIS WRONG")
        print("")
        numincorrect = int(numincorrect) + 1

#End Logic
    total = int(numcorrect) + int(numincorrect)
    score = (numcorrect / total) *100
    overall = round(score, 1)

    print("Your score was " + str(overall) + "%")

    if overall >= 90:
        print("Letter Grade: A")
    elif overall >= 80:
        print("Letter Grade: B")
    elif overall >= 70:
        print("Letter Grade: C")
    elif overall >= 60:
        print("Letter Grade: D")
    elif overall <= 60:
        print("Letter Grade: F")

else:
    print ("Come back when you feel that you are worthy")
