# '''
# NUMBER ANALYSIS PROGRAM
# -----------------------
# Create a program that asks the user for a number and then analyzes it to determine if it is:
# 1.) odd or even - DONE
# 2.) positive, negative or zero
# 3.) inclusively between -100 and +100
#
# A small report will then be printed. Use the following to test your program:
#
# In: 32
# Out:  Test 1: Even
#       Test 2: Positive
#       Test 3: Inclusive
#
# In: -123
# Out:  Test 1: Odd
#       Test 2: Negative
#       Test 3: Exclusive
# '''
a = float(input("Enter in an odd or even number to be analyzed:"))
if a % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")
if a > 0:
    print("this number is positive")
elif a < 0:
    print("this number is negative")
elif a == 0:
    print("this number is zero")
if a < 100 and a > -100:
    print("this number is inclusive")
else:
    print("This number is exclusive")













    # note for later: to find odd or even, ask computer if the number is divisible by 2.