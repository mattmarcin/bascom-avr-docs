# SENDSCAN

Action

Sends scan codes to the PC.

Syntax

SENDSCAN label

Remarks

Label | The name of the label that contains the scan codes.  
---|---  
  
The SENDSCAN statement can send multiple scan codes to the PC.

The label is used to specify the start of the scan codes. The first byte specifies the number of bytes that follow.

The following table lists all mouse scan codes.

Emulated Action | Data sent to host  
---|---  
Move up one | 08,00,01  
Move down one | 28,00,FF  
Move right one | 08,01,00  
Move left one | 18,FF,00  
Press left button | 09,00,00  
Release left button | 08,00,00  
Press middle button | 0C,00,00  
Release middle button | 08,00,00  
Press right button | 0A,00,00  
Release right button | 08,00,00  
  
To emulate a left mouse click, the data line would look like this:

DATA 6 , &H09, &H00, &H00, &H08 , &H00, &H00

^ send 6 bytes

^ left click

^ release

See also

[PS2MOUSEXY](ps2mousexy.md) , [CONFIG PS2EMU](config_ps2emu.md)

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