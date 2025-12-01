# CONFIG HITAG

Action

Configures the timer and HITAG variables.

Syntax

```vb
CONFIG HITAG = prescale, TYPE=tp, DOUT = dout, DIN=din , CLOCK=clock, INT=int

CONFIG HITAG = prescale, TYPE=tp, DEMOD= demod, INT=@int

```
Remarks

syntax for HTRC110

prescale | The pre scaler value that is used by TIMER0. A value of 8 and 256 will work at 8 MHz.   
---|---  
tp | The kind of RFID chip you use. Use HTRC110.  
DOUT | The pin that is connected to the DOUT pin of the HTRC110. This pin is used in input mode since DOUT is an output. A pin that support the pin-change interrupt or the PCINT should be selected.  
DIN | The pin that is connected to the DIN pin of the HTRC110. This pin is used in output mode. You can chose any pin that can be used in output mode.  
CLOCK | The pin that is connected tot the CLOCK pin of the HTRC110. This pin is used in output mode. You can chose any pin that can be used in output mode.  
INT | The interrupt used. Note that you need to precede the interrupt with an @ sign. For example for INT1 you provide : @INT1  
  
syntax for EM4095

prescale | The pre scaler value that is used by TIMER0. A value of 8 and 256 will work at 8 MHz.   
---|---  
tp | The kind of RFID chip you use. Use EM4095.  
demod | The pin that is connected to the DEMOD pin of the EM4095. This pin is used in input mode. A pin that support the pin-change interrupt or the PCINT should be selected.  
INT | The interrupt used. Note that you need to precede the interrupt with an @ sign. For example for INT1 you provide : @INT1  
  
The CONFIG HITAG command will generate a number of internal used variables and constants.

Constants : _TAG_MIN_SHORT, _TAG_MAX_SHORT , _TAG_MIN_LONG and _TAG_MAX_LONG.

See the description of READHITAG to see how they are calculated. The actual value will depend on the prescaler value you use. 

Variables for HTRC110 :

_htr_statemachine , a byte that is used to maintain a state machine.

_htcbit , a byte that will hold the received bit. 

_htcbitcount , a byte to store the number of received bits.

_htcmpulse , a byte that stores the pulse

_htr_pulse_state , a byte that is used to maintain the pulse state machine. 

_htc_retries, a byte that is used for the number of retries. 

_tagdelta , a byte that will held the delta time between 2 edges. 

_tagtime , a byte with the actual timer0 value when an edge is detected.

_taglasttime , a byte with the previous edge time, needed to calculate the

delta time.

_tagparbit , a byte that will held the parity.

_tagdata , a byte where the bits are stored before they are loaded into the serial

number array. 

_tagid , a word that points to the serial number array

The HTRC110.LBX contains a number of other constants that are used to control the HTRC chip.

The _init_Tag routine is called automatically. 

![notice](notice.jpg)The clock output of the Mega88 is used to drive the HTRC110. Since the clock output of the internal oscillator is 8 MHz, the HTRC110 is also configured to work at 8 MHz.

The .equ for Tag_set_config_page3 = &H40 + 48 + Fsel0 in the LBX. You can set it to 12 and 16 MHz too but you can not drive it from the clock output then.

The datasheet specifies the following for FSEL1 and FSEL0

FSEL1 | FSEL0 | Frequency  
---|---|---  
0 | 0 | 4 MHz  
0 | 1 | 8 MHz  
1 | 0 | 12 MHz  
1 | 1 | 16 MHz  
  
So when you want to use a different frequency you can edit the equ in the lbx.

.equ Tag_set_config_page3 = &H40 + 48 + Fsel0 ' 8 Mhz

For 16 Mhz it would become :

.equ Tag_set_config_page3 = &H40 + 48 + Fsel0 + Fsel1 ' 8 Mhz

When you want to send a custom command you can call the internal routine : _Send_htrc110_cmdR25

Just load R25 with the proper value before you do :

R25=8 'readphase command

!call _Send_htrc110_cmdR25

Variables for EM4095 :

_tagflag , a byte that stores the return flag that will be loaded with 1 when a

valid tag is detected

_tag_insync ,a byte that is used to store the state of the bit stream. 

_tag_bitcount , a byte that stores the total bits when not in sync yet 

_tag_tbit , a byte that stores the total received bits

_tag_par , a byte that stores the parity

_tag_timeout ,a byte that is loaded with the time that will be tried to 

detect an RFID chip

