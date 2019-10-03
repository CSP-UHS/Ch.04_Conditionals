'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Chapter 4 Quiz")
print()
input("Type anything to begin: ")
print()
total_correct=0
total_possible=0
print("Question 1")
total_possible+=1
answer_correct =int(input("What is 9+3? "))
if answer_correct ==12:
    print("Correct!")
    total_correct+=1
else:
    print("Incorrect, the correct answer is 12")
print()
print("Question 2")
total_possible+=1
name_correct =input("Who is the current President? ")
if name_correct.lower() == "donald trump" or name_correct.lower()=="trump":
    print("Correct...unfortunately")
    total_correct+=1
else:
    print("Incorrect, the current President is Donald Trump....unfortunately")
print()
print("Question 3")
total_possible+=1
print()
print("A. Mr. Hermon")
print("B. Mr. Davis")
print("C. Mrs. Jacques")
answer_correct =input("Who is the Best Teacher? ")
if answer_correct.lower()== "a" or answer_correct.lower()=="mr. hermon" or answer_correct.lower()=="mr hermon":
    print("Correct!")
    total_correct+=1
else:
    print("You're entilited to your opinion but it's wrong, the correct answer is A. Mr. Hermon.")
print()
print("Question 4")
total_possible+=1
print()
answer_correct= int(input("What is the square root of 100? "))
print()
if answer_correct== 10:
    print("Correct!")
    total_correct+=1
else:
    print("Incorrect, the answer is 10")
print()
print("Question 5")
total_possible+=1
print()
answer_correct=int(input("What is 9+10? "))
if answer_correct==19:
    print("Correct!")
    total_correct+=1
elif answer_correct==21:
    print("You memelord you, i'll allow it")
    total_correct+=1
else:
    print("Incorrect, the answer is 19")
print()
print("Question 6")
total_possible+=1
print()
name_correct=input("Who wrote this exam? ")
if name_correct.lower()=="dylan smith" or name_correct.lower()=="dylan":
    print("Correct!")
    total_correct+=1
else:
    print("Incorrect, it was written by Dylan Smith")
print()
print("Question 7")
total_possible+=1
answer_correct=int(input("What is 99+1? "))
if answer_correct==100:
    print("Correct!")
    total_correct+=1
else:
    print("C'mon man the answer was 100")
print()
input("Type anything to see your score ")
print("Your score was", total_correct, "out of", total_possible)
final_grade=(total_correct/total_possible)*100
print("or", final_grade//1,"%")