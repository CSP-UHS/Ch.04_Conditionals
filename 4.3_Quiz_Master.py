'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
'''
What day did 9/11 happen?
a,9/11
What year did WW2 end?
a,1945
Do you use PC or console for gaming?
a, PC
Do you have a girlfriend?
a, no

Obama?
a, Obama
'''
points=0
qone=input("What day did 9/11 happen?\n")
if qone.upper()=="9/11":
    points+=1
    print("Correct")
    print("Points so far:",points)
elif qone.upper()=="TUESDAY":
    points+=1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

qtwo=input("Who did 9/11?\n")
if qtwo.upper()== "GEORGE W. BUSH":
    points += 1
    print("Correct")
    print("Points so far:", points)
elif qtwo.upper()== "BUSH":
    points += 1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

qthree=input("Which one of these things are correct?\nA: 2+2=4 \nB: COVID-19 is not a big deal \nC: I saw blue vent\n")
if qthree.upper()=="A":
    points += 1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

qfour=input("What year did WW2 end?")
if qfour.upper()=="1945":
    points += 1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

qfive=input("How do you spell my name?")
if qfive.upper()=="GERARDO":
    points += 1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

qsix=input("What school is this?")
if qsix.upper()=="URBANDALE":
    points += 1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

qseven=input("What state is this?")
if qseven.upper()=="IOWA":
    points += 1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

qeight=input("Is this a terrible quiz?")
if qeight.upper()=="YES":
    points += 1
    print("Correct")
    print("Points so far:", points)
else:
    print("Incorrect")
    print("Points so far:", points)

if points>5:
    print("YOU WIN!!!")
    print("Your points: ",points)
if points<5:
    print("YOU LOSE!!!")
    print("Your points: ",points)