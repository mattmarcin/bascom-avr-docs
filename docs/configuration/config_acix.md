# CONFIG ACX

Action

Configures the Analog Comparator of the Xtiny.

Syntax

CONFIG ACX = state, RUNMODE=runmode, OUTPUT=otp ,TRIGGER=trigger, LOW_POWER=lowpow, HYSMODE=hys , MUX_INVERT=muxinv , MUXMIN=muxmin , MUXPOS=muxpos

Remarks

ACIX | The name of the Analog comparator : AC0,AC1, AC2. Some XTINY processors have multiple comparators.   
---|---  
State | ON or OFF. Select ON to turn the comparator on. By default it is OFF.  
Runmode | Possible values :  ENABLED : In Standby sleep mode, the peripheral continues operation DISABLED : In Standby sleep mode, the peripheral is halted  
Trigger | Specifies which comparator event triggers the analog comparator interrupts. This options are : RISING, FALLING or BOTH.  
Hysmode | To prevent quick toggling, a hysteresis is built in. You can chose the mode : \- OFF  \- 10 (10 mV) \- 25 (25 mV) \- 50 (50 mV)  
lowpow | ENABLED or DISABLED. When you enable this mode the current through the comparator is reduced. It reduces power consumption but increase the reaction time of the comparator.   
Muxinv | ENABLED or DISABLED (default) When enabled the output of the AC is inverted. This effectively inverts the input to all the peripherals connected to the signal, and also affects the internal status signals.  
Output | ENABLED or DISABLED (default). When the output is enabled, the output of the comparator is routed to the output pin of the port.   
muxmin | Negative input MUX selection. Possible values : \- AINN0 : negative pin 0 \- AINN1 : Negative pin 1 \- VREF : voltage reference \- DAC : DAC output  
muxpos | Positive input MUX selection. Possible values : \- AINP0 : positive PIN 0 (default) \- AINP1 : positive pin 1  
  
See also

NONE

Example