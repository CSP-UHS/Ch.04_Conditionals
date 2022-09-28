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

number = float(input("What is your favorite number?"))
test1 = number%2
print("hmmm interesting this will help with our reasearch")
if test1 == 0:
    print("Test 1: Even")
else:
    print("Test 1: Odd")
if number > 0:
    print("Test 2: Positive")
else:
    print("Test 2: Negative")
if 100 > number > -100:
    print("Test 3: Inclusive")
else:
    print("Test 3: Exclusive")
print("ha now I have the exact coordinates of your house I will now send a scary Jack in the box to your door")
print("It will arrive in 3-5 business days be afraid :)")