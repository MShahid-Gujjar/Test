# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

inputSignalBitValues = {
                      "a" : ([0, 0, 1, 1]),
                      "b" : ([0, 1, 0, 1])
                      }
inputSignalBit = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
inputSignalValues = ([0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1])


inputSignalBitValuesInverse = {
                      "A" : ([1, 1, 0, 0]),
                      "B" : ([1, 0, 1, 0])
                      }
inputSignalBitInverse = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
inputSignalValuesInverse = ([0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1])

def ANDGateInputCheck(s1, s2):
    if s1 <= s2:
        result1 = True
        print(f's1: {s1} - s2: {s2} - result: {result1}')
    else:
        result1 = False
        print(f's1: {s1} - s2: {s2} - result: {result1}')
        print('Alphabetical order condition for AND gate does not match.')
    return result1


def ORGateInputCheck(s1, s2):
    if s1 > s2:
        result = True
        print(f's1: {s1} - result: {result}')
    else:
        result = False
        print(f's1: {s2} - result: {result}')
        print('Alphabetical order condition for OR gate does not match.')
    return result


def InvertInput(input):
    lowerCase = input.lower()
    upperCase = input.upper()

    if input == lowerCase:
        result = upperCase
        print(f'a: {input} - lowercase inverted to uppercase : {result}')
    elif input == upperCase:
        result = lowerCase
        print(f'a: {input} - uppercase inverted to lowercase : {result}')
    return result

def ANDGate(input1, input2):
    inp1 = [0,0,0,0]
    inp2 = [0,0,0,0]
    output = [0,1,0,0]
    print('*********   AND GATE     ************************\n\n')
    UpdateInputSignalBitValues()

    for x in range(0,len(inputSignalBitValues)):
        if inputSignalBit[x] == input1:
            inp1 = inputSignalValues[x]
        elif inputSignalBit[x] == input2:
            inp2 = inputSignalValues[x]
    print('signal: ', inputSignalBit[x], 'Value: ', inputSignalValues[x])
        
    for y in range(0,4):
        output[y] = inp1[y] & inp2[y]
    print('i1: ', inp1, 'i2: ', inp2, ' Y: ', output)
    
    keyInc = chr(ord(input2) + 1)
    inputSignalBitValues.update({keyInc  : output})
    UpdateInputSignalBitValues()
    
    keyInc = keyInc.upper()
    output = InverseCapitalSignalInput(output)
    inputSignalBitValuesInverse.update({keyInc  : output})
    UpdateInputSignalBitValuesInverse()
    
def ORGate(input1, input2):
    inp1 = [0,0,0,0]
    inp2 = [0,0,0,0]
    output = [0,1,0,0]
    print('*********   OR GATE     ************************\n\n')
    print('i1: ', input1, 'i2: ', input2)
    UpdateInputSignalBitValues()
    UpdateInputSignalBitValuesInverse()

    for x in range(0,len(inputSignalBitValuesInverse)):
        print('for loop')
        if inputSignalBit[x] == input1:
            inp1 = inputSignalValues[x]
        if inputSignalBit[x] == input2:
            inp2 = inputSignalValues[x]
        if inputSignalBitInverse[x] == input1:
            inp1 = inputSignalValuesInverse[x]
        if inputSignalBitInverse[x] == input2:
            inp2 = inputSignalValuesInverse[x]
    # print('signal: ', inputSignalBit, 'Value: ', inputSignalValues)
        
    for y in range(0,4):
        output[y] = inp1[y] | inp2[y]
    print('i1: ', inp1, 'i2: ', inp2, ' Y: ', output)
    
    keyInc = chr(ord(input2) + 1)
    inputSignalBitValues.update({keyInc  : output})
    print('Dictionary: ', inputSignalBitValues)

def UnusedTrueOutput(input1):
    output = 0
    for x in range(0,4):
        if (input1[x]==1):
            output += 1
    print('Unused True Output: ', output)
    return output

def IsCapitalInput(inputAlphabet):
    result = False
    if inputAlphabet.isupper():
        result = True
    return result

def InverseCapitalSignalInput(inputSignal):
    for x in range(0,4):
        print('i: ', inputSignal[x], end=", ")
        if(inputSignal[x] == 0):
            inputSignal[x] = 1
        else:
            inputSignal[x] = 0
        print('o: ', inputSignal[x])
    return inputSignal            
   
def UpdateInputSignalBitValues():
    inputSignalBit = inputSignalBitValues.keys()
    inputSignalBit = list(inputSignalBitValues)
    inputSignalValues = inputSignalBitValues.values()
    inputSignalValues = list(inputSignalValues)         
    print('*** Update **** signal: ', inputSignalBit, 'Value: ', inputSignalValues)

def UpdateInputSignalBitValuesInverse():
    inputSignalBitInverse = inputSignalBitValuesInverse.keys()
    inputSignalBitInverse = list(inputSignalBitValuesInverse)
    inputSignalValuesInverse = inputSignalBitValuesInverse.values()
    inputSignalValuesInverse = list(inputSignalValuesInverse)         
    print('*** Update Inverse **** signal: ', inputSignalBitInverse, 'Value: ', inputSignalValuesInverse)

# Given 2 input bits string function: 1.) Compute output variable from input 2.) Find unutiliued computed variable
def TwoInputBitFunc(sExample1Test1):
    i = 2   # e.g: because in "2 abBA" function logic sequence start from 2nd element
    k = 0           
    inputVariable = ["a", "b"]
    inputVariableInverse = ["A", "B"]
    variableSequence = ["a", "b", "c", "d"]

    UpdateInputSignalBitValues()
    print('Dictionary: ', inputSignalBitValues)
        
    for x in range(i, iTestLength, 2):
        inputVariable.insert(k,sExample1Test1[x])
        inputVariable.insert(k+1,sExample1Test1[x+1])
        print('x: ', x, ' - x+1: ', x+1)
        print(f'inp: {inputVariable[k]} - test: {sExample1Test1[x]}')
        print(f'inp: {inputVariable[k+1]} - test: {sExample1Test1[x+1]}')

        # isCapital = IsCapitalInput(inputVariable[k]) 
        # if isCapital:
        #     A = InverseCapitalSignalInput(a)
            
        # isCapital = IsCapitalInput(inputVariable[k+1]) 
        # if isCapital:
        #     B = InverseCapitalSignalInput(b)

        isANDGate = ANDGateInputCheck(inputVariable[k], inputVariable[k+1])
        isORGate = ORGateInputCheck(inputVariable[k], inputVariable[k+1])
        if isANDGate:
            ANDGate(inputVariable[k], inputVariable[k+1])

        if isORGate:
            ORGate(inputVariable[k], inputVariable[k+1])
        k=i
    

if __name__ == '__main__':

#   ************************** Test Solution *********************************
#   **************************************************************************
#   Example-1 Test-1
    sExample1Test1 = '2 abBA'
    # sTest = '3 abAced'
    iTestLength = len(sExample1Test1)
    sNoOfInputs = sExample1Test1[0]
    iNoOfInputs = int(sExample1Test1[0])
    # print('Input Number: ' + sNoOfInputs + ' - Test Length: ', iTestLength)
    # print('Input Number: ',  iNoOfInputs, ' - Test Length: ', iTestLength)
    
    if iNoOfInputs == 2:
        TwoInputBitFunc(sExample1Test1)
        
    


