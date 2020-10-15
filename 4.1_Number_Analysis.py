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

t1 = int(input("Enter your number:"))

if (t1 % 2) == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

if t1 > 0:
    print("Your number is positive.")
if t1 == 0:
    print("Your number is 0.")
if t1 < 0:
    print("Your number is negative.")

if t1 >= -100 and t1 <= 100:
    print("Your number is inclusive.")
else:
    print("Your number is exclusive.")