# HOME

Action

Place the cursor at the specified line at location 1.

Syntax

HOME UPPER | LOWER | THIRD | FOURTH

Remarks

If only HOME is used than the cursor will be set to the upper line.

You may also specify the first letter of the line like: HOME U

See also

[CLS](cls.md) , [LOCATE](locate.md)

For a complete example see [LCD](lcd_2.md)

Partial Example

Locate 2 , 1 'set cursor position

Lcd "*" 'display this

Home Upper 'select line 1 and return home