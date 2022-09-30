'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("Welcome to The Office Trivia!")
score = 0
TOTAL = 7
print( )
print("Question 1")
print("A. Kevin, Meredith, Dwight")
print("B. Kevin, Oscar, Angela")
print("C. Angela, Oscar, Jim")
Q1 = (input("Who are the three accountants in The Office?"))
if Q1.lower()== "b" or Q1.lower().strip()== "kevin, oscar, angela":
    print("You are correct!")
    score+=1
elif Q1.lower()== "a" or Q1.lower().strip()=="kevin, meredith, dwight" or Q1.lower()=="c" or Q1.lower().strip()=="angela, oscar, jim":
    print("You are wrong, the correct answer was B")
print( )
print("Question 2")
print("Michael Scott was the general manager of Dunder Mifflins Scranton branch")

Q2 = input("Is this statement True or False?")

if Q2.lower()=="true" or Q2.lower()== "t":
    print("You are correct, Michael Scott was Manager from Seasons 1-7")
    score+=1
elif Q2.lower()=="false" or Q2.lower()== "f":
    print("Incorrect, he IS the manager")
print( )
print("Question 3")
print("A. Stamford")
print("B. Nashua")
print("C. Buffalo")
Q3 = input("Which branch merges with Scranton in Season 2?")

if Q3.lower()=="a" or Q3.lower().strip()== "stamford":
    print("You are correct, Stamford merges with Scranton due to downsizing")
    score+=1
elif Q3.lower()=="b" or Q3.lower()=="nashua" or Q3.lower()=="c" or Q3.lower()=="buffalo":
    print("You are incorrect, the correct answer was A")
print( )
print("Question 4")
print("A. The Senator")
print("B. Dwight")
print("C. Andy")
Q4 = input("Who is Angela engaged to first?")

if Q4.lower()== "c" or Q4.lower().strip()== "andy":
    print("You are correct!")
    score+=1
elif Q4.lower()== "a" or Q4.lower().strip()=="the senator" or Q4.lower()=="b" or Q4.lower()=="dwight":
    print("You are incorrect, the answer is C")
print( )
print("Question 5")
Q5 = int(input("How many kids do Pam and Jim have?"))

if Q5==2:
    print("You are correct!")
    score+=1
else:
    print("You are incorrect, they have two kids")
print( )
print("Question 6")
print("A. Robert California")
print("B. Dunder Mifflin")
print("C. David Wallace")
Q6 = input("Who is the original CEO of Dunder Mifflin?")

if Q6.lower() == "c" or Q6.lower().strip()== "david wallace":
    print("You are correct!")
    score+=1
elif Q6.lower()== "b" or Q6.lower().strip()== "dunder mifflin" or Q6.lower()== "a" or Q6.lower().strip()== "robert california":
    print("You are incorrect, the answer is C")
print( )
print("Question 7")
print("Angela Martin is engaged three times throughout the show")

Q7= input("Is this statement True or False?")
if Q7.lower()=="true" or Q7.lower()=="t":
    print("You are correct, she is engaged to Dwight, Andy, and The Senator")
    score+=1
elif Q7.lower()=="false" or Q7.lower()=="f":
    print("You are incorrect, she IS engaged three times")
print( )
print("Thank you for taking the quiz!")
print( )
overall= score/TOTAL*100
print(f"your quiz score is",overall,"%")
print( )
if overall>=93.0:
    print("Your letter grade is an A")
    print("Amazing Job!")
    print("You are an Office expert")
elif overall>=90.0:
    print("Your letter grade is an A-")
    print("Great Job!")
elif overall>=87.0:
    print("Your letter grade is a B+")
    print("Good Job!")
elif overall>=83.0:
    print("Your letter grade is a B")
    print("Nice Job!")
    print("you at least watched the show once")
elif overall>=80.0:
    print("Your letter grade is a B-")
    print("Pretty good.")
elif overall>=77.0:
    print("Your letter grade is a C+")
    print("You did ok.")
elif overall>=73.0:
    print("Your letter grade is a C")
    print("Average.")
    print("you may have watched an episode or two")
elif overall>=70.0:
    print("Your letter grade is a C-")
    print("Just enough.")
elif overall>=67.0:
    print("Your letter grade is a D+")
    print("Barely enough.")
elif overall>=65.0:
    print("Your letter grade is a D")
    print("At least you passed.")
else:
    print("Your letter grade is an F")
    print("Have you even watched the show?")


