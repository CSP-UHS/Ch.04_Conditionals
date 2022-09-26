'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
points = 0
question1 = int(input("What is 1 + 1? "))
if question1 == 2:
    print("Good job 2 is correct!")
    points += 1
else:
    print("No the answer is 2 how did you get that wrong!!?")
print()

question2 = input("What does Mr. Carver say at the end of every announcement? ")
if question2.lower() == "go jhawks" or "go j hawks":
    print("That is correct! GO JHAWKS!!!")
    points += 1
else:
    print("That's a good guess but obviously the answer is GO JHAWKS!!!")
print()

print("What season is it right now?")
print("A. Spring")
print("B. Summer")
print("C. Fall")
print("D. Winter")
question3 = input("")
if question3.lower() == "c":
    print("That is correct!")
    points += 1
else:
    print("Umm no, clearly fall just started")
print()

question4 = input("What month is it? ")
if question4.lower() == "September":
    print("That is correct!")
    points =+ 1
else:
    print("No! C'mon it's obviously september")
print()

question5 = int(input("What year is it? "))
if question5 == 2022:
    print("2022 is correct!")
    points += 1
else:
    print("Nope its 2022 what year are you living in?")
print()

print("Your final score is", points, "/ 5")
