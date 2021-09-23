#a = 4
#b = 5
#if a>b:
    #print("A is greater than B")
#if b>a:
    #print("B is greater than A")
#print ("Completed")
#if a>=b:
    #print("A is equal to or greater than B")
#if a!=b:
    #print ("A doesn't equal B")
#double equals for if statementnts in comparison
#single equals for assignment operator

# and if, greater to equal to less than
#a=False
#b=3
#c=1

#if a<b and a<c:
    #print("a is smaller than b and c")

#if a<b or a<c:
    #print("A isn't the biggest number")
#if a==True:
    #print ("A is true")
#if not a==True:
    #print ("A is false")

#else if
#temp = float (input("Hey, how hot is it today?"))

#if temp>=90:
    #print ("Woah that's hot!")
#elif temp >=50:
    #print ("It's a nice day out!")
#else:
    #print ("Man it's freezing!")

#jedi = (input ("Who is the greatest Jedi?  "))

#if jedi.lower()=="yoda":
    #print ("That is correct!")
#else:
    #print ("Wrong Jedi that is!")

print("Welcome to the Jedi Academy!")
print()
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")
print()
user_input = str(input("Choose a character?"))

if user_input.lower() == "a" or user_input.lower()=="jedi master":
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower()=="sith lord":
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower()=="droid":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity=("")

print("Sensitivity:",sensitivity,)


