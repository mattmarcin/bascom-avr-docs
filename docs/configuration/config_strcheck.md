# CONFIG STRCHECK

Action

Configures string check

Syntax

CONFIG STRCHECK = ON|OFF

Remarks

By default the string check is OFF. You can turn it on for additional string overwrite checking.

Why is it a problem to overwrite a string? A string is in fact a series of bytes that end with a null byte. For this reason a string always uses one more byte than it can store.

DIM S As string * 4 , can hold 4 characters. The internal size is 5 bytes. The extra byte could store the size too, but the advantage of using 0 strings is that you can DIM a large string say 1000 bytes, and still need 1 byte to mark the end. And as always there is a disadvantage too : you can not store a character with a 0 value since it marks the end. 

Consider code like this : 

Dim S as String * 4, b as byte, Z as string * 10 

The data is stored after each other. When you write a too long string to S, you will overwrite the variable B since it is allocated after the string S.

In some cases the compiler can check if you overwrite a string. For example when you assign a constant to a string that is too small to hold the content.

You always get an error in such a case. For example : S = "abcd" is ok, but S="abcdE" will give an error.

The problem is when you use another string to assign a string. Code like this :

Z="abcdefg" : S = Z 

This will overwrite B.

For this purpose the CONFIG STRCHECK=ON can be used.

It will use an alternative piece of code that will check against overwriting. 

When a string will not fit, only the part that will fit will be assigned. 

So this option can give unexpected results as well. But at least no other data will be overwritten.

As the example will show it is still not always possible to guard against overwriting of strings.

Example

```vb
'--------------------------------------------------------------------------------  
'name : string-check.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates string overwrite protection  
'micro : avrDA28  
'suited for demo : no  
'commercial addon needed : yes but change the DAT file to test with any other micro  
'--------------------------------------------------------------------------------  
$regfile = "avrx128da28.dat"  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
'$bigstrings  
  
```
Const Cigoneerror = 1 'make 1 to compile without errors  
Const Cstrcheck = 1 'check strings for overwrite  
Const Cspeclen = 1 'specify length for better checking  
  
```vb
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1 'select system clock and frequency  
  
Config Osc = Enabled, FREQUENCY=24MHZ  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  

#if Cstrcheck  
Config Strcheck = On 'when ON there will be a check so memory is not overwritten. it will create slightly mode code since  
'the size must be passed and checked  

#endif  
Dim Bdummy As Byte 'Xtiny and Xmega auto create internal variables after the first DIM  
dim idx as byte 'index for array  
dim sTarget as string * 10 'this is a string we are going to assign  
Dim Bbeyond As Byte 'put a byte here  
dim sSource as string * 20 'this is the source string  
dim sAr(5) as string * 10 'test an array as well  
  
```
Const Csomestring10 = "0123456789" ' a test constant  
Const Csomestring11 = Csomestring10 + "A" ' and one string 1 byte longer  
Const Csomestring20 = "0123456789abcdefghij" ' a test constant  
```vb
'by default there is no protection against string overwrites. This is because the first processors had little RAM.  
'using large strings on them was not possible. A string is just an array of bytes with a zero byte at the end.  
'for this reason a string can not hold a 0 value.  
'A string always takes 1 more byte in memory than the length of the actual string  
'The length info is not stored inside the string. This has pros and cons. The pro is that you can DIM a string longer than 255 bytes and it will  
'still work. The con is that when you pass strings to sub routines and functions, the maximum length is not passed a long. So there is no check possible.  
  
'first assigna value to bBeyond which is located after the string we assign  
```
Bbeyond = 123 ' the idea is that this remains 123  
  
'There can be a number of problems.  
Starget = Csomestring10 ' this should be fine  

#if Cigoneerror = 0  
Starget = Csomestring11 'here you get an error 119 since you assign a constant with a known length that is too long to fit  

#ENDIF  
  
Ssource = Csomestring11 ' this is no problem since it will fit  
Starget = "a" + Starget ' this is a problem since this will write beyond the string  
  
print bBeyond  
Bbeyond = 123 'the idea is that this remains 123  
  
'--- array test ---  
sAr(2)="0123456789" 'create a string and check if it is not overwritten  
Idx = 1 : Sar(idx) = "ABC" : Sar(idx) = Sar(idx) + Csomestring10 'lets check if it works for arrays as well  
print bBeyond  
Bbeyond = 123 'the idea is that this remains 123  
  

```vb
#if Cspeclen  
declare sub somesub(byval s1 as string * 10,s2 as string * 10)  

#else  
Declare Sub Somesub(byval S1 As String , S2 As String)  

#endif  
declare function myfunc() as string  
  
```
sSource= csomestring11  
Somesub Ssource , Ssource  
```vb
'somesub csomestring11 ,sSource 'will create error in case length is specified  
print bBeyond  
  
```
sTarget=Myfunc()  
print bBeyond  
  
sSource= csomestring20  
Idx = 15 : Starget = Left(ssource , Idx) 'check this too  
  
```vb
end  
  
's1 passed by value, s2 by reference  

#if cSpecLen  
sub somesub(byval s1 as string * 10,s2 as string * 10)  

#else  
sub somesub(byval s1 as string,s2 as string)  

#endif  
```
local test as byte  
test=123  
  
sTarget=s1  
print bBeyond  
bBeyond=123 'the idea is that this remains 123  
  
starget=s2  
print bBeyond  
  
s1="aa"  
s1=s1+csomestring10  
```vb
'when you watch the local test value you will see it is overwritten.  
'so here is a potential problem too  
end sub  
  
  
function myfunc() as string  

#IF cIgoneError=0  
```
myfunc = csomestring11 'this will give an error  

#endif  
myfunc= "a" 'this will work  
myfunc=myfunc + csomestring10 'but here we have a problem !!!  
```vb
'despite the test enabled, we can not know the actual size since  
'this means that when you assign a string with a user string function you need to be careful  
end function

```