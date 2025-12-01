# BUFSPACE

Action

Returns the amount of free space of a serial buffer.

Syntax

Var = BufSpace(n)

Remarks

Var | A word or integer variable that is assigned with the free buffer space.  
---|---  
N | A constant in the range from 0-15. Odd numbers are for the INPUT buffers. Even numbers are for the OUTPUT buffers. A value of 0 : output buffer USART0 (first UART) A value of 1 : input buffer USART0 (first UART) A value of 2 : output buffer USART1 (second UART) A value of 3 : input buffer USART1 (second UART) A value of 4 : output buffer USART2  A value of 5 : input buffer USART2 A value of 6 : output buffer USART3 A value of 7 : input buffer USART3 A value of 8 : output buffer USART4 A value of 9 : input buffer USART4 A value of 10 : output buffer USART5 A value of 11 : input buffer USART5 A value of 12 : output buffer USART6 A value of 13 : input buffer USART6 A value of 14 : output buffer USART7 A value of 15 : input buffer USART7 The function will only work when the processor has the chosen UART and when it has been setup using CONFIG SERIAL.  
  
While serial buffers are great because you do not have to wait/block the processor, the buffer can become full when the micro has no time to empty the buffer. With the bufspace() function you can determine if there is still room in the buffer.

See Also

[CONFIG SERIAL](config_serialout.md) , [CLEAR](clear.md)

Example

'---------------------------------------------------------

NONE