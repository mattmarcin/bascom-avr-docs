# CONFIG SHIFTIN

Action

Instruct the compiler to use new behaviour of the SHIFTIN statement.

Syntax

CONFIG SHIFTIN = value

Remarks

value | This must be COMPATIBLE or NEW. By default the old behaviour is used. So in order to use the new behaviour you must use : CONFIG SHIFTIN=NEW  
---|---  
  
The SHIFTOUT has been enhanced with a number of options which make it incompatible to the old SHIFTOUT.

In order to maintain compatibility with your old code, this option has been added so you have control over which SHIFTIN version is used.

See also

[SHIFTIN](shiftin.md)