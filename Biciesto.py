# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:01:12 2020

@author: ANGELO
"""

def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 !=0:
        return True
    else:
        return False
print(isYearLeap(1987))
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
