from sys import argv
import requests
import os
import enum
#import pprint #Need to figure out how to use this properly to beautify terminal output

class scanner(enum.Enum):
    unset = 0,
    XSS = 1,
    XXE = 2,
    all = 3

def parse_scanner(input):
    x = input.lower()
    if (x == "xss"):
        return scanner.XSS
    elif (x =="xxe"):
        return scanner.XXE
    elif (x =="all"):
        return scanner.all


    return scanner.unset

def write_header(header):
    print(('='*35) + header + ('='*35))    

def end_header():
    print('=' * 80)

def end_vuln():
    print('-' * 70)