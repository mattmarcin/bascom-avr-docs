# CONFIG TWIxSLAVE

Action  
  
Configure the Xmega TWIC,TWID,TWIE or TWIF hardware to be used a a slave.

Syntax

```vb
CONFIG TWICSLAVE = address , BTR = value ,GENCALL=value

CONFIG TWIDSLAVE = address , BTR = value ,GENCALL=value

CONFIG TWIESLAVE = address , BTR = value ,GENCALL=value

CONFIG TWIFSLAVE = address , BTR = value ,GENCALL=value

```
(I2C TWI Slave is part of the I2C-Slave library. This is an add-on library which is not included with Bascom-AVR by default. It is a commercial add on library. It is available from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=34&category_id=6&option=com_phpshop&Itemid=1>) )

See also: [I2C TWI Slave](i2ctwislave.md), [USING I2C Protocol](using_the_i2c_protocol.md), [Using USI](using_usi_universal_serial_int.md), [CONFIG I2CSLAVE](config_i2cslave.md) , [CONFIG USI](config_usi.md)

Remarks

Address | The slave address which is assigned to the slave chip. This must be an Even number. Bit 0 of the address is used to activate the general call address. The GENCAL option will set this bit automatic. I2C uses a 7 bit address from bit 1 to bit 7. Bit 0 is used to specify a read/write operation. In BASCOM the byte transmission address is used for I2C. This means that an I2C 7-bit address of 1 becomes &B10 = 2. And we say the address is 2. This is done so you can copy the address from the data sheets which are in the same format in most cases. So if you work with 7 bit address, you need to multiply the address by 2.  
---|---  
BTR | Bytes to receive. With this constant you specify how many bytes will be expected when the master reads data from the slave. And thus how many bytes will be sent to the master. This value can be changed dynamically.  
GENCALL | General call address activated or not. When you specify 1, the General call address will be activated which mean that the slave will respond not only to it's own address, but also to the general call address 0.  When you omit the option or specify 0, the general call address will not be honored.   
  
The variables TwiX , TwiX_btr, TwiX_CBTR and TwiX_btw are created by the compiler. These are all byte variables.

The X represents the TWI interface letter which can be C, D, E or F.

The TWIx interrupt is enabled as well but you need to enabled the global interrupt

The TWI Slave code is running as an interrupt process. Each time there is a TWI interrupt some slave code is executed. Your BASIC code is called from the low level slave code by a number of events. You must include all these labels in your Slave application. You do not need to write code in all these sub routines.

Label | Event  
---|---  
Twi_stop_rstart_received TwiD_stop_rstart_received TwiE_stop_rstart_received TwiF_stop_rstart_received | The Master sent a stop(i2CSTOP) or repeated start. Typical you do not need to do anything here.  
Twi_addressed_goread TwiD_addressed_goread TwiE_addressed_goread TwiF_addressed_goread | The master has addressed the slave and will now continue to send data to the slave. You do not need to take action here.  
Twi_addressed_gowrite TwiD_addressed_gowrite TwiE_addressed_gowrite TwiF_addressed_gowrite | The master has addressed the slave and will now continue to receive data from the slave. You do not need to take action here.  
Twi_gotdata TwiD_gotdata TwiE_gotdata TwiF_gotdata | The master has sent data. The variable TWIx holds the received value. The byte TWIx_BTW is an index that holds the value of the number of received bytes. The first received byte will have an index value of 1.  
Twi_master_needs_byte TwiD_master_needs_byte TwiE_master_needs_byte TwiF_master_needs_byte | The master reads from the slave and needs a value. The variable TWIx_BTR can be inspected to see which index byte was requested. With the CONFIG parameter BTR, you specify how many bytes the master will read. This value is stored in the variable TWIx_CBTR. You can alter this value but you should not do that in the middle of a transaction.  
  
The name of the label called depends on the used TWI interface. TWIC is the default TWI interface. All I2C commands work with TWIC by default.

In order to make the normal slave code compatible with the Xmega, the TWIC interface uses the same label names as used for normal AVR TWI interface.

This means that your BASCOM slave code for the M32 should work for the TWIC interface without much changes.

![notice](notice.jpg)It is important that you do not use the MASTER TWI routines when using the TWI as a slave. Just supply or read data at the provided routines.

In most cases your main application is just an empty DO LOOP. But when you write a slave that performs other tasks on the background these other tasks are interrupted by the TWI traffic.

Do NOT write blocking code inside an interrupt. While servicing another interrupt, the TWI interrupt can not be serviced.

Also, do not block execution by putting delays in the called routines such as TWI_GOTDATA. All these labels are called from the TWIX SLAVE library which is an interrupt routine that will halt the main application and other interrupts.

