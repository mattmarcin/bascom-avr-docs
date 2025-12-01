# CmdSetFont

Action

Set up a custom font.

Syntax

CmdSetFont font, ptr 

Remarks

font | The bitmap handle from 0 to 14. Bitmap handle 15 can be used conditionally  
---|---  
ptr | The metric block address in RAM. 4 bytes aligned is required.  
  
CmdSetFont is used to register one custom defined bitmap font into the FT800 coprocessor engine. After registration, the FT800

co-processor engine is able to use the bitmap font with its co-processor command.

Details on how to set up custom font, please refer to ROM and RAM Fonts from FTDI's FT800 Series Programmer Guide.PDF

Example

' See demos - DigitTest.bas and FT800 Demo3.bas