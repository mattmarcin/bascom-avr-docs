# DAYOFYEAR

Action

Returns the Day of the Year of a Date

Syntax

Target = DayOfYear()

Target = DayOfYear(bDayMonthYear)

Target = DayOfYear(strDate)

Target = DayOfYear(wSysDay)

Target = DayOfYear(lSysSec)

Remarks

Target | A Integer, that is assigned with the Day of the Year  
---|---  
BDayMonthYear | A Byte, which holds the Day-value followed by Month(Byte) and Year (Byte)  
StrDate | A String, which holds a Date-String in the format specified in the CONFIG DATE statement  
WSysDay | A Variable (Word) which holds a System Day (SysDay)  
LsysSec | A Variable (Long) which holds a System Second (SysSec)  
  
The Function can be used with five different kind of Input:

1.| Without any parameter. The internal Date-values of SOFTCLOCK (_day, _month, _year) are used.  
---|---  
  
2.| With a user defined date array. It must be arranged in same way (Day, Month, Year) as the internal SOFTCLOCK date. The first Byte (Day) is the input by this kind of usage. So the Day of the Year can be calculated of every date.  
---|---  
  
3.| With a Date-String. The date-string must be in the Format specified in the Config Date Statement.  
---|---  
  
4.| With a System Day Number (WORD)  
---|---  
  
5.| With a System Second Number (LONG)  
---|---  
  
The Return-Value is in the Range of 0 to 364 (365 in a leap year). January the first starts with 0.

The function is valid in the 21th century (from 2000-01-01 to 2099-12-31).

See also

[Date and Time Routines](datetime.md) , [SysSec](syssec.md) , [SysDay](sysday.md)

Example

See [DayOfWeek](dayofweek.md)