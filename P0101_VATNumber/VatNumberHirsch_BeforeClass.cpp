//  *****************************************************************************************
//  Developer       : Muhammad Shahid
//  Creation Date   : 22-11-2022
//  Project Name    : P101 VAT number - HIRSCH Maschinenbau  
//  Task            : A text file with VAT number and amount in Cents are provided.
//                    Identify receipts of valid VAT number and sum up the amount in cents. 
//                    Discard the recipts with invalid VAT Number 
//  *****************************************************************************************

#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <sstream>
#include "VATNumberAmount.h"

using namespace std;

void EightToNineDigit(string vATnumber[], string amount[], int lines);
void CalculateAmount(string vATnumber[], string amount[], int lines);

const int iArrayRow = 100;
const int iArrayCol = 2;
string sVATNumberAmount[iArrayRow][iArrayCol] = {};
string sVATNumber[100] = { };
string sAmount[100] = { };

int main()
{
    int x, y, z;
    VATNumberAmount Vnac;
    Vnac.l = 1;
    Vnac.w = 2;
    Vnac.h = 3;

    x = Vnac.l;
    y = Vnac.w;
    z = Vnac.h;
    
    int r = Vnac.getVol(x, y, z);
    int r2 = Vnac.getVol2();
    cout << r <<" - " <<r2;

    string sFileContent, sFileAddress;
    string sLines[100] = { };
    string v, v1, a, a1, sstrSub;
    stringstream sstr;
    int iVATNumber[] = { 0 };
    int iAmount[] = { 0 };
    int iCount = 0, iLines=0;
    ifstream fileRead;

    sFileAddress = "VATNumberReceipt1.txt";
    fileRead.open(sFileAddress, ios::in);

    if (!fileRead)
        printf("\nUnable to open file");

    //while (fileRead >> sFileContent)
    while(getline(fileRead,sFileContent,'\n'))
    {
        printf("\nFile contents: ");
        cout << sFileContent;

        sstr << sFileContent;
        while(sstr>>sstrSub)
        {
            if (iCount == 0)
            {
                sVATNumber[iLines] = sstrSub;
                sVATNumberAmount[iLines][iCount] = sstrSub;
            }                
            else
            {
                sAmount[iLines] = sstrSub;
                sVATNumberAmount[iLines][iCount] = sstrSub;
            }
            cout << "\nVn: " << sVATNumber[iCount] << " mount: " << sAmount[iCount] << 
                 " Count :" <<iCount << " Lines:" << iLines;
            iCount = iCount + 1;
        }
        sstr.clear();
        sstrSub = "";
        iLines++;
        iCount = 0;
    }  
    int q = 2, w = 2, dec=0;
    q = q ^ 2;
    q = pow(2,5);
    printf("q: %i", q);
    for(int i=0; i<10; i++)
    { 
        q = pow(w, i);
        cout << "\ni: " << i << " w: " << q;
    }
    
    //EightToNineDigit(sVATNumber,sAmount, iLines);
    //CalculateAmount(sVATNumber, sAmount, iLines);
}

void EightToNineDigit(string vATnumber[], string amount[], int lines)
{
    int iReceiptLength=lines;
    int Y=0, S;
    int iLenthVATNumber = 0;
    string sVATNumber2 = "", sZero="0", sAmount="";

    for (int i = 0; i < iReceiptLength; i++)
    {
        sVATNumber2 = vATnumber[i];
        iLenthVATNumber = sVATNumber2.length();
        //printf("length: %i - string: %s \n", iLenthVATNumber, sVATNumber2);
        printf(" length: %i - string: %s \n", iLenthVATNumber, sVATNumber2.c_str());

        if (iLenthVATNumber == 8)
        {
            sVATNumber2 = "0" + sVATNumber2;
            cout << " Concate - " <<sVATNumber2;
        }
        sVATNumber[i]= sVATNumber2;
        //cout << " - 2D - " << sVATNumberAmount[i][0];
    }
}

void CalculateAmount(string vATnumber[], string amount[], int lines)
{
    int s =0;
    int iReceiptLength = lines;
    int Y = 0, S=0, A=0, A1=0;
    int iLenthVATNumber = 0, iAmount=0, iAmountBuf = 0;
    string sVATNumber2 = "", sZero = "0", sAmount = "", sBuf="";
    bool bValidVAT = false;

    for (int i = 0; i < iReceiptLength; i++)
    {   
        sVATNumber2 = vATnumber[i];
        sAmount = amount[i];
        //printf("\n*****************************************************"
        //        "Receipt No. -    VATNumber     -   Amount"
        //printf("\n   %i           %s                 %s     ", i, sVATNumber2.c_str(), sAmount.c_str());

        // Calculate S for a given VAT number
        for(int j=0; j<9; j++)
        {
            sBuf = sVATNumber2[j];
            if (j == 0)
            {
                A1 = stoi(sBuf);
                S = S + (A1 * 0);
                //cout << sVATNumber2[j];
                cout << "\nActual: " << sBuf;
                printf(" - i: %i A: %i - S: %i ", j, A1, S);
            }
            else
            {
                //A = int(sVATNumber2[j]);
                A = stoi(sBuf);
                S = S + A * pow(2, j);
                cout << "\nActual: " << sBuf;
                printf(" - i: %i A: %i - S: %i ", j, A, S);
            }
        }
        Y = S % 11;
        printf("\nResult: %i - %i - %i     ", i, S, Y);
        S = 0;

        // Sum up amount of Valid VAT numbers
        if (Y == 10 && A1 == 0)
        {
            sAmount = amount[i];
            iAmountBuf = stoi(sAmount);
            iAmount += iAmountBuf;
        }
        printf(" - iAmount: %i", iAmount);
    }
}   

