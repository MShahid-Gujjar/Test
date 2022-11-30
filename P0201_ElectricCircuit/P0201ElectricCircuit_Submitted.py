# -*- coding: utf-8 -*-
# //  *******************************************************************************************************************
# //  Developer         : Muhammad Shahid
# //  Creation Date   : 26-11-2022
# //  Project Name    : P0201 Electric Circuit - HIRSCH Maschinenbau  
# //  Task            : String function with number of input bits and Boolean logic is given
# //                    Compute Boolean logic and identify unused outout at each gate
# //  Language	      : Python
# //  Folder		  : Folder "P0201_Electric Circuit" contains code files for "P0201 Electric Circuit" assessment task
# //  Miscellaneous Info : Folder "Boolean Logic" contains by hand drawn Boolean logic for defined notations and 
# //		        Digital Electric Circuit diagram for each test 
# //  *******************************************************************************************************************


import numpy as np


# Check AND gate condition i.e. input1 <= input2 
def ANDGateInputCheck(input1, input2):
    if input1 <= input2:
        result = True
        print(f'input1: {input1} <= input2: {input2} - result: {result}')
    else:
        result = False
        print(f'input1: {input1} > input2: {input2} - result: {result}')
        print('Alphabetical order condition for AND gate does not match.')
    return result


# Check OR gate condition i.e. input1 > input2 
def ORGateInputCheck(input1, input2):
    if input1 > input2:
        result = True
        print(f'input1: {input1} > input2: {input2} - result: {result}')
    else:
        result = False
        print(f'input1: {input1} < input2: {input2} - result: {result}')
        print('Alphabetical order condition for OR gate does not match.')
    return result


# Convert lowercase alphabet into uppercase alphabet and vice versa
def InvertInput(input):
    lowerCase = input.lower()
    upperCase = input.upper()

    if input == lowerCase:
        result = upperCase
    elif input == upperCase:
        result = lowerCase
    return result


# Compute AND gate
def ANDGate(input1, input2):
    output = np.array([0,1,0,0])
    for x in range(0,4):
        output[x] = input1[x] & input2[x]
        print('i1: ', input1[x], 'i2: ', input2[x], ' Y: ', output[x])
    return output


# Compute AND gate
def ORGate(input1, input2):
    output = np.array([0,1,0,0])
    for x in range(0,4):
        output[x] = input1[x] | input2[x]
        print('i1: ', input1[x], 'i2: ', input2[x], ' Y: ', output[x])
    return output


# Compute high/true logic occurence in unused remaining gate output
def UnusedTrueOutput(input1):
    output = 0
    for x in range(0,4):
        if (input1[x]==1):
            output += 1
    return output


# Check lower or upper case of input signal in a given test function
def IsCapitalInput(inputAlphabet):
    result = False
    if inputAlphabet.isupper():
        result = True
    return result


# Compute inverse of given input values e.g. a => -a = A
def InverseCapitalSignalInput(inputSignal):
    for x in range(0,4):
        if(inputSignal[x] == 0):
            inputSignal[x] = 1
        else:
            inputSignal[x] = 0
    return inputSignal            
            
            





#   **************************************************************************
# 
#                       Main Function 
# 
#   **************************************************************************

if __name__ == '__main__':

# Example-1 Test-1
    sTest1 = '2 abBA'
    testLength = len(sTest1)
    noOfInputs = sTest1[0]
    noOfInputsInt = int(sTest1[0])
    
    i = 2
    k = 0           
    unusedOutputLogic = []
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
        inputVariable.insert(k,sTest1[x])
        inputVariable.insert(k+1,sTest1[x+1])
        print('x: ', x, ' - x+1: ', x+1)
        print(f'inp: {inputVariable[k]} - test: {sTest1[x]}')
        print(f'inp: {inputVariable[k+1]} - test: {sTest1[x+1]}\n\n')
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
            unusedOutputLogic.append(UnusedTrueOutput(computedResult))
        elif isORGate:
            computedResult = ORGate(signal1, signal2)
            unusedOutputLogic.append(UnusedTrueOutput(computedResult))
        k=i

    print('\n\n******************   Output  ***************************')
    print(f'Unused True output logic for "{sTest1}" are {unusedOutputLogic}')
            
        
















# def ANDGate(input1, input2):
#     input1Values = [0,0,0,0]
#     input2Values = [0,0,0,0]
#     outputValuesAND = [0,1,0,0]
#     print('\n*********   AND GATE     ************************\n')
#     print('input-1: ', input1, 'input-2: ', input2)
#     UpdateInputSignalBitValues()

#     for x in range(0,len(inputSignalBitValues)):
#         if inputSignalBit[x] == input1:
#             input1Values = inputSignalValues[x]
#         elif inputSignalBit[x] == input2:
#             input2Values = inputSignalValues[x]
        
#     for y in range(0,4):
#         outputValuesAND[y] = input1Values[y] & input2Values[y]
#     print('i1: ', input1Values, 'i2: ', input2Values, ' Y: ', outputValuesAND)
    
#     ov = outputValuesAND
#     keyInc = chr(ord(input2) + 1)
#     inputSignalBitValues.update({keyInc  : ov})
#     UpdateInputSignalBitValues()
    
#     return outputValuesAND
