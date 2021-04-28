#!/usr/bin/env python3

import requests             #Imports the requests module
import bs4                  #Imports the BeautifulSoup web page inspecting module

notpurple = requests.get("https://notpurple.com")       #This function will go to the specified URL and get the HTML
notpurple.raise_for_status()           #This function will return an HTTPError object if an error has occured during the process

purpleSoup = bs4.BeautifulSoup(notpurple.text, features="lxml")     #This function will parse whatever file is inserted AS LONG AS it is a string
                                                                    #If successful this will return a BeautifulSoup object ready for parsing. The
                                                                    #features="lxml" argument explicitly specifies BeautifulSoup to use the lxml parser

title = purpleSoup.select('title')              #Creates a variable that stores the value of the BeautifulSoup function select (title in this case)
links = purpleSoup.select('a')                  #Creates a variable that stores the value of the BeautifulSoup function select (links in this case)

print (f"Web Page Title: {title}")
print (f"Web Page Links: {links}")

