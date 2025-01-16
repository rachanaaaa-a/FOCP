#3Write a program that takes a bunch of command-line arguments, and then prints out the shortest. If there is more than one of the shortest length, any will do
import sys
arguments = sys.argv[1:]
shortest_argument = sorted(arguments, key=len)
print(f"The shortest argument is: {shortest_argument}")

   
