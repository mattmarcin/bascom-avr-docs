# Using a BOOTLOADER

With booting we mean starting up like when you power a PC, after a reset.

When you reset the processor your user code will be executed.

A boot loader is a small program which task it is to re-program the processor. That is : in our case. A boot loader could do security checks or have other functions but when we say boot loader it always refer to some code that will reprogram the processor.

A boot loader typically runs just after a reset. But it could be initiated on any possible way. The recommended way is to use the statement : RESET MICRO.

A normal AVR and Xmega have a fuse that can be set to select the reset vector. It can point to address 0 which is the normal start address. Or it can point to an address at the end of flash memory.

When the fuse points to the boot vector, a jump is executed to this memory. And the boot code that is located at this memory is executed. Typically it will receive data and will flash/reprogram the memory from address 0 and up.

After that, the code at address 0 is executed and the normal user code runs. 

The $LOADER directive is used to place the program code at the boot address at the end of memory. The exact address depends on other fuse settings and the processor used.

The normal user code always end up in location 0 and up.

The new Xtiny/MegaX and AVRX processors work different. A reset will always execute address 0. But when you want to program a boot loader, you use a Boot fuse to tell how big the boot loader is. A value of 1 will reserve a size of 512 bytes. A value of 2 will reserve 1024 bytes, etc. So you are flexible in selecting the size of the boot loader.

After the boot block your normal code starts. But now you see the difference : the normal user code runs at a higher address. So we must tell the compiler that all code must be relocated.

We use the $ROMSTART directive for that. 

A boot loader does not have a $ROMSTART directive. 

```vb
While the boot fuse uses blocks of 512 bytes, the flash page size can be different. Do not confuse this. AVRX processors typically have flash page size of 512 bytes. 

For the AVRX series we include here a sample boot loader. 

'----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' Bootloader-AVRX.bas  
'----------------------------------------------------------------  
' This sample demonstrates how you can write your own bootloader  
' in BASCOM BASIC for the AVR DB/DA series  
' The AVRX has a different memory lay out and a different NVM controller  
' Normal AVR starts with normal application code and the boot code is placed at the end of memory.  
' AVRX starts with BOOT memory. So we always start in BOOT mode.  
' With the BOOTEND fuse we can set the size of the BOOT area.  
' Different processors have different page sizes. For DA/DB series the pages size is 512 bytes  
' A value of 1 will give a size of 512 bytes, a value of 2 gives 1024 bytes, etc.  
' In this example we use less than 1536 bytes so we set the fuse to 3.  
' Notice that the fuse page size can differ from the flash page size ! In this case the sizes are equal.  
  
' After the optional boot space there is the APPLICATION CODE  
' And after the APPLICATION CODE there is the APPLICATION DATA  
' When you dont want a boot loader you set the bootend fuse to 0 which is the default.  
' your app will use the boot and application code  
' When you want a boot loader, you determine the size of the boot loader and then  
' set the fuse to the proper size  
' With the MCS boot loader, the code simply checks if the #123 data is received.  
' If so, it starts the loading. If not it continues.  
' It is similar to the normal AVR boot loading. The normal AVR boot starts after the normal space.  
' # There is one important difference. With normal AVR all the code start at &H0000.  
' For the loader we then use the $LOADER directive to place the code at the proper address  
' For XTINY/AVRX the boot loader starts at &H0000 thus is considered a normal application without specific switches  
' Your normal code must now be located AFTER the bootloader. This means you need to instruct the compiler to place the code  
' at a different address. We use $ROMSTART for this purpose.  
' Remember that AVR has word address. Which means that each address uses 2 bytes of memory.  
'  
'-----------------------------------------------------------------  
  
$regfile ="AVRX128da28.dat"  
$crystal = 24000000  
$hwstack = 40  
$swstack = 40  
$framesize = 40  
  
'declare subs and functions  
Declare Sub Erasepage()  
Declare Sub Protected_write_spm(byreg R16 As Byte)  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
'define the baud rate and port/usart  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
```
Const Pagesize_bts = 512 ' page size in bytes is 512 bytes  
Const Fword = Pagesize_bts / 2 ' page size in words is 256  
Const Numpages = 256 ' number of page is 256  
Const Key_ctrla_spm = &H9D ' ccp key write protect for SPM NVM_CTRLA  
Const Key_ctrlb_io = &HD8 ' ccp key write protect for IO NVM_CTRLB  
' NVM Commands  
Const Nocmd = 0 'no command  
Const Noop = 1 'no operation  
Const Flwr = 2 'flash write enable  
Const Flper = 8 'flash erase enable  
  
'flash constants  
Const Maxwordbit = 8  
Const Maxword =(2 ^ Maxwordbit) * 2 '512  
Const Maxwordshift = Maxwordbit + 1 '9  
  
