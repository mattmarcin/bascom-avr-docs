# VERSION

Action

Returns a string with the date and time of compilation.

Syntax

Var = VERSION(frm)

Remarks

Var is a string variable that is assigned with a constant. This version constant is set at compilation time to MM-DD-YY hh:nn:ss Where MM is the month, DD the day of the month, YY the year. hh is the hour is 24-hour format, nn the minutes, and ss the seconds.  
---  
When frm is set to 1, the format date will be shown in European DD-MM-YY hh:nn:ss format.  
When frm is set to 2, the version info from $VERSION will be used.  
When frm is set to 3, the filename will be used.  
When frm is set to 4, the version info from $VERSION will be used without the separating dots. So 1.2.3 will become 123.  
When frm is a string constant, the string constant will be used.  
  
While it is simple to store the version of your program in the source code, it is harder to determine which version was used for a programmed chip.

The Version() function can print this information to the serial port, or to an LCD display.

See Also

[VER](ver.md) , [$VERSION](_version.md)

Example

Print Version()