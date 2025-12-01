# CONFIG OPAMP

Action

This configuration statement configures the OPAMP (OPerational AMPlifier).

Syntax

CONFIG OPAMP=ENABLED|DISABLED , OPTIONn=VALUEn

The options and values depend on the processor. Below is a list of options and values. There can be multiple OPAMP'S. The X indicates the number in the range from 0-2.

Remarks

OPTION | VALUE  
---|---  
OPAMP | \- ENABLED to enable the OPAMP. \- DISABLED to disable the OPAMP.  
TIME_BASE | Controls the maximum value of a counter that counts CLK_PER cycles to achieve a time interval equal to or larger than 1 Î¼s. It should be written with one less than the number of CLK_PER cycles that are equal to or larger than 1 Î¼s. This is used for the internal timing of the warm up and settling times.  
INP_RANGE | Selects the op amp input voltage range. \- RAIL_TO_RAIL : The op amp input voltage range is rail-to-rail \- REDUCED : The op amp input voltage range and power consumption are reduced  
OPAMPx_RUNMODE | Run in standby mode. \- DISABLED : the OPx is disabled when in standby sleep mode and its output driver is disabled. \- ENABLED : the OPx will continue operating as configured in standby sleep mode.  
OPAMP0_ALWAYS_ON | Controls whether the OPAMP is always on or not. \- DISABLED : the OPx is not always on but can be enabled by the ENABLE EVENTx and disabled by the DISABLE EVENTx \- ENABLED : the OPx is always on  
OPAMP0_EVENTS | Controls event reception and generation. \- DISABLED : No events are enabled for OPx \- ENABLED : All events are enabled for OPx  
OPAMP0_OUTMODE | Selects the output mode for the output driver \- OFF : the output driver for OPx is disabled but this can overridden by the DRIVEx event \- NORMAL : the output driver for OPx is enabled in NORMAL mode  
OPAMP0_MUXWIP | Multiplexer for wiper. Selects the resistor ladder wiper (potentiometer) position \- R1_15R_R2_1R : R1=15R , R2=1R \- R1_14R_R2_2R : R1=14R , R2=2R \- R1_12R_R2_4R : R1=12R , R2=4R  \- R1_8R_R2_8R : R1=8R , R2=8R \- R1_6R_R2_10R : R1=6R , R2=10R \- R1_4R_R2_12R : R1=4R , R2=12R \- R1_2R_R2_14R : R1=2R , R2=14R \- R1_1R_R2_15R : R1=1R , R2=15R  
OPAMP0_MUXBOT | Selects the analog signal connected to the bottom resistor in the resistor ladder \- OFF : multiplexer off \- INP : positive input pin for OPx \- INN : negative input pin for OPx \- DAC : DAC output (DAC and DAC output buffer must be enabled) \- LINKOUT : OPx-1 output. When selecting LINKOUT for OP0 MUXBOT is connected to the output of OP2 \- GND : ground  
OPAMP0_MUXTOP | Selects the analog signal connected to the top resistor in the resistor ladder \- OFF : multiplexer off \- OUT : OPx output \- VDD : VDD  
OPAMP0_MUXNEG | Selects which analog signal is connected to the inverting(-) input of OPx \- INN : negative input pin for OPx \- WIP : wiper from OPx resistor ladder \- OUT : OPx output (unity gain) \- DAC : DAC output (DAC and DAC output buffer must be enabled)  
OPAMP0_MUXPOS | Selects which analog signal is connected to the non inverting(+) input of OPx \- INP : positive input pin for OPx \- WIP : wiper from OPx resistor ladder \- DAC : DAC output (DAC and DAC output buffer must be enabled) \- GND : ground \- VDDDIV2 : VDD / 2  \- LINKOUT : OPx-1 output. Only available for OP1 and OP2  \- LINKWIP : wiper from OP0 resistor ladder. Setting only available for OP2  
OPAMP0_SETTLE | Specifies the number of microseconds allowed for the opamp to settle. This value together with the value in TIME_BASE is used by an internal timer to determine when to generate the READYx event and set the SETTLED flag in the OPx_STATUS register  
OPAMP0_CAL | This value is a calibration value that adjusts the input offset voltage of the op amp. &H00 provides the most negative value of offset adjustment &H80 provides no offset adjustment, and &HFF provides the most positive value of offset adjustment  
REGMODE | \- OVERWITE : the entire register is updated.  \- PRESERVE : the register bits are preserved. See also the [AVRX](avrx.md) topic.  
  
The OPAMP has settings common for all OP's and each individual OPAMP (named OPx) has settings.

The following image from the datasheet shows a block diagram.

![opamp](opamp.png)

See also

NONE

Example