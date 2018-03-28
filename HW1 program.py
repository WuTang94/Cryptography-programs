# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:50:19 2018

@author: Justin Tang
"""
import math
import numpy

    
def elGamelD(y1, y2, p, a):
    inv = (((y1**a)%p)**(p-2))%p
    decrypt = y2*inv%p
    return decrypt
'''

def main():
    

'''
def ShanksDL(p, alpha, beta):
    n = p - 1
    m = int(math.ceil(math.sqrt(n)))
    product = (alpha**m)%p
    #This creates L1
    print("L1: ")
    L1 = []
    for j in range(0, m):#change m to 30 if we only want the top 30
        x = (product**j)%p
        row = [j, x]
        L1.append(row)
        #print("(",j,",",x,")")
    L1 = numpy.vstack(L1)
    #print (L1)
    '''
    for i in range(0, len(L1)):
        print(L1[i,0],L1[i,1])
    '''    
    #this is L2
    print("L2: ")
    L2 = []
    for i in range(0, m):#change m to 30 if we only want the top 30
        inv = ExtEuclAlg(alpha**i,p)
        y = (beta*inv%p)
        row = [i, y]
        L2.append(row)
        #print("(",i,",",y,")")
    L2 = numpy.vstack(L2)
    
    
    #print(L2)
    #print(L1)
    '''
    for j in range(0, len(L2)):
        print(L2[j,0],L2[j,1])
    '''
    #print(L2)
    #print(set(L1[]) & set(L2[]))
    '''
    for val in length(0, m):
        if
    '''
    for i in range(0, len(L1)):
        for j in range (0, len(L2)):
            if L1[i,1] == L2[j,1]:
                x = L1[i,0]
                y = L2[j,0]
                print ("x =", x, "y =", y)
                print (L1[i,1],L2[j,1])
                
    

  
def ExtEuclAlg(a, b):
    x, lastX = 0, 1
    y, lastY = 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    return (lastX)
    
#print(egcd(729,809))

#def bruteForce():
    
print(ShanksDL(31847,5,18074))


def main():
    #initialize plaintext
    plaintext = ""
    #this opens a handle to the file containing the original ciphertext
    file_handle = open('ciphertexthw1.txt', 'r')
    #read in all 
    print("Original Plaintext:")
    for row in file_handle:
        #print(row)
        array = row.split(" ")
        L1 = int(array[0])
        L2 = int(array[1])
        #print(elGamelD(row))
        #This is the original plaintext
        numPlain = elGamelD(L1, L2, 31847, 7899)
        #print (numPlain)
        """
        now to divide it into three letters through my makeshift modular exponentiation
        """
        firstl = math.floor(numPlain/(26**2))
        secondl = math.floor((numPlain%26**2)/26)
        thirdl = (numPlain)%26
        print (firstl, secondl, thirdl)
        
        '''
        #To match these numbers to their respective ASCII characters, simply add 97
    '''
        plaintext+=chr(firstl+97)
        plaintext+=chr(secondl+97)
        plaintext+=chr(thirdl+97)
        
    print(plaintext)

print(main())