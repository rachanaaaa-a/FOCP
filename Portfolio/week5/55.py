#5Last week you wrote a program that processed a collection of temperature readings entered by the user and displayed the maximum, minimum, and mean. Create a
#version of that program that takes the values from the command-line instead. Be sure to handle the case where no arguments are provided!
import sys


def calculation(fahrenheit):
    max_temp = max(fahrenheit)
    min_temp = min(fahrenheit)
    mean_temp = sum(fahrenheit) / len(fahrenheit)
    return max_temp, min_temp, mean_temp

if len(sys.argv) < 3:
    print("Please provide at least two temperature values as command-line arguments.")
else:
    
    temperatures_celsius = []
    for temp in sys.argv[1:]:
        temperatures_celsius.append(float(temp))

    temperatures_fahrenheit = []
    for temp in temperatures_celsius:
        fahrenheit_conversion = (temp * 9/5) + 32
        temperatures_fahrenheit.append(fahrenheit_conversion)

   
    maximum_temperature, minimum_temperature, mean_temperature = calculation(temperatures_fahrenheit)
    print(f"Celsius Temperatures is  {temperatures_celsius}")
    print(f"Fahrenheit Temperatures is {temperatures_fahrenheit}")
    print(f"Maximum Temperature is {maximum_temperature}")
    print(f"Minimum Temperature is {minimum_temperature}")
    print(f"Mean Temperature is {mean_temperature}")

