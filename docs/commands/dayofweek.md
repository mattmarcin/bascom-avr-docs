# DAYOFWEEK

Action

Returns the Day of the Week of a Date.

Syntax

Target = DayOfWeek()

Target = DayOfWeek(bDayMonthYear)

Target = DayOfWeek(strDate)

Target = DayOfWeek(wSysDay)

Target = DayOfWeek(lSysSec)

Remarks

Target | A Byte â variable, that is assigned with the day of the week  
---|---  
BDayMonthYear | A Byte â variable, which holds the Day-value followed by Month(Byte) and Year (Byte)  
StrDate | A String, which holds a Date-String in the format specified in the CONFIG DATE statement  
WSysDay | A Word â variable, which holds the System Day (SysDay)  
LSysSec | A Long â variable, which holds the System Second (SysSec)  
  
The Function can be used with five different kind of Input:

1.| Without any parameter. The internal Date-values of SOFTCLOCK (_day, _month, _year) are used.  
---|---  
  
2.| With a user defined date array. It must be arranged in same way (Day, Month, Year) as the internal SOFTCLOCK date. The first Byte (Day) is the input by this kind of usage. So the Day of the Week can be calculated of every date.  
---|---  
  
3.| With a Date-String. The date-string must be in the Format specified in the Config Date Statement  
---|---  
  
4.| With a System Day â Number.  
---|---  
  
5.| With a System Second - Number  
---|---  
  
The Return-Value is in the range of 0 to 6, Monday starts with 0.

The Function is valid in the 21th century (from 2000-01-01 to 2099-12-31).

See Also

[Date and Time routines](datetime.md) , [CONFIG DATE](config_date.md) , [CONFIG CLOCK](config_clock.md), [SYSDAY](sysday.md), [SYSSEC](syssec.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : datetime_test1,bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : show how to use the Date-Time routines from the DateTime.Lib

'micro : Mega103

'suited for demo : no

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m103def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

```
Const Clockmode = 1

```vb
'use i2c for the clock

#if Clockmode = 1

Config Clock = Soft ' we use build in clock

Disable Interrupts

#else

Config Clock = User ' we use I2C for the clock

'configure the scl and sda pins

Config Sda = Portd.6

Config Scl = Portd.5

'address of ds1307

```
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