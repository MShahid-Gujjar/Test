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
#include "VATNumberAmount.h"    //  To access VATNumberAmount class variables and functions

using namespace std;

int main()
{
    string sParseFileAddress, sFileAddressValidReceipt, sFileAddressInValidReceipt;
    vector<string> vReceiptNumber;

    VATNumberAmount TaxNumAmount;   //  VATNumberAmount class object instantiation

    sFileAddressValidReceipt = "VATNumberReceiptValid.txt";
    sFileAddressInValidReceipt = "VATNumberReceiptInValid.txt";
    sParseFileAddress = TaxNumAmount.SetFileAddress(sFileAddressValidReceipt);
    
    //  Parse all the receipts from the given .txt file - Receipts = VATNumber + Amount
    vReceiptNumber = TaxNumAmount.ParseReceiptFile(sParseFileAddress);

    //  Extract VATnumber and Amount from each Receipt and store them in a separate Array
    TaxNumAmount.ExtractVATNumberAmount(vReceiptNumber);

    //  If VATNumber comprises of 8 digits then add 0 as ninth digit
    TaxNumAmount.EightToNineDigitVATNumber(TaxNumAmount.sVATNumber, TaxNumAmount.iLines);

    // Calculate the Amount according to prescribed logic
    TaxNumAmount.CalculateAmount(TaxNumAmount.sVATNumber, TaxNumAmount.sAmount, TaxNumAmount.iLines);
}

