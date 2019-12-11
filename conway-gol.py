# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:12:46 2019

@author: miles
"""
import numpy as np

# initialise: create empty universe -- np array?
def initialise(dim, pr=[0.5, 0.5]):
    """
    Creates a dim x dim np array randomly filled with 0 and 1 drawn with
    probabilities specified in pr.
    """
    universe = np.random.choice(2, size=(dim,dim), p = pr)
    return universe

print (initialise_nonuniform(10))
# seed: fill universe randomly with 1 and 0
 
# update: given universe in period t, compute universe for period t+1

