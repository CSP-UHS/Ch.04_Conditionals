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


def testNumber(n) :
    return [n % 2 == 0, n > 0, -100 < n < 100]


userNum = float(input("Type a number:\n"))
results = testNumber(userNum)

isEven = results[0] and "Even" or "Odd"
isPositive = results[1] and "Positive" or "Negative"
isInclusive = results[2] and "Inclusive" or "Exclusive"

print("----------------\nIn: {}\nOut: Test 1: {}\nTest 2: {}\nTest 3: {}\n----------------".format(userNum,isEven,isPositive,isInclusive))
