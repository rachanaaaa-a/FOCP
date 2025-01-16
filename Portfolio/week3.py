#1Modify your greeting program so that if the user does not enter a name (i.e. theyjust press enter), the program responds "Hello, Stranger!". Otherwise it should printa greeting with their name as before.'''

name=input("Hello, what is your name?")
if name=="":
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}. Good to meet you!")


#2Write a program that simulates the way in which a user might choose a password.The program should prompt for a new password, and then prompt again. If the twopasswords entered are the same the program should say "Password Set" orsimilar, otherwise it should report an error.
password1=input("create a new password")
password2=input("re-enter the password")
if password1==password2:
    print("Password Set")
else:
    print("Error: please re-enter the password")


#3Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.

password1=input("enter a new password")
if len(password1)>=8 or len(password1)<=12:
    print("error: password must be between 8 and 12 characters long.")
else:
    password2=input("re-enter the password")
    if password1==password2:
        print("Password Set")
    else:
        print("Error: please re-enter the password")


#4Modify your program again so that the chosen password cannot be one of a list ofcommon passwords, defined thus:BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password1=input("enter a new password")
if len(password1)>=8 or len(password1)<=12:
    print("error: password must be between 8 and 12 characters long.")
elif password1 in BAD_PASSWORDS:
    print("Error: This password is very common. Please enter a different password")
else:
    password2=input("re-enter the password")
    if password1==password2:
        print("Password Set")
    else:
        print("Error: please re-enter the password")



#5Modify your program a final time so that it executes until the user successfullychooses a password. That is, if the password chosen fails any of the checks, theprogram should return to asking for the password the first time.
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] 
while True:
        password1=input("enter a new password")
        if len(password1)>=8 or len(password1)<=12:
            print("error: password must be between 8 and 12 characters long.")
        elif password1 in BAD_PASSWORDS:
            print("Error: This password is very common. Please enter a different password")
        else:
            password2=input("re-enter the password")
            if password1==password2:
                print("Password Set")
                break
            else:
                print("Error: please re-enter the password")



#6Write a program that displays the "Seven Times Table". That is, the result ofmultiplying 7 by every number from 0 to 12 inclusive. The output might start:0 x 7 = 0 1 x 7 = 7 2 x 7 = 14and so on.

for i in range(13 ):
    print(f"{i}*7={i*7}")


#7Modify your "Times Table" program so that the user enters the number of the table they require. This number should be between 0 and 12 inclusive.
num=int(input("enter a number between 0 and 12 for the table"))
if num>=0 and num<=12:
    for i in range(13) :
        print(f"{i}*{num}={i*num}")
    else:
        print("please enter the number between 0 and 12")



#8Modify the "Times Table" again so that the user still enters the number of the table,but if this number is negative the table is printed backwards. So entering "-7"would produce the Seven Times Table starting at "12 times" down to "0 times".
num=int(input("enter a number for the table"))

if num>=0:
    for i in range(13) :
        print(f"{i}*{num}={i*num}")
else:
    for i in range(12,-1,-1) :
        print(f"{i}*{num}={i*num}")
 


