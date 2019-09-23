'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero - done
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
number = float(input("Enter a number to be analyzed! "))
if number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")
if number > 0:
    print("This number is positive.")
else:
    print("This number is negative.")
if number < 100 and number > -100:
    print("This number is inclusive.")
else:
    print("This number is exclusive.")