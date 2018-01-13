#!/usr/bin/python
# -*- coding: UTF-8 -*-
import nose
import sys
sys.path.append("/home/learngit/python_test/source")
import prog
def setUp():
    print "function setup"

def tearDown():
    print "function teardown"
    
def Test_listdata():
    prog.readcsv()
    assertRegexpMatches(prog.listdata(),listdata)
    print "Testfunc1"
    assert True

def Testfunc2():
    print "Testfunc2"
    assert True
