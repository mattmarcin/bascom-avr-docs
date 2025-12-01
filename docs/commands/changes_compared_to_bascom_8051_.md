# Changes compared to BASCOM-8051

The design goal was to make BASCOM-AVR compatible with BASCOM-8051.

For the AVR compiler some statements had to be removed.

New statements were also added. And some statements were changed.

They need specific attention, but the changes to the syntax will be made available to BASCOM-8051 too in the future.

Statements that were removed

STATEMENT | DESCRIPTION  
---|---  
```vb
$LARGE | Not needed anymore.  
$ROMSTART | Code always starts at address 0 for the AVR. Added again in 1.11.6.2  
$LCDHEX | Use LCD Hex(var) instead.  
$NOINIT | Not needed anymore. Added in 1.11.6.2  
$NOSP | Not needed anymore  
$NOBREAK | Can't be used anymore because there is no object code that can be used for it.  
$OBJ | Removed.  
```
BREAK | Can't be used anymore because there is no object code that can be used for it.  
PRIORITY | AVR does no allow setting priority of interrupts  
PRINTHEX | You can use Print Hex(var) now  
LCDHEX | You can use Lcd Hex(var) now  
  
Statements that were added

STATEMENT | DESCRIPTION  
---|---  
FUNCTION | You can define your own user FUNCTIONS.  
LOCAL | You can have LOCAL variables in SUB routines or FUNCTIONS.  
^ | New math statement. Var = 2 ^ 3 will return 2*2*2  
SHIFT | Because ROTATE was changed, I added the SHIFT statement. SHIFT works just like ROTATE, but when shifted left, the LS BIT is cleared and the carry doesn't go to the LS BIT.  
LTRIM | LTRIM, trims the leftmost spaces of a string.  
RTRIM | RTRIM, trims the rightmost spaces of a string.  
TRIM | TRIM, trims both the leftmost and rightmost spaces of a string.  
  
Statements that behave differently

STATEMENT | DESCRIPTION  
---|---  
ROTATE | Rotate now behaves like the ASM rotate, this means that the carry will go to the most significant bit of a variable or the least significant bit of a variable.  
CONST | String were added to the CONST statement. I also changed it to be compatible with QB.  
```vb
DECLARE | BYVAL has been added since real subprograms are now supported.  
DIM | You can now specify the location in memory of the variable. Dim v as byte AT 100, will use memory location 100.

```