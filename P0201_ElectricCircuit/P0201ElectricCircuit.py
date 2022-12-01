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

twoInputSignalBitValues = {
                      'a' : ([0, 0, 1, 1]),
                      'b' : ([0, 1, 0, 1])
                      }
inputSignalBit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
inputSignalValues = ([0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1],
                     [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1])


threeInputSignalBitValues = {
                      'a' : ([0, 0, 0, 0, 1, 1, 1, 1]),
                      'b' : ([0, 0, 1, 1, 0, 0, 1, 1]),
                      'c' : ([0, 1, 0, 1, 0, 1, 0, 1])
                      }
threeInputSignalBit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
threeInputSignalValues = (    
                          [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1],
                          [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1],
                          [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1])

# unUsedHighLogic2Bit = {'': []}
unUsedHighLogic2Bit = dict()
unUsedHighLogic3Bit = {'': []}

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

# 2Bit input signal
def ANDGate2Bit(input1, input2):
    input1Values = [0,0,0,0]
    input2Values = [0,0,0,0]
    outputValues = [0,1,0,0]
    print('\n*********   AND GATE     ************************\n')
    print('input-1: ', input1, 'input-2: ', input2)

    twoInputSignalBitKey = twoInputSignalBitValues.keys()
    twoInputSignalBitBuffer = list(twoInputSignalBitKey)
    twoInputSignalValuesKey = twoInputSignalBitValues.values()
    twoInputSignalValuesBuffer = list(twoInputSignalValuesKey)         
    print('*** Update 2 **** signal: ', twoInputSignalBitBuffer, 'Value: ', twoInputSignalValuesBuffer)

    for x in range(0,len(twoInputSignalBitValues)):
        isCapital = IsCapitalInput(input1) 
        if isCapital:
            if (twoInputSignalBitBuffer[x].upper()) == input1:
                input1Values = twoInputSignalValuesBuffer[x]
                input1Values = InverseCapitalSignalInput(input1Values)
        else:
            if twoInputSignalBitBuffer[x] == input1:
                input1Values = twoInputSignalValuesBuffer[x]
                    
        isCapital = IsCapitalInput(input2) 
        if isCapital:
            if (twoInputSignalBitBuffer[x].upper()) == input2:
                input2Values = twoInputSignalValuesBuffer[x]
                input2Values = InverseCapitalSignalInput(input2Values)
        else:
            if twoInputSignalBitBuffer[x] == input2:
                input2Values = twoInputSignalValuesBuffer[x]
          
    for y in range(0,4):
        outputValues[y] = input1Values[y] & input2Values[y]
    print('i1: ', input1Values, 'i2: ', input2Values, ' Y: ', outputValues)

    maxChar = max(twoInputSignalBitValues.keys())
    print('largest char....', maxChar)

    keyInc = chr(ord(maxChar) + 1) 
    twoInputSignalBitValues.update({keyInc  : outputValues})
    unUsedHighLogic2Bit.update({keyInc: outputValues})

    print('2Bit AND Gate Final Output ---------\n', twoInputSignalBitValues)
    return unUsedHighLogic2Bit



