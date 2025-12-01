# CONFIG ACAX|ACBX

Action

Configures the Analog Comparator of the Xmega.

Syntax

CONFIG ACXX = state, TRIGGER=trigger, HISPEED=speed, HYSMODE=hys , MUXPLUS=mp , MUXMIN=mm , OUTPUT=otp , SCALE=scale , WINDOW=w , WINTMODE = wint

Remarks

ACXX | The name of the Analog comparator : ACA0,ACA1, ACB0 or ACB1 Some XMEGA chips might not have (all) comparators.   
---|---  
State | ON or OFF. Select ON to turn the comparator on. By default it is off.  
HiSpeed | When ENABLED, the comparator hi speed mode is activated. Default mode is DISABLED.  
Trigger | Specifies which comparator event triggers the analog comparator interrupts. This options are : RISING, FALLING or BOTH / TOGGLE.  
Hysmode | To prevent quick toggling, a hysteresis is built in. You can chose the mode : \- OFF  \- SMALL  \- LARGE  
MuxPlus | This option controls which pin is connected to the positive input of the comparator. Possible values : 0-7, DAC. When you chose 7, DAC will also be used. So 7 and DAC are equivalent.  
MuxMin | This option controls which pin is connected to the negative input of the comparator. Possible values : 0-7, DAC, BANDGAP, SCALER. 0 - connects pin 0 1 - connects pin 1 2 - connects pin 3 ! 3 - connects pin 5 4 - connects pin 7 5 - connects the DAC output (same as DAC option) 6 - connects the BANDGAP voltage (same as BANDGAP option) 7 - connects the SCALER output (same as SCALE option)  
Output | Enabled or Disabled (default). When the output is enabled, the output of the comparator is routed to pin 7 of the port.  For ACA1 the output is routed to the AC1OUT pin if the Xmega supports this.  
Scale | The input voltage of the negative mux pin can be scaled. The scale value must be in range from 0-63. The scale output voltage is calculated as : (vcc * (scale+1)) / 64 Thus a value of 63 would give VCC. And 32 would give vcc/2  
Windows | Enabled or Disabled (default). When enabled, the two comparators of the port (ACA0 + ACA1) or (ACB0 + ACB1) form a window discriminator so you can control if a voltage is in the range of the lower and upper comparator.  
WintMode | The status register contains the window state. (bit 6 and 7). You can also fire an interrupt at one of the states: ABOVE : interrupt on signal above window INSIDE : interrupt on signal inside window BELOW : interrupt on signal below window OUTSIDE : interrupt on signal outside window  
  
A window is used in battery voltage meters. you could set the lower voltage to 12 V. And the upper voltage to 14 V.

```vb
If the voltage is inside this window : >=12V and <=14V then the battery is OK.

If the voltage is below the battery need to be charged.

If the voltage is above the window the battery if fully charged. The mentioned values are just an example.

```
See also

NONE

Example

```vb
'-----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-AC.bas  
' This sample demonstrates the Analog Comparator  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
'include the following lib and code, the routines will be replaced since they are a workaround  
$lib "xmega.lib"  
$external _xmegafix_clear  
$external _xmegafix_rol_r1014  
  
'First Enable The Osc Of Your Choice , make sure to enable 32 KHz clock or use an external 32 KHz clock  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
'setup comparator pin 0 and pin 1 are the input of portA. Pin 7 is an output in this sample  
Config Aca0 = On , Hysmode = Small , Muxplus = 0 , Muxmin = 1 , Output = Enabled  
  
  
  
Do  
Print Bin(aca_status)  
Print Aca_status.4 ' output ac0  
Waitms 1000  
Loop  
  


```