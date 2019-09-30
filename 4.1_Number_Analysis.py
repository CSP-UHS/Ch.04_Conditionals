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

n=int(input("Number Analysis; Please input a number:"))
if n%2 == 0:
    thing1="Your number is even"
else:
    thing1="Your number is odd"
if n < 0:
    thing2 = "Your number is a negative"
elif n>0:
    thing2 = "Your number is positive"
else:
    thing2 = "Neither, 0"
if n <- 100 or n > 100:
    thing3="Your number is exclusive"
else:
    thing3="Your number is inclusive"

print(thing1)
print(thing2)
print(thing3)
