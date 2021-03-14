#!/usr/bin/env python3

print ("Name: Sean Naatz")

hFile = open("slicing-file.txt","r")
MidtermSlice = hFile.readlines()

#====Step 3a======
string_a = MidtermSlice[-3]
string_a = string_a.replace('\n','')

#====Step 3b======
string_b = " ".join(MidtermSlice[2:5])
string_b = string_b.replace('\n','')

#====Step 3c======
string_c = " ".join(MidtermSlice[-10:-15:-2])
string_c = string_c.replace('\n','')

#====Step 3d======
string_d = " ".join(MidtermSlice[10:13])
string_d = string_d.replace('\n','')

#====Step 3e======
string_e = " ".join(MidtermSlice[8:5:-1])
string_e = string_e.replace('\n','')

#====Creating the quote=======
quote = (f"'{string_a} {string_b} {string_c} {string_d} {string_e}'")
print(f"{quote}")

hFile.close()
