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
n = int(input("put in a number for analysis"))
a = n%2
if a == 0:
    type(float)
    print("This Number is Even")
else:
    print("this number is odd")
if n<0:
    print("this number is negative")
elif n==0:
    print("this number is zero")
else:
    print("this number is positive")
if n >100 or n<-100:
    print("this number is exclusive")
else:
    print("this number inclusive")
    

