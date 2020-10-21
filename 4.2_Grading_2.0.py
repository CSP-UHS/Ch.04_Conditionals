'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
a = int(input("enter semester grade: "))
b = int(input("enter final grade: "))
d = int(input("final worth: "))/100

grading_p = a * (1-d) + b*d
#print (grading_p)

if 100 >= grading_p >= 93:
    print("A")
elif 92 >= grading_p >= 90:
    print("A-")
elif 89 >= grading_p >= 83:
    print("B")
elif 82 >= grading_p >= 80:
    print("B-")
elif 79 >= grading_p >= 73:
    print("C")
elif 72 >= grading_p >= 70:
    print("C-")
elif 69 >= grading_p >= 63:
    print("D")
elif 62 >= grading_p >= 60:
    print("D-")
else:
    print("F")
    print("Transfer to Johnston!")
