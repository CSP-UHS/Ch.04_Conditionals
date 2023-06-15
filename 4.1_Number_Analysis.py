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


user = float(input("Choose a number: "))

print ("Is it odd or even?")
if user%2 == 0:
    print("Even")
else:
    print("Odd")

print ("Is it positive, negative or zero?")
if user > 0:
    print("Positive")
elif user == 0:
    print("Zero")
else:
    print("Negative")

print("Is it inclusively between -100 and +100?")
if user > 100 or user < -100:
    print("Exclusive")
else:
    print("Inclusive")