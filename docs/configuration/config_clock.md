# CONFIG CLOCK

Action

Configures the timer to be used for the Time$ and Date$ variables. 

Syntax

CONFIG CLOCK = SOFT | USER [, GOSUB = SECTIC] 

Syntax Xmega

CONFIG CLOCK = SOFT | USER [, GOSUB = SECTIC] [,RTC=rtc] [,RTC32=rtc32] [,HIGHESR=highesr]

Syntax Xtiny

CONFIG CLOCK = SOFT | USER [, GOSUB = SECTIC] [,RTC=rtc] , RUNMODE=runmode

Remarks

Soft | Use SOFT for using the software based clock routines. You need to add an ENABLE INTERRUPTS statement to your code since the SOFT mode uses the timer in interrupt mode. The timer interrupt is enabled automatic but the global interrupt you need to enable yourself. While the compiler could enable the global interrupt automatic, you would not have control anymore when it is enabled when using multiple interrupts. In general you enable global interrupts after all interrupts are setup. For the SOFT mode you need to connect a special low frequency crystal with a value of 32768 Hz to the ASYNC TIMER oscillator pins. Use USER to write/use your own code in combination with an I2C clock chip for example.  
---|---  
Sectic | This option allows to jump to a user routine with the label sectic. Since the interrupt occurs every second you may handle various tasks in the sectic label. It is important that you use the name SECTIC and that you return with a RETURN statement from this label. The usage of the optional SECTIC routine will use 30 bytes of the hardware stack. This option only works with the SOFT clock mode. It does not work in USER mode. [, GOSUB = SECTIC] is only for SOFT mode.  
RTC XMEGA | This option is only available for processors with an RTC (XMEGA). This option sets the RTC clock source. Valid parameters are : 1KHZ_INT32KHZ_ULP 1 kHz from internal 32 kHz ULP 1KHZ_32KHZ_CRYSTOSC 1 kHz from 32 kHz Crystal Oscillator on TOSC 1KHZ_INT32KHZ_RCOSC 1 kHz from internal 32 kHz RC Oscillator 32KHZ_32KHZ_CRYSTOSC 32 kHz from 32 kHz Crystal Oscillator on TOSC The 1KHz clocks will load the PER register with 1000-1 and the 32 KHz clock will load PER with a value of 32768-1. The overflow mode is used and you can use the compare overflow if required. Do not forget to enable the 32 KHz oscillator and the interrupts as shown in the Xmega example.  
RTC XTINY | This option is only available for processors with an RTC (XTINY). This option sets the RTC clock source. Valid parameters are : 32KHZ_32KHZ_INTOSC : 32 KHz from OSCULP32K 1KHZ_INT32KHZ_ULP : 1 KHz from OSCULP32K 32KHZ_32KHZ_CRYSTOSC : 32 KHz from XOSC32K EXT_OSC_TOSC1 : External clock from TOSC1 pin. When configuring the RTC to use either XOSC32K or the external clock on TOSC1, XOSC32K needs to be enabled and the Source Select bit (SEL) and Run Standby bit (RUNSTDBY) in the XOSC32K Control A register of the Clock Controller (CLKCTRL.XOSC32KCTRLA) must be configured accordingly.  
RTC32 | This option is available for few XMEGA chips. You can use it instead of the RTC. In fact when a processor has an RTC32, it does not have an RTC. You can not use both RTC and RTC32 together. RTC32 only accepts one value : 1KHZ_32KHZ_CRYSTOSC This also means that you must use/connect an external 32 KHz crystal. When you use the RTC32, the battery back register VBAT_CTRL is initialized and setup.   
HIGHESR | This option is available for few XMEGA chips which have RTC32 hardware. This option will set HIGH ESR mode when a value of '1' is selected. By default this option is 0/off. HIGH ESR consumes more power.   
runmode | This only applies to the XTINY. Possible values :  ENABLED : In Standby sleep mode, the peripheral continues operation DISABLED : In Standby sleep mode, the peripheral is halted  
  
When you use the CONFIG CLOCK (in soft or user mode) directive the compiler will DIM the following BYTE variables automatic : 

_sec 

_min 

_hour

_day 

_month

_year

