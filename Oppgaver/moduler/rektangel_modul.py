# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:39:52 2025

@author: AFL015
"""
import numpy as np

def areal_rektangel(l, b):
    a = l*b
    return a
    

def omkrets_rektangel(l, b):
    o = 2*l + 2*b
    return o

def diagonal_rektangel(l, b):
    d = np.sqrt(l**2 + b**2)
    return d