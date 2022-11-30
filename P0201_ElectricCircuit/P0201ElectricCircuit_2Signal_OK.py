# -*- coding: utf-8 -*-
# //  *******************************************************************************************************************
# //  Developer         : Muhammad Shahid
# //  Creation Date   : 26-11-2022
# //  Project Name    : P0201 Electric Circuit - HIRSCH Maschinenbau  
# //  Task            : String function with number of input bits and Boolean logic is given
# //                    Compute Boolean logic and identify unused outout at each gate
# //  Language	      : Python
# //  Folder		: Folder "P0201_Electric Circuit" contains code files for "P0201 Electric Circuit" assessment task
# //  Miscellaneous Info : Folder "Boolean Logic" contains by hand drawn Boolean logic for defined notations and 
# //		        Digital Electric Circuit diagram for each test 
# //  *******************************************************************************************************************


import numpy as np

inputSignalBitValues = {
                      'a' : ([0, 0, 1, 1]),
                      'b' : ([0, 1, 0, 1])
                      }
inputSignalBit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
inputSignalValues = ([0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1])


# inputSignalBitValuesInverse = {
#                       'A' : ([1, 1, 0, 0]),
#                       'B' : ([1, 0, 1, 0])
#                       }
# inputSignalBitInverse = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
# inputSignalValuesInverse = ([0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
#                      [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
#                      [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
#                      [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1])

def ANDGateInputCheck(input1, input2):
    if input1 <= input2:
        result1 = True
        print(f'input1: {input1} - input2: {input2} - result: {result1}')
    else:
        result1 = False
        print(f'input1: {input1} - input2: {input2} - result: {result1}')
        print('Alphabetical order condition for AND gate does not match.')
    return result1


def ORGateInputCheck(input1, input2):
    if input1 > input2:
        result = True
        print(f'input1: {input1} - input2: {input2} - result: {result}')
    else:
        result = False
        print(f'input1: {input1} - input2: {input2} - result: {result}')
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
    input1Values = [0,0,0,0]
    input2Values = [0,0,0,0]
    outputValues = [0,1,0,0]
    print('\n*********   AND GATE     ************************\n')
    print('input-1: ', input1, 'input-2: ', input2)
    UpdateInputSignalBitValues()

    for x in range(0,len(inputSignalBitValues)):
        isCapital = IsCapitalInput(input1) 
        if isCapital:
            if (inputSignalBit[x].upper()) == input1:
                input1Values = inputSignalValues[x]
                input1Values = InverseCapitalSignalInput(input1Values)
        else:
            if inputSignalBit[x] == input1:
                input1Values = inputSignalValues[x]
                    
        isCapital = IsCapitalInput(input2) 
        if isCapital:
            if (inputSignalBit[x].upper()) == input2:
                input2Values = inputSignalValues[x]
                input2Values = InverseCapitalSignalInput(input2Values)
        else:
            if inputSignalBit[x] == input2:
                input2Values = inputSignalValues[x]
          
    for y in range(0,4):
        outputValues[y] = input1Values[y] & input2Values[y]
    print('i1: ', input1Values, 'i2: ', input2Values, ' Y: ', outputValues)

    maxChar = max(inputSignalBitValues.keys())
    print('largest char....', maxChar)

    keyInc = chr(ord(maxChar) + 1) 
    inputSignalBitValues.update({keyInc  : outputValues})
    UpdateInputSignalBitValues()
    
    print('AND Gate Final Output ---------\n', inputSignalBitValues)
    return outputValues
    
def ORGate(input1, input2):
    input1Values = [0,0,0,0]
    input2Values = [0,0,0,0]
    outputValues = [0,1,0,0]
    print('\n*********   OR GATE     ************************\n')
    print('input-1: ', input1, 'input-2: ', input2)

    for x in range(0,len(inputSignalValues)):
        isCapital = IsCapitalInput(input1) 
        if isCapital:
            if (inputSignalBit[x].upper()) == input1:
                input1Values = inputSignalValues[x]
                input1Values = InverseCapitalSignalInput(input1Values)
        else:
            if inputSignalBit[x] == input1:
                input1Values = inputSignalValues[x]
                    
        isCapital = IsCapitalInput(input2) 
        if isCapital:
            if (inputSignalBit[x].upper()) == input2:
                input2Values = inputSignalValues[x]
                input2Values = InverseCapitalSignalInput(input2Values)
        else:
            if inputSignalBit[x] == input2:
                input2Values = inputSignalValues[x]
            
    for y in range(0,4):
        outputValues[y] = input1Values[y] | input2Values[y]
    print('i1: ', input1Values, 'i2: ', input2Values, ' Y: ', outputValues)
    
    maxChar = max(inputSignalBitValues.keys())
    print('largest char....', maxChar)

    keyInc = chr(ord(maxChar) + 1) 
    inputSignalBitValues.update({keyInc  : outputValues})

    print('OR Gate Final Output ---------\n', inputSignalBitValues)
    
    return outputValues

