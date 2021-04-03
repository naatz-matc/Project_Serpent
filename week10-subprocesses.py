#!/usr/bin/env python3

import subprocess   #imports all of the subprocess modules

#=================Step 1 in Lab Assignment================================

#You must specify stdout in order to access the output of myProc later on
myProc = subprocess.run(['ps','-axco','command'], stdout=subprocess.PIPE)

#=================Step 2 in Lab Assignment================================

#This extracts the data from myProc and turns it into usable strings
myProcString = myProc.stdout.decode()

#This turns the the data from strings to a list
myProcList = myProcString.split('\n')

#==================Step 3 in Lab Assignment===============================

#print(len(myProcList))   #This was a test to see what the length was before slicing. It was 190

#This slices my list to eliminate the first element, which is NOT AN ACTUAL PROCESS.
procExtraCredit = myProcList[1:]

#print(len(procExtraCredit))     #This was to see if my slice worked. It did, the new length was 189

#This prints out every element of this list on seperate lines, just like the bash command 'ps -axco command'
for element in procExtraCredit:
    print(element)
