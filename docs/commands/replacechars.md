# REPLACECHARS

Action

Replace all occurrences of a character in a string by a different character.

Syntax

REPLACECHARS  string , old,new

Remarks

string | A string variable.  
---|---  
old | A character or byte with the ASCII value of the character to search for.  
new | A character of byte with the ASCII value with the new value.  
  
When we have a string with a content of : "abcdefabc" and we want to replace the "a" by an "A" we can use :

Replacechars string , "a" , "A" 

All occurrences are replaced. 

REPLACECHARS supports [$BIGSTRINGS](bigstrings.md)

See also

[INSTR](instr.md) , [MID](mid.md) , [CHARPOS](charpos.md) , [DELCHAR](delchar.md) , [INSERTCHAR](insertchar.md) , [DELCHARS](delchars.md)

Example

```vb
$regfile = "m644def.DAT"  
$hwstack = 24 'default use 32 for the hw stack  
$swstack = 24 ' default use 10 for the SW stack  
$framesize = 24 ' default use 40 for the frame  
  
Dim Textout As String * 22  
Dim Var As String * 1  
  
```
Textout = "abcdefabdef"  
Replacechars Textout , "a" , "A"  
Print Textout  
  
Var = "e"  
Replacechars Textout , Var , "A"  
```vb
Print Textout  
  
End

```