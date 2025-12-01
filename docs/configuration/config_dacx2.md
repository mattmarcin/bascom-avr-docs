# CONFIG DACX

Action

This statement configures the DAC0 or DACX in the Xtiny/Megax/AVRX.

Syntax

CONFIG DACx=dac, IO0=IO0, RUNMODE=runmode, OUT_ENABLE =out

Remarks

DACX | Chose either DAC0 or DACX.  
---|---  
dac | ENABLED or DISABLED. Chose ENABLED to enable the DAC.  
runmode | Possible values :  ENABLED : In Standby sleep mode, the peripheral continues operation DISABLED : In Standby sleep mode, the peripheral is halted  
Out | ENABLED or DISABLED. Chose ENABLED to enable the output. This will also set PORTA.6 to output mode. Notice that only DAC0 has the ability to drive an output pin. The output pin varies per processor. The compiler will use the proper pin.  
  
The DAC data register is available in the byte variable DAC0_DATA.

When present, the register names for DAC1 and DAC2 are : DAC1_DATA and DAC2_DATA.  
In version 2086 the WRITEDAC statement exist to write to the registers.

See also

[WRITEDAC](writedac.md)

Example

```vb
'--------------------------------------------------------------------------------  
'name : dac.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates DAC  
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
Config Sysclock = 20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
'configure the internal reference to be 1v1 for both the ADC and the DAC  
Config Vref = Dummy , Adc0 = 1v1 , Dac0 = 1v1  
  
'configure the DAC. We also drive the PA6 output pin  
Config Dac0 = Enabled , Out_enable = Enabled  
  
Print "Test DAC0"  
  
Do  
```
Dac0_data = Dac0_data + 10

```vb
' or use the WRITEDAC statement : WRITEDAC value  
Print "DAC0:" ; Dac0_data  
Waitms 100  
Loop  
  
End

```