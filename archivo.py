# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:00:15 2020

@author: ANGELO
"""

devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)
