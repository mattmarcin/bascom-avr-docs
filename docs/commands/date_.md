# DATE$

Action

Internal variable that holds the date.

Syntax

DATE$ = "mm/dd/yy"

var = DATE$

Remarks

The DATE$ variable is used in combination with the [CONFIG CLOCK](config_clock.md) directive.

The [CONFIG CLOCK](config_clock.md) statement will create an interrupt that occurs every second. In this interrupt routine the _Sec, _Min and _Hour variables are updated. The _dat, _month and _year variables are also updated. The date format is in the same format as in VB.

When you assign DATE$ to a string variable these variables are assigned to the DATE$ variable.

When you assign the DATE$ variable with a constant or other variable, the _day, _month and _year variables will be changed to the new date.

The only difference with VB is that all data must be provided when assigning the date. This is done for minimal code. You can change this behavior of course.

![important](important.jpg) Do not confuse DATE$ with the DATE function !

ASM

The following ASM routines are called.

When assigning DATE$ : _set_date (calls _str2byte)

When reading DATE$ : _make_dt (calls _byte2str)

See also

[TIME$](time_.md) , [CONFIG CLOCK](config_clock.md) , [DATE](date.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : megaclock.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : shows the new TIME$ and DATE$ reserved variables

'micro : Mega103

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m103def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'With the 8535 and timer2 or the Mega103 and TIMER0 you can

'easily implement a clock by attaching a 32768 Hz xtal to the timer

'And of course some BASCOM code

'This example is written for the STK300 with M103

Enable Interrupts

'[configure LCD]

$lcd = &HC000 'address for E and RS

$lcdrs = &H8000 'address for only E

Config Lcd = 20 * 4 'nice display from bg micro

Config Lcdbus = 4 'we run it in bus mode and I hooked up only db4-db7

Config Lcdmode = Bus 'tell about the bus mode

'[now init the clock]

Config Date = Mdy , Separator = / ' ANSI-Format

Config Clock = Soft 'this is how simple it is

'The above statement will bind in an ISR so you can not use the TIMER anymore!

'For the M103 in this case it means that TIMER0 can not be used by the user anymore

'assign the date to the reserved date$

'The format is MM/DD/YY

```
Date$ = "11/11/00"

```vb
'assign the time, format in hh:mm:ss military format(24 hours)

'You may not use 1:2:3 !! adding support for this would mean overhead

'But of course you can alter the library routines used

```
Time$ = "02:20:00"

```vb
'---------------------------------------------------

'clear the LCD display

```
Cls

Do

Home 'cursor home

Lcd Date$ ; " " ; Time$ 'show the date and time

```vb
Loop

'The clock routine does use the following internal variables:

'_day , _month, _year , _sec, _hour, _min

'These are all bytes. You can assign or use them directly

```
_day = 1

```vb
'For the _year variable only the year is stored, not the century

End

```