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

num = int(input("Enter a whole number"))
print("--------------------------------")
#test 1 odd or even
if num%2==0:
    print(num, "is even!")
else:
    print(num, "is odd!")
print("--------------------------------")
#test 2 positive or negative
if num>0:
    print(num, "is a positive!")
elif num<0:
    print(num, "is a negative!")
else:
    print(num, "is 0. Now I don't know if 0 is positive or negative."
               "\nSo I decided to just make an extra program just to be sure.")
print("--------------------------------")
#test 3 between -100 and 100
if num<=100 and num>=-100:
    print(num, "is <=100 and >=-100")
else:
    print(num, "is not <=100 and >=-100")
print("--------------------------------")