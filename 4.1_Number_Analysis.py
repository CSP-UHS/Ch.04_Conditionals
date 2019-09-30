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
x=int(input("Give me a number for analyzing"))
if x % 2 == 0:
    Test1 = "Even"
else:
    Test1= "Odd"

if x<0 :
    Test2 = "Negative"
elif x>0:
    Test2 = "Positive"
else:
    Test2 = "Neither, 0"

if x<-100 or x>100:
    Test3 = "Exclusive"
else:
    Test3 = "Inclusive"

print("Your number is",Test1)
print(Test2)
print(Test3)