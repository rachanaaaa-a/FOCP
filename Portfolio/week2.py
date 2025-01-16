#1 Last week you wrote a program that printed out a cheery greeting including your name. Take a copy of it, and modify it so that the user enters their name at the
#keyboard, and then receives a greeting
name=input("Hello, what is your name?")
print(f"Hello, {name}.Good to meet you!")

#2 Write a program that prompts a user to enter a temperature in Celsius, and then displays the corresponding temperature in Fahrenheit, like so: Enter a temperature in Celsius: 32.5
#32.5C is equivalent to 90.5F.
celsius=float(input("enter a temperature in celsius"))
fahrenheit=(9/5*celsius)+32
print(f"{celsius}C is equvalent to {fahrenheit}F")

#3The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is usually 24 students, but this is
#sometimes varied to create groups of similar size. Write a program that prompts for
#the number of students and group size, and then displays how many groups will be needed and how many will be left over in a smaller grou
numberofstudents=int(input("How many students?"))
size=int(input("Required group size?"))
nofgroups=numberofstudents//size
leftovers=numberofstudents%size
group_singular="group" if nofgroups==1 else"groups"
student_singular="student" if leftovers==1 else "students"
print(f"There will be {nofgroups} {group_singular} with {leftovers} {student_singular} left over.")

#4 A kindly teacher wishes to distribute a tub of sweets between her pupils. She will first count the sweets and then divide them according to how many pupils attend
#that day. Write a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left ove
sweets=int(input("How many sweets are there?"))
pupils=int(input("How many pupils are there?"))
sweets_each=sweets//pupils
leftovers=sweets%pupils
print(f"each will get {sweets_each} sweets and {leftovers} sweets left over.")
                 
                           