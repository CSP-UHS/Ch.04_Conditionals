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
'''

num = int(input("Please enter a number to test whether it's odd or even:"))
if (num % 2) == 0:
    print("Okay, even.")
else:
    print("Okay, odd.")

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is equal to zero.")

if -100 < num > 100:
    print("Inclusive")
else:
    print("Exclusive")



'''




In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''
