# CONFIG PS2EMU

Action

Configures the PS2 mouse data and clock pins.

Syntax

CONFIG PS2EMU= int , DATA = data, CLOCK=clock

Remarks

Int | The interrupt used such as INT0 or INT1.  
---|---  
DATA | The pin that is connected to the DATA line. This must be the same pin as the used interrupt.  
CLOCK | The pin that is connected to the CLOCK line.  
  
![ps2-male](ps2-male.gif) | ![ps2-female](ps2-female.gif) | 5-pin DIN (AT/XT):  1 - Clock 2 - Data 3 - Not Implemented 4 - Ground 5 - +5v  
---|---|---  
  
![ps2-male6](ps2-male6.gif) | ![ps2-female6](ps2-female6.gif) | 6-pin Mini-DIN (PS/2): 1 - Data 2 - Not Implemented 3 - Ground 4 - +5v 5 - Clock 6 - Not Implemented  
---|---|---  
  
Old PCâs are equipped with a 5-pin DIN female connector. Newer PCâs have a 6-pin mini DIN female connector.

The male sockets must be used for the connection with the micro.

Besides the DATA and CLOCK you need to connect from the PC to the micro, you need to connect ground. You can use the +5V from the PC to power your microprocessor.

The config statement will setup an ISR that is triggered when the INT pin goes low. This routine you can find in the library.

The ISR will retrieve a byte from the PC and will send the proper commands back to the PC.

The SENDSCAN and PS2MOUSEXY statements allow you to send mouse commands.

Note that the mouse emulator is only recognized after you have booted your PC. Mouse devices can not be plugged into your PC once it has booted. Inserting a mouse or mouse device when the PC is already booted, may damage your PC.

See also

[SENDSCAN](sendscan.md), [PS2MOUSEXY](ps2mousexy.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : ps2_emul.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : PS2 Mouse emulator

'micro : 90S2313

'suited for demo : NO, commercial addon needed

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "mcsbyteint.lbx" ' use optional lib since we use only bytes

'configure PS2 pins

Config Ps2emu = Int1 , Data = Pind.3 , Clock = Pinb.0

' ^------------------------ used interrupt

' ^----------- pin connected to DATA

' ^-- pin connected to clock

'Note that the DATA must be connected to the used interrupt pin

Waitms 500 ' optional delay

Enable Interrupts ' you need to turn on interrupts yourself since an INT is used

Print "Press u,d,l,r,b, or t"

Dim Key As Byte

Do

```
Key = Waitkey() ' get key from terminal

```vb
Select Case Key

Case "u" : Ps2mousexy 0 , 10 , 0 ' up

Case "d" : Ps2mousexy 0 , -10 , 0 ' down

Case "l" : Ps2mousexy -10 , 0 , 0 ' left

Case "r" : Ps2mousexy 10 , 0 , 0 ' right

Case "b" : Ps2mousexy 0 , 0 , 1 ' left button pressed

```
Ps2mousexy 0 , 0 , 0 ' left button released

```vb
Case "t" : Sendscan Mouseup ' send a scan code

Case Else

End Select

Loop

```
Mouseup:

Data 3 , &H08 , &H00 , &H01 ' mouse up by 1 unit