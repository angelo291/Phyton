# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:54:52 2020

@author: ANGELO
"""
import numpy as np
unos=np.ones((3,4))
print(unos)

ceros=np.zeros((3,4))
print(ceros)

espacio1=np.arange(0,30,5)
print(espacio1)

espacio2=np.linspace(0,2,5)
print(espacio2)

identidad1=np.eye(4,4)
print(identidad1)

identidad2=np.identity(4)
print(identidad2)

a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)

b=np.array([(8,9,10),(11,12,13)])
print(b)
print("\n"*2)
b=b.reshape(3,2)
print(b)

c=np.array([2,4,8])
print(c.min())
print(c.max())
print(c.sum())

d=np.array([(1,2,3),(3,4,5)])
print("\n"*2)
print(np.sqrt(d))
print("\n"*2)
print(np.std(d))