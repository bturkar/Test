"""
**************************Types of Operator*************************
1-Arithmetic operators---------- +,-,*,/,%,//,**
2-Assignment operators---------- +=,-=,*=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=
3-Comparison operators---------- <=,>=,==,!=
4-Logical operators------------- and,or,not
5-Identity operators------------ is,is not
6-Membership operators---------- in, not in
7-Bitwise operators------------- &,|,^,~,<<,>>
-----------------------------------------------------------------------------------------------------------------------
4-Logical operators
   -----------------
  4.1 and ==> Ex=a=8,b=5  ==> a<9  and b<6 =o/p=True
  4.2 or ==> Ex=a=8,b=5  ==> a<9  or b<6 =o/p=True
  4.3 not ==> reversing operation ==> Ex. x=True ==> x=nor x  o/p==> False

------------------------------------------------------------------------------------------------------------------------
5-Identity operators
  ------------------
  x = ["apple", "banana"]
  y = ["apple", "banana"]
  z = x
  print(x is z) # returns True because z is the same object as x
  print(x is y) # returns False because x is not the same object as y, even if they have the same content
  print(x == y) # to demonstrate the difference between "is" and "==": this comparison returns True because x is
                  equal to y
------------------------------------------------------------------------------------------------------------------------
7-Bitwise operators
   --------------------
   7.1 & Ex.12&13 o/p==12   12==>00001100
                         &  13==>00001101
                            ---------------
                                 00001100 ==>12

   7.2 | ==> Same as above except or operation

   7.3 ^ ==>XOR operation  0 0==0     EX.12^13 o/p==1
                           0 1==1     Exp.12 = 00001100
                           1 0==1        ^13 = 00001101
                           1 1==0         ---------------
                                               00000001 ==>1

   7.4 ~ Ex.~12  o/p=-13
         12==>00001100==>1'S complement==>11110011
         -13==>00001101==>1's complement ==>11110010==>2's complement
         11110010
         +      1
         ---------
         11110011  ==>-13 ==>2's complement of 13=-13
        we always store positive number in system hence need to convert all
        negative values to positive bh using 2's compliment

   7.5 << ==> left ship operator  Ex. 10<<2 o/p=40 gaining
                                 Exp.10==  1010==>101000 add two 0 to left side (because 2 is given in question)
                                                  101000==32+8=40

   7.6 >> ==> right shift operator Ex. 10>>2 o/p=2   loosing
                                 Exp. 10== 1010==>10 ==> 2   neglect 2 bits from right (because 2 is given in question)

------------------------------------------------------------------------------------------------------------------------
            """