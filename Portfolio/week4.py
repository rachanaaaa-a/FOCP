#1Write a function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise. Write a short program to test the function.
def check(num1):
    if num1>=0 and num1<=100:
        return True
    else:
        return False
    
num1=int(input("enter a integer number between 0 and 100"))
if check(num1):
    print("the integer is in the range 0 to 100")
else:
    print("the integer is not  in the range 0 to 100")


#2Write a function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase letters in the string. Test the function with a short program.
def casecount(text):
    upper=0
    lower=0
    
    for char in text:
        if char.isupper():
            upper +=1
        elif char.islower():
            lower +=1
    return upper,lower
string=input("enter a string")
upper,lower =casecount(string)
print("Uppercase letters", upper)
print("Lowercase letters", lower)


#3Modify your "greetings" program so that the first letter of the name entered is always in uppercase with the rest in lowercase. This should happen even if the user entered their name differently. So if the user entered arthur, ARTHUR, or ev arTHur the name should be displayed as Arthur
name=input("what is your name?")
name=name.capitalize()
print(f"Hello, {name}.Good to meet you!")


#4When processing data it is often useful to remove the last character from so input (it is often a newline). Write and test a function that takes a string paramet and returns it with the last character removed. (If the string contains one or fewer characters, return it unchanged.)
def remove(string):
    if len(string)>1:
        return string[:-1]
    else :
        return string
    
a=input("enter a string")
print(remove(a))


#5Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion. Test both functions. (Google will find you the formulae).
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
num1=float(input("Enter temperature in Celsius "))
num2 = celsius_to_fahrenheit(num1)
print(f"{num1}C is equal to {num2}F")

num3 = float(input("Enter temperature in Fahrenheit "))
num4 = fahrenheit_to_celsius(num3)
print(f"{num3}F is equal to {num4}C")


#6Write a program that takes a centigrade temperature and displays the equivalent in fahrenheit. The input should be a number followed by a letter C. The output should be in the same format.

num=input("enter the temperature in Celsius followed by C ")
if num[-1:].upper()=="C":
    celsius=float(num[:-1])
    fahrenheit=(celsius * 9/5) + 32
    print(f"{fahrenheit}F")
else:
    print("Please enter the temperature followed by C.")


#7Write a program that reads 6 temperatures (in the same format as before), and displays the maximum, minimum,
# and mean of the values. Hint: You should know there are built-in functions for max and min. If you hunt, you might also find one for the mean.
temperatures=[]
for i in range(6):
    num=input("enter the temperature in Celsius ")
    if num[-1:].upper()=="C":
        celsius=float(num[:-1])
        fahrenheit=(celsius * 9/5) + 32
        temperatures.append(fahrenheit)
    else:
        print("Please enter the temperature followed by C.")
max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)
print(f"Maximum Temperature: {max_temp}F")
print(f"Minimum Temperature: {min_temp}F")
print(f"Mean Temperature: {mean_temp}F")


#8Modify the previous program so that it can process any number of values. The input
#terminates when the user just pressed "Enter" at the prompt rather than entering a value.
temperatures = []
while True:
    num = input("Enter the temperature in Celsius" )
    
    if num == "": 
        break
    
    if num[-1:].upper()=="C":
        celsius=float(num[:-1])
        fahrenheit=(celsius * 9/5) + 32
        temperatures.append(fahrenheit)
    else:
        print("Please enter the temperature followed by C.")
if temperatures:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    print(f"Maximum Temperature: {max_temp}F")
    print(f"Minimum Temperature: {min_temp}F")
    print(f"Mean Temperature: {mean_temp}F")
else:
    print("Please enter temperatures")