#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse

import sys

#function_switch={'i':insertdata(),'l':listdata(),'g':getdata(),'d':deldata()}
def insertdata():
    print '*****insertdata*****'

def listdata():
    print '*****listdata*****'

def getdata():
    print '*****listdata*****'

def deldata():
    print '*****deldata*****'


#yyfunction_switch={'i':insertdata(),'l':listdata(),'g':getdata(),'d':deldata()}
def init(): 
    parser = argparse.ArgumentParser(description='test parsing arguments')
    parser.add_argument('-p', type=str,choices=['i','l','g','d'],default='l', help='i insert;l list;g find;d del')
    arg = parser.parse_args()
    if arg.p=='i':
        insertdata()
    elif arg.p=='l':
        listdata()
    elif arg.p=='g':
        getdata()
    elif arg.p=='d':
        deldata()
    else:
        print 'input error'
    # print parser.print_help()
#function_switch={'i':insertdata(),'l':listdata(),'g':getdata(),'d':deldata(
if __name__ == '__main__':
    init()
