# HIGH

Action

Retrieves the most significant byte of a variable.

Sets the most significant byte of a WORD variable. 

Syntax

var = HIGH( s )

HIGH( s ) = value

Remarks

Var | The variable that is assigned with the MSB of var S.  
---|---  
S | The source variable to get the MSB from when used as a function.  The target variable to set the MSB when used in an assignment   
value | The value to assign when used in an assignment.  
  
![notice](notice.jpg)When used in an assignment , only the second byte of the variable will be set. The intention purpose is to set the MSB of a WORD or INTEGER. 

It will also work on a LONG or DWORD but it will set the second byte in memory which is not the MSB of a LONG/DWORD.

Also, this will work on arrays, but there is no type checking which means that you should not use this on a single BYTE since it could overwrite other memory.

In version 2083 the HIGH function can also be used to set the MSB of a variable. This for compatibility with BASCOM-8051.

See also

[LOW](low.md) , [HIGHW](highw.md)

Example

Dim I As Integer , Z As Byte

I = &H1001

Z = High(i) ' is 10 hex or 16 dec

End