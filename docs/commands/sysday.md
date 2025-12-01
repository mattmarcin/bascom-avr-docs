# SYSDAY

Action

Returns a number, which represents the System Day

Syntax

Target = SysDay()

Target = SysDay(bDayMonthYear)

Target = SysDay(strDate)

Target = SysDay(lSysSec)

Remarks

Target | A Variable (WORD), that is assigned with the System-Day  
---|---  
bDayMonthDay | A Byte, which holds the Day-value followed by Month(Byte) and Year (Byte)  
strDate | A String, which holds a Date-String in the format specified in the CONFIG DATA statement  
lSysSec | A variable, which holds a System Second (SysSec)  
  
The Function can be used with 4 different kind of inputs:

1.| Without any parameter. The internal Date-values of SOFTCLOCK (_day, _month, _year) are used.  
---|---  
  
2.| With a user defined date array. It must be arranged in same way (Day, Month, Year) as the internal SOFTCLOCK date. The first Byte (Day) is the input by this kind of usage. So the Day of the Year can be calculated of every date.  
---|---  
  
3.| With a Date-String. The date-string must be in the Format specified in the Config Date Statement.  
---|---  
  
4.| With a System Second Number (LONG)  
---|---  
  
The Return-Value is in the Range of 0 to 36524. 2000-01-01 starts with 0.

The Function is valid in the 21th century (from 2000-01-01 to 2099-12-31).

See also

[Date and Time Routines](datetime.md) , [Config Date](config_date.md) , [Config Clock](config_clock.md) , [SysSec](syssec.md)

Example

```vb
Enable Interrupts

Config Clock = Soft

Config Date = YMD , Separator =.' ANSI-Format

Dim Strdate As String * 8

Dim Bday Asbyte , Bmonth As Byte , Byear As Byte

Dim Wsysday As Word

Dim Lsyssec As Long

' Example 1 with internal RTC-Clock

```
_day = 20 : _Month = 11 : _Year = 2 ' Load RTC-Clock for example - testing

Wsysday = Sysday()

```vb
Print "System Day of " ; Date$ ; " is " ; Wsysday

' System Day of 02.11.20 is 1054

' Example 2 with defined Clock - Bytes (Day / Month / Year)

```
Bday = 24 : Bmonth = 5 : Byear = 8

Wsysday = Sysday(bday)

```vb
Print "System Day of Day=" ; Bday ; " Month=" ; Bmonth ; " Year=" ; Byear ; " is " ; Wsysday

' System Day of Day=24 Month=5 Year=8 is 3066

' Example 3 with Date - String

```
Strdate = "04.10.29"

Wsysday = Sysday(strdate)

```vb
Print "System Day of " ; Strdate ; " is " ; Wsysday

' System Day of 04.10.29 is 1763

' Example 4 with System Second

```
Lsyssec = 123456789

Wsysday = Sysday(lsyssec)

```vb
Print "System Day of System Second " ; Lsyssec ; " is " ; Wsysday

' System Day of System Second 123456789 is 1428"Now it's " ; Lsystemsecondselapsed ; " seconds later"

```