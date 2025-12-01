# How to add another SPI device with the FT800

Bascom continuously Streams Data to the SPI bus trying to minimize additional commands sent over the SPI bus by taking advantage of some the the FT800 capabilities. Because of method used you have to be aware you can just add another SPI device and just let your micro talk to it.

What happens here, is that the CHIP Select line is held LOW for most of the time (depending on what code the Bascom FT800 is running at the time), if another SPI device wants to communicate with that micro then the data from that device will also be sent to the FT800 which means that you will get unexpected results!.

Wait, don't fear, here is some example code to show you how it can be done easily.

Our friend is Endtransfer

In the example below AVR-DOS needs to enable the Chip Select to do it's job (reading/writing), before doing so you have to call Endtransfer which tells the Micro to Set the Chip Select line to the FT800.

Note: The Chip Select line for the FT800 should/will automatically Reset next time it has to execute commands.

```vb
'-------------------------------------------------------------------------------------------  
Sub LoadJpeg( Byval file As Byte)  
'-------------------------------------------------------------------------------------------  
' API's used to upload the image to GRAM from SD card  
  
```
Local fsize As Dword  
Local BlockLen As Word, Ptr1 As Word, Ptr2 As Word, Ptr3 As Word  
  
Endtransfer '<\--------  
Open imagename(file) for Binary as #1  
  
fsize = Lof(1)  
  
Ptr1 = 1 ' Start at the first byte  
BlockLen = Chunk  
```vb
While fsize > 0  
If fsize > Chunk Then BlockLen = Chunk Else BlockLen = fsize  
```
fsize = fsize - BlockLen  
Endtransfer '<\--------  
Get #1, Dat, Ptr1, BlockLen  
  
ALign4 BlockLen  
  
Ptr2 = BlockLen  
Ptr3 = _base  
  
While Ptr2 > 0  
Cmd8 aDat(Ptr3)  
Incr Ptr3  
Decr Ptr2  
Wend  
  
EndTransfer '<\--------  
WaitCmdFifoEmpty  
  
Ptr1 = Ptr1 + BlockLen  
Wend  
Close #1  
  
End Sub ' LoadJpeg