'''
QUIZ MASTER PROJECT
-------------------
two of your student colleagues before you run it by your instructor.
Print the correct answer if the user gets it wrong.
At the end of the program print the percentage of questions the user gets right and their letter grade.
Keep the following in mind when creating the program:
Calculate the percentage by using a formula at the end of the game. Don't just add a certain percentage for each question the user gets correct. If you add a certain percentage each time, then you have to change the program in all of those places if some day you want to add another question. With a formula, you only need 1 change.
To print a blank line so that all the questions don't run into each other, use the following code:
print( )
Remember the program can print multiple items on one line. This can be useful when printing the user's score and grade at the end.
print("The value in x is", x)
Separate out your code by using blank lines to group sections together. For example, put a blank line between the code for each question.
Sometimes it makes sense to re-use variables. Rather than having a different variable to hold the user's answer for each question, you could reuse the same one.
Use descriptive variable names. x is a terrible variable name. Instead use something like number_correct.
You must have at least two other people take your quiz to give you feedback before officially demonstrating it to your instructor for completion
'''
print("THE GREAT NASCAR TEST!!")
total = 0
quest1 = int(input("Question 1: What was the number I did in my python drawing?? : "))
if quest1 == 24:
    print("Correct, great job, well done, beautiful!!")
    total = total + 1
else:
    print("Get a better memory")
print("Questions correct: " + str(total))
quest2 = input("Who won the 2020 Cup Series Championship?? : ")
if quest2 == "Chase Elliot" or quest2 == "Chase elliot" or quest2 == "chase elliot" or quest2 == "chase Elliot":
    print("Correct, great job, well done, beautiful!!")
    total = total + 1
else:
    print("Come on now, you could have just googled it!")
print("Questions correct: " + str(total))
quest3 = input("Question 3: Who drives the 24 car?; A = Chad Knaus; B = William Byron; C = Ronald Reagan; ")
if quest3 == "a" or quest3 == "A":
    print("Nah he is a crew cheif")
elif quest3 == "B" or quest3 == "b":
    print("Correct, great job, well done, beautiful!!")
    total = total + 1
elif quest3 == "C" or quest3 == "c":
    print("Silly Billy, that's a president")
else:
    print("Bro is it that hard to pick one of the three options?")
print("Questions correct: " + str(total))
quest4 = float(input("What is your favorite number??: "))
if quest4 >= 0:
    print("There is no wrong answer. But you seem pretty POSITIVE with your response! Get it?")
    total = total + 1
else:
    print("You seem like a NEGATIVE type of person! Get it? Get it? hahahaha.")
    total = total + 1
print("Questions correct: " + str(total))
quest5 = int(input("How many 7 time champions are there in NASCAR?? : "))
if quest5 == 3:
    print("Correct, great job, well done, beautiful!!")
    total = total + 1
else:
    print("Nope there are 3.")
print("Questions correct: " + str(total))
quest6 = input("Which driver has the most cup wins?? : ")
if quest6 == "Richard Petty" or quest6 == "richard petty" or quest6 == "Richard petty" or quest6 == "richard Petty":
    print("Correct, great job, well done, beautiful!!")
    total = total + 1
else:
    print("Nope, it is Richard Petty.")
