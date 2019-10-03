'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Welcome to my Shrek Quiz!")
print()

number_correct = 0
correct = "Correct. Do the Roar!"

answer = input("Question #1\nWhat year was the original Shrek movie released? ")
if answer=="2001":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect.\nShrek was released in 2001.")
print()

answer = input("Question #2\nHow many Shrek movies have been released? \nA. 4\nB. 3\nC. 1\nD. 2")
if answer.lower()=="a" or answer=="4" or answer.lower()=="a. 4":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect.\n4 (A) Shrek movies have been released.")
print()

answer = input("Question #3\nFinish the quote: What are you doing in my _____? ")
if answer.lower()=="swamp":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect.\nSwamp is the correct answer.")
print()

answer = input("Question #4\nWhat does Gingy insist that Lord Farquaad not touch? \nA. his gumdrop eyes\nB. his heart\nC. his eyes\nD. his gumdrop buttons")
if answer.lower()=="d" or answer.lower()=="his gumdrop buttons" or answer.lower()=="d. his gumdrop buttons":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect. Gingy did not want his gumdrop buttons (D) touched.")
print()

answer = input("Question #5\nWhat character(s) turn(s) into a frog before their death? \nA. King Harold\nB. Lord Farquaad\nC. Gingy\nD. all of the above")
if answer.lower()=="a" or answer.lower()=="king harold" or answer.lower()=="a. king harold":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect. King Harold turned into a frog before his death.")
print()

answer = input("Question #6\nTrue or False: The Fairy Godmother is Prince Charming's grandma. ")
if answer.lower()=="true":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect. The Fairy Godmother is Prince Charming's grandma.")
print()

answer = input("Question #7\nIn what language does Shrek mean monster? \nA. Italian\nB. Armenian\nC. Yiddish\nD. Swahili")
if answer.lower()=="c" or answer.lower()=="yiddish" or answer.lower()=="c. yiddish":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect. In Yiddish, Shrek means monster.")
print()

answer = input("Question #8\nWhich of the following is Cal's favorite Shrek movie? \nA. Shrek\nB. Shrek the Third\nC. Shrek Forever After\nD. Shrek 2")
if answer.lower()=="b" or answer.lower()=="shrek the third" or answer.lower()=="b. shrek the third":
    print(correct)
    number_correct+=1
else:
    print("Sorry, that is incorrect. My favorite Shrek movie is Shrek the Third.")
print()


ovr_grade = float((number_correct)/8)*100
if ovr_grade >=90:
    print("Your overall grade is an A and",ovr_grade)
    print("You are a strong ogre. Do the Roar!")
elif ovr_grade <90 and ovr_grade >=80:
    print("Your overall grade is a B and",ovr_grade)
    print("You are an ogre. Do the Roar!")
elif ovr_grade <80 and ovr_grade >=70:
    print("Your overall grade is a C and",ovr_grade)
    print("Watch the Shrek movies!")
elif ovr_grade <70 and ovr_grade >=60:
    print("Your overall grade is a D and",ovr_grade)
    print("Watch the Shrek movies!")
else:
    print("Your overall grade is a F and",ovr_grade)
    print("Watch the Shrek movies!")