![notice](notice.jpg)The DATETIME library will also be included by the compiler. For this reason it is important that you use CONFIG CLOCK when you use any of the date time functions.

The variables Time$ and Date$ will also be dimensioned. These are special variables since they are treated different. See [TIME$](time_.md) and [DATE$](date_.md).

Following a way to set Time$ and Date$ :

Date$ = "11/11/00"

Time$ = "02:20:00"

You can change the date format by using: Config Date = Mdy , Separator = "/" ' ANSI-Format

See [CONFIG DATE](config_date.md)

The _sec, _min and other internal variables can be changed by the user too.

But of course changing their values will change the Time$ and Date$ variables.

The compiler also creates an ISR that gets updated once a second. This works for AVR chips which can be asynchronously clocked from the TOSC1/2 pins.

TOSC1 = Timer Oscillator Pin 1

TOSC2 = Timer Oscillator Pin 2

For example the Timer/Counter 2 of an ATMEGA16 can be used as a Real Time Counter (RTC). The Timer/Counter 2 will then be asynchronously clocked from the TOSC Pin's. The Timer/Counter 2 can NOT be used for other tasks when configured in asynchronous mode.

![notice](notice.jpg)Notice that you need to connect a 32768 Hz crystal in order to use the timer in async mode, the mode that is used for the clock timer in SOFT mode. You also need to enable interrupts because of the interrupt service routine.

When you choose the USER option, only the internal variables are created (like _sec , _min , _hour....). 

With the USER option you need to write the clock code yourself (so the USER need to update for example the System Second or Secofday).

This means the one second clock must be generated by a "USER" source like a Timer which use the internal clock or an XTAL depending on the Xtal configuration.

There are so called "AVR Timer Calculator" online available where you input the clock frequency from xtal, which Timer you use (8 or 16 Bit) and the period you want to achieve (like 1 second or 1000ms) than it will give you number which you need to configure the timer.

You also configure the interrupt of the timer and then the program will jump to the timer interrupt routine where you can set the new system second.

Config Clock = User 'Use USER to write/use your own code  
  
You also need to include the following labels with config clock = user:  
  
Getdatetime:  
```vb
'called when date or time is read  
Return  
  
```
Setdate:  
```vb
'called when date$ is set  
Return  
  
```
Settime:  
```vb
'scanned when time$ is set  
Return

```
Example for config clock = user in Bascom-Simulator

Following example use $sim so it can be used in Bascom-Simulator. It uses config clock in user mode.

The second tick is generated by Timer1 and the time updated in the Timer interrupt service routine.

You can run this example direct in Bascom Simulator and you need to CLICK ON RUN BUTTON (in the simulator) go to Interrupts Tab and hit the OVF1 BUTTON to simulate an Timer interrupt.

Then you will see how the program jump to the interrupt service routine and updates the time !!

The Simulator output give you following:

01.09.09

00:00:01

00:00:02

00:00:03

00:00:04

00:00:05

00:00:06

00:00:07

That's it !

```vb
$regfile = "m16def.dat"  
$crystal = 12000000  
$hwstack = 80  
$swstack = 80  
$framesize = 80  
$baud = 19200  
$sim 'ONLY FOR SIMULATOR MODE !!!!  
  
Dim second_tick As Long  
  
Config Clock = User 'Use USER to write/use your own code  
Config Date = Dmy , Separator = . 'Day.Month.Year  
Config Timer1 = Timer , Prescale = 256  
On Timer1 Timer_irq  
```
Const Timer_preload = 18661 'Timervorgabe für Sekunden Takt  
  
```vb
Enable Timer1  
Enable Interrupts  
  
```
Date$ = "01.09.09"  
Time$ = "00:00:00"  
  
```vb
Print Date$  
  
Do  
```
!NOP  
```vb
Loop  
  
End 'end program  
  
```
Timer_irq: 'Timer1 IRQ (once per second)  
Incr Second_tick  
Time$ = Time(second_tick)  
Timer1 = Timer_preload  
  
```vb
Print Time$ 'only for Bascom-Simulator  
Return  
  
```
Settime:  
Return  
  
Getdatetime:  
Return  
  
Setdate:  
Return

Using a DS1307 with config clock

See the datetime_test1.bas example from the SAMPLES\DATETIME folder that shows how you can use a DS1307 clock chip for the date and time generation.

