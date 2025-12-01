# DriveReadSector

Action

Read a Sector (512 Bytes) from the (Compact Flashcard) Drive

Syntax

bErrorCode = DRIVEREADSECTOR(wSRAMPointer, lSectorNumber)

Remarks

bErrorCode | A Byte Variable, which is assigned with the error code of the function  
---|---  
wSRAMPointer | A Word Variable, which contains the SRAM address (pointer) , to which the Sector from the Drive should be written  
lSectorNumber | A Long Variable, which give the sector number on the drive be transfer.  
  
Reads a Sector (512 Bytes) from the Drive and write it to SRAM starting at the address, to which the content of the variable wSRAMPointer is pointing. The functions returns 0 if no error occurred. For Error code see section Error codes.

Note: wSRAMPointer is not the variable, to which the content of the desired drive-sector should be written, it is the Word-Variable/Value which contains the SRAM address of the range, to which 512 Bytes should be written from the Drive. This gives you the flexibility to read and write every SRAM-Range to and from the drive, even it is not declared as variable. If you know the SRAM-Address (from the compiler report) of a buffer you can pass this value directly, otherwise you can get the address with the BASCOM-function VARPTR (see example).

See also

[DriveCheck](drivecheck.md), [DriveReset](drivereset.md) , [DriveInit](driveinit.md) , [DriveGetIdentity](drivegetidentity.md) , [DriveWriteSector](drivewritesector.md)

ASM

Calls | _DriveReadSector |   
---|---|---  
Input | Z: SRAM-Address of buffer *) | X: Address of Long-variable with sectornumber  
Output | r25: Errorcode | C-Flag: Set on Error  
  
![notice](notice.jpg)This is not the address of wSRAMPointer, it is its content, which is the starting-address of the buffer.

Partial Example

```vb
Dim bError as Byte

Dim aBuffer(512)as Byte' Hold Sector to and from CF-Card

Dim wSRAMPointer as Word' Address-Pointer for write

Dim lSectorNumber as Long' Sector Number

' give Address of first Byte of the 512 Byte Buffer to Word-Variable

```
wSRAMPointer =VarPtr(aBuffer(1))

' Set Sectornumber, sector 32 normally holds the Boot record sector of first partition

lSectorNumber = 32

' Now read in sector 32 from CF-Card

bError = DriveReadSector( wSRAMPointer , lSectorNumber)

' Now Sector number 32 is in Byte-Array bBuffer