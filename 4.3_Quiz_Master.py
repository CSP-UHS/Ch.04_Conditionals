'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

number_correct = 0

print()
print("Question 1")
print()

print("A. 5")
print("B. 92")
print("C. 16")
print("D. 8")

user_input = input("What is 12+12-12/6*4 :")

if user_input.upper() == "C":
    print("Correct")
    number_correct += 1
elif user_input == "16":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is C")

print()
print("Question 2")
print()

answer = input("What is the square root of 1,000,000 :")

if answer == "1000":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is 1000")

print()
print("Question 3")
print()

answer = input("What is the radius of the Moon in miles (don't need label) :")

if answer == "1079.4":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is 1079.4")

print()

answer = str(input("Who is the biggest procrastinator in the world :"))

if answer.lower() == "jake perman":
    print("Correct")
    number_correct += 1
elif answer.lower() == "jake":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct is Jake")

print()
print("Question 4")
print()

print("A. 0.166 g")
print("B. 2.528 g")
print("C. 0.063 g")
print("D. 28.02 g")

user_input = input("What is the gravity on the Moon :")

if user_input.upper() == "A":
    print("Correct")
    number_correct += 1
elif user_input == "0.166 g":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is A")

print()
print("Question 5")
print()

print("A. 761 mph")
print("B. 777 mph")
print("C. 755 mph")
print("D. 792 mph")

user_input = input("What is the speed of sound :")

if user_input.upper() == "A":
    print("Correct")
    number_correct += 1
elif user_input == "761 mph":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is A")

print()
print("Question 6")
print()

print("A. Lockheed SR-71 Blackbird")
print("B. Lockheed A-12")
print("C. Thrust SSC")
print("D. North American X-15")

user_input = input("What is the fastest plane in the world :")

if user_input.upper() == "D":
    print("Correct")
    number_correct += 1
elif user_input == "North American X-15":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is D")

print()
print("Question 7")
print()

answer = str(input("Who is the richest man in the world :"))

if answer.lower() == "jeff bezos":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is Jeff Bezos")

print()
print("Question 8")
print()

print("A. Martin Van Buren")
print("B. Chester Arthur")
print("C. Millard Fillmore")
print("D. John Tyler")

user_input = input("Who was the 21st President of the United States :")

if user_input.upper() == "B":
    print("Correct")
    number_correct += 1
elif user_input == "Chester Arthur":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is B")

print()
print("Question 9")
print()

print("A. Martin Van Buren")
print("B. Chester Arthur")
print("C. Millard Fillmore")
print("D. John Tyler")

user_input = input("Who was the 8th president of the United States")

if user_input.upper() == "A":
    print("Correct")
    number_correct += 1
elif user_input == "Martin Van Buren":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is A")

print()
print("Question 10")
print()

print("A. 663,600 square miles")
print("B. 1.3 million square miles")
print("C. 3.7 million square miles")
print("D. 5.4 million square miles")

user_input = input("How much land is under Antarctica's's ice")

if user_input.upper() == "D":
    print("Correct")
    number_correct += 1
elif user_input == "5.4 million square miles":
    print("Correct")
    number_correct += 1
else:
    print("Wrong, the correct answer is D")

print()
print("You got", number_correct, "/ 10 correct")