See also example below !

Using config clock with ATXMEGA

With ATXMEGA there are devices with 16-Bit RTC like ATXMEGA128A1 and 32-Bit RTC like ATXMEGA256A3B or ATXMEGA256A3BU. 

ATXMEGA with 16-Bit RTC:

•| Can be used with one of the two internal RC oscillator options or external 32.768kHz crystal oscillator  
---|---  
  
•| The internal 32 kHz Ultra Low Power (ULP) is a very low power clock source, and it is not designed for high accuracy.  
---|---  
  
•| If you want to use the internal 32Khz RC oscillator you need to enable it with config osc  
---|---  
  
Config Osc = Disabled , 32mhzosc = Enabled , 32khzosc = Enabled

ATXMEGA with 32-Bit RTC (for example ATXMEGA256A3B or ATXMEGA256A3BU):

•| An external 32.768kHz crystal oscillator must be used as the clock source  
---|---  
  
•| The 32-Bit RTC is combined with a Battery Backup System  
---|---  
  
Numeric Values to calculate with Date and Time:

•| SecOfDay: (Type LONG) Seconds elapsed since Midnight. 00:00:00 start with 0 to 85399 at 23:59:59.  
---|---  
  
•| SysSec: (Type LONG) Seconds elapsed since begin of century (at 2000-01-01!). 00:00:00 at 2000-01-01 start with 0 to 2147483647 (overflow of LONG-Type) at 2068-01-19 03:14:07  
---|---  
  
•| DayOfYear: (Type WORD) Days elapsed since first January of the current year.  
---|---  
  
•| First January start with 0 to 364 (365 in a leap year)  
---|---  
  
•| SysDay: (Type WORD) Days elapsed since begin of century (at 2000-01-01!). 2000-01-01 starts with 0 to 36524 at 2099-12-31  
---|---  
  
•| DayOfWeek: (Type Byte) Days elapsed since Monday of current week. Monday start with 0 to Sunday = 6  
---|---  
  
With the numeric type calculations with Time and date are possible. Type 1 (discrete Bytes) and 2 (Strings) can be converted to an according numeric value. Than Seconds (at SecOfDay and SysSec) or Days (at DayOfYear, SysDay), can be added or subtracted. The Result can be converted back.

See also

[TIME$](time_.md) , [DATE$](date_.md) , [CONFIG DATE](config_date.md), [Memory usage](memory_usage.md), [Date and Time Routines](datetime.md)

ASM

The following ASM routines are called from datetime.lib

_soft_clock. This is the ISR that gets called once per second.

Example 1

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
Xmega Sample 

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-RTC.bas  
' This sample demonstrates the Xmega128A1 RTC  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
Config Portb = Output  
  
'First Enable The Osc Of Your Choice , make sure to enable 32 KHz clock or use an external 32 KHz clock  
Config Osc = Enabled , 32mhzosc = Enabled , 32khzosc = Enabled  
' For the CLOCK we use the RTC so make sure the 32 KHZ osc is enabled!!!  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
```
Open "COM1:" For Binary As #1  
  
```vb
Config Clock = Soft , Rtc = 1khz_int32khz_ulp ' we select the internal 1 KHz clock from the 32KHz internal oscillator  
'the following clocks can be used to clock the RTC  
' 1KHZ_INT32KHZ_ULP 1 kHz from internal 32 kHz ULP  
' 1KHZ_32KHZ_CRYSTOSC 1 kHz from 32 kHz Crystal Oscillator on TOSC  
' 1KHZ_INT32KHZ_RCOSC 1 kHz from internal 32 kHz RC Oscillator  
' 32KHZ_32KHZ_CRYSTOSC 32 kHz from 32 kHz Crystal Oscillator on TOSC  
  
  
Config Priority = Static , Vector = Application , Lo = Enabled ' the RTC uses LO priority interrupts so these must be enabled !!!  
Enable Interrupts ' as usual interrupts must be enabled  
  
Do  
Print Time$ ' print the time  
Waitms 1000  
Loop  
  
'TO USE THE SECTIC in the sample you must use GOSUB=SECTIC in CONFIG CLOCK !!!

  
```
Sectic:  
```vb
Toggle Portb 'optional toggle some leds when using the gosub=sectic option  
Return

