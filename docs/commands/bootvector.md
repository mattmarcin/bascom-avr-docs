# $BOOTVECTOR

Action

This compiler directive will force the compiler to create an interrupt vector table(IVR).

Syntax

$BOOTVECTOR

Remarks

By default an IVR is always created for normal applications. There is no good reason not to create an IVR for a normal application.

When making a boot loader application things are different. A boot loader application resides in upper flash memory inside the boot area. And when the boot loader applications runs, it has special rights so it can update the flash memory which resides in the lower flash memory.

The boot loader area size depends on the processor but is usual small. An interrupt vector table can use up to 250 bytes or more and it would be a waste of space in many cases. So by default the $LOADER directive which is used to create a boot loader application, will not create an IVR. The downside is that when you do not have an IVR you can not use interrupts.

The $BOOTVECTOR directive will force the compiler to create an IVR when the $LOADER directive is used. This way your boot loader application will include an IVR and you can use interrupts in your code.

![notice](notice.jpg)The $BOOTVECTOR directive will only work when the processor has an option to move the IVR to the boot area using the IVSEL bit.

By default the interrupts are located after address 0. Address 0 is the reset vector and usually contains a jump to the real code. Behind the reset address, a table with jumps to the interrupt routines is located. That the code contains an IVR is not enough : in case of a boot loader the interrupt table must be moved to the boot area. For this purpose most processors have a register and bit to switch the IVR between the normal address 0 and the boot loader address.

In BASCOM you can use : Config Intvectorselection = Enabled to set the selection to the boot area.

When the boot loader application finishes, it is best to use a watchdog timeout to reset the processor so the intvector selection is set to the default address 0.

Or you can use Config Intvectorselection = Disabled in your main (normal) application before you enable the interrupts. 

So in short you only need to add the $BOOTVECTOR directive and Config Intvectorselection = Enabled to your code. And do not forget to switch back the intvectorselection in the main application!

See also

[$LOADER](loader.md) , [CONFIG INTVECTORSELECTION](config_intvectorselection.md) , [$REDUCEIVR](reduceivr.md)

Example

```vb
'-----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' BootEDB-IVSEL.bas  
' This Bootloader is for the BASCOM-EDB  
' VERSION 4 of the BOOTLOADER.  
' IMPORTANT :  
' When changing the vector table in the boot loader you MUST  
' reset the vector table in your code using :  
' Config Intvectorselection = Disabled  
' otherwise your code points to the wrong table  
'-----------------------------------------------------------------  
'The loader is supported by the IDE  
  
$prog &HFF , &HE2 , &HDF , &HF8 ' generated. Take care that the chip supports all fuse bytes.'----------------------------------------------------------------  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
$crystal = 8000000  
$baud = 38400 'this loader uses serial com  
'It is VERY IMPORTANT that the baud rate matches the one of the boot loader  
'do not try to use buffered com as we can not use interrupts  
  
'This bootloader uses buffers serial input  
Config Serialin = Buffered , Size = 250  
  
'in order to use interrupts in a bootloader, the processor must support IVSEL  
'since the vector table occupies space some processors will not support it.  
$bootvector ' put int table into bootloader section so we can use interrupts  
Config Intvectorselection = Enabled ' enabled means that the vector table points to the boot section  
  
'since this boot loader uses interrupts we need to activate them but :  
'AFTER the interrupt vector table is enabeld  
Enable Interrupts  
  
'$regfile = "m8def.dat"  
'Const Loaderchip = 8  
  
'$regfile = "m168def.dat"  
'Const Loaderchip = 168  
  
'$regfile = "m16def.dat"  
'Const Loaderchip = 16  
  
'$regfile = "m32def.dat"  
'Const Loaderchip = 32  
  
$regfile = "m88def.dat"  
```
Const Loaderchip = 88  
  
```vb
'$regfile = "m162def.dat"  
'Const Loaderchip = 162  
  
'$regfile = "m128def.dat"  
'Const Loaderchip = 128  
  
'$regfile = "m64def.dat"  
'Const Loaderchip = 64  
  

#if Loaderchip = 88 'Mega88  
$loader = $c00 'this address you can find in the datasheet  
'the loader address is the same as the boot vector address  
```
Const Maxwordbit = 5  
Const Maxpages = 96 - 1 ' total WORD pages available for program  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 168 'Mega168  
$loader = $1c00 'this address you can find in the datasheet  
'the loader address is the same as the boot vector address  
```
Const Maxwordbit = 6  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 32 ' Mega32  
$loader = $3c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit '  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  

#if Loaderchip = 8 ' Mega8  
$loader = $c00 ' 1024 words  
```
Const Maxwordbit = 5 'Z5 is maximum bit '  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  

