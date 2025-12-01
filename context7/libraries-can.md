# CAN Libraries

> CAN bus communication

## AT90CAN128

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

![can128](can128.png)

---

## AT90CAN32

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

![can128](can128.png)

---

## CAN



---

## CANBAUD

Action

Sets the baud rate of the CAN bus.

Syntax

CANBAUD = value

Remarks

All devices on the CAN bus need to have the same baud rate. The value must be a constant. The baud rate depends on the used crystal. The compiler uses the $CRYSTAL value to calculate the CAN baud rate. Higher baud rates require a higher system clock.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Canbaud = 125000 ' use 125 KB

---

## CANCLEARALLMOBS

Action

Clear all Message Objects.

Syntax

CANCLEARALLMOBS

Remarks

Use CANCLEARALLMOBS after you reset the CAN controller to set all registers in the proper state. All registers belonging to the MOB will be clear (set to 0).

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Canclearallmobs ' clear alle message objects

---

## CANCLEARMOB

Action

Clears a Message Object.

Syntax

CANCLEARMOB ObjectNr

Remarks

The ObjectNr is the number of the Message Object you want to clear. This is a number in the range 0-14. 

A message object need to be cleared before it can be used. CONFIG CANMOB will clear the object by default.

You can also use CANCLEARALLMOBS to clear all message objects.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

---

## CANGETINTS

Action

Reads the CAN interrupt registers and store into the _CAN_MOBINTS word variable.

Syntax

CANGETINTS

Remarks

This statement is intended to be used in the CAN Interrupt routine. It will read the CAN interrupt registers and stores it into a word variable.

Multiple Message Objects can cause an interrupt at the same time. This means that all message objects need to be checked for a possible interrupt.

In the example this is done with a For Next loop.

Cangetints ' read all the interrupts into variable _can_mobints

```vb
For _can_int_idx = 0 To 14 ' for all message objects  
If _can_mobints._can_int_idx = 1 Then ' if this message caused an interrupt

```
Canselpage _can_int_idx ' select message object  


The loop checks all bits and if a message object interrupt has been set, the message object will be selected with CANSELPAGE. 

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md)

Example

---

## CANID

Action

Returns the ID from the received CAN frame.

Syntax

value = CANID()

Remarks

The CANID function can return a 11 bit or 29 bit ID. You need to assign it to a WORD or DWORD variable. 

The CANID functions works at the current selected MOB and is typically used inside the CAN interrupt.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Dim _canid As Dword

_canid = Canid() ' read the identifier

---

## CANRECEIVE

Action

Receives data from a received CAN frame and stores it into a variable.

Syntax

numrec = CANRECEIVE(var [, bytes])

Remarks

numrec | Number of bytes received.  
---|---  
var | The variable into which the received data is stored. This must be a numeric variable or array. Version 2076 supports strings as well.  
bytes | This is an optional parameter and specifies the number of bytes to retrieve.  
  
The compiler will use the data type of the variable to determine how many bytes need to be retrieved. So when you use a variable that was [DIM](dim.md)ensioned as a long, an attempt will be made to read 4 bytes.

The CANRECEIVE function operates on the current selected Message Object which is selected with CANSELPAGE.

The CANRECEIVE function is intended to be used inside the CAN interrupt routine.

After you have retrieved the data from the received CAN frame, the Message Object is free to be used again. You MUST configure it again in order to receive a new interrupt.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Breceived = Canreceive(porta) ' read the data and store in PORTA  
```vb
Print #2 , "Got : " ; Breceived ; " bytes" ' show what we received  
Print #2 , Hex(porta)  
Config Canmob = -1 , Bitlen = 11 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK

```

---

## CANRESET

Action

Reset the CAN controller.

Syntax

CANRESET

Remarks

CANRESET will reset the CAN controller. It is also reset when the processor is reset.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Canreset ' reset can controller

---

## CANSELPAGE

Action

Selects the Message Object index or page.

Syntax

CANSELPAGE index

Remarks

All 15 message objects share the same registers. With CANSELPAGE you select the index of the MOB you want to access.

The index is a constant or variable in the range of 0-14.

You should save and restore the CANPAGE register when changing the index. This is shown in the CAN [example](config_canbusmode.md).

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANGETINTS](cangetints.md)

Example

---

## CANSEND

Action

Puts the Message Object into Transmit mode and send out data.

Syntax blocking function

status = CANSEND(object, var[,bytes])

Syntax non blocking statement

CANSEND object, var[,bytes]

Remarks

status | The status of sending the frame. This should be 0 if there was no problem. If there is an error it will return 1 or higher. The return value is the CANSTMOB register content with the TX bit cleared.  
---|---  
object | The message object number in the range from 0-14. The MOB must have been configured into the DISABLED mode before CANSEND can be used.   
var | A variable or array which content will be send. The data type of the variable will be used to determine the number of bytes to send.  
bytes | This is an optional value. You can specify how many bytes must be transmitted.   
  