```
Example 2

  
```vb
$regfile = "m128def.dat"  
$hwstack = 80  
$swstack = 80  
$framesize = 160  
$crystal = 8000000  
$baud = 19200  
  
Enable Interrupts  
  
'[now init the clock]  
Config Date = Mdy , Separator = / ' ANSI-Format  
  
Config Clock = Soft 'this is how simple it is  
'The above statement will bind in an ISR so you can not use the TIMER anymore!  
  
'assign the date to the reserved date$  
'The format is MM/DD/YY  
```
Date$ = "11/11/05"  
  
```vb
'assign the time, format in hh:mm:ss military format(24 hours)  
'You may not use 1:2:3 !! adding support for this would mean overhead  
'But of course you can alter the library routines used  
  
```
Time$ = "23:59:50"  
```vb
Do  
Waitms 500  
Print Date$ ; Spc(3) ; Time$  
Loop

```
Example 3 (using DS1307 with Config clock)

```vb
'-------------------------------------------------------------------------------  
' DateTime_test.bas  
' This sample show how to use the Date-Time routines from the DateTime.Lib  
' written by Josef Franz Vögel  
'-------------------------------------------------------------------------------  
  
$regfile = "m328pdef.dat"  
$crystal = 12e6 '16MHz  
$hwstack = 80  
$swstack = 80  
$framesize = 160  
  
  
```
Const Clockmode = 1  
```vb
'use i2c for the clock  
  

#if Clockmode = 1  
Config Clock = Soft ' we use build in clock  
Disable Interrupts  

#else  
Config Clock = User ' we use I2C for the clock  
'configure the scl and sda pins (using software I2C routines)  
Config Sda = Portd.6  
Config Scl = Portd.5  
```
I2cinit  
  
'address of ds1307  
Const Ds1307w = &HD0 ' Addresses of Ds1307 clock  
Const Ds1307r = &HD1  

```vb
#endif  
  
  
'configure the date format  
Config Date = Ymd , Separator = - ' ANSI-Format  
'This sample does not have the clock started so interrupts are not enabled  
' Enable Interrupts  
  
'dim the used variables  
Dim Lvar1 As Long  
Dim Mday As Byte  
Dim Bweekday As Byte , Strweekday As String * 10  
Dim Strdate As String * 8  
Dim Strtime As String * 8  
Dim Bsec As Byte , Bmin As Byte , Bhour As Byte  
Dim Bday As Byte , Bmonth As Byte , Byear As Byte  
Dim Lsecofday As Long  
Dim Wsysday As Word  
Dim Lsyssec As Long  
Dim Wdayofyear As Word  
  
  
  
  
' =================== DayOfWeek =============================================  
' Example 1 with internal RTC-Clock  
  
```
_day = 4 : _month = 11 : _year = 2 ' Load RTC-Clock for example - testing  
Bweekday = Dayofweek()  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of " ; Date$ ; " is " ; Bweekday ; " = " ; Strweekday  
  
  
' Example 2 with defined Clock - Bytes (Day / Month / Year)  
```
Bday = 26 : Bmonth = 11 : Byear = 2  
Bweekday = Dayofweek(bday)  
Strweekday = Lookupstr(bweekday , Weekdays)  
Strdate = Date(bday)  
```vb
Print "Weekday-Number of Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " is " ; Bweekday ; " (" ; Date(bday) ; ") = " ; Strweekday  
  
  
' Example 3 with System Day  
```
Wsysday = 2000 ' that is 2005-06-23  
Bweekday = Dayofweek(wsysday)  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of System Day " ; Wsysday ; " (" ; Date(wsysday) ; ") is " ; Bweekday ; " = " ; Strweekday  
  
  
  
' Example 4 with System Second  
```
Lsyssec = 123456789 ' that is 2003-11-29 at 21:33:09  
Bweekday = Dayofweek(lsyssec)  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of System Second " ; Lsyssec ; " (" ; Date(lsyssec) ; ") is " ; Bweekday ; " = " ; Strweekday  
  
  
  
  
' Example 5 with Date-String  
```
Strdate = "04-11-02" ' we have configured Date in ANSI  
Bweekday = Dayofweek(strdate)  
Strweekday = Lookupstr(bweekday , Weekdays)  
```vb
Print "Weekday-Number of " ; Strdate ; " is " ; Bweekday ; " = " ; Strweekday  
  
  
  
  
' ================= Second of Day =============================================  
' Example 1 with internal RTC-Clock  
```
_sec = 12 : _min = 30 : _hour = 18 ' Load RTC-Clock for example - testing  
  
