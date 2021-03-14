#!/usr/bin/env python3

print ("Name: Sean Naatz")
with  open("Midterm-if.txt","r") as hFile:
    Total = 0
    ListFile = hFile.readlines()
    var_1 = 'gmeach18@ed.gov'
    var_2 = '248.253.63.149'
    var_3 = 'Whiteland'
    var_4 = '80.222.19.190'
    var_5 = 'Kayley'
    var_6 = 'dcassyqw@microsoft.com'
    for element in ListFile:
        if var_1 in element:
            int_1 = element[0:2]
            int_1 = int(int_1)
            Total = Total + int_1
        elif var_2 in element:
            int_2 = element[0:3]
            int_2 = int(int_2)
            Total = Total + int_2
        elif var_3 in element:
            int_3 = element[0:2]
            int_3 = int(int_3)
            Total = Total + int_3
        elif var_4 in element:
            int_4 = element[0:3]
            int_4 = int(int_4)
            Total = Total + int_4
        elif var_5 in element:
            int_5 = element[0:3]
            int_5 = int(int_5)
            Total = Total + int_5
        elif var_6 in element:
            int_6 = element[0:3]
            int_6 = int(int_6)
            Total = Total + int_6

print (f"The total is: {Total}")






