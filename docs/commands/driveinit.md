# DriveInit

Action

Sets the AVR-Hardware (PORTs, PINs) attached to the Drive and resets the Drive.

Syntax

bErrorCode = DRIVEINIT()

Remarks

BErrorCode | A Byte Variable, which is assigned with the error code of the function  
---|---  
  
Set the Ports and Pins attaching the Drive for Input/Output and give initial values to the output-pins. After that the Drive is reset. 

Which action is done in this function depends of the drive and its kind of connection to the AVR. The functions returns 0 if no error occurred.

For Error code see section Error codes.

See also

[DriveCheck](drivecheck.md), [DriveReset](drivereset.md) , [DriveGetIdentity](drivegetidentity.md) , [DriveWriteSector](drivewritesector.md) , [DriveReadSector](drivereadsector.md), [AVR-DOS File System](avr_dos_file_system.md)

ASM

Calls | _DriveInit |   
---|---|---  
Input | none |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Partial Example

Dim bError as Byte

bError = DriveInit()