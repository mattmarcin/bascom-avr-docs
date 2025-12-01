# TIME

Action

Returns a time-value (String or 3 Byte for Second, Minute and Hour) depending of the Type of the Target

Syntax

bSecMinHour = Time(lSecOfDay)

bSecMinHour = Time(lSysSec)

bSecMinHour = Time(strTime)

strTime = Time(lSecOfDay)

strTime = Time(lSysSec)

strTime = Time(bSecMinHour)

Remarks

bSecMinHour | A BYTE â variable, which holds the Second-value followed by Minute (Byte) and Hour (Byte)  
---|---  
strTime | A Time â String in Format âhh:mm:ss"  
lSecOfDay | A LONG â variable which holds Second Of Day (SecOfDay)  
lSysSec | A LONG â variable which holds System Second (SysSec)  
  
Converting to a time-string:

The target string strTime must have a length of at least 8 Bytes, otherwise SRAM after the target-string will be overwritten.

Converting to Softclock format (3 Bytes for Second, Minute and Hour):

Three Bytes for Seconds, Minutes and Hour must follow each other in SRAM. The variable-name of the first Byte, that one for Second must be passed to the function.

![notice](notice.jpg) Time not to be confused with Time$ !

See also

[Date and Time Routines](datetime.md) , [SECOFDAY](secofday.md), [SYSSEC](syssec.md)

Partial Example

```vb
Enable Interrupts

Config Clock = Soft

Dim Strtime As String * 8

Dim Bsec As Byte , Bmin As Byte AT Bsec + 1 , Bhour As Byte AT Bmin +1

Dim Lsecofday As Long

Dim Lsyssec As Long

' Example 1: Converting defined Clock - Bytes (Second / Minute / Hour) to Time - String

```
Bsec = 20 : Bmin = 1 : Bhour = 7

Strtime = Time(bsec)

```vb
Print "Time values: Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour ; " converted to string " ; Strtime

' Time values: Sec=20 Min=1 Hour=7 converted to string 07:01:20

' Example 2: Converting System Second to Time - String

```
Lsyssec = 123456789

Strtime = Time(lsyssec)

```vb
Print "Time of Systemsecond " ; Lsyssec ; " is " ; Strtime

' Time of Systemsecond 123456789 is 21:33:09

' Example 3: Converting Second of Day to Time - String

```
Lsecofday = 12345

Strtime = Time(lsecofday)

```vb
Print "Time of Second of Day " ; Lsecofday ; " is " ; Strtime

' Time of Second of Day 12345 is 03:25:45

' Example 4: Converting System Second to defined Clock - Bytes (Second / Minute / Hour)

```
Lsyssec = 123456789

Bsec = Time(lsyssec)

```vb
Print "System Second " ; Lsyssec ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour

' System Second 123456789 converted to Sec=9 Min=33 Hour=21

' Example 4: Converting Second of Day to defined Clock - Bytes (Second / Minute / Hour)

```
Lsecofday = 12345

Bsec = Time(lsecofday)

```vb
Print "Second of Day " ; Lsecofday ; " converted to Sec=" ; Bsec ; " Min=" ; Bmin ; " Hour=" ; Bhour

' Second of Day 12345 converted to Sec=45 Min=25 Hour=3

```