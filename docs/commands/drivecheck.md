# DriveCheck

Action

Checks the Drive, if it is ready for use

Syntax

bErrorCode = DRIVECHECK()

Remarks

bErrorCode | A Byte Variable, which is assigned with the return value of the function  
---|---  
  
This function checks the drive, if it is ready for use (for example, whether a compact flash card is inserted). The functions returns 0 if the drive can be used, otherwise an error code is returned. For Error code see section Error codes.

See also

[DriveReset](drivereset.md) , [DriveInit](driveinit.md) , [DriveGetIdentity](drivegetidentity.md) , [DriveWriteSector](drivewritesector.md) , [DriveReadSector](drivereadsector.md)

ASM

Calls | _DriveCheck |   
---|---|---  
Input | none |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Partial Example

Dim bError as Byte

bError = DriveCheck()