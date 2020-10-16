'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
corr = 0
wrng = 0

ans = int(input("\n\033[1;34mHow many wins does NA have at worlds 2020?"))
if ans == 2:
    print("\033[92mThank FlyQuest and G2 for ruining the meme. Take a point")
    corr = corr + 1
else:
    print("\033[31mIncorrect")
    print("\033[0mThe correct answer was 1")
    wrng = wrng + 1

ans = input("\n\033[1;34mWho is going to win worlds?")
if ans.upper() == "TOP" or ans.upper() == "TOP ESPORTS" or ans.upper() == "JDG" or ans.upper() == "JD GAMING":
    print("\033[32mPossibly, Here's a point.")
    corr = corr + 1
elif ans.upper() == "SNG" or ans.upper() == "SUNING" or ans.upper() == "LGD" or ans.upper() == "LGD GAMING":
    print("\033[32mPossibly, Here's a point.")
    corr = corr + 1
elif ans.upper() == "DRX" or ans.upper() == "DWG" or ans.upper() == "DAMWON GAMING" or ans.upper() == "GG":
    print("\033[32mPossibly, Here's a point.")
    corr = corr + 1
elif ans.upper() == "GENG" or ans.upper() == "MACHI" or ans.upper() == "G2" or ans.upper() == "G2 ESPORTS":
    print("\\033[32mPossibly, Here's a point.")
    corr = corr + 1
elif ans.upper() == "PSG" or ans.upper() == "PSG TALON" or ans.upper() == "UOL" or ans.upper() == "UNICORNS OF LOVE":
    print("\033[32mPossibly, Here's a point.")
    corr = corr + 1
elif ans.upper() == "FNC" or ans.upper() == "FNATIC" or ans.upper() == "RGE" or ans.upper() == "ROGUE":
    print("\033[32mPossibly, Here's a point.")
    corr = corr + 1
elif ans.upper() == "TSM" or ans.upper() == "TL" or ans.upper() == "TEAM LIQUID" or ans.upper() == "FLQ":
    print("\033[31mReally? NA? hahahha negative 1 points.")
    print("\033[0mThe correct answer was literally anyone else but an NA team.")
    corr = corr - 1
    wrng = wrng + 1
elif ans.upper() == "TSM" or ans.upper() == "TL" or ans.upper() == "TEAM LIQUID" or ans.upper() == "FLQ":
    print("\033[31mReally? NA? hahahha negative 1 points.")
    print("\033[0mThe correct answer was literally anyone else but an NA team.")
    corr = corr - 1
    wrng = wrng + 1
else:
    print("\033[31mThat either isn't a team competing, or you typed it in wrong, no consequences")

ans = input("\n\033[1;34mAre Mr. Hermons' and Joes' puns bad?")
if ans.upper() == "YES":
    print("\033[32mCorrect!")
    corr = corr + 1
else:
    print("\033[31mIncorrect")
    print("\033[0mThe correct answer was yes.")
    wrng = wrng + 1

ans = input("\n\033[1;34mIs coding hard?")
if ans.upper() == "NO":
    print("\033[32mCorrect!")
    corr = corr + 1
else:
    print("\033[31mIncorrect")
    print("\033[0mThe correct answer was no.")
    wrng = wrng + 1

print("\n\033[0mA. These questions are fantastic")
print("\033[0mB. These questions are hard to think of")
print("\033[0mC. This quiz is cool")
print("\033[0mD. Mr. Hermon is a bad teacher")
ans = input("\n\033[1;34mWhich of these statements are true?")
if ans.upper() == "B":
    print("\033[32mCorrect!")
    corr = corr + 1
else:
    print("\033[31mIncorrect")
    print("\033[0mThe correct answer was B.")
    wrng = wrng + 1

ans = input("\n\033[1;34mFill in the blank, 'Jake is a(n) _____")
if ans.upper() == "IDIOT":
    print("\033[32mCorrect!")
    corr = corr + 1
else:
    print("\033[31mIncorrect")
    print("\033[0mThe correct answer was 'idiot'.")
    wrng = wrng + 1

ans = input("\n\033[1;34mWho is my favorite LOL player?")
if ans.upper() == "CAPS" or ans.upper() == "PERKZ":
    print("\033[32mCorrect!")
    corr = corr + 1
else:
    print("\033[31mIncorrect")
    print("\033[0mThe correct answers were either Caps or Perkz")
    wrng = wrng + 1

ttlscr = int(corr / (corr+wrng)*100)
print("\n\033[0mYour final score is:")
print(corr,"/",(corr+wrng))
print(ttlscr, "%\n")

if ttlscr > 90:
    print("\033[0mStop taking your own test Alex")
elif ttlscr >= 80:
    print("\033[0mPretty good, thats a B!")
elif ttlscr == 69:
    print("\033[0mNICE")
else:
    print("\033[0mI cant be asked to make a statment regarding your score, try again I guess...")
