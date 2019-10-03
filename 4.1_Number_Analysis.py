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

print("Welcome to my number analysis")
enter=int(input("Enter a number: "))
if enter>-100 and enter<100:
    print("Your number is inclusive")
else:
    print("Your number is exclusive")
if (enter%2)==0:
    print("Your number is even")
else:
    print("Your number is odd")
if enter<=-1:
    print("Your number is negative")
elif enter>=1:
    print("Your number is positive")
else:
    print("Your number is zero")