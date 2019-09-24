'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("\nHello and welcome to my Quiz!!!")
print("lets Begin!!\n")

print("1. What inspired that game Pac Man?\n")

print("Space Invaders")
print("Pizza")
print("Comic Book")

answer = input("Which is true?? : ")
end_score = 0

if answer.upper() == "Space Invaders" or answer.lower() == "space invaders" :
    end_score+=1
else:
    print("Oops Better luck next time!\n")

# print("2. What is considered very rude and insulting in japanese restaurants\n")
#
# print("Farting")
# print("Tipping")
# print("Coughing")
#
# if answer.upper() == "Tipping" or answer.lower() == "tipping" :
#     end_score+=1
# else:
#     print("Oops Better luck next time!\n")
#
# print("3. What do Fifteen percent of Women do during Valentines day\n?")
#
# print("A. Eat chocolate")
# print("B. hang out with their significant other")
# print("C. Send themselves flowers")
#
# if answer.upper() == "C" or answer.lower() == "c" :
#     end_score+=1
# else:
#     print("Oops Better luck next time!\n")

print("Have a fun time playing! Well this is your end score", end_score)