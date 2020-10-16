'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

Quiz_Score=0

Question_1_answer = input("What tank did americans use in WW2?")
if Question_1_answer == "Sherman":
    Quiz_Score += 1
    print("Correct")
else:
    print("Incorrect")

print("A. KV")
print("B. T-34")
print("C. BT-7")
print("D. IS")
Question_2_answer = input("What tank did soviets use in WW2?")
if Question_2_answer == "B":
    Quiz_Score += 1
    print("Correct")
else:
    print("Incorrect")

Weight_Tiger_Two_answer = float(input("How many Tons did the King Tiger weigh?"))
if Weight_Tiger_Two_answer == 68:
    Quiz_Score += 1
    print("right")
else:
    print("Nope")

print("What Tank Destroyer was made using porsche tiger chassis? It also used long 88mm gun.")
print("A. Elephant")
print("B. Nashorn")
print("C. Ferdinand")
print("D. Sturmgeschutz")

Question_4_answer = input("Type answer here: ")
if Question_4_answer == "A" or "C":
    Quiz_Score+=1
    print("Correct")
else:
    print("Wrong one")

Question_5_answer = input("Was B-24 Liberator the most produced bomber of WW2?: True/False")

if Question_5_answer == "True":
    Quiz_Score += 1
    print("Right")
else:
    print("Incorrect")

Question_6_answer = input("What american bomber had the highest max altitude?")
if Question_6_answer == "B29":
    Quiz_Score += 1
    print("That's right")
else:
    print("Incorrect")

Question_7_answer = input("What year did WW2 end?")
if Question_7_answer == "1945":
    Quiz_Score +=1
    print("Correct")
else:
    print("Wrong")


print(Quiz_Score,"/7")