def UnusedTrueoutputValues(input1):
    outputValues = 0
    for x in range(0,4):
        if (input1[x]==1):
            outputValues += 1
    print('Unused True outputValues: ', outputValues)
    return outputValues

def IsCapitalInput(inputAlphabet):
    result = False
    if inputAlphabet.isupper():
        result = True
    return result

def InverseCapitalSignalInput(inputSignal):
    inputSignalBuf = inputSignal
    for x in range(0,4):
        print('input: ', inputSignalBuf[x], end=", ")
        if(inputSignalBuf[x] == 0):
            inputSignalBuf[x] = 1
        else:
            inputSignalBuf[x] = 0
        print('inverse: ', inputSignalBuf[x])
    return inputSignalBuf            
   
def UpdateInputSignalBitValues():
    inputSignalBit = inputSignalBitValues.keys()
    inputSignalBit = list(inputSignalBit)
    inputSignalValues = inputSignalBitValues.values()
    inputSignalValues = list(inputSignalValues)         
    print('*** Update **** signal: ', inputSignalBit, 'Value: ', inputSignalValues)
    

def UpdateInputSignalBitValuesInverse():
    print('*** Compliment Check 0 **** ', inputSignalBitValues)
    inputSignalBitInverse = inputSignalBitValues.keys()
    inputSignalBitInverse = list(inputSignalBitInverse)
    inputSignalValuesInverse = inputSignalBitValues.values()
    inputSignalValuesInverse = list(inputSignalValuesInverse)         
    # print('*** Update Inverse **** signal: ', inputSignalBitInverse, 'Value: ', inputSignalValuesInverse)
    print('*** Compliment Check 1 **** signal: ', inputSignalBitInverse, 'Value: ', inputSignalValuesInverse)
    
    for x in range(0,len(inputSignalBitValues)):
        keyInc = inputSignalBitInverse[x].upper()
        outputValues = InverseCapitalSignalInput(inputSignalValuesInverse[x])
        inputSignalBitValuesInverse.update({keyInc  : outputValues})
    print('*** Compliment Check 3 **** ', inputSignalBitValuesInverse)

# Given 2 input bits string function: 1.) Compute outputValues variable from input 2.) Find unutiliued computed variable
def TwoInputBitFunc(sExample1Test1):
    Declare2InputSignalValues()
    i = 2   # e.g: because in "2 abBA" function logic sequence start from 2nd element
    k = 0           
    inputVariable = ["a", "b"]
    inputVariableInverse = ["A", "B"]
    variableSequence = ["a", "b", "c", "d"]
    computedResult = np.array([0, 0, 0, 0])
    unusedOutputLogic = []

    UpdateInputSignalBitValues()
    print('2 bit Func called - Dictionary: ', inputSignalBitValues)
        
    for x in range(i, iTestLength, 2):
        inputVariable.insert(k,sExample1Test1[x])
        inputVariable.insert(k+1,sExample1Test1[x+1])
        print('x: ', x, ' - x+1: ', x+1)
        print(f'inp: {inputVariable[k]} - inp: {inputVariable[k+1]}')

        isANDGate = ANDGateInputCheck(inputVariable[k], inputVariable[k+1])
        isORGate = ORGateInputCheck(inputVariable[k], inputVariable[k+1])
        if isANDGate:
            computedResult = ANDGate(inputVariable[k], inputVariable[k+1])
            unusedOutputLogic.append(UnusedTrueOutput(computedResult))
        
        if isORGate:
            computedResult = ORGate(inputVariable[k], inputVariable[k+1])
            unusedOutputLogic.append(UnusedTrueOutput(computedResult))
        print('\n\n******************   Output  ***************************')
        print(f'Unused True output logic for "{sExample1Test1}" are {unusedOutputLogic}')
        k=i
    

def Declare2InputSignalValues():
    twoInputSignalValues = {
                            "a" : ([0, 0, 1, 1]),
                            "b" : ([0, 1, 0, 1])
                            }
    

def Declare3InputSignalValues():
    threeInputSignalValues = {
                              "a" : ([0, 0, 0, 0, 1, 1, 1, 1]),
                              "b" : ([0, 0, 1, 1, 0, 0, 1, 1]),
                              "c" : ([0, 1, 0, 1, 0, 1, 0, 1]),
                              }

def Declare4InputSignalValues():
    fourInputSignalValues = {
                            "a" : ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]),
                            "b" : ([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]),
                            "c" : ([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]),
                            "d" : ([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),
                            }


# Compute high/true logic occurence in unused remaining gate output
def UnusedTrueOutput(input1):
    output = 0
    for x in range(0,4):
        if (input1[x]==1):
            output += 1
    return output


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
        
    