Lsecofday = Secofday()  
```vb
Print "Second of Day of " ; Time$ ; " is " ; Lsecofday  
  
  
' Example 2 with defined Clock - Bytes (Second / Minute / Hour)  
```
Bsec = 20 : Bmin = 1 : Bhour = 7  
Lsecofday = Secofday(bsec)  
```vb
Print "Second of Day of Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " (" ; Time(bsec) ; ") is " ; Lsecofday  
  
  
' Example 3 with System Second  
```
Lsyssec = 1234456789  
Lsecofday = Secofday(lsyssec)  
```vb
Print "Second of Day of System Second " ; Lsyssec ; "(" ; Time(lsyssec) ; ") is " ; Lsecofday  
  
  
' Example 4 with Time - String  
```
Strtime = "04:58:37"  
Lsecofday = Secofday(strtime)  
```vb
Print "Second of Day of " ; Strtime ; " is " ; Lsecofday  
  
  
  
' ================== System Second ============================================  
  
' Example 1 with internal RTC-Clock  
' Load RTC-Clock for example - testing  
```
_sec = 17 : _min = 35 : _hour = 8 : _day = 16 : _month = 4 : _year = 3  
  
Lsyssec = Syssec()  
```vb
Print "System Second of " ; Time$ ; " at " ; Date$ ; " is " ; Lsyssec  
  
  
' Example 2 with with defined Clock - Bytes (Second, Minute, Hour, Day / Month / Year)  
```
Bsec = 20 : Bmin = 1 : Bhour = 7 : Bday = 22 : Bmonth = 12 : Byear = 1  
Lsyssec = Syssec(bsec)  
Strtime = Time(bsec)  
Strdate = Date(bday)  
```vb
Print "System Second of " ; Strtime ; " at " ; Strdate ; " is " ; Lsyssec  
  
  
' Example 3 with System Day  
  
```
Wsysday = 2000  
Lsyssec = Syssec(wsysday)  
```vb
Print "System Second of System Day " ; Wsysday ; " (" ; Date(wsysday) ; " 00:00:00) is " ; Lsyssec  
  
  
' Example 4 with Time and Date String  
```
Strtime = "10:23:50"  
Strdate = "02-11-29" ' ANSI-Date  
Lsyssec = Syssec(strtime , Strdate)  
```vb
Print "System Second of " ; Strtime ; " at " ; Strdate ; " is " ; Lsyssec ' 91880630  
  
  
  
  
' ==================== Day Of Year =========================================  
' Example 1 with internal RTC-Clock  
```
_day = 20 : _month = 11 : _year = 2 ' Load RTC-Clock for example - testing  
Wdayofyear = Dayofyear()  
```vb
Print "Day Of Year of " ; Date$ ; " is " ; Wdayofyear  
  
  
' Example 2 with defined Clock - Bytes (Day / Month / Year)  
```
Bday = 24 : Bmonth = 5 : Byear = 8  
Wdayofyear = Dayofyear(bday)  
```vb
Print "Day Of Year of Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(bday) ; ") is " ; Wdayofyear  
  
  
  
' Example 3 with Date - String  
```
Strdate = "04-10-29" ' we have configured ANSI Format  
Wdayofyear = Dayofyear(strdate)  
```vb
Print "Day Of Year of " ; Strdate ; " is " ; Wdayofyear  
  
  
' Example 4 with System Second  
  
```
Lsyssec = 123456789  
Wdayofyear = Dayofyear(lsyssec)  
```vb
Print "Day Of Year of System Second " ; Lsyssec ; " (" ; Date(lsyssec) ; ") is " ; Wdayofyear  
  
  
' Example 5 with System Day  
```
Wsysday = 3000  
Wdayofyear = Dayofyear(wsysday)  
```vb
Print "Day Of Year of System Day " ; Wsysday ; " (" ; Date(wsysday) ; ") is " ; Wdayofyear  
  
  
  
  
  
' =================== System Day ======================================  
' Example 1 with internal RTC-Clock  
```
_day = 20 : _month = 11 : _year = 2 ' Load RTC-Clock for example - testing  
Wsysday = Sysday()  
```vb
Print "System Day of " ; Date$ ; " is " ; Wsysday  
  
  
' Example 2 with defined Clock - Bytes (Day / Month / Year)  
```
Bday = 24 : Bmonth = 5 : Byear = 8  
Wsysday = Sysday(bday)  
```vb
Print "System Day of Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(bday) ; ") is " ; Wsysday  
  
  
' Example 3 with Date - String  
```
Strdate = "04-10-29"  
Wsysday = Sysday(strdate)  
```vb
Print "System Day of " ; Strdate ; " is " ; Wsysday  
  
' Example 4 with System Second  
```
Lsyssec = 123456789  
Wsysday = Sysday(lsyssec)  
```vb
Print "System Day of System Second " ; Lsyssec ; " (" ; Date(lsyssec) ; ") is " ; Wsysday  
  
  
  
' =================== Time ================================================  
' Example 1: Converting defined Clock - Bytes (Second / Minute / Hour) to Time - String  
```
Bsec = 20 : Bmin = 1 : Bhour = 7  
Strtime = Time(bsec)  
```vb
Print "Time values: Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " converted to string " ; Strtime  
  
  
' Example 2: Converting System Second to Time - String  
```
Lsyssec = 123456789  
Strtime = Time(lsyssec)  
```vb
Print "Time of Systemsecond " ; Lsyssec ; " is " ; Strtime  
  
  
' Example 3: Converting Second of Day to Time - String  
```
Lsecofday = 12345  
Strtime = Time(lsecofday)  
```vb
Print "Time of Second of Day " ; Lsecofday ; " is " ; Strtime  
  
  
' Example 4: Converting System Second to defined Clock - Bytes (Second / Minute / Hour)  
  
```
Lsyssec = 123456789  
Bsec = Time(lsyssec)  
```vb
Print "System Second " ; Lsyssec ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " (" ; Time(lsyssec) ; ")"  
  
  
  
' Example 5: Converting Second of Day to defined Clock - Bytes (Second / Minute / Hour)  
```
Lsecofday = 12345  
Bsec = Time(lsecofday)  
```vb
Print "Second of Day " ; Lsecofday ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " (" ; Time(lsecofday) ; ")"  
  
' Example 6: Converting Time-string to defined Clock - Bytes (Second / Minute / Hour)  
```
Strtime = "07:33:12"  
Bsec = Time(strtime)  
```vb
Print "Time " ; Strtime ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour  
  
  
  
' ============================= Date ==========================================  
  
' Example 1: Converting defined Clock - Bytes (Day / Month / Year) to Date - String  
```
Bday = 29 : Bmonth = 4 : Byear = 12  
Strdate = Date(bday)  
```vb
Print "Dat values: Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " converted to string " ; Strdate  
  
  
' Example 2: Converting from System Day to Date - String  
```
Wsysday = 1234  
Strdate = Date(wsysday)  
```vb
Print "System Day " ; Wsysday ; " is " ; Strdate  
  
  
' Example 3: Converting from System Second to Date String  
```
Lsyssec = 123456789  
Strdate = Date(lsyssec)  
```vb
Print "System Second " ; Lsyssec ; " is " ; Strdate  
  
  
' Example 4: Converting SystemDay to defined Clock - Bytes (Day / Month / Year)  
  
```
Wsysday = 2000  
Bday = Date(wsysday)  
```vb
Print "System Day " ; Wsysday ; " converted to Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(wsysday) ; ")"  
  
  
' Example 5: Converting Date - String to defined Clock - Bytes (Day / Month / Year)  
```
Strdate = "04-08-31"  
Bday = Date(strdate)  
```vb
Print "Date " ; Strdate ; " converted to Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear  
  
  
' Example 6: Converting System Second to defined Clock - Bytes (Day / Month / Year)  
```
Lsyssec = 123456789  
Bday = Date(lsyssec)  
```vb
Print "System Second " ; Lsyssec ; " converted to Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " (" ; Date(lsyssec) ; ")"  
  
  
  
' ================ Second of Day elapsed  
  
```
Lsecofday = Secofday()  
_hour = _hour + 1  
Lvar1 = Secelapsed(lsecofday)  
Print Lvar1  
  
