# INITFILESYSTEM

Action

Initialize the file system

Syntax

bErrorCode = INITFILESYSTEM (bPartitionNumber)

Remarks

bErrorCode | (Byte) Error Result from Routine, Returns 0 if no Error  
---|---  
bPartitionNumber | (Byte) Partition number on the Flashcard Drive (normally 1)  
  
Reads the Master boot record and the partition boot record (Sector) from the flash card and initializes the file system.

This function must be called before any other file-system function is used.

See also

[OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md), [AVR-DOS File System](avr_dos_file_system.md)

ASM

Calls | _GetFileSystem |   
---|---|---  
Input | r24: partitionnumber (1-based) |   
Output | r25: Errorcode | C-Flag: Set on Error  
  
Partial Example

Dim bErrorCode as Byte

bErrorCode = InitFileSystem(1)

```vb
If bErrorCode > 0 then

Print "Error: "; bErrorCode

Else

Print "Filesystem successfully initialized"

End If

```