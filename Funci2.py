# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:48:59 2020

@author: ANGELO
"""

def hiEverybody(myList):
    for name in myList:
        print("Hi,", name)
        
hiEverybody(["Adam","John","Lucy"])

def createList(n):
    myList = []
    for i in range (n):
        myList.append(i)
    return myList
    
print(createList(5))