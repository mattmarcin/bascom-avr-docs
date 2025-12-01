# VARPTR

Action

Retrieves the memory-address of a variable.

Syntax

var = VARPTR( var2 )

var = VARPTR( "var3" )

Remarks

Var | The variable that receives the address of var2.  
---|---  
Var2 | A variable to retrieve the address from.  
var3 | A constant  
  
Sometimes you need to know the address of a variable, for example when you like to peek at it's memory content.

The VARPTR() function assigns this address.

You can also get the address of a register using VARPTR.

The address of registers are constants you can find in the DAT file.

See also

[LOADADR](loadadr.md) , [SIZEOF](sizeof.md) , [CONFIG VARPTRMODE](config_varptrmode.md)

Example

```vb
Dim W As Byte

Print Hex(varptr(w)) ' 0060 depends on processor

```