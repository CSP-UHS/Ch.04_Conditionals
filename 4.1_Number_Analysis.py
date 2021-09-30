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

n = float(input("pick a number? "))
# even or odd
if n % 2 == 0:
    e = "even"
else:
    e = "odd"
# positive negative or zero
if n > 0:
    p = "positive"
elif n < 0:
    p = "negative"
else:
    p = "equal to zero"
# Inclusive
if 100 >= n >= -100:
    i = "This number is between -100 and 100,"
else:
    i = "This number is not between -100 and 100,"

print(i, "is an", e, "number, and is", p,)
