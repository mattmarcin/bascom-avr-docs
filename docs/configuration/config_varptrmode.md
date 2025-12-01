# CONFIG VARPTRMODE

Action

This options sets the behavior of the VARPTR() function.

Syntax

CONFIG VARPTRMODE= Relave | Absolute

Remarks

Different AVR processors have different memory architectures. 

Plan old AVR like atmega8 start with the 32 registers, then IO registers with address 0-&H3F then a gap of 32 bytes after which the SRAM memory starts.

The registers R0-R31 are accessible using memory pointer ST/LD. They occupy the absolute address 0-31.

The IO registers with address 0-&H3F can be indexed as well. But an offset of 32 must be added. So IO register TWBR which is at location 0 requires an offset of 32 when using a pointer like LD/ST. Port operations like IN/OUT requires the address from the DAT file thus 0-&H3F.

The Xmega works different. Here the registers R0-R31 can not be accessed by pointers. So here we use the relative address. 

And the same applies to the Xtiny platorm processors. There is no way you can address registers by a pointer either. 

When you use VARPTR with an IO register to assign a constant the absolute address was returned up to version 2086.

This was wrong since the absolute address was returned instead of the relative address.

Now this is fixed in 2087. But you need to add a CONFIG statement in order to fix this. 

In order not to break code this bug can be corrected with a new CONFIG directive.

You may change the behavior between the 2 modes.

The default is the wrong absolute mode.

```vb
CONFIG VarptrMode= Relative will set the mode to the relative address. This will give the desired output which will match that of the report file and the Code Explorer. The Code Explorer will always show the relative value which will match the value from the DAT file.

CONFIG VarptrMode = Absolute will set the mode to absolute address so it will be ideal for BASIC INP/OUT operations. Do not confuse with ASM IN/OUT instructions which will always require the relative address !

```
See also

[VARPTR](varptr.md)

Example

```vb
$Regfile="m2560def.dat"  
$Crystal=16000000  
$hwstack=40  
$swstack=32  
$framesize=32  
  
' the default is the old 2086 mode which gives a wrong result for normal AVR IO registers  
Config VarptrMode=relative  
  
'pina=0  
```
Const Test1 = VarPtr(PINA) ' IO &h00  
Const Test2 = VarPtr(EECR) ' IO &h1F  
Const Test3 = VarPtr(EEDR) ' IO &h20  
Const Test4 = VarPtr(SREG) ' IO &h3F  
Const Test5 = VarPtr(WDTCSR) ' extIO &h60  
Const Test6 = VarPtr(UDR3) ' extIO &h136  
'(  
Report:  
TEST1 &H00  
TEST2 &H1F  
TEST3 &H20  
TEST4 &H3F  
TEST5 &H60  
TEST6 &H136  
```vb
')  
  
Print "&h";Hex(VarPtr(PINA)) ' IO &h00  
Print "&h";Hex(VarPtr(EECR)) ' IO &h1F  
Print "&h";Hex(VarPtr(EEDR)) ' IO &h20  
Print "&h";Hex(VarPtr(SREG)) ' IO &h3F  
Print "&h";Hex(VarPtr(WDTCSR)) ' extIO &h60  
Print "&h";Hex(VarPtr(UDR3)) ' extIO &h136  
Print  
'(  
```
Output:  
&h0020  
&h003F  
&h0040  
&h005F  
&h0060  
&h0136  
```vb
')  
  
' when you set the mode to relative you get the correct value  
Config VarptrMode=relative  
'pina=0  
```
Const Test11 = VarPtr(PINA) ' IO &h00  
```vb
print hex(test11) 'prints 00  
End

```