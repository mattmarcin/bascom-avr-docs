# PRINTBIN

Action

Print binary content of a variable to the serial port.

Syntax

PRINTBIN var [ ; varn] [;varn [,bytes]]

PRINTBIN #channel, var [; varn] [;varn [,bytes]]

Remarks

Var | The variable which value is send to the serial port.  
---|---  
varn | Optional variables to send.  
bytes | The number of bytes to send  
  
The channel is optional and intended to be used with the [OPEN](open.md) statement.

PRINTBIN is equivalent to PRINT CHR(byteVar);

Notice that the PRINT line is ending with ; to suppress the CR+LF to be send.

When you use a Long for example, 4 bytes are printed.

Multiple variables may be sent. They must be separated by the ; sign.

Just like PRINT the ; is used to separate the data. While INPUT/INPUTBIN uses a comma (,) to separate the data.

The number of bytes to send can be specified by an additional numeric constant. This is convenient when sending the content of an array.

Printbin ar(1) ; 3 ' will send 3 bytes from array ar(1) starting at index element 1.

Printbin ar(1) ; 2 ; ar(2) ; 4 ' will send 2 bytes from array ar1() starting at index 1, then 4 bytes from array ar() starting at index 2.

When you use Printbin ar(1) the whole array will be printed assuming that CONFIG BASE=1.

When you need to print the content of a big array(array with more then 255 elements) or with a data size that exceeds 255 bytes, you need to use the CONFIG PRINTBIN option.

Variable number of bytes

Since version 2082 you can use a variable to specify the number of bytes to send. In order to keep the syntax compatible with older compilers, you must use a comma followed by the number of bytes. The number of bytes can be either a numeric constant or a numerical integer value.

Printbin Z , 1 ; Ar(1 , 1) , Q

In this example we sent 1 byte of variable Z , followed by Q bytes from variable ar(). The number will depend on the value of the variable Q.

Another example:

Dim Array(10) As Byte, Bytes_to_send As Byte

Bytes_to_send = 8

Printbin Array(1) , Bytes_to_send ' this will send 8 bytes

Bytes_to_send = 6

Printbin Array(1) , Bytes_to_send ' this will send 6 bytes, you should use comma if number of bytes is specified with variable

RS-485

When the [CONFIG PRINT](configprint.md) option is used for RS-485, the direction pin will be used by PRINTBIN as well.

When RS-485 is used, the following will happen :

\- the direction pin is toggled

\- all variables are transmitted

\- a check if performed to ensure the last byte is transmitted

\- the direction pin is toggled again

See also

[INPUTBIN](inputbin.md) , [CONFIG PRINTBIN](config_printbin.md) , [CONFIG PRINT](configprint.md), [CONFIG INPUTBIN](config_inputbin.md)

Example

```vb
Dim A(10) As Byte, C As Byte

For C = 1 To 10

```
A(c)= c ' fill array

Next

Printbin A(1) 'print content of a(1). Note that the whole array will be sent!

End