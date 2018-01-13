#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("/home/learngit/python_test/source")
import prog
import dostest

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
if __name__=='__main__':
    doctest.testmod(verbose=True)
