# DELCHAR

Action

Delete one character from a string.

Syntax

DELCHAR string, pos

Remarks

string | The string where the character is removed from.  
---|---  
pos | The position where the character must be removed from. A value of 1 would remove the first character.  
  
Do not confuse with the DELCHARS statement which removes all characters based on a character value.

The DELCHAR removes one character from a string based on an index. 

DELCHAR supports [$BIGSTRINGS](bigstrings.md)

See also

[DELCHARS](delchars.md) , [INSERTCHAR](insertchar.md) , [INSTR](instr.md) , [MID](mid.md) , [CHARPOS](charpos.md) , [REPLACECHARS](replacechars.md)

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