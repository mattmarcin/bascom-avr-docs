# CONFIG WATCHDOG

Action

Configures the watchdog timer.

Syntax

CONFIG WATCHDOG = time 

Syntax XTINY

CONFIG WATCHDOG = time [,window=time]

Remarks

Time | The interval constant in ms the watchdog timer will count to before it will reset your program. Possible settings : 16 , 32, 64 , 128 , 256 , 512 , 1024 and 2048. Some newer chips : 4096, 8192. The XMEGA has a 1 KHz clocked watchdog. For Xmega the following value in millisecond need to be used : 8 ,16,32,64,125,250,500,1000,2000,4000,8000  So 2000 will sets a timeout of 2 seconds. The XTINY platform accepts the following values : 0 - will turn off the WD 8 - 8 clock cycles which is 7.8 ms 16 - 16 clock cycles which is 16.625 ms 32 - 32 clock cycles which is 32.25 ms 64 - 64 clock cycles which is 62.5 ms 128 - 128 clock cycles which is 0.125 ms 256 - 256 clock cycles which is 0.250 ms 512 - 512 clock cycles which is 0.500 ms 1000 - 1000 clock cycles which is 1 sec 2000 - 2000 clock cycles which is 2 sec 4000 - 4000 clock cycles which is 4 sec 8000 - 8000 clock cycles which is 8 sec The Xtiny also has an optional window value that can be set.  
---|---  
  
Note that some new AVR's might have additional reset values such as 4096 and 8192.

Normal AVR

When the WatchDog is started, a reset will occur after the specified number of mS.

With a value of 2048, a reset will occur after 2 seconds, so you need to reset the WD in your programs periodically with the RESET WATCHDOG statement.

Some AVR's might have the WD timer enabled by default. You can change this by changing the Fuse Bits.

![notice](notice.jpg)Global Interrupts should be disabled when they are active. The reason is that changing the WD, a special timed sequence is required. An interrupt could extend the time, making the timed sequence fail.

![notice](notice.jpg)After the CONFIG WATCHDOG statement, the watchdog timer is disabled. You can also use CONFIG WATCHDOG to change the time out value. This will stop the watchdog timer and load the new value.

After a CONFIG WATCHDOG, you always need to start the Watchdog with the START WATCHDOG statement.

Most new AVR chips have an MCUSR register that contains some flags. One of the flags is the WDRF bit. This bit is set when the chip was reset by a Watchdog overflow. The CONFIG WATCHDOG will clear this bit, provided that the register and bit are available in the micro.

When it is important to examine at startup if the micro was reset by a Watchdog overflow, you need to examine this MCUSR.WDRF flag before you use CONFIG WATCHDOG, since that will clear the flag.

ALL PLATFORMS

![notice](notice.jpg)For chips that have an enhanced WD timer, the WD timer is cleared as part of the chip initialize procedure. This because otherwise the WD timer will only work once. If it is important to know the cause of the reset, you can read the register R0 before you run other code.

When the chip resets, the status registers with the reset cause bits is saved into register R0.

This is done because the compiler need to reset these flags since otherwise they can not occur again. And before clearing the bits, the status is saved into register R0.

The sample below demonstrates how to store the WDRF bit if you need it, and print it later. 

The compiler will read R0 from the correct register which depends on the used platform (normal AVR, Xmega, Xtiny)

XTINY

The XTINY platform differs from the normal AVR. The WD timer will be turned off with a value of 0. Normal AVR use a bit for that.

When you use STOP WATCHDOG, a value of 0 will be written to the control register to turn off the WD.

This also means that when you configure the Watchdog with a value other than 0, it will start immediately.

Since there is no control bit it means that START WATCHDOG will only work when the WD timer has been previously configured with a value other than 0.

This value will be written to the Watchdog in order to start it.

When there is no window value provided, the watchdog timer is in the normal mode. In the normal mode a single time out period is set for the WDT. 

If the WDT is not reset during the defined time-out period, the WDT will issue a system reset.

In order to prevent overflow of the WDT a reset must be done using : RESET WATCHDOG statement.

When a window value is defined the WDT will be in window mode. In window mode the WDT uses two different time-out periods :

\- the closed window time-out period (TOwdtw) define a duration from 8 ms to 8 sec where the WDT can not be reset. If the WDT is reset during this period, the WDT will issue a system reset.

\- the open window time-out period (TOwdt) which is also 8 ms to 8s sec, defines the open period during which the WDT can (and needs to) be reset. The open period will always follow the closed period, so the total duration of the time-out perio is the sum of the closed window and the open window time-out periods.

The following picture is taken from the datasheet 

![wd_xtiny_window](wd_xtiny_window.png)

![notice](notice.jpg)When setting the Watchdog FUSE , this value is loaded when the processor boots. After that this value can not be changed since a LOCK bit is set.

This also means that when using the FUSE you can not stop the watchdog.

See also

