# DriveGetIdentity

Action

Returns the Parameter information from the Card/Drive

Syntax

bErrorCode = DRIVEGETIDENTITY(wSRAMPointer)

Remarks

BErrorCode | A Byte Variable, which is assigned with the error code of the function  
---|---  
wSRAMPointer | A Word Variable, which contains the SRAM address (pointer) , to which the information of the Drive should be written  
  
The Identify Drive Function returns the parameter information (512 Bytes) from the Compact Flash Memory Card/Drive and writes it to SRAM starting at the address, to which the content of the variable wSRAMPointer is pointing. This information are for example number of sectors of the card, serial number and so on. Refer to the Card/Drive manual for further information. The functions returns 0 if no error occurred. For Error code see section Error codes.

Note: For meaning of wSRAMPointer see Note in DriveReadSector

See also

[DriveCheck](drivecheck.md), [DriveReset](drivereset.md) , [DriveInit](driveinit.md) , [DriveWriteSector](drivewritesector.md) , [DriveReadSector](drivereadsector.md)

ASM

Calls | _DriveGetIdentity |   
---|---|---  
Input |  | Z: SRAM-Address of buffer *)  
Output | r25: Errorcode | C-Flag: Set on Error  
  
![notice](notice.jpg) *) Please note: This is not the address of wSRAMPointer, it is its content, which is the starting-address of the buffer.

Partial Example

```vb
Dim bError as Byte

Dim aBuffer(512) as Byte' Hold Sector to and from CF-Card

Dim wSRAMPointer as Word' Address-Pointer for write

' give Address of first Byte of the 512 Byte Buffer to Word-Variable

```
wSRAMPointer =VarPtr(aBuffer(1))

' Now read the parameter Information from CF-Card

bError = DriveGetIdentity( wSRAMPointer)