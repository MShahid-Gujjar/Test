# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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
    output = np.array([])
    isAlphabetCondition = ANDGateInputCheck(input1, input2)
    if isAlphabetCondition:
        listLength = len(valueInput1)
        for x in range(listLength):
            output.append(valueInput1[x] & valueInput2[x])
            print('x: ', output[x])


def ORGate(input1, input2):
    valueInput1 = [0,0,1,1]
    valueInput2 = [0,1,0,1]
    output = []
    isAlphabetCondition = ORGateInputCheck(input1, input2)
    if isAlphabetCondition:
        listLength = len(valueInput1)
        for x in range(listLength):
            output.append(valueInput1[x] | valueInput2[x])
            print('x: ', output[x])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# greater2 = ANDGateInputCheck('c', 'a')
# greater3 = ORGateInputCheck('d', 'e')

# input1 = 'k'
# inverseA = InvertInput(input1)
# input2 = 'k'
# inverseA = InvertInput(input1)

#   ************************** Test Solution *********************************
#   **************************************************************************
# Example-1 Test-1
test1 = '2 abBA'
testLength = len(test1)
noOfInputs = test1[0]
noOfInputsInt = int(test1[0])
print('Input Number: ' + noOfInputs + ' - Test Length: ', testLength)
print('Input Number: ',  noOfInputsInt, ' - Test Length: ', testLength)

i = 2
j = 3
k = 0
gates = []
inputVariable = []
signal1 = np.array([0, 0, 1, 1])
signal2 = np.array([0, 1, 0, 1])
signalInvert1 = np.array([1, 1, 0, 0])
signalInvert2 = np.array([1, 0, 1, 0])

for x in range(i, testLength, 2):
    inputVariable.append(test1[x])
    inputVariable.append(test1[x+1])
    print('x: ', x, ' - x+1: ', x+1)
    print(f'inp: {inputVariable[x]} - 1.) test: {test1[x]}')
    print(f'inp: {inputVariable[x+1]} - 1.) test: {test1[x+1]}')
    isANDGate = ANDGateInputCheck(inputVariable[x], inputVariable[x+1])
    if isANDGate:
        ANDGate(signal1, signal2)


ORGate('a', 'b')


