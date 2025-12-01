# DISKSIZE

Action

Returns the size of the Disk in KB.

Syntax

lSize = DISKSIZE()

Remarks

lSize | A Long Variable, which is assigned with the capacity of the disk in Kilo Bytes  
---|---  
  
This functions returns the capacity of the disk in KB.

With the support of FAT32, the return value was changed from byte into KB.

See also

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [GET](get.md) , [PUT](put.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [FILELEN](filelen.md) , [WRITE](write.md) , [INPUT](input.md)

ASM

Calls | _GetDiskSize  
---|---  
Input | none  
Output | 16-r19: Long-Value of capacity in Bytes  
  
Partial Example

Dim Gbtemp1 As Byte ' scratch byte

Gbtemp1 = Initfilesystem(1) ' we must init the filesystem once

```vb
If Gbtemp1 > 0 Then

Print#1 ,"Error "; Gbtemp1

Else

Print#1 ," OK"

Print "Disksize : "; Disksize() ' show disk size in bytes

Print "Disk free: "; Diskfree() ' show free space too

End If

```