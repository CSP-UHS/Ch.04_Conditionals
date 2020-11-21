'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
grade= int(input("Please enter your grade: "))
exam= int(input("Please enter your exam score: "))
worth= int(input("Please enter your exam worth: "))
examworth=worth/100
gradeworth=(100-worth)/100
ave=grade*(gradeworth)+exam*examworth
print()
print("Here is your final grade: ",ave,)
if ave>90:
    print("Here is your letter grade: A!")
elif ave>80:
    print("Here is your letter grade: B!")
elif ave>70:
    print("Here is your letter grade C")
elif ave>60:
    print("Here is your letter grade D")
else:
    print("Here is your letter grade F")
    print("Transfer to Johnston!")