#!/usr/bin/env python3

#Converting Fahrenheit to Celsius
def fahrenheit_to_celsius():
    degrees_fahrenheit = int(input("Please enter a temperature in Fahrenheit: "))  #This asks for user input and converts to an integer
    degrees_celsius = int((degrees_fahrenheit-32)*5/9)  #This creates a varialbe that takes the input and turns it into an integer in Celsius
    return degrees_celsius

def f2c():
    degrees_fahrenheit = int(input("Please enter Fahrenheit temperature: "))
    degrees_celsius = int((degrees_fahrenheit-32)*5/9)
    return degrees_celsius

"""
Below is using the if __name__ == '__main__' statement. This statement is used to determine
whether a file is being run directly in itself or if it is being run as an imported function
or file. In the example below, if the function is being run directly, Python assigns a variable
automatically, hence __name__ will equal __main__. The if condition means that if the __name__
variable is __main__, it means that this function is being run directly and to run the desired
function. This is helpful when a file with multiple functions is imported and some of those
functions are not required to run. By creating if statements with the __name__ == '__main__'
attached to certain functions, this ensures that those functions will not be run when the file
is imported.
"""

if __name__ == '__main__':
    print ("The temperature in Celsius is", fahrenheit_to_celsius())

