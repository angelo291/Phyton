# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:59:46 2020

@author: ANGELO
"""

firstName = input("Cúal es tu primer nombre?")
lastName = input("Cúal es tu apellido?")
location = input("Cúal es tu ubicación?")
age = int(input("Cúal es tu edad?"))
space = " "
print("Hola"+space+firstName+space+lastName+space+"tu ubicación es"+space+location)
if age >=1 and age <=15:
    print("Tienes",age,"años",",Tu todavía eres un niño")
elif age >=15 and age <=30:
    print("Tienes",age,"años",",Tu eres un adolescente")
elif age >=31 and age <=60:
    print("Tienes",age,"años",",Tu eres un adulto")
elif age >61:
    print("Tienes",age,"años",",Tu eres un anciano")
else:
    print("Edad no correcta")
    