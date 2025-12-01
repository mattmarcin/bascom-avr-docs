# DATETIME

The DateTime library is written by Josef Franz VÃ¶gel. It extends the clock routines with date and time calculation.

The following functions are available:

[DayOfWeek](dayofweek.md) | Returns the day of the week  
---|---  
[DayOfYear](dayofyear.md) | Returns the day of the year  
[SecOfDay](secofday.md) | Returns the second of the day  
[SecElapsed](secelapsed.md) | Returns the elapsed Seconds to a former assigned time-stamp  
[SysDay](sysday.md) | Returns a number, which represents the System Day  
[SysSec](syssec.md) | Returns a Number, which represents the System Second  
[SysSecElapsed](syssecelapsed.md) | Returns the elapsed Seconds to a earlier assigned system-time-stamp  
[Time](time.md) | Returns a time-value (String or 3 Byte for Second, Minute and Hour) depending of the Type of the Target  
[Date](date.md) | Returns a date-value (String or 3 Bytes for Day, Month and Year) depending of the Type of the Target  
  
![notice](notice.jpg) Date and time not to be confused with Date$ and Time$ !

The date starts at 1.1.2000 and valid from 2000 to 2099

If you wish to convert to NTP which starts at 1.1.1970, which is 30 years earlier, you need to subtract a value of 946684800

BASCOM DATE_TIME = NTP - 946684800

![notice](notice.jpg)Most of the Date and Time functions accept variables which must be in sequential memory order. Like bSec, bMin, bHour

When using DIM like this : Dim bSec As Byte, bMin As Byte, bHour As byte , the variables will be in sequential order, but this might change in the future.

Better would be to be explicit : Dim bSec as byte , bMin as byte at bSec + 1 , bHour as byte at bMin + 1

This will ensure that the bytes will be mapped in the right order. 

![notice](notice.jpg)It is important that you use the [CONFIG CLOCK](config_clock.md) option since this will include the date time library. 

See also

[config clock](config_clock.md), [config date](config_date.md)