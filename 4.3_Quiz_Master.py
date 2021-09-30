'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
a = 0
b = 7
print("Would you like to take a quiz?")
print("yes")
print("no")
an = input(str())
if an.lower() == "yes":
    print("Correct, let's get started")
    a+=1
else:
    print("the answer is yes, and your taking it anyway")
print("A.barking at the mailman.")
print("B.Making a resume.")
print("C.coding.")
print("D.asking for mints")
dog = input(str("What da dog doin?"))
if dog.lower() == "asking for mints" or dog.lower()== "d":
    print("That is correct nice job")
    a+=1
else:
    print("The correct answer is, asking for mints")
print("In Final Fantasy 13, what is lightnings real name")
print("A.Serah")
print("B.Claire")
print("C.Tifa")
print("D.Vanille")
sava = input()
if sava.lower() == "b" or sava.lower() == "claire":
    print("Correct, nice job")
    a+=1
else:
    print("Good try, but incorrect. It's b")
print("When did 1984 end")
ans = input()
if ans == "1985":
    print("I think thats right")
    a+=1
else:
    print("wrong :/, 1985")
print("What is 3, cubed, cubed?")
k = input()
if k == "19683":
    print("Great, big brain")
    a+=1
else:
    print("bad, small brain, it's 19683")

fav = input(str("What is denis's favorite number"))
if fav == "13":
    print("Congratulations, you are correct")
    a+=1
else:
    print("You are incorrect, the answer is 13")

print("A.Vans")
print("B.Nike")
print("C.Adidas")
print("D.Barefoot")
ustu = input(str("What shoes are denis wearing"))

if ustu.lower() == "c" or ustu.lower() == "adidas":
    print("You are correct :)")
    a+=1
else:
    print("sad day, incorrect, he is wearing Adidas")

print("You got",a,"out of",b)
print()
ove = (a/b)*100
print(ove,"%")
if ove >= 90:
    print("you have an A")
elif ove <= 89 and ove >=80:
    print("you have a B")
elif ove <=79 and ove >=70:
    print("you have a C")
elif ove <= 69 and ove >= 60:
    print("you have a D")
else:
    print("you got an F, Your grade sucks")
