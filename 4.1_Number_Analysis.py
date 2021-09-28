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
num = int(input("Give me a whole number plz"))
numy = num%2
if numy == 1:
    print("Your number is odd")
elif num == 0:
    print("your number is Zero:/")
else:
    print("Your number is even")
if num == 0:
    print("Your number is neither negative nor positive")
elif num < 0:
    print("your number is negative")
else:
    print("Your number is positive")
if num <= 100 and num >= -100:
    print("Your number is inclusive")
else:
    print("Your number is exlusive")