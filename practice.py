import random
number = random.randrange(1,101)

done = False
count = 0
record = 10000000000000000
print("This is a guess numbers game")

while not done:

    count += 1

    #ask the user for a number
    guess = (input("Type in a number or Q to quit: "))
    if guess=="q":
        done = True

    elif int(guess)>number:
        print("Too high!")

    elif int(guess)<number:
        print("Too low!")

    else:
        print("Congratulations, you guessed the number!")
        print("It took you",count,"times")
        if count<record:
            record=count
        print("Your current record is",record,"times")
        number = random.randrange(1,101)
        count = 0
        done = True