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

number = int(input("Please enter a number to determine its properties"))

# Checks if number is even or odd
if number%2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Checks if number is positive, negative, or zero.
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print("your number is 0")

# Checks if number is inclusive or exclusive
if -100 <= number <= 100 :
    print(number, "is inclusive")
else:
    print(number, "is exclusive")




