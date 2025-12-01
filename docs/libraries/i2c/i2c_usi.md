# I2C_USI

The I2C_USI library is an alternative I2C master library. It is intended to be used with processors that have an USI interface.

Using the hardware is better since it will use less processor resources. 

```vb
If a processor has TWI, use the TWI

If a processors has USI, use the USI

If a processor has no hardware I2C, use the default built in software routines. 

```
To use the USI in master mode, use [CONFIG USI](config_usi.md).

```vb
'------------------------------------------------------------------------------  
' (c) 1995-2025 MCS Electronics  
' USI-MASTER.bas  
' USI used as TWI master demo  
'------------------------------------------------------------------------------  
  
$regfile = "attiny2313.dat"  
$crystal = 8000000  
$hwstack = 40  
$swstack = 16  
$framesize = 24  
$baud = 19200  
  
config usi = twimaster , mode = fast  
  
dim b as byte  
  
```
i2cinit  
  
do  
i2cstart  
i2cwbyte &H40 'send slave WRITE address for PCF8574  
i2cwbyte &B10101010 'send a pattern  
i2crepstart 'repeated start  
  
i2cwbyte &H41 'send slave READ address  
i2crbyte b , ack 'read a byte  
i2crbyte b , nack 'and again  
i2cstop 'end transaction and free bus  
  
```vb
waitms 100 'some delay not required only when you print  
loop

```