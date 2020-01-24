# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:34:59 2020

@author: ANGELO
"""

def message():
    print("Enter next value")

print("We start here")
message()
print("The end is here")

def hi(name):
    print("Hi,",name)
    
hi("Greg")

def address (street, city, postalCode):
    print("Your address is;", street, "St.,", city, postalCode)
    
s = input("Street:")
pC = input ("Postal Code: ")
c = input ("City: ")

address(s,c,pC)

def subtra(a,b):
    print(a-b)
    
subtra(5,2)
subtra(2,5)

def multiply(a,b):
    return a*b
    
print(multiply(3,4))

def wishes():
    print("My wishes")
    return "Happy Birthday"
wishes()