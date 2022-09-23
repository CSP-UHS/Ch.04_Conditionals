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

nmb=float(input("give me a number   :"))
print("--------------------")
if nmb%2==0:
    print("it is even")
else:
    print("it is odd")
print("--------------------")
if nmb<0:
    print("it is negative")
if nmb>0:
    print("it is positive")
print("--------------------")
if nmb > -100 and nmb < 100:
    print("your number is less than greater than -100 and less than 100")
else:
    print("PUT A DIFFERENT NUMBER NOW")
print("--------------------")