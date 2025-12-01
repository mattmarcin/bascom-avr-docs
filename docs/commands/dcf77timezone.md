# DCF77TIMEZONE

Action

This function will return the offset to Greenwich Time.

Syntax

res = DCF77TimeZone()

Remarks

Res | The target variable that is assigned with the result. The result will be: \- 0: when there is no valid DCF77 data yet \- 1: when in "Middle Europe Normal Time" \- 2: when in "Middle Europe daylight saving Time"  
---|---  
  
In Middle Europe, daylight saving is used to make better use of the day light in the summer.

The last Sunday in March at 02:00 AM the Daylight Saving will start. All clocks are set from 2:00 to 3:00.

Your weekend, is one hour shorter then.

But the last Sunday of October is better : at 03:00 AM, the Daylight Saving will end and all clocks are set from 03:00 to 02:00.

When you have a lot of clocks in your house, you can understand why DCF77 synchronized clocks are so popular.

See also

[CONFIG DCF77](configdcf77.md)

Example

Print = DCF77TimeZone()