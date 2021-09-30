'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
#input and grade
s = float(input("What was your semester grade? "))
f = float(input("What did you score on your final? "))
p = float(input("What percentage of your grade is your final? "))
o = round((1-(p/100))*s+((p/100)*f), 1)
# Determining letter grade
if o >= 93:
    g = "A"
elif 90 <= o < 93:
    g = "A-"
elif 87 <= o < 90:
    g = "B+"
elif 83 <= o < 87:
    g = "B"
elif 80 <= o < 83:
    g = "B-"
elif 77 <= o < 80:
    g = "C+"
elif 73 <= o < 77:
    g = "C"
elif 70 <= o < 73:
    g = "C-"
elif 67 <= o < 70:
    g = "D+"
elif 65 <= o < 67:
    g = "D"
else:
    g = 1
# Final output
if not g == 1:
    print("Your final grade is", o, "%, that is a", g)
else:
    print("Transfer to Johnston")
