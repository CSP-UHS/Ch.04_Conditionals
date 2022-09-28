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
num = int(input("Type in a number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
if num==0:
    print("The number is neither positive nor negative")
elif num>0:
    print("The number is positive")
else:
    print("The number is negative")
if num>=-100 and num<=100:
    print("The number is between -100 and 100")
else:
    print("The number is not between -100 and 100")