print("Questions correct: " + str(total))
quest7 = input("In your own words, what are three examples of symbolism in Romeo and Juliet, with in text reasoning?")
if quest7 == "Light and DarknessThe disparity between lightness and darkness is one of the play’s most significant symbols. Innocent, gentile characters like Romeo, Juliet, Mercutio and Benvolio, who display qualities of goodness are often seen during the daylight, while characters who exhibit evil or violence, such as Lord Capulet and Paris, are usually seen only at night. Take Romeo’s famous soliloquy, in which he describes Juliet as the giver of light: “But, soft! what light through yonder window breaks? / It is the east, and Juliet is the sun.” Contrast that with the speech Prince Escalus gives at the very end of the play, after the death of Romeo and Juliet: “A glooming peace this morning with it brings / The sun, for sorrow, will not show his head.” Poison Taken in its literal sense, the poison that Romeo acquires from the apothecary is what brings the play to its tragic end. However, the poison symbolizes much more than a toxic potion; rather, it symbolizes the extent of Romeo’s love for his beloved Juliet. Upon hearing that she has died, Romeo decides that he cannot live without her, and secures the poison to kill himself at Juliet’s tomb: “Here's to my love! O true apothecary! Thy drugs are quick. Thus with a kiss I die.” The poison also helps the plot build to its final moment of suspense, in which Juliet awakens and finds Romeo to be dead. Deciding that she cannot live without him, either, she attempts to take the poison from his lips: “O churl! drunk all, and left no friendly drop / To help me after? I will kiss thy lips / Haply some poison yet doth hang on them / To make die with a restorative.” Silver and Gold Shakespeare uses gold and also silver to explore the pettiness of the feuding between the Capulets and the Montagues. In Act V, when he visits the apothecary, Romeo pays him in gold, stating, ”There is thy gold / worse poison to men’s souls.” This quip highlights Romeo’s understanding that above all, money is and has been the impetus for the feuding between the two aristocratic families. As further proof that neither family has learned from the tragedy, both state they will erect golden statues in their deceased children's honor. By contrast, silver represents love and beauty, such as when Romeo states, “How silver-sweet sound lovers' tongues by night when a musician claims that “Music has a silver sound.":
    print("Great job knowing your old english!!")
    total = total + 1
else:
    print("The correct answer is: Light and DarknessThe disparity between lightness and darkness is one of the play’s most significant symbols. Innocent, gentile characters like Romeo, Juliet, Mercutio and Benvolio, who display qualities of goodness are often seen during the daylight, while characters who exhibit evil or violence, such as Lord Capulet and Paris, are usually seen only at night. Take Romeo’s famous soliloquy, in which he describes Juliet as the giver of light: “But, soft! what light through yonder window breaks? / It is the east, and Juliet is the sun.” Contrast that with the speech Prince Escalus gives at the very end of the play, after the death of Romeo and Juliet: “A glooming peace this morning with it brings / The sun, for sorrow, will not show his head.” Poison Taken in its literal sense, the poison that Romeo acquires from the apothecary is what brings the play to its tragic end. However, the poison symbolizes much more than a toxic potion; rather, it symbolizes the extent of Romeo’s love for his beloved Juliet. Upon hearing that she has died, Romeo decides that he cannot live without her, and secures the poison to kill himself at Juliet’s tomb: “Here's to my love! O true apothecary! Thy drugs are quick. Thus with a kiss I die.” The poison also helps the plot build to its final moment of suspense, in which Juliet awakens and finds Romeo to be dead. Deciding that she cannot live without him, either, she attempts to take the poison from his lips: “O churl! drunk all, and left no friendly drop / To help me after? I will kiss thy lips / Haply some poison yet doth hang on them / To make die with a restorative.” Silver and Gold Shakespeare uses gold and also silver to explore the pettiness of the feuding between the Capulets and the Montagues. In Act V, when he visits the apothecary, Romeo pays him in gold, stating, ”There is thy gold / worse poison to men’s souls.” This quip highlights Romeo’s understanding that above all, money is and has been the impetus for the feuding between the two aristocratic families. As further proof that neither family has learned from the tragedy, both state they will erect golden statues in their deceased children's honor. By contrast, silver represents love and beauty, such as when Romeo states, “How silver-sweet sound lovers' tongues by night when a musician claims that “Music has a silver sound.")
print("Questions correct: " + str(total))
num_questions = 7
num_grade = (total/num_questions) * 100
print(num_grade)
if num_grade <= 100 and num_grade >= 90:
    print("A")
elif num_grade < 90 and num_grade >= 80:
    print("B")
elif num_grade < 80 and num_grade >= 70:
    print("C")
elif num_grade < 70 and num_grade >= 60:
    print("D")
else:
    print("F")