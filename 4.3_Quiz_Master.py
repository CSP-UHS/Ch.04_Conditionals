"""
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with
two of your student colleagues before you run it by your instructor.
"""
print()
print("Movie Trivia")
score = 0
total = 0
print()
print("** Choose the best option that the following quotes are from.")
print()
print("#1: Multiple Choice")
print("     A. Age of Ultron")
print("     B. Endgame")
print("     C. Infinity War")
num1 = (str(input("   - Which MCU movie is this 'Avengers...assemble' from?")))
if num1.upper() == "ENDGAME":
    print("  - Correct!! Nice Job!")
    score += 1
    total += 1
elif num1.upper() == "B":
    print("  - Correct!! Nice Job!")
    score += 1
    total += 1
else:
    print(" - Wrong choice. Nice try. It was Endgame")
    total += 1
print()
print("#2: Multiple Choice")
print("   - Choices:")
print("     A. C3PO")
print("     B. R2D2")
print("     C. Darth Vader")
num2 = (str(input(" - Which Star wars character (along with same actor) has been in all 9 star wars movies?")))
if num2.upper() == "C3PO":
    print("   - Correct!! Nice Job!")
    score += 1
    total += 1
elif num2.upper() == "A":
    print("  - Correct!! Nice Job!")
    score += 1
    total += 1
else:
    print("Wrong choice. Nice try. It was C3PO (played by Anthony Daniels)")
    print("   - R2D2 was in all 9 movies, BUT there were multiple actors who played him.")
    print("   - Darth Vader wasn't in the first 2 movies as it was Anakin Skywalker, his alter ego, in them.")
    total += 1
print()
print("** Type in the correct answer for the following questions.")
print()
num3 = (str(input("#3: What movie franchise is 'Shaken, not stirred' from?")))
if num3.upper() == "JAMES BOND":
    print("   - Correct!! Nice Job!")
    score += 1
    total += 1
else:
    print("   - Wrong Answer, though nice try. It was James Bond!")
    total += 1
print()
num4 = (str(input("#4: What movie is 'Here's Johnny!' from?")))
if num4.upper() == "THE SHINING":
    print("   - Correct!! Nice Job!")
    score += 1
    total += 1
elif num4.upper() == "SHINING":
    print("   - Correct!! Nice Job!")
    score += 1
    total += 1
else:
    print("   - Nice try, but the answer was The Shining!")
    total += 1
print()
print("** Type in the correct number of installments of each movie franchise")
print()
num5 = (str(input("#5: As of 2022, how many live action Lord of the Rings & Hobbit movies are there?")))
if num5.upper() == "6":
    print("   - Correct!! Nice Job!!")
    score += 1
    total += 1
elif num5.upper() == "SIX":
    print("   - Correct!! Nice Job!!")
    score += 1
    total += 1
else:
    print("   - Nice try, but there are currently 6 LOTR and Hobbit movies")
    total += 1
print()
num6 = (str(input("#6: As of 2022, how many Indiana Jones' movies are there?")))
if num6.upper() == "4":
    print("   - Correct!! Nice Job!!")
    score += 1
    total += 1
elif num6.upper() == "FOUR":
    print("   - Correct!! Nice Job!!")
    score += 1
    total += 1
else:
    print("   - Nice try, but there are currently 4 Indiana Jones movies.")
    total += 1
print()
num7 = (str(input("#7: As of 2022, how many Terminator movies are there?")))
if num7.upper() == "6":
    print("   - Correct!! Nice Job!!")
    score += 1
    total += 1
elif num7.upper() == "SIX":
    print("   - Correct!! Nice Job!!")
    score += 1
    total += 1
else:
    print("   - Nice try, but there are currently 6 Terminator movies.")
    total += 1
print()
print()
print("Your final score is", score)
score /= total
final = score * 100
if final >= 97:
    print("Your grade is an 'A*'. Great Job!!")
elif 90 <= final < 97:
    print("Your grade is an 'A'. Great Job!!")
elif 80 <= final < 90:
    print("Your grade is a 'B'. Good Job!!")
elif 70 <= final < 80:
    print("Your grade is a 'C'. Good Job! but do better next time.")
elif 60 <= final < 70:
    print("Your grade is a 'D'. You did good, but do better next time.")
else:
    print("Your grade is a 'F'. You Failed. Do it again and do better.")
print(final, "%")
