#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:06:51 2018

@author: jamesbellagio
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    dKeys = aDict.keys()
    dValues = aDict.values()
    keys = list(dKeys)
    values = list(dValues)
    retList=[]
    uniqueness = []
    for i in aDict:
        if aDict[i] not in uniqueness:
            uniqueness.append(aDict[i])
            retList.append(aDict[i])
        elif aDict[i] in uniqueness:
            if aDict[i] in retList:
                retList.remove(aDict[i])
    
    keyList = []
    for j in range(len(values)):
        if values[j] in retList:
            keyList.append(keys[j])
    
    keyList.sort()
    
    return keyList