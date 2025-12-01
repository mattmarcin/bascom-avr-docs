# SHIFTLCD

Action

Shift the LCD display left or right by one position.

Syntax

SHIFTLCD LEFT / RIGHT

Remarks

NONE

See also

[SHIFTCURSOR](shiftcursor.md) , [SHIFTCURSOR](shiftcursor.md) , [INITLCD](initlcd.md) , [CURSOR](cursor.md)

Partial Example

Cls 'clear the LCD display

Lcd "Hello world." 'display this at the top line

Wait 1

Lowerline 'select the lower line

Wait 1

Lcd "Shift this." 'display this at the lower line

```vb
Wait 1

For A = 1 To 10

```
Shiftlcd Right 'shift the text to the right

```vb
Wait 1 'wait a moment

Next

For A = 1 To 10

```
Shiftlcd Left 'shift the text to the left

```vb
Wait 1 'wait a moment

Next

```
Locate 2 , 1 'set cursor position

Lcd "*" 'display this

Wait 1 'wait a moment

Shiftcursor Right 'shift the cursor

Lcd "@" 'display this