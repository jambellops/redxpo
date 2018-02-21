#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:03:11 2018

@author: jamesbellagio
"""


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    
    def fun_appliedto(x):
        applied_sum = 0
        for i in range(len(L)):
            applied_sum += L[i]*(x**(len(L)-i-1))

        return applied_sum
    return fun_appliedto
    