def ANDGate3Bit(input1, input2):
    input1Values = [0,0,0,0,0,0,0,0]
    input2Values = [0,0,0,0,0,0,0,0]
    input3Values = [0,0,0,0,0,0,0,0]
    outputValues = [1,0,0,0,0,0,0,1]
    print('\n*********   AND GATE  3Bit   ************************\n')
    print('input-1: ', input1, 'input-2: ', input2)

    threeInputSignalBitKey = threeInputSignalBitValues.keys()
    threeInputSignalBitBuffer = list(threeInputSignalBitKey)
    threeInputSignalValuesKey = threeInputSignalBitValues.values()
    threeInputSignalValuesBuffer = list(threeInputSignalValuesKey)         
    print('*** Update 2 **** signal: ', threeInputSignalBitBuffer, 'Value: ', threeInputSignalValuesBuffer)

    for x in range(0,len(threeInputSignalBitValues)):
        isCapital = IsCapitalInput(input1) 
        if isCapital:
            if (threeInputSignalBitBuffer[x].upper()) == input1:
                input1Values = threeInputSignalValuesBuffer[x]
                input1Values = InverseCapitalSignal3Input(input1Values)
        else:
            if threeInputSignalBitBuffer[x] == input1:
                input1Values = threeInputSignalValuesBuffer[x]
                    
        isCapital = IsCapitalInput(input2) 
        if isCapital:
            if (threeInputSignalBitBuffer[x].upper()) == input2:
                input2Values = threeInputSignalValuesBuffer[x]
                input2Values = InverseCapitalSignal3Input(input2Values)
        else:
            if threeInputSignalBitBuffer[x] == input2:
                input2Values = threeInputSignalValuesBuffer[x]
          
    for y in range(0,8):
        outputValues[y] = input1Values[y] & input2Values[y]
    print('3i1: ', input1Values, '3i2: ', input2Values, ' 3Y: ', outputValues)

    maxChar = max(threeInputSignalBitValues.keys())
    print('largest char....', maxChar)

    keyInc = chr(ord(maxChar) + 1) 
    threeInputSignalBitValues.update({keyInc  : outputValues})
    
    print('3Bit AND Gate Final Output ---------\n', threeInputSignalBitValues)
    return outputValues

#   2Bit OR Gate 
def ORGate2Bit(input1, input2):
    input1Values = [0,0,0,0]
    input2Values = [0,0,0,0]
    outputValues = [0,1,0,0]
    print('\n*********   OR GATE 2Bit    ************************\n')
    print('input-1: ', input1, 'input-2: ', input2)

    twoInputSignalBitKey = twoInputSignalBitValues.keys()
    twoInputSignalBitBuffer = list(twoInputSignalBitKey)
    twoInputSignalValuesKey = twoInputSignalBitValues.values()
    twoInputSignalValuesBuffer = list(twoInputSignalValuesKey)         
    print('*** Update 2 **** signal: ', twoInputSignalBitBuffer, 'Value: ', twoInputSignalValuesBuffer)

    for x in range(0,len(twoInputSignalBitValues)):
        isCapital = IsCapitalInput(input1) 
        if isCapital:
            if (twoInputSignalBitBuffer[x].upper()) == input1:
                input1Values = twoInputSignalValuesBuffer[x]
                input1Values = InverseCapitalSignalInput(input1Values)
        else:
            if twoInputSignalBitBuffer[x] == input1:
                input1Values = twoInputSignalValuesBuffer[x]
                    
        isCapital = IsCapitalInput(input2) 
        if isCapital:
            if (twoInputSignalBitBuffer[x].upper()) == input2:
                input2Values = twoInputSignalValuesBuffer[x]
                input2Values = InverseCapitalSignalInput(input2Values)
        else:
            if twoInputSignalBitBuffer[x] == input2:
                input2Values = twoInputSignalValuesBuffer[x]
            
    for y in range(0,4):
        outputValues[y] = input1Values[y] | input2Values[y]
    print('i1: ', input1Values, 'i2: ', input2Values, ' Y: ', outputValues)
    
    maxChar = max(twoInputSignalBitValues.keys())
    print('largest char....', maxChar)

    keyInc = chr(ord(maxChar) + 1) 
    twoInputSignalBitValues.update({keyInc  : outputValues})

    print('2Bit OR Gate Final Output ---------\n', twoInputSignalBitValues)
    unUsedHighLogic2Bit.update({keyInc: outputValues})
    
    return unUsedHighLogic2Bit


