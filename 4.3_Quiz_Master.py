'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Bienvenido a la prueba. Buena suerte.")
score = 0
q1=input("Cual es la respuesta a la vida \n a. Bob \n b. 42 \n c. Nha \n")
if q1.lower() == "a" or q1.lower() == "bob":
    print("Correctumundo!!!!!!")
    score+=1
else:
    print("Tienes un cerebro pequeño! \n")
q2=input("En qué año se lanzó Minecraft \n a. 2010 \n b. 2009 \n c. 1999 \n")
if q2.lower() == "b" or q2 == "2009":
    print("Correctumundo!!")
    score+=1
else:
    print("Tienes un cerebro pequeño! \n")
q3=input("Cuál es mi nombre? \n a. Bob \n b. Nellie \n c. Nha \n")
if q3.lower() == "c" or q3.lower() == "nha":
    print("Correctumundo!!!")
    score+=1
else:
    print("Tienes un cerebro pequeño! \n")
q4=input("Que es 2+2? \n")
if q4 == "4" or q4.lower() == "four":
    print("Muy bien!")
    score+=1
else:
    print("Tienes un cerebro pequeño!")
q5=str(input("¿nombrar a un hermano Hemsworth \n"))
if q5.lower() == "chris hemsworth" or "chris" or "liam" or "liam hemsworth" or "luke" or "luke hemsworth":
    print("Goodo Job")
    score+=1
else:
    print("Tienes un cerebro pequeño!")
q6=input("Answer the next lyrics in English: Quiero ser el mejor \n")
if q6.lower() == "like no one ever was" or q6.lower() == "like no one ever was!":
    print("Pokemon!!")
    score+=1
else:
    print("Bruh...")
q7=input("Translate in English: puedes sentir el amor esta noche \n")
if q6.lower() == "can you feel the love tonight" or "can you feel the love tonight?":
    print("Lion King wow")
    score+=1
else:
    print("Mufasa nooo!!!")

print("Your got score the is!:", score)
