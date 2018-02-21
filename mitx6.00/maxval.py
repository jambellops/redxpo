#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:31:12 2018

@author: jamesbellagio
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    ret_max = 0
    max_inscope = []
    if type(t) == int:
        ret_max = t
        return ret_max
    elif (type(t) == tuple) or (type(t) == list):
        for i in t:
            if (type(i) == tuple) or (type(i) == list):
                max_inscope.append(max_val(i))
            elif type(i) == int:
                max_inscope.append(i)
        return max(max_inscope)
            
                                    
            