#   3Bit OR Gate 
def ORGate3Bit(input1, input2):
    input1Values = [0,0,0,0,0,0,0,0]
    input2Values = [0,0,0,0,0,0,0,0]
    input3Values = [0,0,0,0,0,0,0,0]
    outputValues = [1,0,0,0,0,0,0,1]
    print('\n*********   OR GATE  3Bit   ************************\n')
    print('input-1: ', input1, 'input-2: ', input2)

    threeInputSignalBitKey = threeInputSignalBitValues.keys()
    threeInputSignalBitBuffer = list(threeInputSignalBitKey)
    threeInputSignalValuesKey = threeInputSignalBitValues.values()
    threeInputSignalValuesBuffer = list(threeInputSignalValuesKey)         
    print('*** Update 2 **** signal: ', threeInputSignalBitBuffer, 'Value: ', threeInputSignalValuesBuffer)
        
    for x in range(0,len(threeInputSignalBitValues)):
        isCapital = IsCapitalInput(input1) 
        if isCapital:
            if (threeInputSignalBitBuffer[x].upper()) == input1:
                input1Values = threeInputSignalValuesBuffer[x]
                input1Values = InverseCapitalSignal3Input(input1Values)
        else:
            if threeInputSignalBitBuffer[x] == input1:
                input1Values = threeInputSignalValuesBuffer[x]
                print('\ninput-1: ', input1, 'Match in bit: ', threeInputSignalBitBuffer[x],
                      'Value in Dic: ', threeInputSignalValuesBuffer[x], 'Value actual: ', input1Values,
                      '\nx -- ', x, 'Key - ', threeInputSignalBitBuffer[x]
                      )
                    
        isCapital = IsCapitalInput(input2) 
        if isCapital:
            if (threeInputSignalBitBuffer[x].upper()) == input2:
                input2Values = threeInputSignalValuesBuffer[x]
                input2Values = InverseCapitalSignal3Input(input2Values)
        else:
            if threeInputSignalBitBuffer[x] == input2:
                input2Values = threeInputSignalValuesBuffer[x]
          
    for y in range(0,8):
        outputValues[y] = input1Values[y] | input2Values[y]
    print('3i1: ', input1Values, '3i2: ', input2Values, ' 3Y: ', outputValues)

    maxChar = max(threeInputSignalBitValues.keys())
    print('largest char....', maxChar)

    keyInc = chr(ord(maxChar) + 1) 
    threeInputSignalBitValues.update({keyInc  : outputValues})
    
    print('3Bit OR Gate Final Output ---------\n', threeInputSignalBitValues)
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


def InverseCapitalSignal3Input(inputSignal):
    inputSignalBuf = inputSignal
    for x in range(0,8):
        print('input: ', inputSignalBuf[x], end=", ")
        if(inputSignalBuf[x] == 0):
            inputSignalBuf[x] = 1
        else:
            inputSignalBuf[x] = 0
        print('inverse: ', inputSignalBuf[x])
    return inputSignalBuf   
       

# Given 2 input bits string function: 1.) Compute outputValues variable from input 2.) Find unutiliued computed variable
def TwoInputBitFunc(sExample1Test1):
    Declare2InputSignalValues()
    i = 2   # e.g: because in "2 abBA" function logic sequence start from 2nd element
    k = 0           
    inputVariable = ["a", "b"]
    computedResult = np.array([0, 0, 0, 0])
    unusedOutputLogic = []

    print('2 bit Func called - Dictionary: ', twoInputSignalBitValues)
        
    for x in range(i, iTestLength, 2):
        inputVariable.insert(k,sExample1Test1[x])
        inputVariable.insert(k+1,sExample1Test1[x+1])
        print('x: ', x, ' - x+1: ', x+1)
        print(f'inp: {inputVariable[k]} - inp: {inputVariable[k+1]}')

        isANDGate = ANDGateInputCheck(inputVariable[k], inputVariable[k+1])
        isORGate = ORGateInputCheck(inputVariable[k], inputVariable[k+1])
        if isANDGate:
            computedResult = ANDGate2Bit(inputVariable[k], inputVariable[k+1])
        
        if isORGate:
            computedResult = ORGate2Bit(inputVariable[k], inputVariable[k+1])
        unUsedHighLogic2BitBuffer = UnusedTrueOutput2Bit(unUsedHighLogic2Bit)
        print('\n\n******************   Output  ***************************')
        print(f'Unused True output logic for "{sExample1Test1}" are {unUsedHighLogic2BitBuffer}')
        k=i
    

