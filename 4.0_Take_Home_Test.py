"""
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________


  1. What is missing from this code?

     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians >= 10000:
         print("You have serious Jedi potential")
     else:
         print("Jedi, you will never be.")
"""
midichlorians = float(input("Enter midichlorian count: "))
if midichlorians >= 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")

# Missing the extra parenthesis after midichlorian count
     
'''
  2. This runs, but there is something wrong. What is it?
     
     user_input = input("R2D2 is a: ")
     print("A. Droid")
     print("B. Storm Trooper")
     if user_input.upper() == "A":
         print("Correct!")
     else:
         print("Incorrect.")
'''
# It prints part of the question after you answer

'''
     
  3. There are two things wrong with this code that tests if x is set to a
     positive value. One prevents it from running, and the other is subtle.
     Make sure the if statement works no matter what x is set to.
     Identify both issues. 
    
     x == 4
     if x >= 0:
         print("x is positive.")
     else:
         print("x is not positive.")
 '''
# Change to just > not >=
# If and else are indented to much
 
 '''
  4. What three things are wrong with the following code?
     
     x = input("Enter a number: ")
     if x = 3
         print("You entered 3")
 '''
 # Must have float or int in front of input
 # Need colon and indent after the if
 # Put x in parenthesis to make it work and not just print 3 every time
 0
 '''
  5. There are four things wrong with this code. Identify all four issues. 
     
     answer = input("What is the name of Poe Dameron's Droid? ")
     if a = "BB8":
         print("Correct!")
         else
         print("Incorrect! It is BB8.")
'''
# Change answer to a
# put the answer input to bb8 and put if a.lower
# else needs to not be indented and needs to have a colon after
# It needs to be == not just =

'''
  6. This program doesn't work correctly. What is wrong?
     
     x = input("Who are the top 3 greatest Jedi?")
     if x == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi":
         print("That is correct!")
'''

# It must be x == "Yoda" or x == Luke Skywalker or x == "Obi-Wan Kenobi"



'''
  7. Look at the code below. Write your best guess here on what it will print.
     Next, run the code and see if you are correct.
     Clearly label your guess and the actual answer.
     
     x = 5
     y = x == 6
     z = x == 5
     print("x=", x)
     print("y=", y)
     print("z=", z)
     if y:
         print("Star Wars Episodes 1,2,3 are the best!")
     if z:
         print("Star Wars Episodes 4,5,6 are the best!")
'''
#Guess - It will print episodes 4,5,6

#Answer - It printed episodes 4,5,6, were the best

'''
 8. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. 
     
     x = 5
     y = 10
     z = 10
     print(x < y)
     print(y < z)
     print(x == 5)
     print(not x == 5)
     print(x != 5)
     print(not x != 5)
     print(x == "5")
     print(5 == x + 0.00000000001)
     print(x == 5 and y == 10)
     print(x == 5 and y == 5)
     print(x == 5 or y == 5)
'''
# Print true false stuff

# Printed true false stuff

'''
 9. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. (HINT: when comparing strings, ASCII codes are used. https://www.ascii-code.com/)
     
     print("3" == "3")
     print(" 3" == "3")
     print(3 < 4)
     print("3" < "4")
     print("3" < 4)
     print("<" < ">")
     print((2 == 2) == "True")
     print((2 == 2) == True)
     print("?"<"!")
'''
# Print true false stuff

# Printed true, false, true, true

'''
 10. What things are wrong with this section of code?
     The programmer wants to set the force sensitivity variable 
     according to the character the user selects.
     
     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input = A:
         sensitivity = 1000
     else if user_input = B:
         sensitivity = 900
     else if user_input = C:
         sensitivity = 0
'''
print("Welcome to the Jedi Academy!")
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")
user_input = input("Choose a character?" )

if user_input.upper() == "A":
    sensitivity = 1000
elif user_input.upper() == "B":
    sensitivity = 900
else:
    sensitivity = 0
