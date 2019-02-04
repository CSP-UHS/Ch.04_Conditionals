'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
wronganswers=0

print("Welcome to the hardest quiz of your life! To begin, enter your name.")
name=input("")

print("First question: What is 2+2?")
firstanswer=input("")
if int(firstanswer) == 4:
    print ("Correctamundo!")
else:
    print("Ouch, sorry. That's incorrect.")

print("Second question: What is the name the main character of Naruto?")