Lsyssec = Syssec()  
_day = _day + 1  
Lvar1 = Syssecelapsed(lsyssec)  
Print Lvar1  
  
  
  
  
  
  
Looptest:  
  
' Initialising for testing  
_day = 1  
_month = 1  
_year = 1  
_sec = 12  
_min = 13  
_hour = 14  
  
  
  
```vb
Do  
If _year > 50 Then  
Exit Do  
End If  
  
```
_sec = _sec + 7  
If _sec > 59 Then  
Incr _min  
_sec = _sec - 60  
End If  
  
_min = _min + 2  
If _min > 59 Then  
Incr _hour  
_min = _min - 60  
End If  
  
_hour = _hour + 1  
If _hour > 23 Then  
Incr _day  
_hour = _hour - 24  
End If  
  
_day = _day + 1  
  
  
```vb
If _day > 28 Then  
Select Case _month  
Case 1  
```
Mday = 31  
Case 2  
Mday = _year And &H03  
If Mday = 0 Then  
Mday = 29  
Else  
Mday = 28  
```vb
End If  
Case 3  
```
Mday = 31  
Case 4  
Mday = 30  
Case 5  
Mday = 31  
Case 6  
Mday = 30  
Case 7  
Mday = 31  
Case 8  
Mday = 31  
Case 9  
Mday = 30  
Case 10  
Mday = 31  
Case 11  
Mday = 30  
Case 12  
Mday = 31  
```vb
End Select  
If _day > Mday Then  
```
_day = _day - Mday  
Incr _month  
If _month > 12 Then  
_month = 1  
Incr _year  
```vb
End If  
End If  
End If  
If _year > 99 Then  
Exit Do  
End If  
  
```
Lsecofday = Secofday()  
Lsyssec = Syssec()  
Bweekday = Dayofweek()  
Wdayofyear = Dayofyear()  
Wsysday = Sysday()  
  
  
```vb
Print Time$ ; " " ; Date$ ; " " ; Lsecofday ; " " ; Lsyssec ; " " ; Bweekday ; " " ; Wdayofyear ; " " ; Wsysday  
  
  
Loop  
End  
  
  
'only when we use I2C for the clock we need to set the clock date time  

#if Clockmode = 0  
'called from datetime.lib  
Dim Weekday As Byte  
```
Getdatetime:  
I2cstart ' Generate start code  
I2cwbyte Ds1307w ' send address  
I2cwbyte 0 ' start address in 1307  
  
