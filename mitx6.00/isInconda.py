#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:02:39 2018

@author: jamesbellagio
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    mid = int((len(aStr)-1)/2)
    if aStr == char:
        return True
    elif aStr == '':
        return False
    elif len(aStr) == 1:
        return False
    elif aStr[mid] == char:
        return True    
    else:
        if char < aStr[mid]:
            return isIn(char, aStr[0:mid])
        else:
            return isIn(char, aStr[mid:0])
        
isIn('m', 'ceefikmmopqrrsttvyzz')