#if Loaderchip = 161 ' Mega161  
$loader = $1e00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit '  

```vb
#endif  

#if Loaderchip = 162 ' Mega162  
$loader = $1c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit '  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 64 ' Mega64  
$loader = $7c00 ' 1024 words  
```
Const Maxwordbit = 7 'Z7 is maximum bit '  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 128 ' Mega128  
$loader = &HFC00 ' 1024 words  
```
Const Maxwordbit = 7 'Z7 is maximum bit '  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  

#if Loaderchip = 16 ' Mega16  
$loader = $1c00 ' 1024 words  
```
Const Maxwordbit = 6 'Z6 is maximum bit '  
```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0  

#endif  
  
  
  
```
Const Maxword =(2 ^ Maxwordbit) * 2 '128  
Const Maxwordshift = Maxwordbit + 1  
Const Cdbg = 0 ' leave this to 0  
  

```vb
#if Cdbg  
Print Maxword  
Print Maxwordshift  
' Print Maxpages  

#endif  
  
  
  
'Dim the used variables  
Dim Bstatus As Byte , Bretries As Byte , Bblock As Byte , Bblocklocal As Byte  
Dim Bcsum1 As Byte , Bcsum2 As Byte , Buf(128) As Byte , Csum As Byte  
Dim J As Byte , Spmcrval As Byte ' self program command byte value  
  
Dim Z As Long 'this is the Z pointer word  
Dim Vl As Byte , Vh As Byte ' these bytes are used for the data values  
Dim Wrd As Word , Page As Word 'these vars contain the page and word address  
Dim Bkind As Byte , Bstarted As Byte  
'Mega 88 : 32 words, 128 pages  
  
  
'in this loader we may not disable interrupts !  
'Disable Interrupts 'we do not use ints  
  
  
'Waitms 100 'wait 100 msec sec  
'We start with receiving a file. The PC must send this binary file  
  
'some constants used in serial com  
```
Const Nak = &H15  
Const Cack = &H06  
Const Can = &H18  
  
```vb
'we use some leds as indication in this sample , you might want to remove it  
Config Pind.7 = Output  
```
Portd.7 = 0  
  
```vb
$timeout = 200000 'we use a timeout  
'When you get LOADER errors during the upload, increase the timeout value  
'for example at 16 Mhz, use 200000  
  
```
Bretries = 5 'we try 5 times  
Testfor123:  

```vb
#if Cdbg  
Print "Try " ; Bretries  
Print "Wait"  

#endif  
```
Bstatus = Waitkey() 'wait for the loader to send a byte  

```vb
#if Cdbg  
Print "Got "  

#endif  
  
Print Chr(bstatus);  
  
If Bstatus = 123 Then 'did we received value 123 ?  
```
Bkind = 0 'normal flash loader  
Goto Loader  
Elseif Bstatus = 124 Then ' EEPROM  
Bkind = 1 ' EEPROM loader  
Goto Loader  
Elseif Bstatus <> 0 Then  
Decr Bretries  
```vb
If Bretries <> 0 Then Goto Testfor123 'we test again  
End If  
  
For J = 1 To 10 'this is a simple indication that we start the normal reset vector  
Toggle Portd.7 : Waitms 100  
Next  
  

#if Cdbg  
Print "RESET"  

#endif  
Goto _reset 'goto the normal reset vector at address 0  
  
  
'this is the loader routine. It is a Xmodem-checksum reception routine  
```
Loader:  

```vb
#if Cdbg  
Print "Clear buffer"  

#endif  
Do  
```
Bstatus = Waitkey()  
```vb
Loop Until Bstatus = 0  
  
  
For J = 1 To 3 'this is a simple indication that we start the normal reset vector  
Toggle Portd.7 : Waitms 250  
Next  
  
If Bkind = 0 Then  
```
Spmcrval = 3 : Gosub Do_spm ' erase the first page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
End If  
  
  
Bretries = 10 'number of retries  
  
Do  
Bblocklocal = 1  
Bstarted = 0 ' we were not started yet  
Csum = 0 'checksum is 0 when we start  
```vb
Print Chr(nak); ' firt time send a nack  
Do  
  
```
Bstatus = Waitkey() 'wait for statuse byte  
  
