#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:34:50 2018

@author: memoherrera
"""

def mult (a,b) :
    c = 0
    while a>0 : 
        c += b
        a -= 1
    
    return c

print(mult(5,9))


def sumar(n) :
    return (n*(n+1))/2

print(sumar(6))      