# READUSERSIG

Action

This function reads data from the User Signature Area available in the UPDI platform.

Syntax

targ = ReadUserSig(address [, bytes])

Remarks

targ | A variable that is assigned with the data byte(s)  
---|---  
address | The address where reading must start. This must be in the range from 0 up to the available data length - 1. So when the user signature is 32 bytes, the range is from 0-31.  
bytes | The number of bytes to read. This is an optional variable. When not used the target variable data type is used to determine how many bytes must be read.  
  
The User Signature Data area can be written by the UPDI. See also the $USER directive.

See also

[READSIG](readsig.md) , $USER

Example