```vb
'It is VERY IMPORTANT that the baud rate match the one of the boot loader  
'do not try to use buffered com since we do not use interrupts  
'you could however use interrupts but it occupies more space  
  
'Possible return codes of the PC bootloader.exe  
' -6005 Cancel requested  
' -6006 Fatal time out  
' -6007 Unrecoverable event during protocol  
' -6008 Too many errors during protocol  
' -6009 Block sequence error in Xmodem  
' -6016 Session aborted  
  
'since this is a boot loader we do not want a vector table  
'we reduce the vector table to 0  
$reduceivr  
  
'Dim the used variables  
Dim Z As Dword ' this is the Z pointer word  
Dim Vl As Byte , Vh As Byte ' these bytes are used for the data values  
Dim Wrd As Word , Page As Word ' these vars contain the page and word address  
  
Dim Bstatus As Byte , Bretries As Byte , Bblock As Byte , Bblocklocal As Byte  
Dim Bcsum1 As Byte , Bcsum2 As Byte , Buf(128) As Byte , Csum As Byte  
Dim J As Byte , Wptr As Word  
  
  
'We start with receiving a file. The PC must send this binary file  
  
'some constants used in serial com  
```
Const Cnak = &H15  
Const Cack = &H06  
  
```vb
$timeout = 400000 ' we use a timeout  
'When you get LOADER errors during the upload, increase the timeout value  
'for example at 16 Mhz, use 200000  
  
```
Bretries = 5 ' we try 5 times  
Do  
Bstatus = Waitkey() ' wait for the loader to send a byte  
```vb
Print Chr(bstatus); ' echo back  
  
If Bstatus = 123 Then ' did we received value 123 ?  
Goto Loader ' jump into boot loader  
End If  
```
Decr Bretries  
```vb
Loop Until Bretries = 0  
  
'if we arrive here, there was not boot character received. we simply continue  
Goto Application_start_noload ' goto the normal code  
  
  
'this is the loader routine. It is a Xmodem-checksum reception routine  
```
Loader:  
Do  
Bstatus = Waitkey() ' flush the data  
```vb
Loop Until Bstatus = 0  
  
'just like the normal AVR loader we need to erase a page first  
'but since we write beyond the loader we need to set the page to the proper value which is essential the same as the FUSE BOOT SIZE value !  
```
page=3 'remember each page uses 512 bytes, this code is less than 1536 so the normal app start on page 3  
Erasepage 'erase it  
  
Bretries = 10 ' number of retries  
Do  
Bblocklocal = 1  
Csum = 0 ' checksum is 0 when we start  
```vb
Print Chr(cnak); ' first time send a nack  
Do  
  
```
Bstatus = Waitkey() ' wait for status byte  
  
```vb
Select Case Bstatus  
Case 1: ' start of heading, PC is ready to send  
```
Csum = 1 ' checksum is 1  
Bblock = Waitkey() : Csum = Csum + Bblock ' get block  
Bcsum1 = Waitkey() : Csum = Csum + Bcsum1 ' get checksum first byte  
For J = 1 To 128 ' get 128 bytes  
Buf(j) = Waitkey() : Csum = Csum + Buf(j)  
Next  
Bcsum2 = Waitkey() ' get second checksum byte  
```vb
If Bblocklocal = Bblock Then ' are the blocks the same?  
If Bcsum2 = Csum Then ' is the checksum the same?  
Gosub Writepage ' yes go write the page  
Print Chr(cack); ' acknowledge  
```
Incr Bblocklocal ' increase local block count  
```vb
Else ' no match so send nak  
Print Chr(cnak);  
End If  
Else  
Print Chr(cnak); ' blocks do not match  
End If  
Case 4: ' end of transmission , file is transmitted  
' Waitms 100 ' OPTIONAL REMARK THIS IF THE DTR SIGNAL ARRIVES TO EARLY  
Print Chr(cack); ' send ack and ready  
Waitms 20  
Goto Application_start ' start new program  
Case &H18: ' PC aborts transmission  
Goto Application_start ' ready  
Case 123 : Exit Do ' was probably still in the buffer  
Case Else  
Exit Do ' no valid data  
End Select  
Loop  
If Bretries > 0 Then ' attempte left?  
Waitms 1000  
```
Decr Bretries ' decrease attempts  
```vb
Else  
Exit Do ' reset chip  
End If  
Loop  
  
```
Application_start:  
Protected_write_SPM nocmd ' clear current command  
Cpu_ccp = key_CTRLB_io  
Rstctrl_swrr = 1 ' perform a soft reset  
  
'no code between the label above and below !  
  
