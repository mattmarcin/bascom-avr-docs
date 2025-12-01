# DriveWriteSector

Action

Write a Sector (512 Bytes) to the (Compact Flashcard) Drive

Syntax

bErrorCode = DRIVEWRITESECTOR(wSRAMPointer, lSectorNumber)

Remarks

bErrorCode | A Byte Variable, which is assigned with the error code of the function  
---|---  
wSRAMPointer | A Word Variable, which contains the SRAM address (pointer), from which the Sector to the Drive should be written  
lSectorNumber | A Long Variable, which give the sector number on the drive to transfer.  
  
Writes a Sector (512 Bytes) from SRAM starting at the address, to which the content of the variable wSRAMPointer is pointing to the Drive to sector number lSectornumber. The functions returns 0 if no error occurred. For Error code see section Error codes.

![notice](notice.jpg) For the meaning of wSRAMPointer see Note in DriveReadSector

See also

[DriveCheck](drivecheck.md), [DriveReset](drivereset.md) , [DriveInit](driveinit.md) , [DriveGetIdentity](drivegetidentity.md) , [DriveReadSector](drivereadsector.md)

ASM

Calls | _DriveWriteSector |   
---|---|---  
Input | Z: SRAM-Address of buffer *) | X: Address of Long-variable with sectornumber  
Output | r25: Errorcode | C-Flag: Set on Error  
  
![notice](notice.jpg) This is not the address of wSRAMPointer, it is its content, which is the starting-address of the buffer.

Partial Example

```vb
Dim bError as Byte

Dim aBuffer(512) as Byte' Hold Sector to and from CF-Card

Dim wSRAMPointer as Word' Address-Pointer for read

Dim lSectorNumber as Long' Sector Number

' give Address of first Byte of the 512 Byte Buffer to Word-Variable

```
wSRAMPointer =VarPtr(aBuffer(1))

' Set Sectornumber

lSectorNumber = 3

' Now Write in sector 3 from CF-Card

bError = DriveWriteSector( wSRAMPointer , lSectorNumber)