'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''


number = int(input("Give me a number!"))
nb = number/2
if (nb % 1) == 0:
    print("Your number is even!")
else:
    print("Your number is Odd!")
if nb < 0:
    print("Your number is negative")
else:
    print("Your number is positive")
if number > -100 and number < 100:
    print("You number is Inclusive!")
else:
    print("Your number is Exclusive!")
