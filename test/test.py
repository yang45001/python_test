#!/usr/bin/python
# -*- coding: UTF-8 -*-
import nose
def setUp():
    print "function setup"

def tearDown():
    print "function teardown"
    
def Testfunc1():
    print "Testfunc1"
    assert True

def Testfunc2():
    print "Testfunc2"
    assert True
