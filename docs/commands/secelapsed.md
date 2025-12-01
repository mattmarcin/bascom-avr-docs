# SECELAPSED

Action

Returns the elapsed Seconds to a former assigned time-stamp.

Syntax

Target = SECELAPSED(TimeStamp)

Remarks

Target | A variable (LONG), that is assigned with the elapsed Seconds  
---|---  
TimeStamp | A variable (LONG), which holds a timestamp like the output of an earlier called SecOfDay()  
  
The Function works with the SOFTCLOCK variables _sec, _min and _hour and considers a jump over midnight and gives a correct result within 24 hour between two events.

The Return-Value is in the range of 0 to 86399.

See also

[Date and Time Routines](datetime.md) , [SecOfDay](secofday.md) , [SysSecElapsed](syssecelapsed.md)

Partial Example

Lsecofday = Secofday()

_hour = _hour + 1

Lvar1 = Secelapsed(lsecofday)

Print Lvar1