The CANSEND function will disable the TX interrupt and then polls the CANSTMOB register for a change of flags. The TX flag is cleared so that a successful transmission returns a 0.

In case of ACK errors or other errors, a value other then 0 will be returned. Right after the status has changed, the TX and Error interrupt are enabled again and the CAN interrupt routine is executed. You need to reconfigure the MOB in all cases otherwise you can not send new data.

The CANSEND statement will send the data and returns immediately.

The advantage is that your code can continue running other code. Before new data can be sent it must however have been processed. Check out the CAN-elektor-V2.bas example from the samples\CAN folder.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Have a look at [CONFIG CANBUS](config_canbusmode.md) for a full example.

The code below only demonstrates that you MUST configure the MOB again in the interrupt routine.

The code below is taken from the sample you find under CONFIG CANBUS

The \examples\CAN folder contains 2 examples too.

Elseif Canstmob.6 = 1 Then 'transmission ready  
```vb
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK

```
Elseif Canstmob.0 = 1 Then 'ACK ERROR  
```vb
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK  


```

---

## SENDSCAN

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

---

## SENDSCANKBD

Action

Sends keyboard scan codes to the PC.

Syntax

SENDSCANKBD label | var

Remarks

Label | The name of the label that contains the scan codes.  
---|---  
var | The byte variable that will be sent to the PC.  
  
The SENDSCANKBD statement can send multiple scan codes to the PC.

The label is used to specify the start of the scan codes. The first byte specifies the number of bytes that follow.

You can also send the content of a variable. This way you can send dynamic information.

You need to make sure you send the make and break codes.

The following tables lists all scan codes.

AT KEYBOARD SCANCODES

Table reprinted with permission of Adam Chapweske

http://panda.cs.ndsu.nodak.edu/~achapwes

