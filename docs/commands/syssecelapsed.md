# SYSSECELAPSED

Action

Returns the elapsed Seconds to a earlier assigned system-time-stamp.

Syntax

Target = SysSecElapsed(SystemTimeStamp)

Remarks

Target | A variable (LONG), that is assigned with the elapsed Seconds  
---|---  
SystemTimeStamp | A variable (LONG), which holds a Systemtimestamp like the output of an earlier called SysSec()  
  
The Return-Value is in the Range of 0 to 2147483647. The Function is valid from 2000-01-01 to 2068-01-19 at 03:14:07. In the year 2068 a LONG â overflow will occur.

The difference to the pair DayOfSec and SecElapsed is, that SysSec and SysSecElapsed can be used for event distances larger than 24 hours.

See also

[Date and Time Routines](datetime.md) , [SECELAPSED](secelapsed.md), [SYSSEC](syssec.md)

Example

```vb
Enable Interrupts

Config Clock = Soft

Dim Lsystemtimestamp As Long

Dim Lsystemsecondselapsed As Long

```
Lsystemtimestamp = Syssec()

```vb
Print "Now it's " ; Lsystemtimestamp ; " seconds past 2000-01-01 00:00:00"

' do other stuff

' some time later

```
Lsystemsecondselapsed = Syssecelapsed(lsystemtimestamp)

Print "Now it's " ; Lsystemsecondselapsed ; " seconds later"