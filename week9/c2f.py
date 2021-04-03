#!/usr/bin/env python3

def celsius_to_fahrenheit():
    degrees_celsius = int(input("Please enter a temperature in Celcius: "))  #This takes input from the user and turns it into an integer
    degrees_fahrenheit = int((degrees_celsius*9/5) + 32)  #This changes the user input and turns it into a temperature in Fahrenheit as an integer
    return degrees_fahrenheit

def c2f():
    degrees_celsius = int(input("Please enter Celsius temperature: "))
    degrees_fahrenheit = int((degrees_celsius*9/5) + 32)
    return degrees_fahrenheit

"""
Below is using the if __name__ == '__main__' statement. This statement is used to determine
whether a file is being run directly in itself or if it is being run as an imported function
or file. In the example below, if the function is being run directly, Python assigns a variable
automatically, hence __name__ will equal __main__. The if condition means that if the __name__
variable is __main__, it means that this function is being run directly and to run the desired
function. This is helpful when a file with multiple functions is imported and some of those
functions are not required to run. By creating if statements with the __name == '__main__'
attached to certain functions, this ensures that those functions will not be run when the file
is imported.
"""

if __name__ == '__main__':
    print ("The temperature in Fahrenheit is", celsius_to_fahrenheit())