The TWI Slave code will save all used registers.

In order to get a working slave it is important that the slave matches the protocol used by the master. Thus if the slave reads data from the master and only expects 2 bytes, the master should not send less or more. We advise to make a simple slave first like a PCF8574 clone.

See also

[CONFIG TWIX](config_twi.md)

Example

The following example uses two TWI interfaces. TWID is used in master mode while TWIC is used as the slave.

```vb
'------------------------------------------------------------------------------  
'name : xmega-twi-slave.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates Xmega TWI slave add on  
'micro : Xmega128A1  
'suited for demo : yes  
'commercial addon needed : yes  
'------------------------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
'Config Serialin = Buffered , Size = 50  
  
'Enable Interrupts  
```
Open "COM1:" For Binary As #1  
  
Open "twid" For Binary As #4 ' or use TWIC,TWIE oR TWIF  
```vb
Config Twid = 100000 'CONFIG TWI will ENABLE the TWI master interface  
'you can also use TWIC, TWID, TWIE of TWIF  
'!!!!!!!!!!! WITHOUT a channel identifier, TWIC will be used !!!!!!!!!!!!!!  
'SCL is on pin 1  
'SDA is on pin 0  
'This demo uses TWID as master and TWIC as SLAVE  
'Thus portc.0 connects with portD.0 and  
' portc.1 connects with portD.1  
  
'The TWIC when used as a slave has megaAVR compatible labels  
'The TWID,TWIE and TWIF have unique new labelnames  
'These labels are the labels in your code which are called from the slave ISR.  
'For example : Twi_addressed_gowrite is named TwiD_addressed_gowrite for TWID  
  
  
Dim Twi_start As Byte , j as byte , b as byte  
```
I2cinit #4 'init the master  
```vb
config TWIcslave = &H70 , btr = 2 'use address &H70 which is &H38 in 7-bit i2c notation  
  
Enable INTERRUPTS 'for the slave to work we must enable global interrupts  
  
do  
Print #1 , "test xmega"  
  
For J = 0 To 120 Step 1 'notice that we scan odd and even addresses  
```
I2cstart #4 'send start  
I2cwbyte J , #4 'send value of J  
```vb
If Err = 0 Then ' no errors  
Print #1 , "FOUND : " ; Hex(j)  
if j.0 = 0 then 'ONLY if R/W bit is not set we may write data !!!  
```
I2cwbyte 100 , #4 'just write to values to the slave  
I2cwbyte 101 , #4  
else 'read  
I2crbyte b , Ack , #4 : print #1 , "GOT : " ; b 'read 2 bytes  
I2crbyte b , nAck , #4 : print #1 , "GOT : " ; b  
```vb
end if  
End If  
```
I2cstop #4 'done  
```vb
Next  
waitms 2000 'wait some time  
loop  
  
  
'the following labels are called from the library when master send stop or start  
'notice that these label names are valid for TWIC.  
'for TWID the name would be TWID_stop_rstart_received:  
```
Twi_stop_rstart_received:  
```vb
Print #1 , "Master sent stop or repeated start"  
Return  
  
'master sent our slave address and will not send data  
```
Twi_addressed_goread:  
```vb
Print #1 , "We were addressed and master will send data"  
Return  
  
  
```
Twi_addressed_gowrite:  
```vb
Print #1 , "We were addressed and master will read data"  
Return  
  
'this label is called when the master sends data and the slave has received the byte  
'the variable TWIx holds the received value  
'The x is the TWI interface letter  
```
Twi_gotdata:  
```vb
Print #1 , "received : " ; Twic ; " byte no : " ; Twic_btw  
'here you would do something with the received data  
' Select Case Twic_btw  
' Case 1 : Portb = Twi ' first byte  
' Case 2: 'you can set another port here for example  
' End Select   
Return  
  
'this label is called when the master receives data and needs a byte  
'the variable twix_btr is a byte variable that holds the index of the needed byte  
'so when sending multiple bytes from an array, twix_btr can be used for the index  
'again the variable name depends on the twi interface  
```
Twi_master_needs_byte:  
```vb
Print #1 , "Master needs byte : " ; Twic_btr  
Select Case Twic_btr  
Case 1: ' first byte  
```
twic = 66 'we assign a value but this could be any value you want  
Case 2 ' send second byte  
twic = 67  
```vb
End Select  
Return  
  
  
'when the mast has all bytes received this label will be called  
```
Twi_master_need_nomore_byte:  
```vb
Print #1 , "Master does not need anymore bytes"  
Return  
  
End

```