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
print("Welcome to Smith's Number Analysis Program")
N=int(input("Enter any Number"))
if N%2==0:
    print("Test 1: Even")
else:
    print("Test 1: Odd")
if N>0:
    print("Test 2: Positive")
elif N==0:
    print("Test 2: Zero")
else:
    print("Test 2: Negative")
if N<-100 or N>100:
    print("Test 3: Exclusive")
else:
    print("Test 3: Inclusive")