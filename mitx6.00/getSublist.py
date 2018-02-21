#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 08:28:41 2018

@author: jamesbellagio
"""

def getSublists(L, n):
    ''' L: non-empty list
        n: non-zero integer < len(L)
        return: a list of all possible n-length slices of L as sublists
        '''
    retList =[]
    for i in range(len(L)):
        if i+n <= len(L):
            retList.append(L[i:(i+n)])
    return retList
        