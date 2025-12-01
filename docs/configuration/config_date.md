# CONFIG DATE

Action

Configure the Format of the Date String for Input to and Output from BASCOM â Date functions

Syntax

CONFIG DATE = DMY , Separator = char

Remarks

DMY | The Day, month and year order. Use DMY, MDY or YMD.  
---|---  
Char | The character used to separate the day, month and year. Old syntax : / , - or . (dot). Preferred new syntax : MINUS, SLASH or DOT. Example: Config Date = DMY, SEPARATOR=MINUS  
  
The following table shows the common formats of date and the associated statements.

Country | Format | Statement  
---|---|---  
American | mm/dd/yy | Config Date = MDY, Separator = SLASH  
ANSI | yy.mm.dd | Config Date = YMD, Separator = DOT  
Britisch/French | dd/mm/yy | Config Date = DMY, Separator = SLASH  
German | dd.mm.yy | Config Date = DMY, Separator = DOT  
Italian | dd-mm-yy | Config Date = DMY, Separator = MINUS  
Japan/Taiwan | yy/mm/dd | Config Date = YMD, Separator = SLASH  
USA | mm-dd-yy | Config Date = MDY, Separator = MINUS  
  
When you live in Holland you would use :

CONFIG DATE = DMY, separator = MINUS

This would print 24-04-02 for 24 November 2002.

When you line in the US, you would use :

CONFIG DATE = MDY , separator = SLASH

This would print 04/24/02 for 24 November 2002.

See also

[CONFIG CLOCK](config_clock.md) , [DATE TIME functions](datetime.md) , [DayOfWeek](dayofweek.md) , [DayOfYear](dayofyear.md) , [SecOfDay](secofday.md) , [SecElapsed](secelapsed.md) , [SysDay](sysday.md) , [SysSec](syssec.md) , [SysSecElapsed](syssecelapsed.md) , [Time](time.md) , [Date](date.md)

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

Config Date = Mdy , Separator = SLASH ' ANSI-Format

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