_taglasttime , a byte that stores the last time a valid edge was detected

_tagid , a word that points to the serial number array

See also

[READHITAG](readhitag.md)

Example HTRC110

```vb
'--------------------------------------------------------------------------

' (c) 1995-2025 , MCS Electronics

' sample : readhitag.bas

' demonstrates usage of the READHITAG() function

'--------------------------------------------------------------------------

$regfile = "m88def.dat" ' specify chip

$crystal = 8000000 ' used speed

$baud = 19200 ' baud rate

'Notice that the CLOCK OUTPUT of the micro is connected to the clock input of

```
the HTRC110

'PORTB.0 of the Mega88 can optional output the clock. You need to set the

fusebit for this option

```vb
'This way all parts use the Mega88 internal oscillator

'The code is based on Philips(NXP) datasheets and code. We have signed an

```
NDA to get the 8051 code

```vb
'You can find more info on Philips website if you want their code

Print "HTC110 demo"

Config Hitag = 64 , Type = Htrc110 , Dout = Pind.2 , Din = Pind.3 , Clock = Pind.4 , Int = @int0

' ^ use timer0 and select prescale value 64

' ^ we used htrc110 chip

' ^-- dout of HTRC110 is connected to PIND.2

```
which will be set to input mode

' ^ DIN of HTRC100 is connected

to PIND.3 which will be set to output mode

' ^clock of

HTRC110 is connected to PIND.4 which is set to output mode

```vb
' ^ interrupt

'the config statement will generate a number of constants and

```
internal variables used by the code

```vb
'the htrc110.lbx library is called

Dim Tags(5) As Byte 'each tag has 5 byte serial

Dim J As Byte ' a loop counter

'you need to use a pin that can detect a pin level change

'most INT pins have this option

'OR , you can use the PCINT interrupt that is available on some chips

'In case you want PCINT option

' Pcmsk2 = &B0000_0100 'set the mask to ONLY use the pin connected to DOUT

' On Pcint2 Checkints 'label to be called

' Enable Pcint2 'enable this interrupt

'In case you want to use INT option

On Int0 Checkints ' PIND.2 is INT0

Config Int0 = Change 'you must configure the pin to work in pin change intertupt mode

Enable Interrupts ' enable global interrupts

Do

If Readhitag(tags(1)) = 1 Then 'check if there is a new tag ID

For J = 1 To 5 'print the 5 bytes

Print Hex(tags(j)) ; ",";

Next

Else 'there was nothing

Print "Nothing"

End If

Waitms 500 'some delay

Loop

'this routine is called by the interrupt routine

```
Checkints:

Call _checkhitag 'you must call this label

```vb
'you can do other things here but keep time to a minimum

Return

```
Example EM4095

```vb
'-------------------------------------------------------------------------------

' (c) 1995-2025 MCS Electronics

' This sample will read a HITAG chip based on the EM4095 chip

' Consult EM4102 and EM4095 datasheets for more info

'-------------------------------------------------------------------------------

' The EM4095 was implemented after an idea of Gerhard Günzel

' Gerhard provided the hardware and did research at the coil and capacitors.

' The EM4095 is much simpler to use than the HTRC110. It need less pins.

' A reference design with all parts is available from MCS

'-------------------------------------------------------------------------------

$regfile = "M88def.dat"

$baud = 19200

$crystal = 8000000

$hwstack = 40

$swstack = 40

$framesize = 40

'Make SHD and MOD low

Dim Tags(5) As Byte 'make sure the array is at least 5 bytes

Dim J As Byte

Config Hitag = 64 , Type = Em4095 , Demod = Pind.3 , Int = @int1

Print "Test EM4095"

'you could use the PCINT option too, but you must mask all pins out 

```
so it will only respond to our pin

```vb
' Pcmsk2 = &B0000_0100

' On Pcint2 Checkints

' Enable Pcint2

On Int1 Checkints Nosave 'we use the INT1 pin all regs are saved in the lib

Config Int1 = Change 'we have to config so that on each pin change the routine will be called

Enable Interrupts 'as last we have to enable all interrupts

Do

Print "Check..."

If Readhitag(tags(1)) = 1 Then 'this will enable INT1

For J = 1 To 5

Print Hex(tags(j)) ; ",";

Next

Print

Else

Print "Nothing"

End If

Waitms 500

Loop

```
Checkints:

Call _checkhitag 'in case you have used a PCINT, you could have other code here as well

Return