# DEFxxx

Action  
  
Declares all variables that are not dimensioned of the DefXXX type.

Syntax

DEFBIT b | Define BIT  
---|---  
DEFBYTE c | Define BYTE  
DEFINT I | Define INTEGER  
DEFWORD x | Define WORD  
DEFLNG l | Define LONG  
DEFSNG s | Define SINGLE  
DEFDBL z | Define DOUBLE  
  
Remarks

While you can DIM each individual variable you use, you can also let the compiler handle it for you.

All variables that start with a certain letter will then be dimmed as the specified type.

Example

Defbit b : DefInt c ' default type for bit and integers

Set b1 ' set bit to 1

c = 10 ' let c = 10