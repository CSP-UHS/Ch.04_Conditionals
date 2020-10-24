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
times = 0
points = 0
# Answer checking function
def answerchk(useransw, rightansw, attempts):
    global correct
    global times
    global quest_num
    global points
    trys = attempts
    # takes the input of the user and compares it against the specified answer
    # Also supports functionality for multiple tries, if a parameter is specified
    if useransw.lower() == rightansw.lower():
        print("\033[32mCorrect.\n")
        correct += 1
        if times == 0:
            points += 1
            times = 0
        elif times == 1:
            points += .75
            times = 0
        else:
            points += .5
            times = 0
        trys = 0
    elif attempts > 0:
        trys -= 1
        times += 1
        if trys == 0:
            print("\033[91mIncorrect,\033[37m", trys, "\033[91mtrys remaining\n")
            times += 1
        elif trys > 0:
            print("\033[91mIncorrect,\033[37m", trys, "\033[91mtrys remaining\n")
    if trys == 0:
        quest_num += 1
        if useransw.lower() != rightansw.lower():
            print("\033[37mThe correct answer was\033[32m", rightansw, "\n")
            times = 0
            print("\033[95mCurrent Score:\033[37m", correct, "\033[95mout of\033[37m", quest_num, "\033[95mquestions correct")
            print("\033[95mCurrent Points:\033[37m", points, "\033[95mpoints out of\033[37m", quest_num, "\033[95mpoints possible\n")
        else:
            print("\033[95mCurrent Score:\033[37m", correct, "\033[95mout of\033[37m", quest_num, "\033[95mquestions correct")
            print("\033[95mCurrent Points:\033[37m", points, "\033[95mpoints out of\033[37m", quest_num, "\033[95mpoints possible\n")
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
        letters = ["A", "B", "C", "D"]
        # Prints the question
        print("\033[33m" + str(quest_num+1) + ")", quest)
        # prints out the four options in random sequence, but will not print a duplicate.
        for x in range(0, len(letters)):
            # converts a random value from the list into a single value in a string
            option = " ".join(random.sample(options, 1))
            print("\033[94m" + letters[x] + ") " + option)
            # option = "".join(random.sample(options, 1))
            # allows the program to determine which letter is the correct answer, even though it is assigned randomly.
            if option == answ:
                rightansw = letters[x]
            options.remove(option)
        useransw = input(":")
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
        useransw = str(input("\033[33m" + str(quest_num+1) + ") " + quest))
        result = answerchk(useransw, rightansw, trys)
        trys = result


# All of the test questions. Created using the above functions
# Question One: What color is an orange?
multi("What is the color of an orange?", "medium orange", "light orange", "dark orange", "orange", 2)

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
openend("Do you know your abc's? If so please type them all out in order:", "abcdefghijklmnopqrstuvwxyz", 2)

# Question Eight: Which question number is this? PS: its not 8
openend("Which question number is this? PS: its not 8.", "2^3", 3)

# Question Nine: True or False, french fries are made of banana peppers?
openend("True or False, french fries are made of banana peppers?", "False", 1)

# Question 10: Using what you know from the last question, where might the the eiffel tower located?
multi("Using what you know from the last question, where might the eiffel tower located?", "Ohio", "In the Royal palace",
      "On uranus (The planet. you dirty dog)", "The bermuda triangle", 1)

# Question 11: Get it? Ohio is the potato state, and french fries are made of potatoes, not banana peppers, and the
# eiffel tower is in france. Anyways, which form of potatoes is inferior to the rest?
multi("Get it? Ohio is the potato state, and french fries are made of potatoes, not banana peppers and the eiffel "
      "\ntower is in france. Anyways, which form of potatoes is inferior to the rest?",
      "twice baked", "raw", "mashed", "smashed", 1)
if points == 11 and correct == 11:
    print("Well would you look at that, you got 100%. You want a cookie or something?")
elif correct == 11:
    print("You got all the questions correct, but it took you multiple trys so you only got", str(round(points/11*100, 2)) + "%")
    print("Please try again")
else:
    print("Wow, only", str(round(correct/11*100, 2)) + "%?", "I gave you multiple trys \nand you STILL couldnt get them"
          "all? try it again. And do better this time will you?")









