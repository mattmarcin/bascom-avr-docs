# $PROGRAMMER

Action

Will set the programmer from the source code.

Syntax

```vb
$PROGRAMMER = number [,"COMx"] 

$PROGRAMMER = number [,"serial"] 

```
Remarks

Number | A numeric constant that identifies the programmer.   
---|---  
COMx | An optional parameter in double quotes that specifies the COM port to use. Future versions might offer additional options. Example : "COM3"  
serial | For MCSEDBG this can be the product name with serial number. Use this when you have multiple programmers connected.  
  
The $PROGRAMMER directive requires that you set the option 'Use New Method' in Options, Environment, IDE.

The $PROGRAMMER directive will set the programmer just before it starts programming.

When you press F4 to program a chip, the selected programmer will be made active. This is convenient when you have different projects open and use different programmers.

But it can also lead to frustration as you might think that you have the 'STK200' selected, and the directive will set it to USB-ISP.

The following values can be used :

Value | Programmer  
---|---  
0 | AVR-ISP programmer(old AN 910) *  
1 | STK200/STK300 *  
2 | PG302 *  
3 | External programmer  
4 | Sample Electronics *  
5 | Eddie Mc Mullen *  
6 | KITSRUS K122 *  
7 | STK500  
8 | Universal MCS Interface *  
9 | STK500 extended  
10 | Lawicel Bootloader *  
11 | MCS USB  
12 | USB-ISP I *  
13 | MCS Bootloader  
14 | Proggy *  
15 | FLIP (Atmel)  
16 | USBprog Programmer/ AVR ISP mkII (Atmel)  
17 | Kamprog for AVR  
18 | MyAVR MKII/AVR910  
19 | USBASP  
20 | JTAG MKII  
21 | STK600  
22 | ARDUINO (using stk500v1 protocol)  
23 | ARDUINO V2 (using stk500v2 protocol)  
24 | MINI-MAX/AVR-C (BIPOM)  
25 | mySmart USB light STK500 mode  
26 | MSC UPDI programmer  
27 | MCS EDBG programmer  
  
* - not recommended for purchase/use

The file prog.inc in the \INC subfolder contains constants for all programmers.

We recommend to use the constant since it is more clear which programmer is used.

An additional parameter can be used to specify the COM port to use. Like : $PROGRAMMER 26, "COM45"

Notice that there is no double point after the COM port number.

```vb
For the MCS EDBG programmer you can specify an optional product name with serial number. 

For example : 

$programmer = prgMCSEDBG,"mEDBG CMSIS-DAP:SNAP"

```
See also

[$PROG](_prog.md)

ASM

NONE

Example

```vb
$regfile = "AVRX64EA28.dat"  
$crystal = 20000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64

  
$programmer = Prgmcsedbg , "nEDBG CMSIS-DAP:MC020059804RYN000236"  
' use MCS EDBG programmer. The USB product name is nEDBG CMSIS-DAP and the serial is MC020059804RYN000236

```