Application_start_noload:  
r23=&B111 ' set value  
Cpu_ccp = key_CTRLB_io ' configuration change protect  
Nvmctrl_ctrlb = R23 ' enable boot section read protect, appdatawrite protect, appcode protect  
```vb
'the addres to go to is a word address, since our loader is less than 1536 bytes, this is 600 in hex and divided by 2 for words gives 300  
Goto &H300 ' normal app code  
  
'this sub routine will write the pages  
```
Writepage:  
For J = 1 To 128 step 2 ' get 128 bytes  
Z = Page ' make equal to page  
Shift Z , Left , Maxwordshift ' shift to proper place  
Z = Z + Wrd ' add word  
r0= Buf(j) ' r0:r1 point to the DATA for SPM  
R1 = Buf(j + 1)  
! lds r30,{Z} ; Z points to address  
! lds r31,{Z+1}  
  

#if _romsize > 65536  
! lds r24,{Z+2}  
! sts rampz,r24 ' we need to set rampz also for 128KB chips  

#endif  
!spm ; this actual executes the instruction  
wrd=wrd+2 ' we write word data so increase by 2  
```vb
Next  
  
if wrd=maxword then ' page is full  
```
wrd=0 ' reset word counter for next page  
page=page+1 ' increase page  
Erasepage ' erase so we can write  
```vb
end if  
return  
  
'erase a page based on PAGE value  
'RAMPZ ZH ZL (bit0 for low high byte selection)  
' 7 bits for word address : 128 word address  
' 1 bit from ZH -> 256 word address  
' leves 7 bit for PAGE address  
'zzzz,pppppppw,wwwwwwwx  
Sub Erasepage()  
```
Z = Page ' make equal to page  
Shift Z , Left , Maxwordshift ' shift to proper place  
  
bitwait NVMCTRL_STATUS.0,reset ' make sure flash is not busy  
Protected_write_SPM nocmd ' clear current command  
Protected_write_SPM flper ' erase page enable  
'dummy write needed, how dum  
  
! lds r30,{Z}  
! lds r31,{Z+1}  

#if _romsize > 65536  
! lds r24,{Z+2}  
! sts rampz,r24 ' we need to set rampz also for 128KB chips  

#endif  
! clr r0 ; data must be 0 for the dummy write  
! clr r1  
  
!spm ; execute dummy write  
  
bitwait NVMCTRL_STATUS.0,reset ' make sure flash is not busy  
Protected_write_SPM nocmd ' clear current command  
Protected_write_SPM flwr ' enable write to flash  
```vb
end sub  
  
sub Protected_write_SPM(byreg r16 as byte)  
```
CPU_CCP= key_CTRLA_spm 'change protect key  
NVMCTRL_CTRLA=r16 'write to SPM register  
```vb
end sub  
  
'this loader takes less than 1536 bytes so the BOOT FUSE is set to 3.  
'do NOT FORGET that your normal app must use $ROMSTART=&H300 in that case : halve of the bytes size of the loader  
  
'one other thing : the reset pin works in UPDI mode by default. so your chip will not reset when you do not change the fuse  
'but there are other ways of reset such as soft reset, bod and wd.

```
You compile the code and from the report you can find that the code size is 1214 bytes. Because the boot fuse block is 512, it means the value must be : 1214/512=2.31 We round up so end with 3.

We now run the MCS UPDI programmer and select the fuses TAB

![bootloader_fuses](bootloader_fuses.png)

The boot section size must be set to 3 as shown above.

You can also use the WRITE CONFIG button to write a CONFIG FUSE line in your code.

Just make sure the editor is set to a new line. in this case we end up with :

Config Fuses = Off , Lock = Off , Fuse0 = &H00 , FUSE1 = &H20 , FUSE2 = &HF0 , FUSE5 = &HDA , FUSE6 = &HF8 , FUSE7 = &H00 , FUSE8 = &H03 , UROW0 = &H00 , UROW31 = &H31

All user row values with a non default value are included too. 

When you compile with CONFIG FUSES=OFF, nothing will happen. Only when you change the FUSES=OFF to FUSES=ON, the fuses will be programmed when you auto program the chip.

And when you change LOCK=OFF to LOCK=ON, the processor will be locked too. The lock will make sure the data can not be read any longer. only the UNLOCK chip option from the programmer can unlock the chip. An operation that will also erase the chip. So typically writing LOCK bytes is something you do when all is tested.

Once we have programmed our boot loader and set the boot fuse to the correct size, we can use the MCS Boot loader to load new code.

Do not forget to chose the MCS Boot loader.

The only thing you need to remember : include the $ROMSTART=&H300 line in your NORMAL code. 

Most examples you find do not have this directive. 

Instead of the MCS Bootloader you can also make a boot loader that use Blue Tooth, Wifi, or an SD card. 

The mechanism is always : at boot check some condition, when met, perform the update.

The actual boot loader will remain in the processor. 

When you have suitable hardware like an external EEPROM with the size of the FLASH memory, you could update the firmware in your normal code. The boot code then would copy from EEPROM when required.

A boot loader could use decryption so your firmware can not be easily disassembled.