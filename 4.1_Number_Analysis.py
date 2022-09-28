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

number = float(input("Enter a number: "))

if number%2 == 1:
    print("Test 1: Odd")
else:
    print("Test 1: Even")

if number < 0:
    print("Test 2: Negative")
elif number > 0:
    print("Test 2: Positive")
else:
    print("Test 2: Zero")

if number > -100 and number < 100:
    print("Test 3: Inclusive")
else:
    print("Test 3: Exclusive")