```vb
Select Case Bstatus  
Case 1: ' start of heading, PC is ready to send  
```
Csum = 1 'checksum is 1  
Bblock = Waitkey() : Csum = Csum + Bblock 'get block  
Bcsum1 = Waitkey() : Csum = Csum + Bcsum1 'get checksum first byte  
For J = 1 To 128 'get 128 bytes  
Buf(j) = Waitkey() : Csum = Csum + Buf(j)  
Next  
Bcsum2 = Waitkey() 'get second checksum byte  
```vb
If Bblocklocal = Bblock Then 'are the blocks the same?  
If Bcsum2 = Csum Then 'is the checksum the same?  
Gosub Writepage 'yes go write the page  
Print Chr(cack); 'acknowledge  
```
Incr Bblocklocal 'increase local block count  
```vb
Else 'no match so send nak  
Print Chr(nak);  
End If  
Else  
Print Chr(nak); 'blocks do not match  
End If  
Case 4: ' end of transmission , file is transmitted  
If Wrd > 0 Then 'if there was something left in the page  
```
Wrd = 0 'Z pointer needs wrd to be 0  
Spmcrval = 5 : Gosub Do_spm 'write page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
```vb
End If  
Print Chr(cack); ' send ack and ready  
  
```
Portd.7 = 0 ' simple indication that we are finished and ok  
```vb
Waitms 20  
Goto _reset ' start new program  
Case &H18: ' PC aborts transmission  
Goto _reset ' ready  
Case 123 : Exit Do 'was probably still in the buffer  
Case 124 : Exit Do  
Case Else  
Exit Do ' no valid data  
End Select  
Loop  
If Bretries > 0 Then 'attempte left?  
Waitms 1000  
```
Decr Bretries 'decrease attempts  
```vb
Else  
Goto _reset 'reset chip  
End If  
Loop  
  
  
  
'write one or more pages  
```
Writepage:  
```vb
If Bkind = 0 Then  
For J = 1 To 128 Step 2 'we write 2 bytes into a page  
```
Vl = Buf(j) : Vh = Buf(j + 1) 'get Low and High bytes  
! lds r0, {vl} 'store them into r0 and r1 registers  
! lds r1, {vh}  
Spmcrval = 1 : Gosub Do_spm 'write value into page at word address  
Wrd = Wrd + 2 ' word address increases with 2 because LS bit of Z is not used  
If Wrd = Maxword Then ' page is full  
Wrd = 0 'Z pointer needs wrd to be 0  
Spmcrval = 5 : Gosub Do_spm 'write page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
  
  
If Page < Maxpages Then 'only if we are not erasing the bootspace  
Page = Page + 1 'next page  
Spmcrval = 3 : Gosub Do_spm ' erase next page  
Spmcrval = 17 : Gosub Do_spm ' re-enable page  
Else  
Portd.7 = 0 : Waitms 200  
```vb
End If  
End If  
Next  
  
Else 'eeprom  
For J = 1 To 128  
```
Writeeeprom Buf(j) , Wrd  
Wrd = Wrd + 1  
```vb
Next  
End If  
Toggle Portd.7 : Waitms 10 : Toggle Portd.7 'indication that we write  
Return  
  
  
```
Do_spm:  
Bitwait Spmcsr.0 , Reset ' check for previous SPM complete  
Bitwait Eecr.1 , Reset 'wait for eeprom  
  
Z = Page 'make equal to page  
Shift Z , Left , Maxwordshift 'shift to proper place  
Z = Z + Wrd 'add word  
! lds r30,{Z}  
! lds r31,{Z+1}  
  

#if Loaderchip = 128  
! lds r24,{Z+2}  
! sts rampz,r24 ' we need to set rampz also for the M128  

#endif  
  
Spmcsr = Spmcrval 'assign register  
! spm 'this is an asm instruction  
! nop  
! nop  
```vb
Return  
  
  
'Sub Isr_urx()  
  
'End Sub  
  
  
  
'How you need to use this program:  
'1- compile this program  
'2- program into chip with sample elctronics programmer  
'3- select MCS Bootloader from programmers  
'4- compile a new program for example M88.bas  
'5- press F4 and reset your micro  
' the program will now be uploaded into the chip with Xmodem Checksum  
' you can write your own loader.too  
'A stand alone command line loader is also available  
  
  
'How to call the bootloader from your program without a reset ???  
'Do  
' Print "test"  
' Waitms 1000  
' If Inkey() = 27 Then  
' Print "boot"  
' Goto &H1C00  
' End If  
'Loop  
  
'The GOTO will do the work, you need to specify the correct bootloader address  
'this is the same as the $LOADER statement.

```