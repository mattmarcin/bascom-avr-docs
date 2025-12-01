# GETATKBD

Action

Reads a key from a PC AT keyboard.

Syntax

var = GETATKBD()

Remarks

var | The variable that is assigned with the key read from the keyboard. It may be a byte or a string variable. When no key is pressed a 0 will be returned.  
---|---  
  
The GETAKBD() function needs 2 input pins and a translation table for the keys. You can read more about this at the [CONFIG KEYBOARD](config_keyboard.md) compiler directive.

The Getatkbd function will wait for a pressed key. When you want to escape from the waiting loop you can set the ERR bit from an interrupt routine for example.

Getatkbd is using 2 bits from register R6 : bit 4 and 5 are used to hold the shift and control key status.

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
  
These are the usable scan codes from the keyboard. If you want to implement F1 , you look at the generated scan code : 05 hex. So in the table, at position 5+1=6, you write the value for F1.

In the sample program below, you can find the value 200. When you now press F1, the value form the table will be used so 200 will be returned.

See also

[CONFIG KEYBOARD](config_keyboard.md) , [GETATKBDRAW](getatkbdraw.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : getatkbd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : PC AT-KEYBOARD Sample

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "8535def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'For this example :

'connect PC AT keyboard clock to PIND.2 on the 8535

'connect PC AT keyboard data to PIND.4 on the 8535

'The GetATKBD() function does not use an interrupt.

'But it waits until a key was pressed!

'configure the pins to use for the clock and data

'can be any pin that can serve as an input

'Keydata is the label of the key translation table

Config Keyboard = Pind.2 , Data = Pind.4 , Keydata = Keydata

'Dim some used variables

Dim S As String * 12

Dim B As Byte

'In this example we use SERIAL(COM) INPUT redirection

$serialinput = Kbdinput

'Show the program is running

Print "hello"

Do

'The following code is remarked but show how to use the GetATKBD() function

' B = Getatkbd() 'get a byte and store it into byte variable

'When no real key is pressed the result is 0

'So test if the result was > 0

' If B > 0 Then

' Print B ; Chr(b)

' End If

'The purpose of this sample was how to use a PC AT keyboard

'The input that normally comes from the serial port is redirected to the

'external keyboard so you use it to type

Input "Name " , S

'and show the result

Print S

'now wait for the F1 key , we defined the number 200 for F1 in the table

Do

```
B = Getatkbd()

```vb
Loop Until B <> 0

Print B

Loop

End

'Since we do a redirection we call the routine from the redirection routine

'

```
Kbdinput:

```vb
'we come here when input is required from the COM port

'So we pass the key into R24 with the GetATkbd function

' We need some ASM code to save the registers used by the function

$asm

```
push r16 ; save used register

push r25

push r26

push r27

Kbdinput1:

rCall _getatkbd ; call the function

tst r24 ; check for zero

breq Kbdinput1 ; yes so try again

pop r27 ; we got a valid key so restore registers

pop r26

pop r25

pop r16

```vb
$end Asm

'just return

Return

'The tricky part is that you MUST include a normal call to the routine

'otherwise you get an error

'This is no clean solution and will be changed

```
B = Getatkbd()

'This is the key translation table

Keydata:

'normal keys lower case

Data 0 , 0 , 0 , 0 , 0 , 200 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , &H5E , 0

Data 0 , 0 , 0 , 0 , 0 , 113 , 49 , 0 , 0 , 0 , 122 , 115 , 97 , 119 , 50 , 0

Data 0 , 99 , 120 , 100 , 101 , 52 , 51 , 0 , 0 , 32 , 118 , 102 , 116 , 114 , 53 , 0

Data 0 , 110 , 98 , 104 , 103 , 121 , 54 , 7 , 8 , 44 , 109 , 106 , 117 , 55 , 56 , 0

Data 0 , 44 , 107 , 105 , 111 , 48 , 57 , 0 , 0 , 46 , 45 , 108 , 48 , 112 , 43 , 0

Data 0 , 0 , 0 , 0 , 0 , 92 , 0 , 0 , 0 , 0 , 13 , 0 , 0 , 92 , 0 , 0

Data 0 , 60 , 0 , 0 , 0 , 0 , 8 , 0 , 0 , 49 , 0 , 52 , 55 , 0 , 0 , 0

Data 48 , 44 , 50 , 53 , 54 , 56 , 0 , 0 , 0 , 43 , 51 , 45 , 42 , 57 , 0 , 0

'shifted keys UPPER case

Data 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0

Data 0 , 0 , 0 , 0 , 0 , 81 , 33 , 0 , 0 , 0 , 90 , 83 , 65 , 87 , 34 , 0

Data 0 , 67 , 88 , 68 , 69 , 0 , 35 , 0 , 0 , 32 , 86 , 70 , 84 , 82 , 37 , 0

Data 0 , 78 , 66 , 72 , 71 , 89 , 38 , 0 , 0 , 76 , 77 , 74 , 85 , 47 , 40 , 0

Data 0 , 59 , 75 , 73 , 79 , 61 , 41 , 0 , 0 , 58 , 95 , 76 , 48 , 80 , 63 , 0

Data 0 , 0 , 0 , 0 , 0 , 96 , 0 , 0 , 0 , 0 , 13 , 94 , 0 , 42 , 0 , 0

Data 0 , 62 , 0 , 0 , 0 , 8 , 0 , 0 , 49 , 0 , 52 , 55 , 0 , 0 , 0 , 0

Data 48 , 44 , 50 , 53 , 54 , 56 , 0 , 0 , 0 , 43 , 51 , 45 , 42 , 57 , 0 , 0