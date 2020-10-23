'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
import random

# sets neccessary variables needed to calculate the overall score
correct = 0
quest_num = 0

# Answer checking function
def answerchk(useransw, rightansw, attempts):
    global correct
    trys = attempts

    # takes the input of the user and compares it against the specified answer
    # Also supports functionality for multiple tries, if a parameter is specified
    if useransw.lower() == rightansw.lower():
        print("Correct.")
        correct += 1
        trys = 0
    elif attempts > 0:
        trys -= 1
        print("Incorrect,", trys, "trys remaining")
    else:
        print("Incorrect,", trys, "trys remaining")
        print("The correct answer was", rightansw)
    if trys == 0:
        print("Current Score:", correct, "out of", quest_num)
    # returns the amount of trys remaining. program gets stuck in a loop without this line
    return trys

# Function for the first kind of quiz question, multiple choice. Only supports 4 choices. no more, no less.
def multi(quest, answ, c2, c3, c4, trys):
    while trys > 0:
        # allows the function to use these varibles defined outside its scope
        global quest_num
        global correct
        # creates a list of options based on function parameters
        options = [answ, c2, c3, c4]
        print(quest)
        letters = ["A", "B", "C", "D"]
        # prints out the four options in random sequence, but will not print a duplicate.
        for i in range(4):
            # converts a random value from the list into a single value in a string
            letter = "".join(random.sample(letters, 1))
            option = "".join(random.sample(options, 1))
            # allows the program to determine which letter is the correct answer, even though it is assigned randomly.
            if option == answ:
                rightansw = letter
            choice = letter + ") " + option
            print(choice)
            # removes any value that has already been used from the list so it will not be printed again
            letters.remove(letter)
            options.remove(option)
        useransw = input(":")
        quest_num += 1
        # Calls the answercheck function to verify the users answer.
        # Then it sets the value returned by the function to a variable in order to properly manage the remaining trys
        result = answerchk(useransw, rightansw, trys)
        trys = result
# Function created for open ended questions. Very simple since it requires no random apsects
# This can be used for open ended text input, math equations, or true/false. All values are converted to strings
def openend(quest, answ, trys):
    while trys > 0:
        global quest_num
        global correct
        rightansw = str(answ)
        useransw = str(input(quest))
        quest_num += 1
        result = answerchk(useransw, rightansw, trys)
        trys = result


# Question One: What color is an orange?
multi("What is the color of an orange", "medium orange", "light orange", "dark orange", "orange", 3)

# Question Two: What is 12 * 12?
openend("What is 12 * 12?", 144, 1)

# Question Three: What is the color of the sky?
openend("What is the color of the sky?", "sky blue", 2)

# Question Four: Is the python a venomous snake?
multi("Is the python a venomous snake?", "no", "yes", "maybe", "all of the above/below/inbetween", 1)

# Question Five: How many hours did it take me to write this program?
multi("How long did it take me to write this program?", "About 3 hours", "Over 6 hours", "Roughly A week", "Only 47 "
                                                                                                           "minutes", 1)

# Question Six: What is the square root of 89.0000000000 with the appropriate amount of significant figures?
openend("What is the square root of 89.0000000000 with the appropriate amount of sig figs?", "9.43398113205", 1)

# Question Seven: Do you know your abc's? If so please type them out in order:
openend("Do you know your abc's? If so please type them all out in order:", "abcdefghijklmnopqrstuvwxyz", 3)

# Question Eight: Which question number is this? PS: its not 8. Good luck :) PS: no cheating.
openend("Which question number is this? PS: its not 8. Good luck :) PS: no cheating.", "2^3", 4)

# Question Nine: True or False, french fries are made of banana peppers?
openend("True or False, french fries are made of banana peppers?", "False", 1)

# Question 10: Using what you know from the last question, where might the the eiffel tower located?
multi("Using what you know from the last question, where might the eiffel tower located?", "Ohio", "In the Royal palace",
      "On uranus (The planet. you dirty dog)", "The bermuda triangle", 1)

# Question 11: Get it? Ohio is the potato state, and french fries are made of potatoes, not banana peppers and the
# eiffel tower is in france. Anyways, which form of potatoes is inferior to the rest?
multi("Get it? Ohio is the potato state, and french fries are made of potatoes, not banana peppers and the eiffel "
      "\ntower is in france. Anyways, which form of potatoes is inferior to the rest?",
      "hashbrowns", "raw potatoes", "mashed", "smashed", 1)
if correct == 11:
    print("Great job!")
else:
    print("You suck, now go do it again. Try and do better this time, will you?")









