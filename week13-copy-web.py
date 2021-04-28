#!/usr/bin/env python3

import requests         #This will import the request module

page = requests.get("https://notpurple.com")        #The requests.get function will go to the specified URL and get the HTML code and store it in the
                                                    #variable specified

with open("my_web_file.html","w") as hFile:         #This will create the specified file name. The write(page.text) function will put
    hFile.write(page.text)                          #The web page code into text and readable format


