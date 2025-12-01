# UPPERLINE

Action

Reset LCD cursor to the upper line.

Syntax

UPPERLINE

Remarks

Optional you can also use the LOCATE statement.

See also

[LOWERLINE](lowerline.md) , [THIRDLINE](thirdline.md) , [FOURTHLINE](fourthline.md) , [LCD](lcd_2.md), [CLS](cls.md) , [LOCATE](locate.md)

Example

Dim A As Byte

A = 255

Cls

Lcd A

Thirdline

Lcd A

Upperline

End