"""
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________
"""

  #1. What is missing from this code?

     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians >= 10000:
         print("You have serious Jedi potential")
     else:
         print("Jedi, you will never be.")

midichlorians = float(input("Enter midichlorian count: "))
if midichlorians >= 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")

# Missing the extra parenthesis after midichlorian count
     

 
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
