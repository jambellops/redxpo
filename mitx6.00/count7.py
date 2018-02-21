#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 08:04:56 2018

@author: jamesbellagio
"""

def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N%10 == 7:
        return count7(N//10) + 1
    elif N//10 == 0:
        return 0
    else:
        return count7(N//10)

