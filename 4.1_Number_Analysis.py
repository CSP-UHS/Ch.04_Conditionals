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

number = int(input('Please enter a number: '))

if number%2 == 1: #if the number is odd
    print('\n'+str(number)+' is an odd number')
else:
    print('\n'+str(number)+' is an even number')

if number > 0:
    print(str(str(number)+' is positive'))
elif number == 0:
    print(str(number)+' is zero')
else:
    print(str(number)+' is negative')

if number >= -100 and number <= 100:
    print(str(number)+' is inclusive')
else:
    print(str(number)+' is not inclusive')