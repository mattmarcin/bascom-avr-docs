# CONFIG TCD0

Action

This configuration statement configures timer TCD0 found in the XTINY.

Syntax

CONFIG TCD0=mode, PRESCALE=prescale , CLOCK_SOURCE=clock_source , SYNC_PRESCALER=sync_prescaler, RUN=run , CMPD_SEL=cmpd_sel , 

CMPC_SEL=cmpc_sel, FIFTY=fifty , AUT_UPDATE=auto_update , CMP_OVR=cmp_over , CMP_VAL=cmp_val , 

EVENTA_CONFIG=eventA_config , EVENTB_CONFIG=eventb_config , EVENTA_ACTION=eventa_action , EVENTB_ACTION=eventb_action ,

EVENTA_TRIG=eventa_trig, EVENTB_TRIG=eventb_trig , TRIGA_INT=triga_int , TRIGB_INT=trigb_int , OVF_INT=over_int , 

INP_MODEA=inp_modea ,INP_MODEB=inp_modeb ,CMPAEN=cmpaen, CMPBEN=cmpben ,CMPCEN=cmpcen ,CMPDEN=cmpden, 

CMPA=cmpa, CMPB=cmpb , CMPC=cmpc ,CMPD=cmpd, DLY_PRESCALER=dly_prescaler , DLY_TRIGGER=dly_trigger

DLY_SEL=dly_sel ,DLY_VAL=dly_val , DIT_CTRL=dit_ctrl , DIT_VAL=dit_val , 

DIS_EOC=dis_eoc , SOFT_CAPB=soft_capb , SOFT_CAPA=soft_capa , RESTART_STROBE=restart_strobe , SYNC_STROBE=sync_strobe, 

SYNC_EOC=sync_eoc

Remarks

The timer TCD0 is found in a number of XTINY processors.

The TCD0 is is a 12 bit timer with the following capabilities :

â¢ 12-bit timer/counter

â¢ Programmable prescaler

â¢ Double buffered compare registers

â¢ Waveform generation

â One ramp mode

â Two ramp mode

â Four ramp mode

â Dual-slope mode

â¢ Two separate input capture, double buffered

â¢ Connection to event system

â Programmable filter

â¢ Conditional waveform on external events

â Fault handling

â Input blanking

â Overload protection function

â Fast emergency stop by hardware

â¢ Supports both half bridge and full bridge output

You best read that before you use the timer.

After reading the data sheet the following options will make more sense.

mode | This options sets the Timer wave generation mode. Possible values : \- ONE_RAMP : One ramp mode \- TWO_RAMP : Two ramp mode \- FOUT_RAMP : Four ramp mode \- DUAL_SLOPE : dual slope mode \- A value between 0-3 will load the mode.   
---|---  
PRESCALE | The counter prescaler selects the division factor of the TCD counter clock. Possible values : \- 1 , 4 and 32  
CLOCK_SOURCE | The clock source for the TCD clock \- OSC16_20MHZ : the internal 16/20 MHz oscillator \- EXTERNAL : an external clock signal \- SYSTEM : system clock  
SYNC_PRESCALER | The synchronization prescaler select the division factor of the TCD clock.  Possible values : 1, 2 , 4 and 8  
RUN | This enables or disables the timer. Possible values : ENABLED : TCD is enabled and running DISABLED : TCD is disabled  
CMPD_SEL | Compare D output select \- PWMA : Waveform A \- PWMB : Waveform B  
CMPC_SEL | Compare C output select \- PWMA : Waveform A \- PWMB : Waveform B  
FIFTY | Fifty percent waveform.  \- ENABLED : chose this when two waveforms have identical characterics. This will cause any values written to CMPBSET/CLR register also to be written to register CMPASET/CLR  
AUT_UPDATE | Automatic Update. ENABLED : A synchronization at the end of the TCD cycle is automatically requested after the compare B Clear High register (CMPBCLRH) is written, DISABLED : no sync   
CMP_OVR | Compare output value override.  ENABLED : default values of the waveform outputs A and B are overridden by the values written in the compare X value in active state bit fields in the control D register CTRLD.CMPnxVAL. DISABLED : no action  
CMP_VAL | The CMPVAL register contains compare values for compare A and B. This is only used when CMP_OVR is enabled. A numeric value must be used between 0-255. The upper nible writes to CMPBVAL. The lower nibble writes to CMPAVAL. | CMPxVAL | A_off | A_on | B_off | B_on  
---|---|---|---|---  
PWMA | CMPAVAL[0] | CMPAVAL[1] | CMPAVAL[2] | CMPAVAL[3]  
PWMB | CMPBVAL[0] | CMPBVAL[1] | CMPBVAL[2] | CMPBVAL[3]  
  
In One Ramp mode, PWMA will only use A_off and A_on values and PWMB will only use B_off and B_on values.

This is due to possible overlap between the values A_off, A_on, B_off and B_on.  
  
