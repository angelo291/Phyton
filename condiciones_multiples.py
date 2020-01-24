# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:35:13 2020

@author: ANGELO
"""

aclNum = int(input("What is the IPv4 ACL numer?"))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <=199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")
    
