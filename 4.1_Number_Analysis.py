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
o = float(input("Give me a number and I will determine if it is odd or even."))
if o % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")

p = float(input("Give me a number and I will determine if it is positive, negative, or zero."))
if p == 0:
    print("It is zero.")
elif p>0:
    print("It is positive.")
else:
    print("It is negative.")

h = float(input("Give me a number and I will determine whether it is between -100 and 100, or if it isn't."))
if h > -100 and h < 100:
    print("It is inclusive.")
else:
    print("It is exclusive.")