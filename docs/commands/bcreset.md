# BCRESET

Action

Resets the BasicCard by performing an ATR.

Syntax

BCRESET

Array(1) = BCRESET()

Remarks

Array(1) | When BCRESET is used as a function it returns the result of the ATR to the array named array(1). The array must be big enough to hold the result. Dim it as a byte array of 25.  
---|---  
  
This statements uses BCCARD.LIB, a library that is available separately from MCS Electronics.

An example of the returned output when used as a function:

```vb
'TS = 3B

'T0 = EF

'TB1 = 00

'TC1 = FF

'TD1 = 81 T=1 indication

'TD2 = 31 TA3,TB3 follow T=1 indicator

'TA3 = 50 or 20 IFSC ,50 =Compact Card, 20 = Enhanced Card

'TB3 = 45 BWT block waiting time

'T1 -Tk = 42 61 73 69 63 43 61 72 64 20 5A 43 31 32 33 00 00

' B a s i c C a r d Z C 1 2 3

```
See the BasicCard manual for more information

When you do not need the result you can also use the BCRESET statement.

See Also

[CONFIG BCCARD](config_bccard.md) , [BCDEF](bcdef.md) , [BCCALL](bccall.md)

Partial Example (no init code shown)

```vb
'----and now perform an ATR as a function

Dim Buf(25)AsByte, I AsByte

```
Buf(1)=Bcreset()

```vb
For I = 1 To 25

Print I ;" ";Hex(buf(i))

Next

'typical returns :

'TS = 3B

'T0 = EF

'TB1 = 00

'TC1 = FF

'TD1 = 81 T=1 indication

'TD2 = 31 TA3,TB3 follow T=1 indicator

'TA3 = 50 or 20 IFSC ,50 =Compact Card, 20 = Enhanced Card

'TB3 = 45 BWT blocl waiting time

'T1 -Tk = 42 61 73 69 63 43 61 72 64 20 5A 43 31 32 33 00 00

' B a s i c C a r d Z C 1 2 3

```