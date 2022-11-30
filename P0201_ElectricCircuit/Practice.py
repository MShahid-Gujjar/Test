# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:03:18 2022

@author: mshah
"""

import numpy as np

arr = np.array([[1,2,3,4], [1,2,3,4]])
print(arr[0,3])

thisdict = {
            "a" : ([0, 0, 1, 1]),
            "b" : ([0, 1, 0, 1])
            }

# Loop through keys
for x in thisdict:
    y = chr(ord(x) + 1)
    print(x, type(x), y)

# Loop through values
for x in thisdict:
    print(thisdict[x], type(thisdict[x]))    

#	Converting Dictionary into List to access individual element
thisdict = {
            "a" : ([0, 0, 1, 1]),
            "b" : ([0, 1, 0, 1])
            }
dictKeys = thisdict.keys()
dictKeys = list(dictKeys)
dictValues = thisdict.values()
dictValues = list(dictValues)
print(dictKeys[1])
print(dictValues[1])

c='a'
d='b'
e=1
f=10
g=20

if c==d:
    print('True sC')
else:
    print('False sC')
    
#  short hand if else
print("A") if c > d else print("B")
e=f if c < d else g



# def TwoInputBitFunc(sTest):
#     i = 2   # e.g: because in "2 abBA" function logic sequence start from 2nd element
#     k = 0           
#     inputVariable = ["a", "b"]
#     inputVariableInverse = ["a", "b"]
#     variableSequence = ["a", "b", "c", "d"]
#     inputSignalBit = {
#                       "a" : ([0, 0, 1, 1]),
#                       "b" : ([0, 0, 1, 1]),
#                       }
#     print('Dictionary: ', inputSignalBit)
#     a = np.array([0, 0, 1, 1])
#     b = np.array([0, 1, 0, 1])
#     A = np.array([1, 1, 0, 0])
#     B = np.array([1, 0, 1, 0])
        
#     for x in range(i, iTestLength, 2):
#         inputVariable.insert(k,sTest[x])
#         inputVariable.insert(k+1,sTest[x+1])
#         print('x: ', x, ' - x+1: ', x+1)
#         print(f'inp: {inputVariable[k]} - test: {sTest[x]}')
#         print(f'inp: {inputVariable[k+1]} - test: {sTest[x+1]}')

#         isCapital = IsCapitalInput(inputVariable[k]) 
#         if isCapital:
#             A = InverseCapitalSignalInput(a)
            
#         isCapital = IsCapitalInput(inputVariable[k+1]) 
#         if isCapital:
#             B = InverseCapitalSignalInput(b)

#         isANDGate = ANDGateInputCheck(inputVariable[k], inputVariable[k+1])
#         isORGate = ORGateInputCheck(inputVariable[k], inputVariable[k+1])
#         if isANDGate:
#             computedResult = ANDGate(a, b)
#             UnusedTrueOutput(computedResult)

#         if isORGate:
#             computedResult = ORGate(a, b)
#             UnusedTrueOutput(computedResult)
#         k=i
