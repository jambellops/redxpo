#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:55:11 2018

@author: jamesbellagio
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    oddTup = ()
    
    for t in range(len(aTup)):
        if (t%2 == 0):
            oddTup += (aTup[t],)
    
    return oddTup