'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
points=0
score=points/7
print("A.Black Air Forces")
print("B.Jordan 1's")
print("C.Vans")
print("D.Crocs")
print("E.Barefoot")
print()
b=str(input("What footwear does Gavin wear?"))
print()
if b.lower()=="vans" or b.lower()=="c":
    print("Correct! How could you know that?")
    points+1
else:
    print("Incorrect! The correct option was C.Vans")
print()
c=int(input("Name one of the years the Houston Rockets won a championship"))
print()
if c==1995 or c==1994:
    print("Correct! Surprised you got that one!")
    points + 1
else:
    print("Incorrect! 1994 and 95 were acceptable answers")
print()
d=str(input("What is the darkest paint called?"))
if d.lower()=="vantablack":
    print("Correct! Surprised you knew that one!")
    points + 1
else:
    print("Incorrect! The correct answer was Vantablack!")
print()
e=float(input("What are first 6 digits of pi?"))
if e==3.14159:
    print("Correct! You must be a math mathmatician")
    points + 1
else:
    print("Incorrect! It was 3.14159")
print()
print("A.Giraffe")
print("B.Penguin")
print("C.Tortoise")
print("D.Rhino")
print()
f=str(input("What species of animal use to be 6'8 and called Collosal"))
print()
if f.lower()=="penguin" or f.lower()=="b":
    print("Correct! You are a genius!")
    points + 1
else:
    print("Incorrect! Delete System 32!")
print()
g=str(input("How fast was the first person that was convicted of speeding going?"))
if g=="8" or g.lower()=="8 mph" or g.lower()=="8mph":
    print("Correct!")
    points + 1
else:
    print("Incorrect! The answer was 8 mph!")
print()
print("A.Michael Jordan played his last season in the nba")
print("B.New all time points leader")
print("C.Creation of 2 new expansion teams")
print("D.Malice at the Palace")
print()
h=(input("What major NBA event happened on November 19th, 2004?"))
if h.lower()=="d" or h.lower()=="malice at the palace":
    print("Correct!")
    points + 1
else:
    print("Incorrect! the correct answer was D. Malice at the Palace")
print()
print("Your overall score was",score,"% !")



