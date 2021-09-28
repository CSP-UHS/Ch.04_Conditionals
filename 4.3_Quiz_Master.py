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
    print("Too bad, your taking it anyway")
print("A.The dog is playing")
print("B.The dog is eating dinner.")
print("C.The dog is sleeping.")
dog = input(str("What da dog doin?"))
if dog.lower() == "the dog is partaking in a minuscule amount of trickery":
    print("That is correct nice job")
    a+=1
else:
    print("That was a trick question, the correct answer is, The dog is Partaking in a minuscule amount of trickery")
print("In the destiny universe, what is Savathun trying to accomplish")
print("A.Revive Cayde 6, the fallen exo")
print("B.Remove her worm")
print("C.Harness the light and stop the Guardians")
sava = input()
if sava.lower() == "b" or sava.lower() == "remove her worm":
    print("Correct, nice job")
    a+=1
else:
    print("Good try, but incorrect")
print("When did 1984 end")
ans = input()
if ans == "1985":
    print("I think thats right")
    a+=1
else:
    print("wrong :/")
print("What is 3, cubed, cubed?")
k = input()
if k == "7625597484987":
    print("Great, big brain")
    a+=1
else:
    print("bad, small brain")

fav = input(str("What is denis's favorite number"))
if fav == "13":
    print("Congratulations, you are correct")
    a+=1
else:
    print("You are incorrect, the answer is 13")
ustu = input(str("What is 9+10"))
if ustu == "21":
    print("You are correct :)")
    a+=1
else:
    print("sad day, incorrect, the")

print("You got",a,"out of",b)