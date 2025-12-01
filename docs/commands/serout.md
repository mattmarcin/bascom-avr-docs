# SEROUT

Action

Sends serial data through a dynamic software UART.

Syntax

SEROUT var , bts , port , pin, baud , parity , dbits , sbits [,INVERTED]

Remarks

While the OPEN and CLOSE statements can be used for software UARTS, they do not permit to use the same pin for input and output. The settings used when opening the communication channel can also not be changed at run time.

The SERIN and SEROUT statements are dynamic software UART routines to perform input and output. You can use them on the same pin for example to send some data with SEROUT and get back an answer using SERIN.

Since the SERIN and SEROUT routines can use any pin and can use different parameter values, the code size of these routines is larger.

Parameter | Description  
---|---  
Var | A variable which content is send through the UART. A constant can NOT be used.  
Bts | The number of bytes to send. For strings you can specify 0. In that case the whole string will be sent.  
Port | The name of the port to use. For example : portA.  
Pin | The pin number you want to use of the port. This must be in the range from 0-7.  
Baud | The baud rate you want to use. For example 19200.  
Parity | A number that codes the parity. 0= NONE, 1 = EVEN, 2 = ODD  
Dbits | The number of data bits. Use 7 or 8.  
Sbits | The number of stop bits. 1 to 2.  
INVERTED | This is an optional parameter. When set, the signal will be inverted.   
  
The use of SEROUT will create an internal variable named ___SER_BAUD. This is a LONG variable. It is important that you specify the correct crystal value with $CRYSTAL so the correct calculation can be made for the specified baud rate.

Note that ___SER_BAUD will not hold the passed baud rate but will hold the bit delay which is used internal.

Since the SW UART is dynamic you can change all the parameters at run time. For example you can store the baud rate in a variable and pass this variable to the SEROUT routine.

Your code could change the baud rate under user control this way.

It is important to realize that software timing is used for the bit timing. Any interrupt that occurs during SERIN or SEROUT will delay the transmission. Disable interrupts while you use SERIN or SEROUT.

![notice](notice.jpg)SEROUT can be used in PORT and open collector TRI-state mode. 

PORT mode means that the defined PORT PIN will be set to output mode, and that the pin output will be switched between 0 and 1.

The disadvantage of this mode is that you can not connect multiple outputs together. (never connect 2 outputs together). 

For this reason there is also the TRI state/open collector mode.

By default TRI-state mode will be used. This mode requires an external pull up resistor on the Xmega/Xtiny. For the normal AVR this external pull up resistor is optional.

Since the port architecture differs for all platforms there are different implementations to create the bit stream in open collector mode.

The normal AVR has a pull up resistor that can be activated by writing 1 to a port. The Xmega has a special register to activate the pull up resistor. And the Xtiny has a special register as well to activate the pull up resistor. For all platforms, a zero bit is created by setting the data direction register to output mode and clear the output pin.

To create a one, the normal AVR is set to input mode and the pull up is activated by writing a one to data direction.

For the Xmega the code is similar but more code is required for the pinctrl register since each pin has its own register. The pull up mode is the wired and mode. 

In Open Collector mode you can connect several AVR chip pin and poll the âbusâ with the [SERIN](serin.md) statement.   
When you want to use the pins in PORT OUTPUT mode, the pins can not be tied together.

Define a constant named SEROUT_EXTPULL with a value of 1 for the TRI-STATE open collector mode. 

Define a constant named SEROUT_EXTPULL with a value of 0 to work in PORT mode.

When you do not define a constant the SEROUT_EXTPULL will be created automatically with a value of 1.

![notice](notice.jpg)The mode you chose is fixed and global for all SEROUT statements. You can not switch between SEROUT_EXTPULL value in your code dynamically.

ASM

The routine called is named _serout and is stored in mcs.lib. An overloaded version is placed in xmega.lib and xtiny.lib

For the baud rate calculation, _calc_baud is called.

See also

[SERIN](serin.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : serin_out.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstration of DYNAMIC software UART

'micro : AT90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'tip : Also look at OPEN and CLOSE

'some variables we will use

Dim S As String * 10

Dim Mybaud As Long

'when you pass the baud rate with a variable, make sure you dimesion it as a LONG

```
Mybaud = 19200

```vb
Do

'first get some data

```
Serin S , 0 , PORTD , 0 , Mybaud , 0 , 8 , 1

'now send it

Serout S , 0 , PORTD , 1 , Mybaud , 0 , 8 , 1

```vb
' ^ 1 stop bit

' ^---- 8 data bits

' ^------ even parity (0=N, 1 = E, 2=O)

' ^-------------- baud rate

' ^-------------------- pin number

' ^----------------------- port so PORTA.0 and PORTA.1 are used

' ^--------------------------- for strings pass 0

' ^-------------------------------- variable

Wait 1

Loop

End

'because the baud rate is passed with a variable in this example, you could change it under user control

'for example check some DIP switches and change the variable mybaud

```