# Given 3 input bits string function: 1.) Compute outputValues variable from input 2.) Find unutilized computed variable
def ThreeInputBitFunc(sExample1Test1):
    Declare3InputSignalValues()
    i = 2   # e.g: because in "2 abBA" function logic sequence start from 2nd element
    k = 0           
    inputVariable = ["a", "b"]
    computedResult = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    unusedOutputLogic = []

    print('3 bit Func called - Dictionary: ', threeInputSignalBitValues)
        
    for x in range(i, iTestLength, 2):
        inputVariable.insert(k,sExample1Test1[x])
        inputVariable.insert(k+1,sExample1Test1[x+1])
        print('x: ', x, ' - x+1: ', x+1)
        print(f'inp: {inputVariable[k]} - inp: {inputVariable[k+1]}')

        isANDGate = ANDGateInputCheck(inputVariable[k], inputVariable[k+1])
        isORGate = ORGateInputCheck(inputVariable[k], inputVariable[k+1])
        if isANDGate:
            computedResult = ANDGate3Bit(inputVariable[k], inputVariable[k+1])
            unusedOutputLogic.append(UnusedTrueOutput3Bit(computedResult))
        
        if isORGate:
            computedResult = ORGate3Bit(inputVariable[k], inputVariable[k+1])
            unusedOutputLogic.append(UnusedTrueOutput3Bit(computedResult))
        print('\n\n******************   Output  ***************************')
        print(f'Unused True output logic for "{sExample1Test1}" are {unusedOutputLogic}')
        k=i

# Compute high/true logic occurence in unused remaining gate output
def UnusedTrueOutput2Bit(unUsedHighLogicInput):
    output = []
    highLogic = 0
    unUsedHighLogic = unUsedHighLogicInput
    unUsedHighLogicKey = unUsedHighLogic.keys()
    unUsedHighLogicKeyBuffer = list(unUsedHighLogicKey)
    unUsedHighLogicValues = unUsedHighLogic.values()
    unUsedHighLogicValuesBuffer = list(unUsedHighLogicValues)         
    print('%%%%%%% unUsed 2Bit %%%% signal: ', unUsedHighLogicKeyBuffer, 'Value: ', unUsedHighLogicValuesBuffer)

    for x in range(0,len(unUsedHighLogic)):
        if (sExample1Test1.find(unUsedHighLogicKeyBuffer[x]) == -1):
            temp = unUsedHighLogicValuesBuffer[x]  
            for y in range(0,4):
                if (temp[y]==1):
                    highLogic += 1
            output.append(highLogic)
            highLogic = 0
        print(f'Check --- Test: {sExample1Test1} highlogic: {highLogic}  \
                  Key: {unUsedHighLogicKeyBuffer[x]} Values: {unUsedHighLogicValuesBuffer[x]}')
    return output


def UnusedTrueOutput3Bit(input1):
    output = 0
    for x in range(0,8):
        if (input1[x]==1):
            output += 1
    return output

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


if __name__ == '__main__':

#   ************************** Test Solution *********************************
#   **************************************************************************
#   Example-1 Test-1
    sExample1Test1 = '2 abBA'
    # sExample1Test1 = '3 abAced'
    # sTest = '3 abAced
    # sExample1Test1 = '2 abABdcCD'
    iTestLength = len(sExample1Test1)
    sNoOfInputs = sExample1Test1[0]
    iNoOfInputs = int(sExample1Test1[0])
    # print('Input Number: ' + sNoOfInputs + ' - Test Length: ', iTestLength)
    # print('Input Number: ',  iNoOfInputs, ' - Test Length: ', iTestLength)
    
    if iNoOfInputs == 2:
        TwoInputBitFunc(sExample1Test1)
    if iNoOfInputs == 3:
        ThreeInputBitFunc(sExample1Test1)
        
    


