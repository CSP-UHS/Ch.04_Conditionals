'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
import time

x=0
y=0
print("Welcome to Family Guy Trivia!")
print("---") #q1
time.sleep(6)
print("Who founded Quahog, Rhode Island?"
      "\nA. James Woods"
      "\nB. Peter Griffin"
      "\nC. Griffin Peterson"
      "\nD. Stewie Griffin")
q1=input("What is your answer?")
if q1.upper().strip() == "C":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was Griffin Peterson.")
    y += 1
print("---") #q2
print("How old is Quagmire?"
      "\nA. 61"
      "\nB. 73"
      "\nC. 52"
      "\nD. 48")
q1=input("What is your answer?")
if q1.upper().strip() == "A":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was 61.")
    y += 1
print("---") #q3
print("Who did Joe say put him in his wheelchair??"
      "\nA. Yertle the Turtle"
      "\nB. Horton"
      "\nC. The Lorax"
      "\nD. The Grinch")
q1=input("What is your answer?")
if q1.upper().strip() == "D":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was The Grinch")
    y += 1
print("---") #q4
print("What is the name of the giant chicken?"
      "\nA. Ernie"
      "\nB. Bert"
      "\nC. Josh"
      "\nD. Doesn't have a name")
q1=input("What is your answer?")
if q1.upper().strip() == "A":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was Ernie")
    y +=1
print("---") #q5
print("Where was Peter born?"
      "\nA. America"
      "\nB. Mexico"
      "\nC. International waters"
      "\nD. Canada")
q1=input("What is your answer?")
if q1.upper().strip() == "B":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was Mexico.")
    y += 1
print("---") #q6
print("What is Peter's favorite song?"
      "\nA. Poker Face"
      "\nB. Surfin' Bird"
      "\nC. Fat"
      "\nD. Just Screams")
q1=input("What is your answer?")
if q1.upper().strip() == "B":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was Surfin' Bird.")
    y += 1
print("---") #q7
print("What is Meg's real name?"
      "\nA. Megan"
      "\nB. Megazoid"
      "\nC. Megatron"
      "\nD. Megideth")
q1=input("What is your answer?")
if q1.upper().strip() == "C":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was Megatron.")
    y += 1
print("---") #q8
print("When drunk what instrument is Peter good at?"
      "\nA. Trombone"
      "\nB. Guitar"
      "\nC. Harp"
      "\nD. Piano")
q1=input("What is your answer?")
if q1.upper().strip() == "D":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was the piano.")
    y += 1
print("---") #q9
print("What is Peter's real name?"
      "\nA. Justin"
      "\nB. Peter"
      "\nC. Zach"
      "\nD. Finn")
q1=input("What is your answer?")
if q1.upper().strip() == "A":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was Justin.")
    y += 1
print("---") #q10
print("Who caused the Big Bang?"
      "\nA. God"
      "\nB. Nature"
      "\nC. Peter Griffin"
      "\nD. Stewie Griffin")
q1=input("What is your answer?")
if q1.upper().strip() == "D":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was Stewie Griffin.")
    y += 1
print("---") #q11
print("What is the name of the bar in Family Guy?"
      "\nA. The Drunken Clam"
      "\nB. Moe's Tavern"
      "\nC. Shoney's"
      "\nD. The Drunk Dad")
q1=input("What is your answer?")
if q1.upper().strip() == "A":
    print("Correct!")
    x += 1
else:
    print("Wrong the answer was The Drunken Clam.")
    y += 1
print("-------------------------------------------------------")
z= 100*(x/(x+y))
print("You got" ,z, "% of the questions correct.")