I2cstart ' Generate start code  
I2cwbyte Ds1307r ' send address  
I2crbyte _sec , Ack  
I2crbyte _min , Ack ' MINUTES  
I2crbyte _hour , Ack ' Hours  
I2crbyte Weekday , Ack ' Day of Week  
I2crbyte _day , Ack ' Day of Month  
I2crbyte _month , Ack ' Month of Year  
I2crbyte _year , Nack ' Year  
I2cstop  
_sec = Makedec(_sec) : _min = Makedec(_min) : _hour = Makedec(_hour)  
_day = Makedec(_day) : _month = Makedec(_month) : _year = Makedec(_year)  
Return  
  
Setdate:  
_day = Makebcd(_day) : _month = Makebcd(_month) : _year = Makebcd(_year)  
I2cstart ' Generate start code  
I2cwbyte Ds1307w ' send address  
I2cwbyte 4 ' starting address in 1307  
I2cwbyte _day ' Send Data to SECONDS  
I2cwbyte _month ' MINUTES  
I2cwbyte _year ' Hours  
I2cstop  
Return  
  
Settime:  
_sec = Makebcd(_sec) : _min = Makebcd(_min) : _hour = Makebcd(_hour)  
I2cstart ' Generate start code  
I2cwbyte Ds1307w ' send address  
I2cwbyte 0 ' starting address in 1307  
I2cwbyte _sec ' Send Data to SECONDS  
I2cwbyte _min ' MINUTES  
I2cwbyte _hour ' Hours  
I2cstop  
```vb
Return  
  

#endif  
  
  
```
Weekdays:  
Data "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"