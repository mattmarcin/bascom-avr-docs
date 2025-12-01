# $XRAMSTART

Action

Specifies the location of the external RAM memory.

Syntax

$XRAMSTART = [&H]address

Remarks

Address | The (hex)-address where the data is stored. Or the lowest address that enables the RAM chip. You can use this option when you want to run your code in systems with external RAM memory. Address must be a constant.  
---|---  
  
By default the extended RAM will start after the internal memory so the lower addresses of the external RAM can't be used to store information.

When you want to protect an area of the chip, you can specify a higher address for the compiler to store the data. For example, you can specify &H400. The first dimensioned variable will be placed in address &H400 and not in &H260.

It is important that when you use $XRAMSTART and $XRAMSIZE that $XRAMSTART comes before $XRAMSIZE.

See also

[$XRAMSIZE](xramsize.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : m128.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrate using $XRAM directive

'micro : Mega128

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m128def.dat" ' specify the used micro

$crystal = 1000000 ' used crystal frequency

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

$xramstart = &H1000

$xramsize = &H1000

Dim X As X

```