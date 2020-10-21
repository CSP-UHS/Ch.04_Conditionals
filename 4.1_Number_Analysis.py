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
Num= int(input("Give me a number: "))
if Num >100 and Num % 2 == 0:
    print("Test 1: Even")
    print("Test 2: Positive")
    print("Test 3: Exclusive")
elif Num >100 and Num % 2 == 1:
    print("Test 1: Odd")
    print("Test 2: Positive")
    print("Test 3: Exclusive")
elif Num >0 and Num % 2 == 0:
    print("Test 1: Even")
    print("Test 2: Positive")
    print("Test 3: Inclusive")
elif Num >0 and Num % 2 ==1:
    print("Test 1: Odd")
    print("Test 2: Positive")
    print("Test 3: Inclusive")
elif Num ==0:
    print("Test 1: Zero")
    print("Test 2: Zero")
    print("Test 3: Inclusive")
elif Num <-100 and Num % 2 == 0:
    print("Test 1: Even")
    print("Test 2: Negative")
    print("Test 3: Exclusive")
elif Num <-100 and Num % 2 == 1:
    print("Test 1: Odd")
    print("Test 2: Negative")
    print("Test 3: Exclusive")
elif Num <0 and Num % 2 == 0:
    print("Test 1: Even")
    print("Test 2: Negative")
    print("Test 3: Inclusive")
elif Num <0 and Num % 2 == 1:
    print("Test 1: Odd")
    print("Test 2: Negative")
    print("Test 3: Inclusive")

