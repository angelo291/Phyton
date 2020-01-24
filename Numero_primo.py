# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:05:33 2020

@author: danny
"""
'''
while True:

    num = int(input("Ingrese valor: "))
    
    def primo(num):
        if num%2 == 0 or num%3 == 0 or num%4 == 0 or num%5 == 0:
            if num == 2:
                return True
            else:    
                return False
        else:
            return True
            
    print(primo(num))
'''
    
def isPrime(num):
    if num%2 == 0 or num%3 == 0 or num%4 == 0 or num%5 == 0:
            if num == 2:
                return True
            else:    
                return False
    else:
        return True

for num in range(1, 100):
	if isPrime(num + 1) != False:
			print(num + 1, end=" ")
            
print()