| The following config options are intended to be used alone. For example : config tcd0=mode,DIS_EOC=ENABLED The datasheet does not make it clear if these commands can be combined.   
DIS_EOC | Disable at end of TCD cycle strobe. When ENABLED the ENRDY bit in TCD0_STATUS will keep low until the TCD is disabled. Writing to this bit only has effect if there no ongoing synchronization of Enable. (RUN=ENABLED) The ENRDY bit tells when the ENABLE value is synchronized to the TCD domain and is ready to be written again. The following clears the ENRDY bit :  \- writing to the ENABLE bit (RUN=ENABLED|DISABLED) \- DIS_EOC strobe=ENABLED  
SOFT_CAPB | Software Capture B strobe. When ENABLED a software capture to capture register B is done as soon as the strobe is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
SOFT_CAPA | Software Capture A strobe. When ENABLED a software capture to capture register A is done as soon as the strobe is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
RESTART_STROBE | Restart Strobe. When ENABLED a restart of the TCD counter is executed as soon as this bit is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
SYNC_STROBE | Synchronize Strobe When ENABLED the double buffered registers will be loaded to the TCD domain as soon as this bit is synchronized to the TCD domain. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
SYNC_EOC | Synchronize end of TCD cycle strobe. When ENABLED the double buffered registers will be loaded to the TCD domain at the end of the next TCD cycle. Writing to this bit only has effect if there is no ongoing synchronization of a command. See also CMDRDY bit in TCD.STATUS.  
|   
EVENTA_CONFIG EVENTB_CONFIG | Event A|B configuration. When the Input Capture Noise canceler is activated (FILTERON), the Event input is filtered. The filter function requires four successive equal valued samples of the Retrigger pin for changing its output. The Input Capture is therefore delayed by four clock cycles when the noise canceler is enabled. When the Asynchronous Event is enabled (ASYNCON), the Event input will qualify the output directly. Possible values : \- NEITHER : Neither Filter nor Asynchronous Event is enabled. \- FILTER_ON : Input Capture Noise Cancellation Filter enabled. \- ASYNC_ON : Asynchronous Event output qualification enabled.  
EVENTA_EDGE EVENTB_EDGE | Edge Selection This bit is used to select the active edge or level of the event interrupt \- FALL_LOW : The falling edge or low level of the Event input generates Retrigger or Fault action. \- RISE_HIGH : The rising edge or high level of the Event input generates Retrigger or Fault action.  
EVENTA_ACTION EVENTB_ACTION | Event Action. This bit enables Capture on Event input. By default, the input will trigger a Fault, depending on the Input x register input mode (TCD.INPUTx). It is also possible to trigger a Capture on the Event input. Possible values :  \- FAULT : FAULT Event triggers a Fault. \- CAPTURE : CAPTURE Event triggers a Fault and Capture.  
EVENTA_TRIG EVENTB_TRIG | Trigger Event Input Enable This options enabled or disables the Event as a trigger to input A|B  
TRIGA_INT TRIGB_INT OVF_INT | Interrupts can be enabled/disabled by using the ENABLE and DISABLE statements. Using the timer interrupt names you can also enable/disable them using the CONFIG statement. \- ENABLED : the interrupt will be enabled \- DISABLED : the interrupt is disabled TRIGA_INT : event is executed when trigger input A is received TRIGB_INT : event is executed when trigger input B is received OVF_INT : event is executed when the timer overflows or restarts  
INP_MODEA INP_MODEB | Input mode options. Possible values : \- NONE : input has no action \- JMPWAIT : stop output, jump to opposite compare cycle and wait \- EXECWAIT : stop output, execute opposite compare cycle and wait \- EXECFAULT : stop output , execute opposite compare cycle while fault active \- FREQ : stop all outputs, maintain frequency \- EXECDT : stop all outputs, execute dead time while fault active \- WAIT : stop all outputs, jump to next compare cycle and wait \- WAITSW : stop all outputs, wait for software action \- EDGETRIG : stop all output on edge, jump to next compare cycle \- EDGETRIGFREQ : stop output on edge, maintain frequency \- LVLTRIGFREQ : stop output at level, maintain frequency  
CMPAEN CMPBEN CMPCEN CMPDEN | Compare Enable output pin.  ENABLED : The compare output pin is enabled. DISABLED : The compare output pin disabled (no output) At reset the settings are loaded from FUSE.TCDFG. So configuration should not be required.  
CMPA CMPB CMPC CMPD | Compare value. These bits set the default state from Reset or when a input event triggers a fault causing changes to the output. At reset the content is kept and during the reset sequence loaded from the TCD configuration fuse so configuration should not be required. ENABLED : set the bit to 1. DISABLED : reset the bit to 0.  
DLY_PRESCALER | Delay Prescaler. This option controls the prescaler setting for the blanking or output event delay Possible prescaler values : 1,2,4 and 8  
DLY_TRIGGER | Delay Trigger. These option control what should trigger the blanking or output event delay. \- CMPASET : CMPASET triggers delay \- CMPACLR : CMPACLR triggers delay \- CMPBSET : CMPBSET triggers delay \- CMPBCLR : CMPASET troggers delay (end of cycle)  
DLY_SEL | Delay Select. This option controls what function should be used by the delay trigger the blanking or output event delay \- OFF : delay function not used \- INBLANK : input blanking enabled \- EVENT : event delay enabled  
DLY_VAL | Delay value. This value specifies the blanking output event delay time or event output synchronization in number of prescaled TCD cycles. This is an 8 bit value from 0-255. The default is 0.  
DIT_CTRL | Dither Control. This option configures which compare register is using the dither function. \- ONTIMEB : On-time ramp B \- ONTIMEAB : On-time ramp A and B \- DEADTIMEB : Dead-time ramp B \- DEADTIMEAB : Dead-time ramp A and B  
DIT_VAL | Dither value. These bits configure the fractional adjustment of the on-time or off-time according to Dither Selection bits (DITHERSEL) in the Dither Control register (TCD.DITCTRL). The DITHER value is added to a 4-bit accumulator at the end of each TCD cycle. When the accumulator overflows the frequency adjustment will occur. The DITHER bits are doubled buffered so the new value is copied in at an update condition. The value has a range from 0-15. Default value is 0.  
  
See also

[CONFIG TCA0](config_tca0.md) , [CONFIG_TCB](config_tcb0_tcb1.md)

Example