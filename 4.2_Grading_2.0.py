'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
print("\nThis module will calculate how a given final exam score will impact your semester grade.")
while True:
    sem_gr=int(input("\nCurrent semester grade: "))
    exam_gr=int(input("\n-\n\nExpected exam grade: "))
    exam_wt=int(input("\nFinal exam weight (percentage of grade): "))/100
    final_gr=float((exam_gr*exam_wt)+(sem_gr*(1-exam_wt)))
    print("\n-\n\nFinal grade: ","{:0.1f}".format(final_gr))
    print()
    if final_gr>=90:
        if final_gr>=93:
            print("A")
        else:
            print("A-")
    elif final_gr>=80:
        if final_gr>=88:
            print("B+")
        elif final_gr>=83:
            print("B")
        else:
            print("B-")
    elif final_gr>=70:
        if final_gr>=78:
            print("C+")
        elif final_gr>=73:
            print("C")
        else:
            print("C-")
    elif final_gr>=60:
        if final_gr>=68:
            print("D+")
        elif final_gr>=63:
            print("D")
        else:
            print("D-")
    else:
        print("Congratulations on your admission to Johnston, you absolute nincompoop.")
    print("\n-------------------------------------------")