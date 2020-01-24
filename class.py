# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:36:16 2020

@author: ANGELO
"""

'Common base class for all employees'
class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name:",self.name,",Salary:",self.salary)