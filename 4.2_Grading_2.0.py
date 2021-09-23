'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("Let us help you calculate your grade my friend!")
sem = float(input("What is your semester grade? "))
fin = float(input("What is your final exam grade? "))
w = float(input("How much is the final exam worth? "))
wow = w/100
duh = 1-wow
overall = (sem*duh)+(fin*wow)
if overall <= 100 and overall >= 90:
    print("Your final semester grade is", overall, "%, a solid A grade buddy!")
elif overall >= 80:
    print("Your final semester grade is", overall, "%, a respectable B pal.")
elif overall >= 70:
    print("Your final semester grade is", overall, "%, I'm sorry it's a C man.")
elif overall >= 60:
    print("Your final semester grade is", overall, "%, you really need to do your work, you got a D man.")
else:
    print("Your final semester grade is", overall, "%, transfer to Johnston, get out of my sight.")