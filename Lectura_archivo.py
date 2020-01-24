# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:52:07 2020

@author: ANGELO
"""

file=open("devices.txt","r")
for item in file:
    print(item)
file.close()


file=open("devices.txt","r")
for item in file:
    item=item.strip()
    print(item)
file.close()