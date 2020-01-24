# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:31:35 2020

@author: ANGELO
"""

x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    
x=input("Enter a number to count to: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y > x:
        break
    