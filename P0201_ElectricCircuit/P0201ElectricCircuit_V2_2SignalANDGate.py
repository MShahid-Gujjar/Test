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
inputSignalBit = ["a", "b", "c", "d"]
inputSignalValues = ([0, 0, 1, 1], [0, 1, 0, 1])

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
    print('Dictionary: ', inputSignalBitValues)


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
            

# Given 2 input bits string function: 1.) Compute output variable from input 2.) Find unutiliued computed variable
def TwoInputBitFunc(sTest):
    i = 2   # e.g: because in "2 abBA" function logic sequence start from 2nd element
    k = 0           
    inputVariable = ["a", "b"]
    inputVariableInverse = ["a", "b"]
    variableSequence = ["a", "b", "c", "d"]

    inputSignalBit = inputSignalBitValues.keys()
    inputSignalBit = list(inputSignalBitValues)
    inputSignalValues = inputSignalBitValues.values()
    inputSignalValues = list(inputSignalValues)
    print(inputSignalBit[1])
    print(inputSignalValues[1])
    print('Dictionary: ', inputSignalBitValues)
        
    for x in range(i, iTestLength, 2):
        inputVariable.insert(k,sTest[x])
        inputVariable.insert(k+1,sTest[x+1])
        print('x: ', x, ' - x+1: ', x+1)
        print(f'inp: {inputVariable[k]} - test: {sTest[x]}')
        print(f'inp: {inputVariable[k+1]} - test: {sTest[x+1]}')

        # isCapital = IsCapitalInput(inputVariable[k]) 
        # if isCapital:
        #     A = InverseCapitalSignalInput(a)
            
        # isCapital = IsCapitalInput(inputVariable[k+1]) 
        # if isCapital:
        #     B = InverseCapitalSignalInput(b)

        isANDGate = ANDGateInputCheck(inputVariable[k], inputVariable[k+1])
        # isORGate = ORGateInputCheck(inputVariable[k], inputVariable[k+1])
        if isANDGate:
            print(isANDGate)
            ANDGate(inputVariable[k], inputVariable[k+1])
            #UnusedTrueOutput(computedResult)

        # if isORGate:
        #     computedResult = ORGate(a, b)
        #     UnusedTrueOutput(computedResult)
        k=i
    

if __name__ == '__main__':

#   ************************** Test Solution *********************************
#   **************************************************************************
#   Example-1 Test-1
    sTest = '2 abBA'
    # sTest = '3 abAced'
    iTestLength = len(sTest)
    sNoOfInputs = sTest[0]
    iNoOfInputs = int(sTest[0])
    # print('Input Number: ' + sNoOfInputs + ' - Test Length: ', iTestLength)
    # print('Input Number: ',  iNoOfInputs, ' - Test Length: ', iTestLength)
      

    if iNoOfInputs == 2:
        TwoInputBitFunc(sTest)
        
    


