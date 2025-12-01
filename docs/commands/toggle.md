# TOGGLE

Action

Toggles(inverts) the state of an output pin or bit/Boolean variable. When used on a numeric variable, all bits in the variable are inverted.

Syntax

```vb
TOGGLE pin

TOGGLE var

```
Remarks

pin | Any port pin like PORTB.0 or boolean variable. A port pin must be configured as an output pin before TOGGLE will have effect.  
---|---  
var | A numeric variable like byte, word, integer or long. When you invert a byte, all bits of that byte will be inverted.   
  
With TOGGLE you can simply invert the output state of a port pin.

When the pin is driving a relay for example and the relay is OFF, one TOGGLE statement will turn the relays ON. Another TOGGLE will turn the relays OFF again.

When TOGGLE is used with a variable of the type Byte, Word, Integer or Long, all bits in the variable are toggled. It has the same effect as using the EXOR boolean operand with $FF, $FFFF or $FFFFFFFF

Example:

Toggle Var_byte has the same effect as

Var_byte = Var_byte XOR &HFF

New AVR chips have an enhanced port architecture which allow a toggle of the PORT by setting the PIN register to 1. The DAT files have a setting under the [DEVICE] section named NEWPORT.

When the value is 1, the PIN register will be set to toggle the PORT pin. When the NEWPORT value is set to 0, an XOR will be used to toggle the port pin.

TOGGLE can also be used on numeric variables. It will invert all bits in the variable. It has the same effect as NOT.

var = NOT var ' invert all bits

See also

[CONFIG PORT](config_port.md)

ASM

NONE

Example

```vb
'Bascom Help, Nov 16, 2008  
'ToggleNov15_2008.bas  
'Program example for use in the Help-files for  
' TOGGLE  
  
'Program has been compiled and tested using Bascom 1.11.9.2.003  
'Nard Awater, November 16, 2008  
  
  
$baud = 19200  
$crystal = 16000000  
$regfile = "m32def.dat"  
  
$hwstack = 40  
$swstack = 20  
$framesize = 20  
  
Dim B As Byte , W As Word , I As Integer , L As Long  
```
Led Alias Portb.0 'the anode of the LED connected to PortB.0, cathode with resistor (470 Ohm) to ground  
Config Pinb.0 = Output  
  
B = 0  
```vb
Reset Led  
'Toggle the led  
Do  
Print "Led is off "  
Waitms 500  
Toggle Led  
Print "Led is on "  
Waitms 500  
Toggle Led  
```
Incr B  
```vb
Loop Until B = 5  
  
'Toggle a bit in a variable  
```
B = &B11110000 'assign a new value: 240 in decimal  
```vb
Toggle B.0  
Print "B in decimal " ; B ' print it: result = 241 ; bit0 is set  
Print Bin(b) ' print it: result = 11110001  
Toggle B.0  
Print "B in decimal " ; B ' print it: result = 240 ; bit0 is reset  
Print Bin(b) ' print it: result = 11110000  
  
  
```
W = &H000F '15 in decimal  
I = &H00FF '255 in decimal  
L = &H00CC00DD '13369565 in decimal  
```vb
Toggle W  
Print "toggled W= " ; W ' print it: result = 65520  
Print Hex(w) ' print it: result = &HFFF0  
  
Toggle I  
Print "toggled I= " ; I ' print it: result = -256 ; two's complement !  
Print Hex(i) ' print it: result = &HFF00  
  
Toggle L  
Print "toggled L= " ; L ' print it: result = -13369566 ; two's complement !  
Print Hex(l) ' print it: result = &HFF33FF22  
  
End  


```