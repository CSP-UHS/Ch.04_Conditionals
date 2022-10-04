'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
total = 7
score = 0
print("Random Facts")

print("1. How many months does a person spend at stop lights in their lifetime?")
mon = input("Answer ->")
if mon.lower() == "4 months" or mon == "4":
    print("Good job!")
    score+=1
else:
    print("Wrong! It was 4 months.")

print("2. How much does a person shed their skin in a lifetime?")
print("A. 10 pounds")
print("B. 5 pounds")
print("C. 29 pounds")
print("D. 100 pounds")
skin = input("Answer->")
if skin.lower() == "d" :
    print("Nice! Why do you know that...")
    score += 1
else:
    print("Wrong! 100 pounds of skin. ")

print("3. Is Jousting an official sport of Maryland? ")
print("True or False?")
sport = input("Answer ->")
if sport.lower() == "true":
    print("Correct!")
    score += 1
else:
    print("Wrong. It was the other option.")

print("4. How many days are we at school this year?")
print("A. 202")
print("B. 180")
print("C. 165")
school = input("Answer ->")
if school.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Wrong. We are here for 180 days and counting.")

print("5. A polar bear weights as much as how many lions?")
pol = input("Answer ->")
if pol == "3" or pol.lower == "3 lions":
    print("Correct")
    score += 1
else:
    print("Wrong. 3 lions per 1 polar bear.")

print("6. How many times do we blink in a day?")
print("A. 4,000")
print("B. 25,000")
print("C. 15,000")
bk = input("Answer ->")
if bk.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong. 15,000 times a day.")

print("7. The worlds most expensive cow was sold at how much $?")
print("A. 34,000")
print("B. 175,000")
print("C. 1,200,000")
cow = input("Answer ->")
if cow.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong. Yes someone spent over a million on a cow.")


Percent=score/total*100
if Percent <= 59:
    print("Test Failed!")
if Percent >= 60 and Percent <=69:
    print("Passed with a D")
if Percent >=70 and Percent<=79:
    print("Passed with a C")
if Percent >=80 and Percent <=89:
    print("Passed with a B")
if Percent >=90 and Percent <=100:
    print("You got an A!")


