#!/usr/bin/env python3

import sys
import argparse
import requests
import json

"""
The sys module is imported so you can pass the arguments from the command line into your script while the argparse module is imported
so you can parse the defined arguments from sys.argv and automatically creates a help and usage message along with error messages.
"""
"""
The following two lines of code will set up argument parser in the script so you
can enter arguments before running the script and what is displayed in the help menu
"""
parser = argparse.ArgumentParser(description="This is my JSON Python script")
parser.add_argument('-i','--ip', dest = 'myIP', metavar = '[an IPv4 address]', type=str, help='<required> Enter an IPv4 Address')

args = parser.parse_args()
#This if statement will automatically bring up the help menu if no arguments are input before the script is run
if len(sys.argv) == 1:
    parser.print_help()
    exit(0)
#This defines the URL that will be used in the requests.get command below, which uses {args.myIP} to get the argument value
URL = f'http://ipinfo.io/{args.myIP}/json'

#This line retrieves the json data from the manually entered IP Address represented by {args.myIP} from the  WebAPI
json_raw = requests.get(URL)

#This will convert the raw json byte stream into a readable dictionary
myDict = json.loads(json_raw.text)

#This for loop will for each key in the dictionary print the first level key:value pairs
for key in myDict:
    print(f"{key} : {myDict[key]}")
