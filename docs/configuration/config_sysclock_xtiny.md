# CONFIG SYSCLOCK XTINY

Action

Selects the oscillator source for the system clock.

Syntax

CONFIG SYSCLOCK=sysclock ,  PRESCALE=prescale , CLOCKOUT=clockOtp, CLOCKOUT_PIN=pinmode

Remarks

SYSCLOCK | The oscillator used for generation of the system clock. This oscillator must be running.  Possible values: \- 16_20MHz : internal 20 MHz oscillator or 16 MHz oscillator. This depends on the fuse you set. \- 32KHz_INT : internal ultra low power oscillator \- 32KHz_EXT : 32 Khz external crystal oscillator \- EXTERNAL : external clock  
---|---  
PRESCALE | The Xtiny can divide the oscillator clock with the following values : 1,2,4,8,10,12,16,24,32,48 and 64.  
|   
CLOCKOUT | The Xtiny can route the clock output to a pin. Select ENABLED or DISABLED. Even in input mode the clock signal will be present on the designated pin. But the signal is best when the pin is set to output mode.  
CLOCKOUT_PIN | This option will set the CLOCKOUT put pin into output mode. The only possible value is : OUTPUT  
  
When using the CLOCKOUT option you can either set the output pin yourself into output mode or use the CLOCKOUT_PIN opiont.

Some processors do not have the CLOCKOUT pin. For these processors this option is not present in the DAT files.

See also

NONE

Example

```vb
'--------------------------------------------------------------------------------  
'name : serial-osc.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates USART  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atXtiny816.dat"  
$crystal = 20000000  
$hwstack = 16  
$swstack = 16  
$framesize = 24  
  
'set the system clock and prescaler  
'the clockout_pin is PB.5  
Config Sysclock = 16_20mhz , Prescale = 1 , Clockout = Enabled , Clockout_pin = Output  
  
'configure the USART

'use calibrated offset to compensate the BAUD  
Config Com1 = 250000 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1 , Baud_offset = Osc20_5v  
  
Waitms 2000  
  
Print "Test USART"  
Dim B As Byte  
  
Do  
Print "this is a baud test"  
Print Hex(clkctrl_osc20mcaliba)   
```
B = Inkey()  
If B = "+" Then  
Cpu_ccp = &HD8  
Incr Clkctrl_osc20mcaliba  
Elseif B = "-" Then  
Cpu_ccp = &HD8  
Decr Clkctrl_osc20mcaliba  
```vb
End If  
Waitms 500  
Loop  
  


```