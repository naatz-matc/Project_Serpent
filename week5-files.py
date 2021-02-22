#!/usr/bin/env python3

hFile = open("/etc/passwd","r")
strfiletext = hFile.read()
print ("Question 1:")
print ()
print (f"Length = {len(strfiletext)}")
print ()
print ("The len(strfiletext) function prints out the number of\n " \
      "characters that are in that string, which we set up as\n " \
      "the contents of the /etc/passwd file in the variable 'strfiletext'")
print ()
print ("This method would be best used in a plain text document,\n  " \
       "where the only thing that matters is the entire output being displayed.")
print ()
hFile = open("/etc/passwd","r")
listfiletxt = hFile.readlines()
print ("Question 2:")
print ()
print (f"Length = {len(listfiletxt)}")
print ()
print ("The len(listfiletxt) function reads all of the elements that\n " \
      " are apart of the list, which we set up as the contents of the\n " \
      " /etc/passwd file in the variable 'listfiletxt'")
print ()
print ("This method would be best if you had say a bunch of new users\n " \
      "and usernames that you had to input into a directory of some sort.\n " \
      "That way you could seperate them and either add or remove each element \n " \
      "into a new list. This also works well for organizing log or event files \n " \
      "into an easy to read format.")
print ()
print ("Question 3:")
print ()
hFile = open("/etc/passwd","r")
count = 0
for line in hFile:
    count +=len(line)
print (f"Length = {count}")
print ()
print ("The best situation to use this method would be if you had a\n " \
       "sequence of items that you would need to step through, such \n " \
       "as a list of statistics.")
hFile.close()

