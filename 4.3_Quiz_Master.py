'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
total_correct=0
questions=0
print("Hello and Welcome to my test.")
qs=int(input("1. If p+z=6 and z=5, what is p equal to?\n p = "))
questions+=1
if qs==1:
    print("That is correct!")
    total_correct+=1
else:
    print("That's a big oof\n The correct answer is 1")
qs=input("2. What is the President's last name?")
questions+=1
if qs.lower()=="trump":
    print("Of course!")
    total_correct+=1
else:
    print("No, dumb dumb")
qs=int(input("3. What is the square root of 81"))
questions+=1
if qs==9:
    print("Yep!")
    total_correct+=1
else:
    print("No, go back to 8th grade")
qs=input("4. What is Hermon's name? \n A. Marc\n B. Narc\n C. Mickey\n D. Nick")
questions+=1
if qs.lower()=="a" or pr.lower()=="marc":
    print("Perfect!")
    total_correct+=1
else:
    print("Get out of this class")
qs=int(input("5. What's 9+10?"))
questions+=1
if qs==19:
    print("Smart!")
    total_correct+=1
elif qs==21:
    print("Only for the meme...")
    total_correct+=1
else:
    print("How do you not know math")
qs=input("6. What is my name?")
questions+=1
if qs.lower()=="kenny" or qs.lower()== "kenny flory"or qs.lower()=="ken":
    print("Yay! You know who I am!")
    total_correct+=1
else:
    print("How did you get in here?")
qs=input("7. What is the name of this class?")
questions+=1
if qs.lower()=="csp":
    print("NiCe OnE!")
    total_correct+=1
else:
    print("DuMb DuMb Go BaCk To ClAsS")
total=total_correct/questions
print("That's the end! you got ", total_correct,"\n Out of ", questions, "Your total score is ", total//.01, "%")