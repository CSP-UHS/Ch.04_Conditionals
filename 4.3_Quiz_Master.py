'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

correct_ans = 0
num_questions = 8

print("what is the 88 + 88 ?: ")
ans_1 = float(input("Your answer:>->->->  "))

if ans_1 == 176:
    print("Correct")
    correct_ans += 1
else:
    print("Correct Answer = 176")

print()

print("what is the name of the 4th planet in our solar system?")
ans_2 = input("Your answer:>->->->:  ")

if ans_2.lower() == "mars":
    print("Correct")
    correct_ans += 1
else:
    print("Correct Answer = Mars")

print()

print("what is height of Mount Everest?(feet)")
ans_3 = input("Your answer:>->->->  ")

if ans_3 == 29029:
    print("Correct")
    correct_ans += 1
else:
    print("Correct Answer = 29029")

print()

print("If a giraffe has two eyes,a monkey has two eyes,and an elephant has two eyes, how many eyes do we have?: ")
print("A.2 \nB.4 \nC.6 \nD.8")
ans_4 = input("Your answer:>->->->  ")

if ans_4.islower() == "b" or 4:
    print("Correct")
    correct_ans += 1
else:
    print("Correct Answer = B ")

print()

print("What month of the year has 28 days?")
print("A.January \nB.February \nC.December \nD.All of the above")
ans_5 = input("Your answer:>->->-> ")

if ans_5.lower() == "d":
    print("Correct")
    correct_ans += 1
else:
    print("Correct Answer = D")

print()

print("5+6+5+6+7-7-6-5-5-5= ? ")
ans_6 = float(input("Your answer:>->->-> "))

if ans_6 == 1:
    print("Correct")
    correct_ans += 1
else:
    print("Correct Answer = 1")

print()

print("What is the temperature at the surface of the Sun(Kelvin)? (Do not put the label)")
ans_7 = int(input("Your answer:>->->-> "))

if ans_7 == 5778:
    print("Correct")
    correct_ans += 1
else:
    print("correct Answer = 5778")

print()

print("What is the powerhouse of the cell?")
print("A.midricondiria \nB.midrocrondria \nC.midochondria \nD.mitochondria")
ans_8 = input("Your answer:>->->-> ")

if ans_8.lower() == "d":
    print("Correct")
    correct_ans += 1
else:
    print("Correct Answer = D")

print()

sco = correct_ans / num_questions * 100
print(sco)
