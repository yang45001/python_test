#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import csv

import sys

FILE='test.csv'
savedata=[]
datalen=0
headers=['account','pwd']

#function_switch={'i':insertdata(),'l':listdata(),'g':getdata(),'d':deldata()}
def insertdata():
    global datalen
    name=raw_input("input you name:\n")
    passwd=raw_input("input passwd:\n")
    job={}
    job['account']=name
    job['pwd']=passwd
    datalen=len(savedata)
    for i in range(datalen+1):
        if i>=datalen:
            savedata.append(job)
            writecsv()
            break
        row=savedata[i]
        if row['account']==name:
            print '*****userattricek******'
            print 'frist del usr'
            break
    #if savedata.count(job)==0:
    #    savedata.append(job)
    #    writecsv()
    #    print '*****insertdata*****'
    #else:
    #    print'*****insertfail*****'


def listdata():
    for row in savedata:
        print row[headers[0]],row[headers[1]]
    print '*****listdata*****'

def getdata():
    name=raw_input("input username\n")
    global datalen
    for i in range(datalen+1):
        if i>=datalen:
            print '*****no find user****'
            break
        row=savedata[i]
        if row['account']==name:
            print row['pwd']
            print '*****getdata success*****'
            break

def deldata():
    global datalen
    datalen=len(savedata)
    name=raw_input("input name\n")
#    print datalen
    for i in range(datalen+1):
        if i>=datalen:
            print '*****delfail*****'
            break
        row=savedata[i]
        if row['account']==name:
            savedata.remove(row)
            writecsv()
            print'*****deldata*****'
            break


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

def writecsv():
    with open(FILE,'w') as f:
        writer=csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(savedata)
    pass

def readcsv():
    global datalen
    with open(FILE,'r') as f:
        temp=csv.DictReader(f)
        for row in temp:
            savedata.append(row)
    datalen=len(savedata)
    pass

if __name__ == '__main__':
    readcsv()
    init()
