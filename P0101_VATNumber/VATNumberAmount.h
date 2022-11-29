//  *****************************************************************************************
//  Header file of class VATNumberAmount.cpp, contains variables and functions declarations 
//  *****************************************************************************************

//#pragma once

#ifndef VATNumberAmount_H
#define VATNumberAmount_H

#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <string.h>

using namespace std;

class VATNumberAmount
{
public:

    string sFileContent, sFileAddressInput, sFileAddressOutput;
    string sLines[100] = { };
    string sstrSub;
    string sVATNumberAmount[15][2];
    string sVATNumber[100] = { };
    string sAmount[100] = { };

    stringstream sstrSeparation;
    int iCount = 0, iLines = 0;
    fstream fileRead;
    fstream fileWrite;
    string sFileRW;
    vector<string> vParseReceiptNumber;

	vector<string> ParseReceiptFile(string fileAddress);
    string SetFileAddress(string fileAddress);
    void ExtractVATNumberAmount(vector<string> receipts);
    void EightToNineDigitVATNumber(string vATnumber[], int lines);
    void CalculateAmount(string vATnumber[], string amount[], int lines);
};

#endif // !VATNumberAmount_H
