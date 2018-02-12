# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:07:54 2017

@author: Justin Tang
"""
import math

def bdayA(a, b):
    print ("Results for algorithm from page 300: \n")
    for i in range(a,b+1):
        #print(i)
        result = 1
        #the range starts at 2, so that the first term is (1 - 1/365)
        for t in range(2,i):
            mult = (1 - ((t-1)/365))
            result *= mult
        #probs.append(result)
        print("Probability for", i, ": ", result)
            
    #return probs
   
def bdayB(a, b):
    print("Results for algorithm from page 301: \n")
    for t in range(a, b+1):
        mult = t*(t-1)
        #Normally we'd put 2^n, but in this case let's just do 365    
        result = math.exp(-(mult/(2*365)) )
        print("Probability for", t, ": ", result)
    
    
print(bdayA(15,30))
print(bdayB(15,30))