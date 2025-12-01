# STOP

Action

Stop the specified device. Or stop the program

Syntax

STOP device

STOP

Remarks

Device | TIMER0, TIMER1, COUNTER0 or COUNTER1, WATCHDOG, AC (Analog comparator power) , ADC(A/D converter power) or DAC(D/A converter)  
---|---  
XMEGA | For the Xmega you can also specify : DACA or DACB for the Digital/Analog Converters A and B.  
  
The single STOP statement will end your program by generating a never ending loop. When END is used it will have the same effect but in addition it will disable all interrupts.

The STOP statement with one of the above parameters will stop the specified device.

TIMER0 and COUNTER0 are the same device.

The AC and ADC parameters will switch power off the device to disable it and thus save power.

See also

[START](start.md) , [END](end.md)

Example

See [START](start.md) example