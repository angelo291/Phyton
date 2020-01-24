# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:45:10 2020

@author: ANGELO
"""

while True:
    x=input("Enter a numbre to count to:")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break