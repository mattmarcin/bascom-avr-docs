# EM4095 RFID Reader

Introduction

RFID technology is an exciting technology. The EM4095 chip allows us to create a reader with little code or processor resources.

A complete KIT is available from the web shop at [www.mcselec.com](<http://www.mcselec.com/tiny/shop/8/171>)

This topic describes the reference design. 

The data sheets you can download from:

[EM4095](<http://www.mcselec.com/tiny/dwn/192/54>) (chip) , [EM4102](<http://www.mcselec.com/tiny/dwn/193/54>) (transponder)

The circuit

![em4095_sch](em4095_sch.zoom49.png)

As you can see from the data sheets, the EM4095 needs little external hardware. A coil, capacitors that tune the coil for 125 KHz, are basically all that you need. IC1 is a voltage regulator that regulates the input voltage to 5V. (you can operate it from a 9V battery). The capacitors stabilize the output voltage. The DEMOD output of the EM4095 is connected to the microprocessor and the pin is used in input mode. The MOD and SHD pins are connected to micro pins that are used in output mode.

The micro(mega88) has a small 32 KHz crystal so the soft clock can be used. There are 3 switches that can be used for menu input, and there is a relay that can be used to activate a door opener. Parallel on the relay there is a LED for a visible indication.

IC4 is a serial interface buffer so we can connect the PCB to our computer for logging and programming. The Mega88 is delivered with a Boot loader and thus can be serial programmed with the MCS Boot loader. That is why pin 4 of X6 (DTR) is connected via IC4(pin 8-9) to the reset pin of the micro(pin 1).

Further there is a standard 10-pins ISP programmer connector for the USB-ISP or STK200, and an LCD connector for an optional LCD display.

The PCB

![em4095_pcb](em4095_pcb.zoom67.png)

Part list

Component | Value  
---|---  
C1 | 470uF/25V  
C2,C3,C5,C6,C9,CDEC,CAGND | 100nF (104)  
C4 | 100uF/16V  
CRES1,CRES, CDV2 | 1nF(102)  
CDV1 | 47pF  
CDC2,CFCAP | 10nF(103)  
C11,C12,C13,C14 | 1uF/16V  
RSER | 68  
R4,R6 | 10K  
R5 | 470  
R8 | 47  
R3 | 47K  
R9 | 1K-10K pot  
IC1 | 7805  
IC2 | EM4095  
IC3 | ATMEGA88  
IC4 | MAX232  
20 pin IC feet, 16 pin IC feet |   
  
X1,X2 | 2-pin header  
X3 | 16 pin boxed header  
X4 | 3-pin header  
X5 | 10-pin boxed header  
X6 | DB-9 female connector  
T1 | BC547  
D1 | 1N4148  
LED1 | 3 mm LED, red  
K1 | Relay, 5V  
S1,S2,S3 | switch  
Q1 | 32768 Hz crystal  
Antenna |   
  
M3x6 bolt and nut |   
  
4 rubber feet |   
  
  
Building the PCB

As usually we start with the components that have the lowest height. And normally we would solder all passive components first, and insert/solder the active components last. This to prevent damage to the active components(IC). But since the EM4095 is only available in SMD, we need to solder this chip first. Make sure the chip is lined out right and that pin 1 matches the small dot on the chip which is an indication for pin 1.

Then solder pin 1 and 16 so the chip can not be moved anymore. Now solder the remaining pins. Use an iron with a small tip. When you use too much solder, and two feet are soldered together do not panic. Just finish soldering and when ready, use some copper braid to remove the solder between the 2 feet. This works best when you lay the braid over the 2 pins, then push the solder iron to the braid so it will heat up. Then after some seconds, add some solder which will get sucked into the braid. This will in turn suck the other solder into the braid. While it does not seem logical to add solder, it will conduct the heat better. But since the used SMD chip is relatively large there should not be any problem.

Now mount and solder the following components :

•| RSER (68 ohm)  
---|---  
  
•| R3 (47K)  
---|---  
  
•| R4,R6 (10 K)  
---|---  
  
•| R5 (470)  
---|---  
  
•| R8 (47 for LCD)  
---|---  
  
•| D1 (diode 1N4148). The black line must match the line on the PCB(Kathode)  
---|---  
  
•| C2,C3,C5,C6,C9,CDEC,CAGND (100 nF)  
---|---  
  
•| CRES1,CRES , CDV2 (1nF)  
---|---  
  
•| CDV1 (47pF)  
---|---  
  
•| CDC2,CFCAP (10nF)  
---|---  
  
•| 28 pins IC feet for the Mega88 and 16 pins IC feet for the MAX232  
---|---  
  
•| Bend the wires of IC1 and mount IC1 with the bolt and nut  
---|---  
  
•| Bend the wires of the crystal and mount Q1  
---|---  
  
•| S1,S2,S3 (switches)  
---|---  
  
•| LED1. The square pad matches the longest wire of the LED(Anode)  
---|---  
  
•| R9 (potmeter for LCD contrast)  
---|---  
  
•| T1(transistor BC547)  
---|---  
  
•| Boxed header X5 and X3. Notice the gap in the middle which must match with the PCB  
---|---  
  
•| X6 (DB9-female connector)  
---|---  
  
•| K1 (relay)  
---|---  
  
•| C11,C12,C13,C14 (1uF/16V)  
---|---  
  
•| C4 (100uF/16V)  
---|---  
  
•| X1,X2 (2 pins screw connectors)  
---|---  
  
•| X4 (3 pin screw connector)  
---|---  
  
•| C1 (470 uF/25V)  
---|---  
  
•| 4 rubber feet  
---|---  
  
Operation

Now the PCB is ready. Make sure there are no solder drops on the PCB. You can measure with an Ohm-meter if there is a short circuit.

Measure pin 1 and pin 2 of IC1 (the voltage input) and pin 3 and pin 2 of IC1 (the voltage output). 

When everything is ok, insert the MAX232 and the MEGA88. 

You can connect the battery cord to header X1. The red wire is the plus. Since the circuit is not for beginners, there is no reverse polarity protection. While the 7805 does not mind a short circuit, the C1 elco might not like it. 

Connect the battery and measure with a Volt meter if IC1 actual outputs 5V. If not, check the input voltage, and for a possible shortcut.

Connect the antenna to connector X2. The PCB is now ready for use. When you have the LCD display, connect it to the LCD header and adjust the variable resistor R9 so you can see square blocks.

Since the chip has a boot loader, you can serial program the device. We made a simple AN that can be used as a door opener. It has simple menu, and we can add new tags. When a valid tag is held in front of the antenna, it will activate the relay for 2 seconds. The LED will be turned on as well.

Compile the program AN_READHITAG_EM4095.BAS and select the MCS Boot Loader programmer. Connect a serial cable to X6 and press F4 to program.

You need a normal straight cable.

![db9-cable](db9-cable.png)

When you did not used the MCS Bootloader before, check the COM port settings and make sure the BAUD is set to 38400 as in the following screenshot:

![bootloader_sample](bootloader_sample.png)

You also need to set 'RESET via DTR' on the 'MCS Loader' TAB. 

Now the program will start and show some info on the LCD. Each time you hold a RFID tag before the antenna/coil, the TAG ID will be shown. 

When you press S3, you can store an RFID. Press S3, and then hold the TAG before the coil. When there is room , or the tag is new, it will be stored. Otherwise it will be ignored. The TAG ID is also stored in EEPROM.

Now when you hold the tag before the coil, the relay is activated for 2 seconds. 

The AN is very simple and you can change and extend it easily.

One nice idea from Gerhard : use one TAG as a master tag to be able to add/remove tags.

Security

To make the code more secure you could add a delay so that a valid tag must be received twice, so after the valid TAG, wait 1 second, and then start a new measurement and check if the TAG is valid again.

This will prevent where a bit generator could be used to generate all possible codes. With 64 bit times a second, it would take ages before it would work. 

The other hack would be to listen with a long range 125 KHz antenna, and recording all bits. A long range scanner would be very hard to make. It would be easier to open the door with a crowbar.

When you open your door with this device, make sure you have a backup option like a key in case there is no power. Also, when the door is opened by a magnetic door opener, make sure it has the right quality for the entrance you want to protect. 

![em4095_board](em4095_board.jpg)

AN Code

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

Declare Function Havetag(b As Byte ) As Byte

'Make SHD and MOD low

```
_md Alias Portd.4

Config _md = Output

_md = 0

_shd Alias Portd.5

Config _shd = Output

_shd = 0

Relay Alias Portd.2

Config Relay = Output

S3 Alias Pinb.0

S2 Alias Pinb.2

S1 Alias Pinb.1

Portb = &B111 ' these are all input pins and we activate the pull up resistor

```vb
Config Clock = Soft 'we use a clock

Config Date = Dmy , Separator = -

Enable Interrupts ' the clock and RFID code need the int

```
Date$ = "15-12-07" ' just a special date to start with

Time$ = "00:00:00"

```vb
'Config Lcd Sets The Portpins Of The Lcd

Config Lcdpin = Pin , Db4 = Portc.2 , Db5 = Portc.3 , Db6 = Portc.4 , Db7 = Portc.5 , E = Portc.1 , Rs = Portc.0

Config Lcd = 16 * 2 '16*2 type LCD screen

```
Cls

Lcd " EM4095 sample"

Lowerline : Lcd "MCS Electronics"

```vb
Dim Tags(5) As Byte 'make sure the array is at least 5 bytes

Dim J As Byte , Idx As Byte

Dim Eramdum As Eram Byte ' do not use first position

Dim Etagcount As Eram Byte ' number of stored tags

Dim Etags(100) As Eram Byte 'room for 20 tags

Dim Stags(100) As Byte 'since we have enough SRAM store them in sram too

Dim Btags As Byte , Tmp1 As Byte , Tmp2 As Byte

Dim K As Byte , Tel As Byte , M As Byte

Config Hitag = 64 , Type = Em4095 , Demod = Pind.3 , Int = @int1

Print "EM4095 sample"

'you could use the PCINT option too, but you must mask all pins out so it will only respond to our pin

' Pcmsk2 = &B0000_0100

' On Pcint2 Checkints

' Enable Pcint2

On Int1 Checkints Nosave 'we use the INT1 pin all regs are saved in the lib

Config Int1 = Change 'we have to config so that on each pin change the routine will be called

Enable Interrupts 'as last we have to enable all interrupts

'read eeprom and store in sram

'when the program starts we read the EEPROM and store it in SRAM

For Idx = 1 To 100 'for all stored tags

```
Stags(idx) = Etags(idx)

```vb
Print Hex(stags(idx)) ; ",";

Next

```
Btags = Etagcount ' get number of stored tags

```vb
If Btags = 255 Then ' an empty cell is FF (255)

Print "No tags stored yet"

```
Btags = 0 : Etagcount = Btags ' reset and write to eeprom

```vb
Else ' we have some tags

For J = 1 To Btags

```
Tmp2 = J * 5 'end

Tmp1 = Tmp2 - 4 'start

```vb
Print "RFID ; " ; J ' just for debug

For Idx = Tmp1 To Tmp2

Print Hex(stags(idx)) ; ",";

Next

Print

Next

End If

Do

Print "Check..."

```
Upperline : Lcd Time$ ; " Detect"

If Readhitag(tags(1)) = 1 Then 'this will enable INT1

Lowerline

```vb
For J = 1 To 5

Print Hex(tags(j)) ; ",";

```
Lcd Hex(tags(j)) ; ","

Next

M = Havetag(tags(1)) 'check if we have this tag already

```vb
If M > 0 Then

Print "Valid TAG ;" ; M

```
Relay = 1 'turn on relay

Waitms 2000 'wait 2 secs

Relay = 0 'relay off

```vb
End If

Print

Else

Print "Nothing"

End If

If S3 = 0 Then 'user pressed button 3

Print "Button 3"

```
Cls : Lcd "Add RFID"

```vb
Do

If Readhitag(tags(1)) = 1 Then 'this will enable INT1

If Havetag(tags(1)) = 0 Then 'we do not have it yet

If Btags < 20 Then 'will it fit?

```
Incr Btags 'add one

Etagcount = Btags

Idx = Btags * 5 'offset

Idx = Idx - 4

Lowerline

For J = 1 To 5

Lcd Hex(tags(j)) ; ","

Stags(idx) = Tags(j)

Etags(idx) = Tags(j)

Incr Idx

Next

Cls

Lcd "TAG stored" : Waitms 1000

```vb
End If

End If

Exit Do

End If

Loop

End If

If S2 = 0 Then

Print "Button 2"

End If

If S1 = 0 Then

Print "Button 1"

End If

Waitms 500

Loop

'check to see if a tag is stored already

'return 0 if not stored

'return value 1-20 if stored

Function Havetag(b As Byte ) As Byte

Print "Check if we have TAG : ";

For K = 1 To 5

Print Hex(b(k)) ; ","

Next

For K = 1 To 20

```
Tmp2 = K * 5 'end addres

Tmp1 = Tmp2 - 4 'start

Tel = 0

For Idx = Tmp1 To Tmp2

Incr Tel

```vb
If Stags(idx) <> B(tel) Then 'if they do not match

Exit For 'exit and try next

End If

Next

If Tel = 5 Then 'if we did found 5 matching bytes we have a match

Print "We have one"

```
Havetag = K 'set index

```vb
Exit Function

End If

Next

```
Havetag = 0 'assume we have nothing yet

End Function

Checkints:

Call _checkhitag 'in case you have used a PCINT, you could have other code here as well

Return

Tips and Tricks

The oscillator frequency must be 125 KHz. You can measure this with an oscilloscope. It is possible that you need to remove a few windings of the antenna coil to get an exact 125 KHz. This will result in a higher distance that you can use for the tags.