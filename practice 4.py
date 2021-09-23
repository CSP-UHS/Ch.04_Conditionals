#and/0r
#a=2
#b=3
#c=1
#if a<b and a<c:
#    print("a is the smallest number")

#a=False
#if not a:
#    print("a is false")

#else and else if (elis)
#temp = float(input("How hot is it?"))
#if temp>=90:
#    print("Thats pretty hawt")
#elif temp>=50:
#    print("pretty normal")
#else:
#    print("Ooh, chillers")

#if jedi.lower()==yoda
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")
user_input = str(input("Choose a character?"))

if user_input.lower() == "a" or user_input.lower() == "jedi master":
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "sith lord":
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower() == "droid":
    sensitivity = 0
else:
    print("not a choice")
    sensitivity=("")

print("Sensitivity: ",sensitivity)