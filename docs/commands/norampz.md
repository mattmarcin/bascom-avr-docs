# $NORAMPZ

Action

This compiler directive disables RAMPZ clearing.

Syntax

$NORAMPZ

Remarks

Processors with more then 64 KB of memory need to set the RAMPZ register in order to point to the proper 64 KB page. 

If the RAMPZ register is used, it will be cleared when it is used for something different then accessing the flash.

BASCOM uses the Z register to access flash memory or RAM memory. Since processors with external memory capability can access more then 64KB of RAM, the RAMPZ must be set/cleared when accessing this memory.

Otherwise accessing the flash code could result in a change of RAMPZ, and after this, accessing the RAM would not point to the proper place in memory.

But setting this register requires extra code. When your application just fitted into a M128 or M256 and you do not want this RAMPZ handling because your application works fine, then you can use this $NORAMPZ directive.

To see if your processor 

See also

NONE

Example

NONE