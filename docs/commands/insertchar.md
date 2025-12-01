# INSERTCHAR

Action

Inserts one character into a string.

Syntax

INSERTCHAR string, pos, char

Remarks

string | The string where the character is inserted to.  
---|---  
pos | The position where the character is inserted to. A value of 1 would make the character the first character of the string.  
char | A byte or string or string constant with the character that need to be inserted. For example you can use "A" to insert an "A", or use a byte with the value 65 to insert an "A". Or use a string. In case of a string, only the first character will be used.   
  
INSERTCHAR supports [$BIGSTRINGS](bigstrings.md)

See also

[DELCHAR](delchar.md) , [DELCHARS](delchars.md) , [INSTR](instr.md) , [MID](mid.md) , [CHARPOS](charpos.md) , [REPLACECHARS](replacechars.md)

Example

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' del_insert_chars.bas  
' This sample demonstrates the delchar, delchars and insertchar statements  
'-----------------------------------------------------------------  
$regfile="m88def.dat"  
$crystal = 8000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
dim s as string * 30  
```
s = "This is a test string" ' create a string  
delchar s, 1 ' remove the first char  
print s ' print it  
  
insertchar s,1, "t" ' put a small t back  
print s  
  
delchars s,"s" ' remove all s  
```vb
print s  
end

```
Example

```vb
'--------------------------------------------------------------------------------  
'name : str-test.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates some string routines  
'micro : mega4809  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "mx4809.dat"  
$crystal = 20000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
Config Sysclock = 16_20mhz , Prescale = 1 'set clock freq  
  
  
Dim S1 As String * 10  
Dim S2 As String * 10  
Dim S4 As String * 80  
  
```
S1 = "0123456789"  
S2 = "abcdefghij"  
Mid(s1 , 3 , 2) = "##" 'replace  
Mid(s1 , 13 , 2) = "**" 'try to do at an illegal position  
Mid(s1 , 0 , 2) = "**" 'try to do at an illegal position  
  
S1 = "0123456789"  
S2 = "abcdefghij"  
  
Mid(s1 , 3 ) = "#" 'replace  
Mid(s1 , 13 ) = "*" 'invalid  
  
S1 = "---"  
Mid(s1 , 1) = "ABC"  
  
S4 = "abcdefghijklm"  
Insertchar S4 , 0 , "*"  
Insertchar S4 , 1 , "*"  
Insertchar S4 , 20 , "*"  
  
Delchar S4 , 0  
Delchar S4 , 1  
Delchar S4 , 20  
  
End