# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 09:36:05 2017

@author: Justin Tang unless otherwise stated;
methods that I borrowed online and modified are denoted
"""
import random
#import math

"""
I borrowed this method of Miller Rabin from a website, but I replaced the pow()
function with the Square and Multiply method. Also, I made it so that there is only
one security parameter and thus only one random instance of a 
"""
#Original source: https://www.snip2code.com/Snippet/4311/Python-implementation-of-the-Miller-Rabi
#partly modifications done by me
def MRPTest(p,k):
    #p is the prime candidate, k is the security parameter
    if p%2 == 0:# weeding out the even numbers
        return False
    
    
    r, s = 1, p - 1
    
    while s % 2 == 0:
        r += 1
        s //= 2
    
    for i in range(1,k):
        a = random.randrange(2, p - 1)
        #x = pow(a, s, p)
        x = SquareNMult2(p,a,s)
        if x == 1 or x == p - 1:
            continue
        for j in range(r - 1):
            #x = pow(x, 2, p)
            x = SquareNMult2(p,a,s)
            if x == p - 1:
                break
            else:
                return False
    return True

print (MRPTest(123003,1))


#
"""
another square and multiply function that I found. Only the second method was
particularly useful in my case
"""
"""      
def SquareNMult(x,n):
    return SquareNMult2(1, x, n)
"""        
def SquareNMult2(y,x,n):
    if n < 0: 
        return SquareNMult2(y,1/x,n)
    elif n == 0:
        return y
    elif n == 1:
        return x*y
    elif n % 2 == 0:
        return SquareNMult2(y, x * x, n/2)
    elif n % 2 == 1:
        return SquareNMult2(x * y, x * x, (n - 1)/2)
"""    
print(SquareNMult(2,5))    
print(pow(3,2,10))      
print(2**5)  
"""


#and here's a primality method that I borrowed that I'll test against Miller-Rabin
def is_prime(n):
    """#pre-condition: n is a nonnegative integer
    #post-condition: return True if n is prime and False otherwise."""
    if n < 2: 
         return False;
    if n % 2 == 0:             #weeding out the even numbers
         return n == 2  # return False
    k = 3 #this should work for all other odd numbers
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True


print(is_prime(13))    

#This is the method I wrote to run Miller Rabin for a certain range
#it shows the different errors and calculates total error
def testrange(a,b):
    errorCount = 0;#creating a place to count all errors
    totalErr = 0;
    total = 0
    #prime = False
    
    for i in range(a,b):
        errorCount = 0
        if i % 2 == 1:#odd numbers
            total += 1
            reg = is_prime(i)
            MR1 = MRPTest(i,1)
            for j in range(0,100): #repeating this 10 times
                if reg == MR1:
                     errorCount += 1
            print(i, "Error Probability: ", float(errorCount/1000))
            totalErr += float(errorCount/1000)
    
    ErrProbability = totalErr/total
    print("Total Error: ", ErrProbability, "% for ", total, "tries")
    #return errors

print(testrange(115000,125000))