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
print("Give me a number, any number at all!")
number=input("")

if int(number)%2 == 1:
    print("Yes, your number is odd.")
else:
    print("Yes, your number is very much even.")

if int(number) > 0:
    print("Wow! This number is quite positive.")
elif int(number) < 0:
    print("Interesting, this number is negative.")
else:
    print("This number is zero!")

if int(number) > -100 and int(number) < 100:
    print("Marvelous! This number is inclusively between negative and positive 100!")
else:
    print("Hm.... this number is not in between negative and positive 100.")