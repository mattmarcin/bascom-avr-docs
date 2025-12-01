# CONFIG CANBUSMODE

Action

Configures the CAN bus mode.

Syntax

CONFIG CANBUSMODE =mode

Remarks

mode | The CAN bus can be set to 3 different modes. \- ENABLED : TxCAN and RxCAN are enabled. \- STANDBY : TxCAN is recessive and the receiver is disabled. The registers and mobs can be accessed. \- LISTENING : This mode is transparant for the CAN channel. It enables a hardware loop[ back from the internal TxCAN to the RxCAN. It provides a recessive level on the TxCAN output pin. It does NOT disable the RxCAN pin.  
---|---  
  
The CAN commands are intended for the AVR processor AT90CANXXX series. 

You need to terminate the bus with 120 ohm at both ends.

Your code always need a number of statements. The best solution is to use the can-elektor.bas sample to get started.

CANRESET

Will reset the CAN controller. Use this only once.

CANCLEARALLMOBS

Will clear all message objects. This is best to be done right after the CANRESET.

CANBAUD

All devices on the bus need to have the same baud rate. Set the BAUD right after you have cleared all objects.

CONFIG CANBUSMODE

Now you chose the mode the bus will work in. This is ENABLED in most cases.

CONFIG CANMOB

Here you define the properties of each Message Object. This need to be done only once. But after the message object has been used, you need to configure it again so the new MOB can be used again.

CANGIE , ON CAN_IT

Since the interrupt TX, RX and ERR interrupts are used you need to assign a value of &B10111000 to CANGIE.

You also need to assign an interrupt routine to the CANIT interrupt.

In the main code you can send data using CANSEND. 

The interrupt routine.

The CANPAGE register is saved into the _CAN_PAGE variable. This is required since the interrupt may not change the CANPAGE register.

Then CANGETINTS is used to retreive all message object interrupt flags. The value is stored in _CAN_MOBINTS.

Since multiple Message Objects can cause an interrupt we check all message objects with a For.. Next loop to test all bits. If the bit is set, the Message Object is selected with CANSELPAGE.

```vb
Then the CANSTMOB register is tested for a number of bits/flags.

If bit 5 is set, it means that a frame was received. For the demo the ID is read with CANID. 

```
The CANRECEIVE function reads the data from the frame into a variable. In the example the variable is a PORT which will change value depending on the receive data byte.

After this the CONFIG CANMOB is used with a value of -1 to indicate that the operation must be done on the current selected MOB.

The object is put back into receive mode.

If bit 6 is set it means that data was transmitted with success. Again, we use CONFIG CANMOB so the object can be used again. For transmitting we put the object into DISABLED mode.

And lastly we test bit 0, the MOB error bit. It if was set it means there was an error when data was sent using CANSEND. We must use CONFIG CANMOB so the MOB can be used again. 

We must clear the CANSIT1 and CANSIT2 flag registers before we exit the interrupt routine. We also need to reset the interrupt flags in CANGIT. This is done by writing the same value back to CANGIT. A one will clear the flag if it was set.

Last we restore the CANPAGE register by writing _CAN_PAGE back to it.

While the interrupt routine shows some PRINT statements, it is not a good idea to print inside the/a interrupt routine. You should keep the delay as short as possible otherwise you might not be able to process all CAN frames.

As you can see in the sample, the MOB's are configured at the start AND once they are used so they can be re-used. 

In the example all lines are important except for the PRINT lines. 

See also

[CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

```vb
'------------------------------------------------------------------------  
' CAN-Elektor.bas  
' bascom-avr demo for Auto-CANtroller board  
'------------------------------------------------------------------------  
$regfile = "m32can.dat" ' processor we use  
  
$crystal = 12000000 ' Crystal 12 MHz  
$hwstack = 64  
$swstack = 32  
$framesize = 40  
  
'$prog &HFF , &HCF , &HD9 , &HFF ' generated. Take care that the chip supports all fuse bytes.  
Config Porta = Output ' LED  
Config Portc = Input ' DIP switch  
```
Portc = 255 ' activate pull up  
  
Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
Open "COM2:" For Binary As #2  
  
```vb
Dim _canpage As Byte , _canid As Dword , _can_int_idx As Byte , _can_mobints As Word  
Dim Breceived As Byte , Bok As Byte , Bdil As Byte  
  
On Can_int Can_int ' define the CAN interrupt  
Enable Interrupts ' enable interrupts  
  
```
Canreset ' reset can controller  
Canclearallmobs ' clear alle message objects  
Canbaud = 125000 ' use 125 KB  
  
```vb
Config Canbusmode = Enabled ' enabled,standby,listening  
Config Canmob = 0 , Bitlen = 11 , Idtag = &H0120 , Idmask = &H0120 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled 'first mob is used for receiving data  
Config Canmob = 1 , Bitlen = 11 , Idtag = &H0120 , Msgobject = Disabled , Msglen = 1 ' this mob is used for sending data  
  
```
Cangie = &B10111000 ' CAN GENERAL INTERRUPT and TX and RX and ERR  
```vb
Print #2 , "Start"  
  
Do  
If Pinc <> Bdil Then ' if the switch changed  
```
Bdil = Pinc ' save the value  
Bok = Cansend(1 , Pinc) ' send one byte using MOB 1  
```vb
Print #2 , "OK:" ; Bok ' should be 0 if it was send OK  
End If  
Loop  
  
'*********************** CAN CONTROLLER INTERRUPT ROUTINE **********************  
'multiple objects can generate an interrupt  
```
Can_int:

_canpage = Canpage ' save can page because the main program can access the page too  
Cangetints ' read all the interrupts into variable _can_mobints  
  
```vb
For _can_int_idx = 0 To 14 ' for all message objects  
If _can_mobints._can_int_idx = 1 Then ' if this message caused an interrupt  
  
```
Canselpage _can_int_idx ' select message object  
  
If Canstmob.5 = 1 Then ' we received a frame  
_canid = Canid() ' read the identifier  
Print #2 , Hex(_canid)  
  
Breceived = Canreceive(porta) ' read the data and store in PORTA  
```vb
Print #2 , "Got : " ; Breceived ; " bytes" ' show what we received  
Print #2 , Hex(porta)  
Config Canmob = -1 , Bitlen = 11 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK  
```
Elseif Canstmob.6 = 1 Then 'transmission ready  
```vb
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK  
```
Elseif Canstmob.0 = 1 Then 'ack error when sending data 'transmission ready  
```vb
Print #2 , "ERROR:" ; Hex(canstmob)  
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
End If  
End If  
Next  
```
Cangit = Cangit ' clear interrupt flags  
Canpage = _canpage ' restore page  
Return