#!/usr/bin/env python3

#Here are the 3 variables to be used in this script:

varString = "Here is a nice string to slice"
varTuple = ("Here","is","a","nice","tuple","to","slice")
varList = ["Here","is","a","nice","list","to","slice"]

"""
Here is the following output for all of Step 2 in this order:
'e is a nice string to slice'
'Her'
'e is a ni'
'Hr sanc tigt lc'
'ecils ot gnirts a si ereH'
"""

print(varString[3:30:1])

print(varString[0:3:1])

print(varString[3:12:1])

print(varString[::2])

print(varString[::-1])

"""
Here is the following output for all of Step 3 in this order:
['slice','to','list','nice','a','is','Here']
['a','is','Here']
['a','nice']
['Here','nice','slice']
['is','a','nice','list','to','slice']
"""

print(varList[::-1])

print(varList[2::-1])

print(varList[2:4:1])

print(varList[::3])

print(varList[1:7:1])

# Here is the printing out of each element of varString one line at a time:

for element in varString:
    print(element)

# Here is the printing out of each elment of varList one line at a time:

for element in varList:
    print(element)





