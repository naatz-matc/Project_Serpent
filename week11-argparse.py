#!/usr/bin/env python3

import sys              #Imports the sys.argv module
import argparse         #Imports the argparse module

parser = argparse.ArgumentParser(description="This is Sean Naatz's script")         #This creates the Argument Parser object for the script

#==========Creating the general text argument with a flag================
parser.add_argument('-m', dest='myVar',metavar='BASIC', help='Enter some text')

#==========Creating the integer argument with a flag=====================
parser.add_argument('-i','--integer', dest='varInt', metavar='[an integer]', default=7, type=int, required=False,help='<required> Enter a simple Integer')

#==========Creating the floating number argument with a flag=============
parser.add_argument('-d','--float', dest='varFloat', metavar='[a float]', default=7.0, type=float, required=False, help='Enter a simple Float')

#==========Creating a string argument with a flag========================
parser.add_argument('-s','--string', dest='varString', metavar='[a string]', default='Denver_Broncos', required=False, help='Enter a simple String')

#==========Creating a list argument with a flag==========================
parser.add_argument('-l', dest='varList', metavar='string1] [string2]', nargs="*", default=['XXI','XXII','XXIV','XXXII','XXXIII'], \
help='Enter a list of strings (space delimited)')

#==========How boolean values work with argparse with a flag=============
parser.add_argument('-t','--set-true', dest='varBool_T', default=False, action='store_true', required=False, help='Toggle from default False to True')

parser.add_argument('-f','--set-false', dest='varBool_F', default=True, action='store_false', required=False, help='Toggle from default True to False')

#==========Showing the script version====================================
parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0', help="show program's version number and exit")


args = parser.parse_args()     #This creates a variable that lists all of the arguments in this script, wether they are default or manually entered

#This checks if any arguments were entered. If not, this 'if' statement will automatically print out the help page,
#just as if you would of entered -h on the command line
if len(sys.argv) == 1:
    parser.print_help()
    exit(0)

#print (type(parser.parse_args().myVar))
print ("The value of -m is: " + str(args.myVar))
#print (type(parser.parse_args().varInt))
print ("The value of -i is: " + str(args.varInt))
#print (type(parser.parse_args().varFloat))
print ("The value of -d is: " + str(args.varFloat))
#print (type(parser.parse_args().varString))
print ("The value of -s is: " + str(args.varString))
#print (type(parser.parse_args().varList))
print ("The value of -l is: " + str(args.varList))
#print (type(parser.parse_args().varBool_T))
print ("The value of -t is: " + str(args.varBool_T))
#print (type(parser.parse_args().varBool_F))
print ("The value of -f is: " + str(args.varBool_F))
