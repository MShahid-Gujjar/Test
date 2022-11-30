# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np


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
    output = np.array([0,1,0,0])
    for x in range(0,4):
        output[x] = input1[x] & input2[x]
        print('i1: ', input1[x], 'i2: ', input2[x], ' Y: ', output[x])
    return output


def ORGate(input1, input2):
    output = np.array([0,1,0,0])
    for x in range(0,4):
        output[x] = input1[x] | input2[x]
        print('i1: ', input1[x], 'i2: ', input2[x], ' Y: ', output[x])
    return output

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
            
            

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

#   ************************** Test Solution *********************************
#   **************************************************************************
# Example-1 Test-1
    # test1 = '2 abBA'
    test1 = '3 abAced'
    testLength = len(test1)
    noOfInputs = test1[0]
    noOfInputsInt = int(test1[0])
    # print('Input Number: ' + noOfInputs + ' - Test Length: ', testLength)
    # print('Input Number: ',  noOfInputsInt, ' - Test Length: ', testLength)
    
    i = 2
    j = 3
    k = 0           
    gates = []
    inputVariable = ["a", "b"]
    signal1 = np.array([0, 0, 1, 1])
    signal2 = np.array([0, 1, 0, 1])
    signal2 = np.array([1, 0, 1, 0])
    signalInvert1 = np.array([1, 1, 0, 0])
    signalInvert2 = np.array([1, 0, 1, 0])
    computedResult = np.array([0, 0, 0, 0])
    
    
    for x in range(i, testLength, 2):
        signal1 = np.array([0, 0, 1, 1])
        signal2 = np.array([0, 1, 0, 1])
        inputVariable.insert(k,test1[x])
        inputVariable.insert(k+1,test1[x+1])
        print('x: ', x, ' - x+1: ', x+1)
        print(f'inp: {inputVariable[k]} - test: {test1[x]}')
        print(f'inp: {inputVariable[k+1]} - test: {test1[x+1]}')
        isANDGate = ANDGateInputCheck(inputVariable[k], inputVariable[k+1])
        isORGate = ORGateInputCheck(inputVariable[k], inputVariable[k+1])
        isCapital = IsCapitalInput(inputVariable[k]) 
        if isCapital:
            signal1 = InverseCapitalSignalInput(signal1)
        isCapital = IsCapitalInput(inputVariable[k+1]) 
        if isCapital:
            signal2 = InverseCapitalSignalInput(signal2)
        if isANDGate:
            computedResult = ANDGate(signal1, signal2)
            UnusedTrueOutput(computedResult )
        elif isORGate:
            computedResult = ORGate(signal1, signal2)
            UnusedTrueOutput(computedResult )
        k=i

