'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
Score = 0
print(  "A. Blue    "
        "B. Green   "
        "C. Purple  "
        "D. Red")
Q1 = input("What color is the sky? ")
if Q1.lower().strip()=="a"or Q1.lower().strip()=="blue":
    print("Correct!")
    Score+=1
else:
    print("Wrong!"
          "The Answer is: A. Blue")

print()
Q2 = input("What is 4+4? ")
if Q2.lower().strip()=="8":
    print("Correct! You can do math!")
    Score+=1
else:
    print("Wrong!")

print()
Q3 = input("What is the fifth planet in the solar system? ")
if Q3.lower().strip()=="jupiter":
    print("Correct! You know your planets!")
    Score+=1
else:
    print("Wrong!")

print()
Q4 = input("What birds feathers turn pink because of their messy eating habits? ")
if Q4.lower().strip()=="flamingo"or Q4.lower()=="flamingos"or Q4.lower()=="flamingo's":
    print("Correct!")
    Score+=1
else:
    print("Wrong!")

print()
Q5 = input("What country is to the immediate south of England? ")
if Q5.lower().strip()=="france"or Q5.lower()=="belgium":
    print("Correct! I know you searched up that answer.")
    Score+=1
else:
    print("Wrong!")

print()
Q6 = input("What is the next holiday? ")
if Q6.lower().strip()=="halloween":
    print("Correct! Glad to know some people still celebrate it!")
    Score+=1
else:
    print("Wrong! I bet you put Christmas.")

if Score>3:
    print()
    print("Congrats! You passed the quiz! "
          "Your score is: ",Score,)
else:
    print()
    print("Well, you failed the quiz."
          " However, out of the kindness of my heart I will give you one more chance to right your wrongs."
          " Answer this question and you pass the quiz.")
    print()
    BQ = input("What is the name of my cat? ")
    if BQ.lower().strip()=="ajax":
        print("Correct! Wow im impressed! I'll give you 5 points.")
        Score+=5
        print("Your score is: ",Score)
    else:
        print("To bad, so sad.")
        print("Your score is: ",Score)
if Score>4:
    print("Your numerical score is: A")
elif Score>2 and Score<5:
    print("Your numerical score is: C")
elif Score<3:
    print("Your numerical score is: F")
