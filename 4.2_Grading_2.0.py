'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print("I will code this and I will make it laugh at you if you have an overall of 69. Hopefully.")

semgrade=int(input("Give me your semester grade.  "))

finalexam=int(input("Give me your final exam grade.  "))

examworth=int(input("Cool. How much is the exam worth?  "))

examworth=examworth/100

overall=(semgrade*(1-examworth))+(finalexam*examworth)

if overall >= 90:
    print("A")
    (print("Your overall is:", overall, "Congrats, unless you're Ryan Muetzel"))                    # i mean

elif overall >= 80:
    print("B")
    (print("Your overall is:", overall, "Congrats, unless you're Ryan Muetzel"))                    # it was

elif overall >= 70:
    print ("C")
    (print("Your overall is:", overall, "Congrats, unless you're Ryan Muetzel"))                    # simple enough

elif overall >= 60 and overall < 69:
    print("D")
    (print("Your overall is:", overall, "Congrats, unless you're Ryan Muetzel"))                    # but i couldnt

elif overall == 69:
    print("D")
    print("Your overall is:",overall,"hahahahahahhahahahahahahaha")                                 # ahahahahhahaha teenage brain go brrr
elif overall < 60:
    print("F")
    print("Your overall is:", overall,"Move to Johnston foolish mortal")                            # figure out how to have 1 your overall is ~~~
