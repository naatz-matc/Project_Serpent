#!/usr/bin/env python3

import c2f  #Imports the c2f.py file
import f2c  #Imports the f2c.py file

unit = input("Convert to Fahrenheit or Celsius?: ")
unit = unit.lower() #changes whatever input user entered into the approved arguments for the if-statements

if unit == "celsius" or unit == "c":
    print ("The Celsius equivelent temperature is", f2c.f2c())  #If this condition is ture, the f2c() function in the f2c.py file will run

elif unit == "fahrenheit" or unit == "f":
    print ("The Fahrenheit equivelent temperature is", c2f.c2f())   #If this condition is true, the c2f() function in the c2f.py file will run
