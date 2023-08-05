# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:48:09 2019

@author: yoelr
"""
from numpy import ndarray, asarray

class array(ndarray):
    """Create an array object that functions exactly like a numpy ndarray."""
    # This allows casting to a module array class
    __slots__ = ()
    
    def __repr__(self):
        Type = type(self).__name__
        rep = repr(asarray(self)).replace('array', Type)
        spaces = len(Type)*' '
        return rep.replace('\n     ', '\n' + spaces)