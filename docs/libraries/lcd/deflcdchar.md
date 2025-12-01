# DEFLCDCHAR

Action

Define a custom LCD character.

Syntax

DEFLCDCHAR char,r1,r2,r3,r4,r5,r6,r7,r8

Remarks

char | Constant representing the character (0-7).  
---|---  
r1-r8 | The row values for the character.  
  
You can use the [LCD designer](tools_lcd_designer.md) to build the characters.

\- It is important that a CLS follows the DEFLCDCHAR statement(s).

So make sure you use the DEFLCDCHAR before your CLS statement.

\- When using INITLCD make sure this is called before DEFLCDCHAR since it will reset the LCD controller.

Special characters can be printed with the [Chr](chr.md)() function.

LCD Text displays have a 64 byte memory that can be used to show your own custom characters. Each character uses 8 bytes as the character is an array from 8x8 pixels. You can create a maximum of 8 characters this way. Or better said : you can show a maximum of 8 custom characters at the same time. You can redefine characters in your program but with the previous mentioned restriction.

A custom character can be used to show characters that are not available in the LCD font table. For example a Ã.

You can also use custom characters to create a bar graph or a music note. 

Note:

You cannot use Chr(0)-Deflcdchar 0 in any with any String Variables/Arrays, Chr(0) will be interpreted as a String terminator 

and not as Custom Character for Deflcdchar 0 (Deflcdchar from 1 to 7 is fine).

See also

[Tools LCD designer](tools_lcd_designer.md) , [LCD](lcd_2.md) , [CLS](cls.md) , [CURSOR](cursor.md) , [DISPLAY](display.md) , [LOCATE](locate.md)

Partial Example

Deflcdchar 1 , 225 , 227 , 226 , 226 , 226 , 242 , 234 , 228 ' replace ? with number (0-7)

Deflcdchar 0 , 240 , 224 , 224 , 255 , 254 , 252 , 248 , 240 ' replace ? with number (0-7)

Cls 'select data RAM

Rem it is important that a CLS is following the deflcdchar statements because it will set the controller back in datamode

Lcd Chr(0) ; Chr(1) 'print the special character