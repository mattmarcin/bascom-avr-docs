# DELCHARS

Action

Delete all character from a string matching the provided character value.

Syntax

DELCHARS string, value

Remarks

string | The string where the characters are removed from.  
---|---  
value | The value of the character which must be removed from the string. You can use "A" to remove all capital A characters. Or you can pass a byte with the value of 65 to remove all characters with ASCII value 65 (A)  
  
Do not confuse with the DELCHAR statement which removes one character based on an index value.

DELCHARS removes ALL characters from a string matching value. 

DELCHARS also works with [$BIGSTRINGS](bigstrings.md)

See also

[DELCHAR](delchar.md) , [INSERTCHAR](insertchar.md) , [INSTR](instr.md) , [MID](mid.md) , [CHARPOS](charpos.md) , [REPLACECHARS](replacechars.md)

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