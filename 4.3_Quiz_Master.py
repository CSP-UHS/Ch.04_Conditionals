'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
############################################################
score=0
print("Welcome to my quiz!")
print()
num=int(input("What is 5+15?:"))
if num == 20:
    score = score+1
    print("Correct")
else:
    print("False")

print()
############################################################
num=int(input("What is 55x74+69?:"))
if num == 4139:
    score = score + 1
    print("Correct")
else:
    print("False")
print()
############################################################
abuja=input("What is the capital of Nigeria?:")
if abuja.lower()== "abuja":
    score = score + 1
    print("Correct")
else:
    print("False")
print()
############################################################
neutrons=int(input("How many neutrons are in a colbalt atom?:"))
if neutrons == 27:
    score = score + 1
    print("Correct")
else:
    print("False")
print()
############################################################
states=int(input("How many States are in the United States?:"))
if states == 50:
    score = score + 1
    print("Correct")
else:
    print("False")
print()
############################################################
phones=int(input("How many iPhone models are there?:"))
if phones == 29:
    score = score + 1
    print("Correct")
else:
    print("False")
print()
############################################################
print("A. Franklin D. Roosevelt")
print("B. William Henry Harrison")
print("C. Stephen Grover Cleveland")

user_input=input("Which of the former Presidents served two separate terms?:")

if user_input.lower() == "C":
    score = score + 1
    print("Correct")
else:
    print("False")
print()
############################################################
amazon=input("Who is the CEO of Amazon?:")
if amazon.lower() == "jeff bezos":
    score = score + 1
    print("Correct")
else:
    print("False")
print()
############################################################
yoda=input("What is the most famous Yoda Quote?:")
if yoda.lower() == "do or do not, there is no try":
    score = score + 1
    print("Correct")
else:
    print("False. The correct answer is 'do or do not, there is no try.'")
print()
############################################################
color=input("What is the best color?:")
if color.lower() == "purple":
    score = score + 1
    print("Correct")
else:
    print("What's wrong with you? It's purple!")
print()
############################################################
final_score = score*10
print("Your score is:", final_score , "percent" )
if final_score >= 89 :
    print("The grade is an A")
elif final_score >= 79:
    print("The grade is a B")
elif final_score >= 69:
    print("The grade is a C")
elif final_score >= 59:
    print("The grade is a D")