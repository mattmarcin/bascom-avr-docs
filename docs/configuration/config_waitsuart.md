# CONFIG WAITSUART

Action

Compiler directive that specifies that software UART waits after sending the last byte.

Syntax

CONFIG WAITSUART = value

Remarks

value | A numeric value in the range of 1-255. A higher value means a longer delay in mS.  
---|---  
  
When the software UART routine are used in combination with serial LCD displays it can be convenient to specify a delay so the display can process the data.

See also

[OPEN](open.md)

Example

See [OPEN](open.md) example for more details.