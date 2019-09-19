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
print("Welcome to my NUMBER ANALYSIS PROGRAM!\n")
print("Give me a number and ill determine if it is Odd, Even, Positive, Negative, Zero and inclusively between -100 and +100 ")

n = int(input("Whats your Number?\n"))

if n%2 == 1:
    print("Your number is Even")
else :
    print("Your number is Odd")

if n == 0:
    print("Your number is Sero")
else :
    print("Your number is not Zero")

if n-abs(n) == 0:
    print("your number is negative")
else :
    print("Your number is positive")

if n < -100 or n > 100:
    print("Your number is Exclusive")
else:
    print("Your number is Inclusive")