[START WATCHDOG ](start.md), [STOP WATCHDOG ](stop.md), [RESET WATCHDOG](reset.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : watchd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates the watchdog timer

'micro : Mega88

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m88def.dat" ' specify the used micro

$crystal = 8000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 32 ' default use 32 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim B As Byte

Dim Wdbit As Bit

Dim bWD As Byte

```
bWD= R0 ' read the wd flag

```vb
Print "Watchdog test" 

If bwd.wdrf = 1 Then ' there was a WD overflow

```
Wdbit = 1 'store the flag

```vb
End If

Config Watchdog = 2048 'reset after 2048 mSec

If Wdbit = 1 Then 'just print it now since it is important that CONFIG WATCHDOG runs early as possible

Print "Micro was reset by Watchdog overflow"

End If

```
Start Watchdog 'start the watchdog timer

```vb
Dim I As Word

For I = 1 To 1000

Waitms 100

Print I 'print value

```
B = Inkey() ' get a key from the serial port

If B = 65 Then 'letter A pressed

Stop Watchdog ' test if the WD will stop

Elseif B = 66 Then 'letter B pressed

Config Watchdog = 4096 'reconfig to 4 sec

Start Watchdog 'CONFIG WATCHDOG will disable the WD so start it

Elseif B = 67 Then 'C pressed

```vb
Config Watchdog = 8192 ' some have 8 sec timer

'observe that the WD timer is OFF

```
Elseif B = 68 Then 'D pressed

Start Watchdog ' start it

```vb
End If

'Reset Watchdog

'you will notice that the for next doesnt finish because of the reset

'when you unmark the RESET WATCHDOG statement it will finish because the

'wd-timer is reset before it reaches 2048 msec

'When you press 'A' you will see that the WD will stop

'When you press 'B' you will see that the WD will time out after 4 Sec

'When you press 'C' you will see the WD will stop

'When you press 'D' you will see the WD will start again timing out after 8 secs

Next

End

```
And this shows how to read the register r0:

Dim Breset As Byte

Breset = R0

When you show this value on an LCD display you will see a value of 7 the first time, and later a value of 15 when the WD reset occured.

Xmega Sample

```vb
'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' xm128-WD.bas  
' This sample demonstrates the Xmega128A1 Watchdog  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
'First Enable The Osc Of Your Choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Config Input1 = Cr , Echo = Crlf ' CR is used for input, we echo back CR and LF  
  
```
Open "COM1:" For Binary As #1  
```vb
' ^^^^ change from COM1-COM8  
  
Print #1 , "Xmega revision:" ; Mcu_revid ' make sure it is 7 or higher !!! lower revs have many flaws  
  
Config Watchdog = 4000 'after 4 seconds a reset will occur if the watchdog is enabled  
'possible value : 8 ,16,32,64,125,250,500,1000,2000,4000,8000  
'these values are clock cycles, based on a 1 KHz clock !!!  
  
Dim W As Word , B As Byte  
Do  
```
W = W + 1  
```vb
Print W  
Waitms 500  
```
B = Inkey()  
If B = "a" Then  
Start Watchdog  
Print "start"  
Elseif B = "b" Then  
Stop Watchdog  
Print "stop"  
Elseif B = "c" Then  
```vb
Config Watchdog = 8000  
Print "8 sec"  
```
Elseif B = "d" Then  
```vb
Reset Watchdog  
Print "reset"  
End If  
Loop

```
XTINY Sample

```vb
'--------------------------------------------------------------------------------  
'name : watchdog-avrx128da28.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates Watchdog  
'micro : avra128DA28  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "AVRX128da28.dat"  
  
$crystal = 24000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
Config Submode = New  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'configure the USART  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Config Clock = Soft , Rtc = 32khz_32khz_intosc  
'the RTC requires that global interrupts are enabled  
Enable Interrupts  
  
  
Print "Test WD"  
  
'time out after 8 sec  
'a configuration other then 0 will start the watchdog  
'a configuration of 0 will turn off the watchdog  
Config Watchdog = 8000  
Dim B As Byte  
  
  
Do  
```
B = Inkey()  
```vb
Select Case B  
Case "r" : Reset Watchdog 'reset WD  
Case "s" : Config Watchdog = 8000 'set back to value used in config above  
Case "q" : Config Watchdog = 0 'turn off WD  
Case "1" : Config Watchdog = 1000 'set time out to 1 sec  
Case "2" : Config Watchdog = 2000 'set time out to 2 sec  
Case "4" : Config Watchdog = 4000 'set time out to 4 sec  
Case "8" : Config Watchdog = 8000 'set time out to 8 sec  
End Select  
  
Print "WD:" ; Time$ 'now watch the time  
Waitms 1000  
Loop  
  
End

```
Xtiny Example 2

```vb
'--------------------------------------------------------------------------------  
'name : watchdog.bas  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates Watchdog  
'micro : xtiny816  
'suited for demo : no  
'commercial addon needed : yes  
'--------------------------------------------------------------------------------  
$regfile = "atxtiny816.dat"  
$crystal = 20000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
Dim Bwd As Byte  
```
R0 = Bwd 'store R0 into variable so we can check the reset cause  
```vb
'set the system clock and prescaler  
Config Sysclock = 16_20mhz , Prescale = 1  
  
'configure the USART  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
Config Clock = Soft , Rtc = 32khz_32khz_intosc  
'the RTC requires that global interrupts are enabled  
Enable Interrupts  
  
  
Print "Test WD, reset cause:"  
If Bwd.0 = 1 Then  
Print "power on reset"  
End If  
If Bwd.1 = 1 Then  
Print "brown out reset"  
End If  
If Bwd.2 = 1 Then  
Print "external reset"  
End If  
If Bwd.3 = 1 Then  
Print "watchdog reset"  
End If  
If Bwd.4 = 1 Then  
Print "software reset"  
End If  
If Bwd.5 = 1 Then  
Print "UPDI reset"  
End If  
  
'time out after 8 sec  
Config Watchdog = 8000  
  
Do  
Print "WD:" ; Time$  
Waitms 1000  
Loop  
  
End

```