# INPUTBIN

Action

Read binary data from the serial port.

Syntax

INPUTBIN var1 [;bts] [,var2]

INPUTBIN #channel , var1 [,var2]

Remarks

var1 | The variable that is assigned with the characters from the serial port.  
---|---  
var2 | An optional second (or more) variable that is assigned with the data from the serial input stream.  
bts | Optional numeric variable that specifies how many bytes must be read. This optional variable must be placed after a semi colon delimiter (;)  
  
The channel need to be used in combination with [OPEN ](open.md)and the optional [CLOSE.](open.md)

The number of bytes to read depends on the variable you use.

When you use a byte variable, 1 character is read from the serial port.

An integer will wait for 2 characters and an array will wait until the whole array is filled.

Note that the INPUTBIN statement doesn't wait for a CRLF but just for the number of bytes.

You may also specify an additional numeric parameter that specifies how many bytes will be read. This is convenient when you are filling an array.

Inputbin ar(1) , 4 ' will fill 4 bytes starting at index 1.

In version 2083 the INPUTBIN statement is enhanced with an option to specify the number of bytes to read using a variable.

In earlier versions only a constant could be used. To keep code compatible, use a semi colon followed by a variable to specify how many bytes must be read.

Inputbin ar(1) , bts ' will fill the number of bytes equal with the value of bts

See also

[PRINTBIN](printbin.md) , [CONFIG INPUTBIN](config_inputbin.md)

Example

Dim A As Byte , C As Integer

Inputbin A , C 'wait for 3 characters and fill 2 variables

End