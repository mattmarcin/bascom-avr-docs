# READSIG

Action

This function reads a byte from the signature area.

Syntax

var = READSIG(offset)

Remarks

Var | A byte that is assigned with the signature byte.  
---|---  
Offset | A byte variable or constant with an offset to the signature.  
  
The Xmega has a number of signature bytes that are important.

For example the ADC is calibrated in the factory and the calibration data need to be loaded into the ADC registers in order to achieve 12 bit resolution.

The following offset table is copied from the Xmega128A1 definition file. It should be the same for all other Xmega chips but it is best to check it.

Const NVM_PROD_SIGNATURES_RCOSC2M_offset = &H00 ' RCOSC 2MHz Calibration Value

Const NVM_PROD_SIGNATURES_RCOSC32K_offset =&H02 ' RCOSC 32kHz Calibration Value

Const NVM_PROD_SIGNATURES_RCOSC32M_offset = &H03 ' RCOSC 32MHz Calibration Value

Const NVM_PROD_SIGNATURES_LOTNUM0_offset = &H08 ' Lot Number Byte 0, ASCII

Const NVM_PROD_SIGNATURES_LOTNUM1_offset = &H09 ' Lot Number Byte 1, ASCII

Const NVM_PROD_SIGNATURES_LOTNUM2_offset = &H0A ' Lot Number Byte 2, ASCII

Const NVM_PROD_SIGNATURES_LOTNUM3_offset = &H0B ' Lot Number Byte 3, ASCII

Const NVM_PROD_SIGNATURES_LOTNUM4_offset = &H0C ' Lot Number Byte 4, ASCII

Const NVM_PROD_SIGNATURES_LOTNUM5_offset = &H0D ' Lot Number Byte 5, ASCII

Const NVM_PROD_SIGNATURES_WAFNUM_offset = &H10 ' Wafer Number

Const NVM_PROD_SIGNATURES_COORDX0_offset = &H12 ' Wafer Coordinate X Byte 0

Const NVM_PROD_SIGNATURES_COORDX1_offset = &H13 ' Wafer Coordinate X Byte 1

Const NVM_PROD_SIGNATURES_COORDY0_offset = &H14 ' Wafer Coordinate Y Byte 0

Const NVM_PROD_SIGNATURES_COORDY1_offset = &H15 ' Wafer Coordinate Y Byte 1

Const NVM_PROD_SIGNATURES_ADCACAL0_offset = &H20 ' ADCA Calibration Byte 0

Const NVM_PROD_SIGNATURES_ADCACAL1_offset = &H21 ' ADCA Calibration Byte 1

Const NVM_PROD_SIGNATURES_ADCBCAL0_offset = &H24 ' ADCB Calibration Byte 0

Const NVM_PROD_SIGNATURES_ADCBCAL1_offset = &H25 ' ADCB Calibration Byte 1

Const NVM_PROD_SIGNATURES_TEMPSENSE0_offset = &H2E ' Temperature Sensor Calibration Byte 0

Const NVM_PROD_SIGNATURES_TEMPSENSE1_offset = &H2F ' Temperature Sensor Calibration Byte 0

Const NVM_PROD_SIGNATURES_DACAOFFCAL_offset = &H30 ' DACA Calibration Byte 0

Const NVM_PROD_SIGNATURES_DACACAINCAL_offset = &H31 ' DACA Calibration Byte 1

Const NVM_PROD_SIGNATURES_DACBOFFCAL_offset = &H32 ' DACB Calibration Byte 0

Const NVM_PROD_SIGNATURES_DACBGAINCAL_offset = &H33 ' DACB Calibration Byte 1

```vb
While the XMEGA was the first processor with support of reading the signature row, all new UPDI AVR chips also have this functionality. And some plain AVR processors like the PB series (atmega328PB)

While in UPDI chips (Xtiny, megaX, AVRX) all these signature registers can be accessed by a register, the ReadSig() function can also read the register contents. ReadSig() was added for compatibility.

```
See also

[READUSERSIG](readusersig.md)

Example XMEGA

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-readsig.bas  
' This sample demonstrates how to read signature bytes  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
'include the following lib and code, the routines will be replaced since they are a workaround  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
  
Dim Offset As Byte , J As Byte  
  
For J = 0 To 32  
```
Offset = Readsig(j) : Print J ; " - " ; Offset  
```vb
Next  
End

```
Example MEGA328

```vb
'--------------------------------------------------------------------------------  
'name : m328pb.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates M328pb  
'micro : Mega328pb  
'suited for demo : yes  
'commercial addon needed : no  
'--------------------------------------------------------------------------------  
$regfile = "m328pbdef.dat"  
$crystal = 8000000  
$baud = 19200  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
'USART TX RX  
' 0 D.1 D.0  
' 1 B.3 B.4  
  
'ISP programming  
'MOSI-PB3 MISO-PB4 SCK-PB5  
Config Clockdiv = 1  
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  
  
  
```
Const Device_signature_byte1 = 0  
Const Device_signature_byte2 = 2  
Const Device_signature_byte3 = 4  
Const Rc_oscillator_calibration = 1  
Const Serial_number_byte0 = &H0E  
Const Serial_number_byte1 = &H0F  
Const Serial_number_byte2 = &H10  
Const Serial_number_byte3 = &H11  
Const Serial_number_byte4 = &H12  
Const Serial_number_byte5 = &H13  
Const Serial_number_byte6 = &H14  
Const Serial_number_byte7 = &H15  
Const Serial_number_byte8 = &H16  
Const Serial_number_byte9 = &H17  
  
  
Print "ID : " ; Hex(readsig(device_signature_byte1)) ; Hex(readsig(device_signature_byte2)) ; Hex(readsig(device_signature_byte3))