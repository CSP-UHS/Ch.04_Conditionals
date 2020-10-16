'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score=0
answer=input("How many fingers am I holding up?\n   A: 1\n   B: 7\n   C: 36\n   D: I can't see your hands, fool\n\n   Answer: ")
if answer.lower()=="d" or answer.lower()=="i can't see your hands, fool":
    print("Correct!\n")
    score+=1
else:
    print("Incorrect. You can't see my hands!\n")
answer=input("What is the square root of 64?\n\n   Answer: ")
if answer=="8" or answer.lower()=="eight":
    print("Correct!\n")
    score+=1
else:
    print("Incorrect, the answer was 8.\n")
answer=input("What is the fourth colour of the rainbow?\n\n   Answer: ")
if answer.lower()=="green":
    print("Correct!\n")
    score+=1
else:
    print("Incorrect.  The answer was green.\n")
answer=input("How many petals are on a lucky clover?\n\n   Answer: ")
if answer.lower()=="4" or answer.lower()=="four":
    print("Correct!\n")
    score+=1
else:
    print("Incorrect.  The answer was four.\n")
answer=input("""Which of the following does not belong?\n   A: Mace Windu\n   B: Obi-Wan Kenobi\n   C: Master Yoda
   D: Rey\n\n   Answer: """)
if answer.lower()=="d" or answer.lower()=="rey":
    print("Correct!\n")
    score+=1
else:
    print("Incorrect, Rey does not belong.\n")
answer=input("""And why does Rey not belong?\n   A: She is a terrible jedi\n   B: The force is weak in this one
   C: She sucks at sword fighting\n   D: All of the above\n\n   Answer: """)
if answer.lower()=="d" or answer.lower()=="all of the above":
    print("Correct!  That Mary Sue is a disgrace!\n")
    score+=1
else:
    print("You're close, but it was all of the above.  I'll give you half a point for participation.\n")
    score+=0.5
answer=input("How many questions have been asked so far, including this one?\n\n   Answer: ")
if answer.lower()=="7" or answer.lower()=="seven":
    print("That's right!\n")
    score+=1
else:
    print("Nope, so far it's been seven.  That's okay though, this is CSP, not math class!\n")
print("You scored ", score,"/7",sep="")