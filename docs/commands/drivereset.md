# DriveReset

Action

Resets the Drive.

Syntax

bErrorCode = DRIVERESET()

Remarks

BErrorCode | A Byte Variable, which is assigned with the error code of the function  
---|---  
  
This function resets the drive and brings it to an initial state. The functions returns 0 if no error occurred. For Error code see section Error codes.

See also

[DriveCheck](drivecheck.md), [DriveInit](driveinit.md) , [DriveGetIdentity](drivegetidentity.md) , [DriveWriteSector](drivewritesector.md) , [DriveReadSector](drivereadsector.md)

ASM

Calls | _DriveReset |   
---|---|---  
Input | none |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Partial Example

Dim bError as Byte

bError = DriveReset()