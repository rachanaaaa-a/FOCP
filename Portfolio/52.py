#2Write a program that, when run from the command line, reports how many arguments were provided. (Remember that the program name itself is not an argument)
import sys
argument_count = len(sys.argv) - 1
print(f"Number of arguments provided: {argument_count}")
