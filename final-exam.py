#!/usr/bin/env python3

import sys
import argparse
import socket
import requests
import bs4
import json

parser = argparse.ArgumentParser(description="This is Sean Naatz's Final Exam Python Script")

parser.add_argument('-i','-ip', dest='varIP', metavar='{#.#.#.#}', help='Enter an IPv4 address')
parser.add_argument('-f', dest='varFun', metavar='{an integer}', type=int, help='<REQUIRED> Enter an integer between 1 and 5')

args = parser.parse_args()

URL = f"http://{args.varIP}/q{args.varFun}"

print ("Name: Sean Naatz")
print (URL)

def get_response():
    page = requests.get(URL)
    answer = page.text
    return answer

def parse_string():
    page = requests.get(URL)
    pageSoup = bs4.BeautifulSoup(page.text, features='lxml')
    message = pageSoup.get_text('H3')
    slice = message[27::3]
    return slice

def parse_header():
    page = requests.get(URL)
    response = page.headers
    answer = response.get('MATC-HEADER')
    return answer

def parse_json():
    json_raw = requests.get(URL)
    myDict = json.loads(json_raw.text)
    for item in myDict["Music And Books"]:
        subDictionary = item
        if subDictionary["title"] == '1984':
            return subDictionary["author"]

def socket_client():
    RHOST = f'{args.varIP}'
    SND_DATA = 'secret'
    for port in range(5000,6001):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.25)
                s.connect((RHOST,port))
                s.send(bytearray(SND_DATA,'utf8'))
                RCV_DATA = s.recv(1024)
                answer = RCV_DATA.decode('utf8')
                s.close()
                return answer
        except:
            pass

if args.varFun == 1:
    print (f"ANSWER:",get_response())

elif args.varFun == 2:
    print (f"ANSWER:",parse_string())

elif args.varFun == 3:
    print (f"ANSWER:",parse_header())

elif args.varFun == 4:
    print (f"ANSWER:",parse_json())

elif args.varFun == 5:
    print (f"ANSWER:",socket_client())

if len(sys.argv) == 1:
    parser.print_help()
    exit(0)
