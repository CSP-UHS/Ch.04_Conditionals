'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print("I will code this and I will make it laugh at you if you have an overall of 69. Hopefully.")      #please dont dock me points for this
semgrade=int(input("Give me your semester grade.  "))                                                   #so for the first example thing above
finalexam=int(input("Give me your final exam grade.  "))                                                #how do i get it to stop at 80.9
examworth=int(input("Cool. How much is the exam worth?  "))                                             #instead of having it go on for like 20 digits
examworth=examworth/100                                                                                 #or getting it to stop at 69 instead
overall=(semgrade*(1-examworth))+(finalexam*examworth)                                                  #of 69.0
if overall == 69:                                                                                       #also you should give ryan muetzel and daniel mitchell
    print("Your overall is:",overall,'hahahahahahhahahahahahahaha')                                     #extra points for helping me with the if else statement
else: (print("Your overall is:",overall,"Congrats, unless you're Ryan Muetzel"))                         #please