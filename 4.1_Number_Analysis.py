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

UserInput=float(input("What is your lucky number?"))
OddEven = UserInput % 2
if OddEven != 0:
    print(" Your number is odd.")
else:
    print("Your number is even")

if UserInput>0:
    print("Your number is positive.")
elif UserInput<0:
    print("Your number is negetive.")
else:
    print("Your number is zero.")

if UserInput >= -100 and UserInput <= 100:
    print("Your number is inclusively between -100 and 100.")
else:
    print("Your number is not between -100 and 100.")


