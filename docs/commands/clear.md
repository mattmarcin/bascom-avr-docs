# CLEAR

Action

Clear serial input or output buffer

Syntax

CLEAR bufname

Remarks

Bufname | Serial buffer name to clear.  SERIALIN, SERIALIN0 - COM1/UART0 input buffer SERIALIN1 - COM2/UART1 input buffer SERIALIN2 - COM3/UART2 input buffer SERIALIN3 - COM4/UART3 input buffer SERIALIN4 - COM5/UART4 input buffer SERIALIN5 - COM6/UART5 input buffer SERIALIN6 - COM7/UART6 input buffer SERIALIN7 - COM8/UART7 input buffer SERIALOUT,SERIALOUT0 - COM1/UART0 output buffer SERIALOUT1 - COM2/UART1 output buffer SERIALOUT2 - COM3/UART2 output buffer SERIALOUT3 - COM4/UART3 output buffer SERIALOUT4 - COM5/UART4 output buffer SERIALOUT5 - COM6/UART5 output buffer SERIALOUT6 - COM7/UART6 output buffer SERIALOUT7 - COM8/UART7 output buffer  
---|---  
  
When you use buffered serial input or buffered serial output, you might want to clear the buffer.

While you can make the head pointer equal to the tail pointer, an interrupt could be active which might result in an update of the buffer variables, resulting in an unexpected result.

The CLEAR statement will reset the head and tail pointers of the ring buffer, and it will set the buffer count variable to 0. The buffer count variable is new and introduced in 1.11.8.3. It counts how many bytes are in the buffer.

The internal buffercount variable is named _RS_BUFCOUNTxy , where X is R for Receive, and W for Write, and y is 0 for the first UART, and 1 for the second UART.

See also

[CONFIG SERIALIN](config_serialin.md), [CONFIG SERIALOUT](config_serialout.md)

ASM

Calls _BUF_CLEAR from MCS.LIB

Example

CLEAR SERIALIN