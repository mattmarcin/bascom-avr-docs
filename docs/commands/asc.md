# ASC

Action

Assigns a numeric variable with the ASCII value of the first character of a string.

Syntax

var = ASC(string [,index])

Remarks

Var | Target numeric variable that is assigned.  
---|---  
String | String variable or constant from which to retrieve the ASCII value.  
Index | An optional index value. The index has a range from 1 to the length of the string. When no index is provided, the default value 1 will be used.  
  
Note that only the first character of the string will be used.

When the string is empty, a zero will be returned. 

ASCII stands for American Standard Code for Information Interchange. Computers can only understand numbers, so an ASCII code is the numerical representation of a character such as 'a' or '@' or an action of some sort. ASCII was developed a long time ago and now the non-printing characters are rarely used for their original purpose. Below is the ASCII character table and this includes descriptions of the first 32 non-printing characters. ASCII was actually designed for use with teletypes and so the descriptions are somewhat obscure. If someone says they want your CV however in ASCII format, all this means is they want 'plain' text with no formatting such as tabs, bold or underscoring - the raw format that any computer can understand. This is usually so they can easily import the file into their own applications without issues. Notepad.exe creates ASCII text, or in MS Word you can save a file as 'text only'

![ascii_table](ascii_table.png)

Extended ASCII

As people gradually required computers to understand additional characters and non-printing characters the ASCII set became restrictive. As with most technology, it took a while to get a single standard for these extra characters and hence there are few varying 'extended' sets. The most popular is presented below.

![ascii_table_ext](ascii_table_ext.png)

See also

[CHR](chr.md)

ASM

NONE

Example

```vb
'------------------------------------------------------------------------------  
'name : asc.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates ASC function  
'micro : Mega88  
'suited for demo : yes  
'commercial addon needed : no  
'------------------------------------------------------------------------------  
  
$RegFile = "m88def.dat" ' specify the used micro  
$crystal = 8000000 ' used crystal frequency  
$baud = 19200 ' use baud rate  
$hwstack = 32 ' default use 32 for the hardware stack  
$swstack = 10 ' default use 10 for the SW stack  
$framesize = 40 ' default use 40 for the frame space  
  
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
  
Dim A As Byte , S As String * 10 , idx as Byte  
Print "ASC demo"  
```
S = "ABC"  
A = Asc(s)  
```vb
Print A 'will print 65  
  
print "test with index"  
```
a= asc(s,0) : print a 'invalid range will return 0  
a= asc(s,2) : print a  
a= asc(s,100) : print a 'invalid range will return 0  
  
  
End