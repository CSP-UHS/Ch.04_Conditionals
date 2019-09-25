'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("\nHello and welcome to my Quiz!!!")
print("lets Begin!!\n")

print("1. What inspired that game Pac Man?\n")

print("Space Invaders")
print("Pizza")
print("Comic Book")

answer = input("\nWhich is true?? : ")
end_score = 0

if answer.upper() == "Pizza" or answer.lower() == "pizza":
    end_score+= 1
    print("Good job!")
else:
    print("Oops Better luck next time! The awnser was Pizza\n")

print("\n2. What is considered very rude and insulting in japanese restaurants\n")

print("Farting")
print("Tipping")
print("Coughing\n")

answer = input("Whats your answer? : ")

if answer.upper() == "Tipping" or answer.lower() == "tipping" :
    end_score+=1
    print("Good job!")
else:
    print("Oops Better luck next time! The answer was Tipping\n")

print("\n3. What do Fifteen percent of Women do during Valentines day?\n")

print("A. Eat chocolate")
print("B. hang out with their significant other")
print("C. Send themselves flowers\n")

answer = input("What is your answer? : ")

if answer.upper() == "C" or answer.lower() == "c" :
    end_score+=1
    print("Good job!")
else:
    print("Oops Better luck next time! The answer was C\n")

print("\n4. What is the square root of 25?\n")

print("2")
print("6")
print("5\n")

answer = input("What is your answer? : ")

if answer.upper() == "5":
    end_score+=1
    print("Good job!")
else:
    print("Oops Better luck next time! The answer was 5\n")

print("\n5. What cypher shifts the alphabet one three forward?\n")

print("Ceaser cypher")
print("ROT13 Cypher")
print("Affine Cypjer\n")

answer = input("What is the correct cypher? : ")

if answer.upper() == "Ceaser Cypher" or answer.lower() == "ceaser cypher" :
    end_score+=1
    print("Good job! Thats the correct answer")
else:
    print("Oops Better luck next time! The answer was Ceaser Cypher\n")

print("\n6. What was Cr.Strange's profession before he became Sorcerer Supreme? ")

print("A. Professor")
print("B. Dermatologist")
print("C. Nourosurgeon\n")

answer = input("Which job is right? : ")

if answer.upper() == "C" or answer.lower() == "c" :
    end_score+=1
    print("Good job! Thats the correct answer\n")
else:
    print("Oops Better luck next time! The answer was Nourosurgeon\n")

print("7. Pirates wore eye patches so they could see better in the dark ")

print("True")
print("False\n")

answer = input("Is this true or false? : ")

if answer.upper() == "True" or answer.lower() == "true" :
    end_score+=1
    print("\nGood job! Thats the correct answer\n")
else:
    print("Oops Better luck next time! The answer was True\n")

print("Have a fun time playing! Well this is your end score is /n")

print("End Score : ", end_score)