KEY | MAKE | BREAK |  | KEY | MAKE | BREAK |  | KEY | MAKE | BREAK  
---|---|---|---|---|---|---|---|---|---|---  
A | 1C | F0,1C |  | 9 | 46 | F0,46 |  | [ | 54 | FO,54  
B | 32 | F0,32 |  | ` | 0E | F0,0E |  | INSERT | E0,70 | E0,F0,70  
C | 21 | F0,21 |  | - | 4E | F0,4E |  | HOME | E0,6C | E0,F0,6C  
D | 23 | F0,23 |  | = | 55 | FO,55 |  | PG UP | E0,7D | E0,F0,7D  
E | 24 | F0,24 |  | \ | 5D | F0,5D |  | DELETE | E0,71 | E0,F0,71  
F | 2B | F0,2B |  | BKSP | 66 | F0,66 |  | END | E0,69 | E0,F0,69  
G | 34 | F0,34 |  | SPACE | 29 | F0,29 |  | PG DN | E0,7A | E0,F0,7A  
H | 33 | F0,33 |  | TAB | 0D | F0,0D |  | U ARROW | E0,75 | E0,F0,75  
I | 43 | F0,43 |  | CAPS | 58 | F0,58 |  | L ARROW | E0,6B | E0,F0,6B  
J | 3B | F0,3B |  | L SHFT | 12 | FO,12 |  | D ARROW | E0,72 | E0,F0,72  
K | 42 | F0,42 |  | L CTRL | 14 | FO,14 |  | R ARROW | E0,74 | E0,F0,74  
L | 4B | F0,4B |  | L GUI | E0,1F | E0,F0,1F |  | NUM | 77 | F0,77  
M | 3A | F0,3A |  | L ALT | 11 | F0,11 |  | KP / | E0,4A | E0,F0,4A  
N | 31 | F0,31 |  | R SHFT | 59 | F0,59 |  | KP * | 7C | F0,7C  
O | 44 | F0,44 |  | R CTRL | E0,14 | E0,F0,14 |  | KP - | 7B | F0,7B  
P | 4D | F0,4D |  | R GUI | E0,27 | E0,F0,27 |  | KP + | 79 | F0,79  
Q | 15 | F0,15 |  | R ALT | E0,11 | E0,F0,11 |  | KP EN | E0,5A | E0,F0,5A  
R | 2D | F0,2D |  | APPS | E0,2F | E0,F0,2F |  | KP . | 71 | F0,71  
S | 1B | F0,1B |  | ENTER | 5A | F0,5A |  | KP 0 | 70 | F0,70  
T | 2C | F0,2C |  | ESC | 76 | F0,76 |  | KP 1 | 69 | F0,69  
U | 3C | F0,3C |  | F1 | 05 | F0,05 |  | KP 2 | 72 | F0,72  
V | 2A | F0,2A |  | F2 | 06 | F0,06 |  | KP 3 | 7A | F0,7A  
W | 1D | F0,1D |  | F3 | 04 | F0,04 |  | KP 4 | 6B | F0,6B  
X | 22 | F0,22 |  | F4 | 0C | F0,0C |  | KP 5 | 73 | F0,73  
Y | 35 | F0,35 |  | F5 | 03 | F0,03 |  | KP 6 | 74 | F0,74  
Z | 1A | F0,1A |  | F6 | 0B | F0,0B |  | KP 7 | 6C | F0,6C  
0 | 45 | F0,45 |  | F7 | 83 | F0,83 |  | KP 8 | 75 | F0,75  
1 | 16 | F0,16 |  | F8 | 0A | F0,0A |  | KP 9 | 7D | F0,7D  
2 | 1E | F0,1E |  | F9 | 01 | F0,01 |  | ] | 5B | F0,5B  
3 | 26 | F0,26 |  | F10 | 09 | F0,09 |  | ; | 4C | F0,4C  
4 | 25 | F0,25 |  | F11 | 78 | F0,78 |  | ' | 52 | F0,52  
5 | 2E | F0,2E |  | F12 | 07 | F0,07 |  | , | 41 | F0,41  
6 | 36 | F0,36 |  | PRNT SCRN | E0,12, E0,7C | E0,F0, 7C,E0, F0,12 |  | . | 49 | F0,49  
7 | 3D | F0,3D |  | SCROLL | 7E | F0,7E |  | / | 4A | F0,4A  
8 | 3E | F0,3E |  | PAUSE | E1,14,77, E1,F0,14, F0,77 | -NONE- |  |  |  |   
  
![scancodes](scancodes.jpg)

ACPI Scan Codes

Key | Make Code | Break Code  
---|---|---  
Power | E0, 37 | E0, F0, 37  
Sleep | E0, 3F | E0, F0, 3F  
Wake | E0, 5E | E0, F0, 5E  
  
Windows Multimedia Scan Codes

Key | Make Code | Break Code  
---|---|---  
Next Track | E0, 4D | E0, F0, 4D  
Previous Track | E0, 15 | E0, F0, 15  
Stop | E0, 3B | E0, F0, 3B  
Play/Pause | E0, 34 | E0, F0, 34  
Mute | E0, 23 | E0, F0, 23  
Volume Up | E0, 32 | E0, F0, 32  
Volume Down | E0, 21 | E0, F0, 21  
Media Select | E0, 50 | E0, F0, 50  
E-Mail | E0, 48 | E0, F0, 48  
Calculator | E0, 2B | E0, F0, 2B  
My Computer | E0, 40 | E0, F0, 40  
WWW Search | E0, 10 | E0, F0, 10  
WWW Home | E0, 3A | E0, F0, 3A  
WWW Back | E0, 38 | E0, F0, 38  
WWW Forward | E0, 30 | E0, F0, 30  
WWW Stop | E0, 28 | E0, F0, 28  
WWW Refresh | E0, 20 | E0, F0, 20  
WWW Favorites | E0, 18 | E0, F0, 18  
  
To emulate volume up, the data line would look like this:

DATA 5 , &HE0, &H32, &HE0, &HF0 , &H32

^ send 5 bytes

^ volume up

See also

[CONFIG ATEMU](config_atemu.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : ps2_kbdemul.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : PS2 AT Keyboard emulator

'micro : 90S2313

'suited for demo : no, ADD ON NEEDED

'commercial addon needed : yes

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$lib "mcsbyteint.lbx" ' use optional lib since we use only bytes

'configure PS2 AT pins

Enable Interrupts ' you need to turn on interrupts yourself since an INT is used

Config Atemu = Int1 , Data = Pind.3 , Clock = Pinb.0

' ^------------------------ used interrupt

' ^----------- pin connected to DATA

' ^-- pin connected to clock

'Note that the DATA must be connected to the used interrupt pin

Waitms 500 ' optional delay

'rcall _AT_KBD_INIT

Print "Press t for test, and set focus to the editor window"

Dim Key2 As Byte , Key As Byte

Do

```
Key2 = Waitkey() ' get key from terminal

```vb
Select Case Key2

Case "t" :

Waitms 1500

```
Sendscankbd Mark ' send a scan code

```vb
Case Else

End Select

Loop

Print Hex(key)

```
Mark: ' send mark

Data 12 , &H3A , &HF0 , &H3A , &H1C , &HF0 , &H1C , &H2D , &HF0 , &H2D , &H42 , &HF0 , &H42

```vb
' ^ send 12 bytes

' m a r k

```

---
