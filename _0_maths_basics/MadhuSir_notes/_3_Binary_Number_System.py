''''''
'''
Decimal to Binary:
===================
Integer  : 137
Convert to binary===>  2| 137
                       2| 68 - 1
                       2| 34 - 0
                       2| 17 - 0 
                       2|  8 - 1 
                       2|  4 - 0
                       2|  2 - 0
                        |  1 - 0           Binary format - 10001001
 
 
 
Binary to Decimal:
=================== 
Given binary  number                :  1  0  0  0  1  0  0  1 
                                       -----------------------
position(0-7) left to right :          7  6  5  4  3  2  1  0 
                                      2  2  2  2  2  2  2  2  
Whereever 1 exists,calcuate power : ----------------------------   
                                    128  0  0  0  8  0  0  1  ==> sum => 137
                                   -----------------------------            
                                                           
'''
'''
79==   2|79|
       2|38|1
       2|19|0
       2|9|1
       2|4|1
       2|2|0
       |1|0
       Binary format= 1001101
       1  0  0  1  1  0  1
       6  5  4  3  2  1  0
      2  2  2  2  2  2  2 
--------------------------------
    64  0  0  8  4  2  1==sum=79
       
       
       
       1s complement= 0110010
       2s complement= 1001110


'''
'''
ADDED NOTES
**********Code for Decimal to binary**************
n=int(input('Enter a number to convert into  binary  : '))
def decimalToBinary(n):
    if n>1:
        decimalToBinary(n//2)
    print(n % 2, end=' ')
decimalToBinary(n)
-------------------------------------------------------------------------
*******************code for Binary to Decimal**********
n=int(input('Enter a number to convert into decimal  : '))
def bintodec(n):
    dec=0
    i = 0

    while n!=0:
        d=n%10
        dec=dec+d*pow(2,i)
        n=n//10
        i+=1
    print(dec)
bintodec(n)
--------------------------------------------------------------------------------
'''