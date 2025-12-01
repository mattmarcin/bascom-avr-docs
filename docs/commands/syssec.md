# SYSSEC

Action

Returns a Number, which represents the System Second

Syntax

Target = SYSSEC()

Target = SYSSEC(bSecMinHour)

Target = SYSSEC(strTime, strDate)

Target = SYSSEC(wSysDay)

Remarks

Target | A Variable (LONG), that is assigned with the System-Second  
---|---  
BSecMinHour | A Byte, which holds the Sec-value followed by Min(Byte), Hour (Byte), Day(Byte), Month(Byte) and Year(Byte)  
StrTime | A time-string in the format âhh:mm:ss"  
StrDate | A date-string in the format specified in the Config Date statement  
wSysDay | A variable (Word) which holds the System Day (SysDay)  
  
The Function can be used with 4 different kind of inputs:

1.| Without any parameter. The internal Time and Date of SOFTCLOCK (_sec, _min, _hour, _day, _month, _year) is used.  
---|---  
  
2.| With a user defined time and Date array. It must be arranged in same way (Second, Minute, Hour, Day, Month, Year) as the internal SOFTCLOCK time/date. The first Byte (Second) is the input by this kind of usage. So the System Second can be calculated of every time/date.  
---|---  
  
3.| With a time-String and a date-string. The time-string must be in the Format âhh:mm:ss". The date-string must be in the format specified in the Config Date statement  
---|---  
  
4.| With a System Day Number (Word). The result is the System Second of this day at 00:00:00.  
---|---  
  
The Return-Value is in the Range of 0 to 2147483647. 2000-01-01 at 00:00:00 starts with 0.

The Function is valid from 2000-01-01 to 2068-01-19 03:14:07. In the year 2068 a LONG â overflow will occur.

Unix time stamp starts 1-1-1970 which will limit the use till 2038.

Bascom time stamp starts 1-1-2000 giving longer working time.

If you wish to convert to NTP which starts at 1.1.1970, which is 30 years earlier, you need to subtract a value of 946684800

BASCOM DATE_TIME = NTP - 946684800

See also

[Date and Time Routines](datetime.md) , [SYSSECELAPSED](syssecelapsed.md), [SYSDAY](sysday.md)

Example

```vb
Enable Interrupts

Config Clock = Soft

Config Date = YMD , Separator =.' ANSI-Format

Dim Strdate As String * 8

Dim Strtime As String * 8

Dim Bsec As Byte , Bmin As Byte , Bhour As Byte

Dim Bday As Byte , Bmonth As Byte , Byear As Byte

Dim Wsysday As Word

Dim Lsyssec As Long

' Example 1 with internal RTC-Clock

' Load RTC-Clock for example - testing

```
_sec = 17 : _min = 35 : _hour = 8 : _day = 16 : _month = 4 : _year = 3

Lsyssec = Syssec()

```vb
Print "System Second of " ; Time$ ; " at " ; Date$ ; " is " ; Lsyssec

' System Second of 08:35:17 at 03.04.16 is 103797317

' Example 2 with with defined Clock - Bytes (Second, Minute, Hour, Day / Month / Year)

```
Bsec = 20 : Bmin = 1 : Bhour = 7 : Bday = 22 : Bmonth = 12 : Byear = 1

Lsyssec = Syssec(bsec)

Strtime = Time_sb(bsec) : Strdate = Date_sb(bday)

```vb
Print "System Second of " ; Strtime ; " at " ; Strdate ; " is " ; Lsyssec

' System Second of 07:01:20 at 01.12.22 is 62319680

' Example 3 with Time and Date - String

```
Strtime = "04:58:37"

strDate ="02.09.18"

Lsyssec = Syssec(strtime , Strdate)

```vb
Print "System Second of " ; Strtime ; " at " ; Strdate ; " is " ; Lsyssec

' System Second of 04:58:37 at 02.09.18 is 85640317

' Example 4 with System Day

```
Wsysday = 2000

Lsyssec = Syssec(wsysday)

```vb
Print "System Second of System Day " ; Wsysday ; " (00:00:00) is " ; Lsyssec

' System Second of System Day 2000 (00:00:00) is 172800000 

```