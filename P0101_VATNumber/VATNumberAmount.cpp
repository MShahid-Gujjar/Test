//  *****************************************************************************************
//  Class VATNumberAmount.cpp contains,
//    - Definition of functions declare in header file
//    - Perform all the logic call by main() functionto to implement tasks
//  *****************************************************************************************

#include "VATNumberAmount.h"

string VATNumberAmount::SetFileAddress(string fileAddress)
{
    return sFileAddressInput = fileAddress;
}

//  Parse all the receipts from the given .txt file. 
vector<string> VATNumberAmount::ParseReceiptFile(string fileAddress)
{
    int iReceiptNumber = 0;
    sFileAddressInput = fileAddress;
    fileRead.open(sFileAddressInput, ios::in | ios::out |ios::app);

    printf("\n*************  File Contents *************\n");
    
    if (!fileRead)
    {
        printf("\n---   Unable to open file   --- \
                 \nPlease check file name or file existence.\n\n");
        exit(1);
    }

    //  Parse file line by line and save in a string vector
    while (getline(fileRead, sFileContent, '\n'))
    {
        iReceiptNumber++;
        vParseReceiptNumber.push_back(sFileContent);
        cout << iReceiptNumber << ".) " << sFileContent << endl;
    }

    return vParseReceiptNumber;
}

//  Extract VATnumber and Amount from Receipt number and store them in a separate Array
void VATNumberAmount::ExtractVATNumberAmount(vector<string> receipts)
{
    for (int i = 0; i < vParseReceiptNumber.size(); i++)
    {
        sstrSeparation.str(vParseReceiptNumber[i]);

        //  Considering "Empty space" as a default separator between VATNumber and Amount in a Receipt 
        while (sstrSeparation >> sstrSub)                
        {
            if (iCount == 0)
                sVATNumber[iLines] = sstrSub;
            else
                sAmount[iLines] = sstrSub;

            iCount = iCount + 1;
            sstrSub = "";
        }

        iLines++;   //  Counter for lines or receipt number

        //  Necessary to "clear" for processing next line or receipt number
        sstrSeparation.clear();
        sstrSub = "";
        iCount = 0;
    }
}   

//  If VATNumber comprises of 8 digits then add "0" at first place from left as ninth digit
void VATNumberAmount::EightToNineDigitVATNumber(string vATnumber[], int lines)
{
    int iReceiptLength=lines;
    int iLenthVATNumber = 0;
    int Y = 0, S = 0;
    string sVATNumberBuf = "", sChanged="";
    stringstream sstrDisplay;
    bool bIsEightDigit = false;

    printf("\n\n*************  8 to 9 Digit VATNumber  *************\n");
    for (int i = 0; i < iReceiptLength; i++)
    {
        sVATNumberBuf = vATnumber[i];
        iLenthVATNumber = sVATNumberBuf.length();

        if (iLenthVATNumber == 8)
        {
            sVATNumberBuf = "0" + sVATNumberBuf;
            sChanged = "changed from 8 to 9 digit";
            bIsEightDigit = true;
        }
        sVATNumber[i]= sVATNumberBuf;

        //  Adding each receipt VATNumber into stringstream to print at once in end, 
        //  if there is a need to change from 8 to 9 digit
        sstrDisplay << i << ".) "
                    << sVATNumberBuf 
                    << "     "       << sChanged << endl;
        sChanged = "";
    }

    if (bIsEightDigit)
        cout << sstrDisplay.str();
    else
        cout << "\nNothing changed, every receipt number comprises of 9 digit.";

}

// Calculate the Amount according to prescribed logic
void VATNumberAmount::CalculateAmount(string vATnumber[], string amount[], int lines)
{
    int iReceiptLength = lines;
    int Y = 0, S=0, A=0, A1=0;
    int iLenthVATNumber = 0, iAmount=0, iAmountBuf = 0;
    string sVATNumberBuf = "", sAmount = "", sBuf="";
    bool bValidVAT = false;

    printf("\n\n*************  Calculate Amount *************\n");
    printf("\nVATNumber   -   Amount  -   S   -   Y   -   A1  -   Valid   \n");

    for (int i = 0; i < iReceiptLength; i++)
    {   
        sVATNumberBuf = vATnumber[i];
        sAmount = amount[i];
        iLenthVATNumber = sVATNumberBuf.length();

        // Calculate S for a given VAT number
        // Sequence numbering : A9A8A7A6A5A4A3A2A1 or A8A7A6A5A4A3A2A1
        // Formule for S = A1 * 0 + A2 *2 + A3 * 4 + A4 * 8 + A5 * 16 + A6 * 32 + A7 * 64 + A8 * 128 + A9 * 256
        for(int j=0; j<9; j++)
        {
            sBuf = sVATNumberBuf[j];
            if (j == 8) 
            {
                A1 = stoi(sBuf);
                S = S + (A1 * 0);
            }
            else
            { 
                A = stoi(sBuf);
                S = S + A * pow(2, (8-j));
            }
        }
        Y = S % 11;

        // Sum up amount of Valid VAT numbers
        if ((Y == 10 && A1 == 0) || (Y==A1))
        {
            sAmount = amount[i];
            iAmountBuf = stoi(sAmount);
            iAmount += iAmountBuf;
            bValidVAT = true;
        }
        cout << sVATNumberBuf << "        " << iAmount << "     " << S << "     "
             << Y << "      " << A1 << "            " << bValidVAT << endl;
        S = 0;
    }
    cout << "\n\nAmount: " << iAmount << endl;  //  Final result line

    //  Write Calculated amount of valid VATNumber into a txt file 
    
    //sFileAddressOutput ="C:\\Users\\mshah\\Documents\\Programming\\CPlusPlus\\VatNumberHirsch\\Tax.txt"
    sFileAddressOutput = "VATNumberReceiptValidOutput.txt";
    fileWrite.open(sFileAddressOutput, ios::in | ios::out);
    if (!fileWrite)
    {
        printf("\n---   Unable to open file   --- \
                 \nPlease check file name or file existence.\n\n");
        exit(1);
    }
    //fileWrite.seekp(ios::end);
    fileWrite << "\nSample Input from " << sFileAddressInput << endl;
    for(int i=0; i<vParseReceiptNumber.size(); i++)
    {
        fileWrite << vParseReceiptNumber[i] << endl;
    }
    fileWrite << "\nSample Output\n" << iAmount << endl;
    fileWrite.close();

    fileRead.close();

}
