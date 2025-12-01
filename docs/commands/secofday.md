# SECOFDAY

Action

Returns the Seconds of a Day.

Syntax

Target = SECOFDAY()

Target = SECOFDAY(bSecMinHour)

Target = SECOFDAY(strTime)

Target = SECOFDAY(lSysSec)

Remarks

Target | A variable (LONG), that is assigned with the Seconds of the Day  
---|---  
bSecMinHour | A Byte, which holds the Second-value followed by Minute(Byte) and Hour(Byte)  
strTime | A String, which holds the time in the format âhh:mm:ss"  
LSysSec | A Variable (Long) which holds the System Second  
  
The Function can be used with 4 different kind of inputs:

1.| Without any parameter. The internal Time of SOFTCLOCK (_sec, _min, _hour) is used.  
---|---  
  
2.| With a user defined time array. It must be arranged in same way (Second, Minute, Hour) as the internal SOFTCLOCK time. The first Byte (Second) is the input by this kind of usage. So the Second of Day can be calculated of every time.  
---|---  
  
3.| With a time-String. The time-string must be in the Format âhh:mm:ss".  
---|---  
  
4.| With a System Second Number (LONG)  
---|---  
  
The Return-Value is in the range of 0 to 86399 from 00:00:00 to 23:59:59.

No validity-check of input is made.

See also

[Date and Time Routines](datetime.md) , [SysSec](syssec.md)

Partial Example

```vb
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

Print "Second of Day of " ; Strtime ; " is " ; Lsecofday