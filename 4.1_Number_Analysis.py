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
user_input = int(input("enter a number: "))

if user_input % 2 == 0:
    print("even")
else:
    print("odd")

if user_input < 0:
    print("negative")
elif user_input > 0:
    print("positive")
else:
    print("zero")

if 100 >= user_input >= -100:
    print("inclusive")
else:
    print("exclusive")
