# IDE Reference

> IDE menus, options, and tools

## AVR-DOS File I/O



---

## AVR-DOS File System

AVR-DOS is a Disk Operating System (DOS) for Atmel AVR microcontroller.

The AVR-DOS file system is written by Josef Franz VÃ¶gel. He can be contacted via the BASCOM forum. 

Josef has put a lot of effort in writing and especially testing the routines.

Topics of AVR-DOS File System:

1.| Introduction  
---|---  
  
2.| Important Steps to configure AVR-DOS  
---|---  
  
3.| Requirements  
---|---  
  
4.| Steps to get started with an ATMEGA (and with MMC.lib)  
---|---  
  
5.| Getting started with an ATMEGA and ATXMEGA with MMCSD_HC.LIB  
---|---  
  
6.| Memory Usage of DOS â File System  
---|---  
  
7.| Error Codes  
---|---  
  
8.| Buffer Status: Bit definitions of Buffer Status Byte (Directory, FAT and File)  
---|---  
  
9.| Validity of the file I/O operations regarding the opening modes  
---|---  
  
10.| SD and SDHC specs and pin-out  
---|---  
  
11.| Example 1 for getting started with an ATMEGA and ATXMEGA with MMCSD_HC.LIB  
---|---  
  
12.| Example 1: Following the Config_MMCSD_HC.INC which is included in the main example program  
---|---  
  
13.| Example 1: Following the Config_AVR-DOS.inc which is included in the main example program  
---|---  
  
14.| Example 2: SD and SDHC Card Analysis Example Demo program  
---|---  
  
(Show the Card Capacity and the Card-Register CSD, CID, OCR and SD_Status)

Introduction

AVR-DOS provide the needed libraries to handle:

•| The file system like open and/or create a file, send to or read from a file (Binary files and ASCII files)  
---|---  
  
•| Interface functions (drivers) for [Compact Flash](compact_flashcard_driver.md), hard disk, SD-Cards, SDHC (also microSD or microSDHC). See SD and SDHC pinout below.  
---|---  
  
See also: [New CF-Card Drivers](new_cf_card_drivers.md), [Elektor CF-Interface](elektor_cf_interface.md)

The Filesystem works with:

•| FAT16 formatted partitions  
---|---  
  
•| FAT32 formatted partitions  
---|---  
  
•| Short file name (8.3)  
---|---  
  
•| Files with a long file name can be accessed by their short file name alias  
---|---  
  
•| Files in Root Directory. The root dir can store 512 files. Take in mind that when you use long file names, less filenames can be stored.  
---|---  
  
•| Files in Root directory and sub directories  
---|---  
  
•| LBA mode (Logical block addressing) which is a linear addressing scheme where blocks are located by an integer index.  
---|---  
  
SD-card is a further development of the former MMC (Multi Media Card).

FAT = File Allocation Table and is the name of the file system architecture (FAT16 means 16-Bit version of FAT).

An SD or SDHC card is working at 2.7V ... 3.6V so for ATMEGA running at 5V you need a voltage converter or voltage divider. ATXMEGA are running at 2.7V ... 3.6V anyway so you can connect the sd-card direct to the ATXMEGA pin's.

![notice](notice.jpg)It is very important to use a proper level converter when using high clock rates (above 8 MHz). When using a FET/resistor as a level converter make sure there is enough pull up for a proper clock pulse.

Everything is written in Assembler to ensure a fast and compact code.

The intention in developing the DOS â file system was to keep close to the equivalent VB functions.

![notice](notice.jpg)Note that it is not permitted to use the AVR-DOS file system for commercial applications without the purchase of a license. A license comes with the ASM source. You can buy a user license that is suited for most private users.

When you develop a commercial product with AVR-DOS you need the company license. The ASM source is shipped with both licenses. 

![notice](notice.jpg)Josef nor MCS Electronics can be held responsible for any damage or data loss of your memory cards or disk drives.

FAT16-FAT32

In the root-directory of a FAT16, you have a maximum of 512 directory entries. This limit is defined in the Partition Boot sector. In a FAT16 subdirectory there is a limit of 65535 (2^16 - 1) entries. This Limit depends of the type of the directory entry pointer used in AVR-DOS and can not be increased.

On a FAT32 Partition you have in all kind of directories (Root and Sub) the limit of 65535 entries like the FAT16 Subdirectory.

Please take into account, that long-File-Name Entries will use more than one Directory-Entry depending on the length of the file-name.

So if you use a card with files created on a PC, there a normally more Directory Entries used, than the count of file names.

Important Steps to configure AVR-DOS

1\. Driver interface Library (select one of the following):

```vb
For compactFlash:

$include "Config_CompactFlash_ElektorIF_M128.bas"  
$include "Config_CompactFlash_M128.bas"

For Hard Drives:

$include "Config_HardDisk.bas"

For SD-Cards:

$include "Config_MMC.bas"

For SD-cards and SDHC cards (works also with ATXMEGA !):  
$include "config_MMCSD_HC.inc"

```
2\. After calling the Driver interface library you need check the Error Byte which is Gbdriveerror and which is output of the function [DRIVEINIT()](driveinit.md). If the output is 0 (no error) you can include the AVR-DOS configuration file. Otherwise you should output the error number.

```vb
If Gbdriveerror = 0 Then

$include "Config_AVR-DOS.inc"

End If

```
3\. In case of Gbdriveerror = 0 (No Error) you can Initialize the file system with [INITFILESYSTEM](initfilesystem.md)(1) where 1 is the partition number. For the Error Output var you need to dim a byte variable like Dim Btemp1 As Byte wbefore you call the Initfilesystem.

Btemp1 = Initfilesystem(1)

With Btemp1 = 0 (no error) the Filesystem is successfully initialized and you can use all other AVR-DOS functions like open, close, read and write. 

Functions like [PUT](put.md), [GET](get.md), [SEEK-Set](seek.md) only work when the file is opened in binary mode for example: Open "test.bin" For Binary As #2

When you want change (ejecting from the card socket) the SD-card (during the AVR is running other code than AVR-DOS) you need to call [DRIVEINIT()](driveinit.md) and [INITFILESYSTEM](initfilesystem.md)(1) again in order to reset the AVR-Hardware (PORTs, PINs) attached to the Drive,reset the Drive again and initialize the file system again.

![notice](notice.jpg)When you include a Constant named SHIELD like : CONST SHIELD=1 , the CS line is kept active which is required for some W5100/W5200 shields. 

Requirements:

•| Software: appr. 2K-Word Code-Space (4000 Bytes in flash)  
---|---  
  
•| SRAM: 561 Bytes for File system Info and DIR-Handle buffer  
---|---  
  
•| 517 Bytes if FAT is handled in own buffer (for higher speed), otherwise it is handled with the DIR Buffer  
---|---  
  
•| 534 Bytes for each File handle  
---|---  
  
•| This means that a ATMEGA644, ATMEGA128 or ATXMEGA have enough memory for it.  
---|---  
  
•| Even an ATMEGA32 could work but you really need to know what you do and you need to fully understand the settings in Config_AVR-DOS.BAS to reduce the amount of SRAM used by AVR-DOS (which will also affect AVR-DOS performance)  
---|---  
  
```vb
For example by setting Const Cfilehandles = 1 and handling of FAT- and DIR-Buffer in one SRAM buffer with 561 bytes). You will not have much SRAM left anyway for other tasks in the ATMEGA32 and you can not expect maximum performance. [$HWSTACK](_hwstack.md), [$SWSTACK](_swstack.md) and [$FRAMESIZE](_framesize.md) also needs to be set carefully.

' Count of file-handles, each file-handle needs 524 Bytes of SRAM  
```
Const Cfilehandles = 1 ' [default = 2]  
  
```vb
' Handling of FAT-Buffer in SRAM:  
' 0 = FAT- and DIR-Buffer is handled in one SRAM buffer with 561 bytes  
' 1 = FAT- and DIR-Buffer is handled in separate SRAM buffers with 1078 bytes  
' Parameter 1 increased speed of file-handling  
```
Const Csepfathandle = 0 ' [default = 1]

In the Main.bas you also need a Filename like Dim File_name As String * 12 

With the above configuration and with the filename there is approximately 500 byte SRAM left in an ATMEGA32 for other tasks. Or in other words AVR-DOS needs at least 1500 Byte SRAM in this case. To get detailed values compile your AVR-DOS application and open the Bascom-AVR compiler Report (CTRL+W) then you see the value with Space left : 508 Bytes (then you have 508 Bytes left for other tasks).

```vb
Then you can log data with for example:

Wait 4

```
Open File_name For Append As #100  
Print #100 , "This is what I log to SD-Card !"  
Close #100

When you change now Const Csepfathandle = 1 then you will get an OUT OF SRAM space message from the compiler with an ATMEGA32 which indicates that this will not work with an ATMEGA32. 

•| Other chips have too little internal memory. You could use XRAM memory too to extend the RAM.  
---|---  
  
•| SPI Interface for SD and SDHC cards (can be used in hardware and software SPI mode where hardware SPI mode is faster)  
---|---  
  
TTo get started there are Examples in the ...BASCOM-AVR\SAMPLES\avrdos folder.

Steps to get started with an ATMEGA (and with MMC.lib):

The MMC.lib is for SD-Cards (Standard SD-Cards usually up to 2Gbyte and not for SDHC cards)

1.|  Open Test_DOS_Drive.bas   
---|---  
  
2.|  Add $HWSTACK, $SWSTACK and $FRAMESIZE  
---|---  
  
3.|  Add the hardware driver you want to use (for example for SD-Card this is $include "Config_MMC.bas")  
---|---  
  
4.|  Open the Config_MMC.bas file and configure the SPI interface (hardware or software SPI and which Pin's for example for SPI chip select should be used. Config_MMC.bas will call the MMC.lib library which is located in the ...BASCOM-AVR\LIB folder.  
---|---  
  
5.|  Then you will find in Test_DOS_Drive.bas the Include AVR-DOS Configuration and library ($include "Config_AVR-DOS.BAS"). Config_AVR-DOS.BAS can be also found in ...BASCOM-AVR\SAMPLES\avrdos folder.  
---|---  
  
6.|  In Config_AVR-DOS.BAS you can change the AVR-DOS user settings like the number of file handles or if AT- and DIR-Buffer is handled in one SRAM buffer or in different SRAM buffer. With this settings you can balance between SRAM space used and speed/performance of AVR-DOS.   
---|---  
  
File System Configuration in CONFIG_AVR-DOS.BAS

cFileHandles: | Count of File handles: for each file opened at same time, a file handle buffer of 534 Bytes is needed  
---|---  
cSepFATHandle: | For higher speed in handling file operations the FAT info can be stored in a own buffer, which needs additional 517 Bytes. Assign Constant cSepFATHandle with 1, if wanted, otherwise with 0.  
  
7.|  Config_AVR-DOS.BAS will call AVR-DOS.Lbx library which is located in the ...BASCOM-AVR\LIB folder.  
---|---  
  
8.| Compile, flash and run Test_DOS_Drive.bas  
---|---  
  
Files used in the Test_DOS_Drive.bas example:

```vb
' +-------------------------------------------------+  
' | Test_DOS_Drive.bas | Main  
' +-------------------------------------------------+  
' | |  
' +--------------------+ +----------------------+  
' | config_MMC.bas | | Config_AVR-DOS.bas | Include Files  
' +--------------------+ +----------------------+  
' | |  
' +--------------------+ +----------------------+  
' | MMC.lib | | AVR-DOS.Lbx | Libraries  
' +--------------------+ +----------------------+

```
Getting started with an ATMEGA and ATXMEGA with MMCSD_HC.LIB:

The mmcsd_hc.lib can be found in the ...BASCOM-AVR\LIB folder.

This library support:

•| SD-Cards (also known as SDSC Cards = Secure Digital Standard-Capacity usually up to 2 GByte (also microSD)  
---|---  
  
•| SDHC cards (Secure Digital High Capacity) cards start at 2Gbyte up to 32GByte. You can also use micro SDHC cards.  
---|---  
  
•| It works with ATMEGA and ATXMEGA chips.  
---|---  
  
•| See also : [MMCSD_HC.LIB](mmcsd_hc_lib.md)  
---|---  
  
See ATXMEGA example program below.

Memory Usage of DOS â File System:

1\. General File System information (need 35 Byte in SRAM)

Variable Name | Type | Usage  
---|---|---  
gbDOSError | Byte | holds DOS Error of last file handling routine  
gbFileSystem | Byte | File System Code from Master Boot Record  
glFATFirstSector | Long | Number of first Sector of FAT Area on the Card  
gbNumberOfFATs | Byte | Count of FAT copies  
gwSectorsPerFat | Word | Count of Sectors per FAT  
glRootFirstSector | Long | Number of first Sector of Root Area on the Card  
gwRootEntries | Word | Count of Root Entries  
glDataFirstSector | Long | Number of first Sector of Data Area on the Card  
gbSectorsPerCluster | Byte | Count of Sectors per Cluster  
gwMaxClusterNumber | Word | Highest usable Cluster number  
gwLastSearchedCluster | Word | Last cluster number found as free  
gwFreeDirEntry | Word | Last directory entry number found as free  
glFS_Temp1 | Long | temporary Long variable for file system  
gsTempFileName | String * 11 | temporary String for converting file names  
  
2\. Directory (need 559 Byte in SRAM)

Variable Name | Type | Usage  
---|---|---  
gwDirRootEntry | Word | number of last handled root entry  
glDirSectorNumber | Long | Number of current loaded Sector  
gbDirBufferStatus | Byte | Buffer Status  
gbDirBuffer | Byte (512) | Buffer for directory Sector  
  
3\. FAT (need 517 Byte in SRAM)

FAT Buffer is only allocated if the constant: cSepFATHandle = 1

Variable Name | Type | Usage  
---|---|---  
glFATSectorNumber | Long | Number of current loaded FAT sector  
gbFATBufferStatus | Byte | Buffer status  
gbFATBuffer | Byte(512) | buffer for FAT sector  
  
4\. File handling

Each file handle has a block of 534 Bytes in the variable abFileHandle which is a byte-array of size (534 * cFileHandles)

Variable Name | Type | Usage  
---|---|---  
FileNumber | Byte | File number for identification of the file in I/O operations to the opened file  
FileMode | Byte | File open mode  
FileRootEntry | Word | Number of root entry  
FileFirstCluster | Word | First cluster  
FATCluster | Word | cluster of current loaded sector  
FileSize | Long | file size in bytes  
FilePosition | Long | file pointer (next read/write) 0-based  
FileSectorNumber | Long | number of current loaded sector  
FileBufferStatus | Byte | buffer Status  
FileBuffer | Byte(512) | buffer for the file sector  
SectorTerminator | Byte | additional 00 Byte (string terminator) for direct reading ASCII files from the buffer  
  
Error Codes:

Code | Compiler â Alias | Remark  
---|---|---  
0 | cpNoError | No Error  
1 | cpEndOfFile | Attempt behind End of File  
17 | cpNoMBR | Sector 0 on Card is not a Master Boot Record  
18 | cpNoPBR | No Partition Sector  
19 | cpFileSystemNotSupported | Only FAT16 File system is supported  
20 | cpSectorSizeNotSupported | Only sector size of 512 Bytes is supported  
21 | cpSectorsPerClusterNotSupported | Only 1, 2, 4, 8, 16, 32, 64 Sectors per Cluster is supported. This are values of normal formatted partitions. Exotic sizes, which are not power of 2 are not supported  
22 | Cpcountofclustersnotsupported | The number of clusters is not supported  
33 | cpNoNextCluster | Error in file cluster chain  
34 | cpNoFreeCluster | No free cluster to allocate (Disk full)  
35 | cpClusterError | Error in file cluster chain  
49 | cpNoFreeDirEntry | Directory full  
50 | cpFileExist | File exists  
51 | Cpfiledeletenotallowed | File may not be deleted  
52 | Cpsubdirectorynotempty | Sub directory not empty.You can not delete sub folders which contain files  
53 | Cpsubdirectoryerror | Sub directory error  
54 | Cpnotasubdirectory |   
  
65 | cpNoFreeFileNumber | No free file number available, only theoretical error, if 255 file handles in use  
66 | cpFileNotFound | File not found  
67 | cpFileNumberNotFound | No file handle with such file number  
68 | cpFileOpenNoHandle | All file handles occupied  
69 | cpFileOpenHandleInUse | File handle number in use, can't create a new file handle with same file number  
70 | cpFileOpenShareConflict | Tried to open a file in read and write modus in two file handles  
71 | cpFileInUse | Can't delete file, which is in use  
72 | cpFileReadOnly | Can't open a read only file for writing  
73 | cpFileNoWildCardAllowed | No wildcard allowed in this function  
74 | Cpfilenumberinvalid | Invalid file number  
97 | cpFilePositionError |   
98 | cpFileAccessError | function not allowed in this file open mode  
99 | cpInvalidFilePosition | new file position pointer is invalid (minus or 0)  
100 | cpFileSizeToGreat | File size to great for function BLoad  
&HC0 | Cpdrivererrorstart |   
  
  
Buffer Status: Bit definitions of Buffer Status Byte (Directory, FAT and File)

Bit | DIR | FAT | File | Compiler Alias | Remark  
---|---|---|---|---|---  
0 (LSB) |  |  | ![dot](dot.gif) | dBOF | Bottom of File (not yet supported)  
1 |  |  | ![dot](dot.gif) | dEOF | End of File  
2 |  |  | ![dot](dot.gif) | dEOFinSector | End of File in this sector (last sector)  
3 | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif) | dWritePending | Something was written to sector, it must be saved to Card, before loading next sector  
4 |  | ![dot](dot.gif) |  | dFATSector | This is an FAT Sector, at writing to Card, Number of FAT copies must be checked and copy updated if necessary  
5 |  |  | ![dot](dot.gif) | dFileEmpty | File is empty, no sector (Cluster) is allocated in FAT to this file  
  
Validity of the file I/O operations regarding the opening modes

| Open mode  
---|---  
Action | Input | Output | Append | Binary  
Attr | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif)  
Close | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif)  
Put |  |  |  | ![dot](dot.gif)  
Get |  |  |  | ![dot](dot.gif)  
LOF | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif)  
LOC | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif)  
EOF | ![dot](dot.gif) | 1) | 1) | ![dot](dot.gif)  
SEEK | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif)  
SEEK-Set |  |  |  | ![dot](dot.gif)  
Line Input | ![dot](dot.gif) |  |  | ![dot](dot.gif)  
```vb
Print |  | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif)  
Input | ![dot](dot.gif) |  |  | ![dot](dot.gif)  
```
Write |  | ![dot](dot.gif) | ![dot](dot.gif) | ![dot](dot.gif)  
  
1) Position pointer is always at End of File

Supported statements and functions:

[INITFILESYSTEM](initfilesystem.md) , [OPEN](open.md) , [CLOSE](close.md), [FLUSH](flush.md) , [PRINT](print.md), [LINE INPUT](line_input.md), [LOC](loc.md), [LOF](lof.md) , [EOF](eof.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [SEEK](seek.md) , [BSAVE](bsave.md) , [BLOAD](bload.md) , [KILL](kill.md) , [DISKFREE](diskfree.md) , [DISKSIZE](disksize.md) , [GET](get.md) , [PUT](put.md) ,[FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [DIR](dir.md) , [WRITE](write.md) , [INPUT](input.md) , [FILELEN](filelen.md)

SD and SDHC specs and pin-out: (also microSD and microSD pin-out for SPI mode):

SD/SDHC Specs:

•| SD and SDHC Cards offer a cost-effective and way to store large amounts of data on a removable memory and is ideal for data logging applications.  
---|---  
  
•| SDHC has a different protocol than SD card with standard Capacity (therefore there was different libraries available at the beginning)  
---|---  
  
•| Standard SD-Cards have a byte addressing. SDHC-Cards have sector-addressing like hard-disks and CF-Cards. One Sector is a portion of 512Bytes. SD cards and SDHC cards also have differences in the protocol at initializing the card, which can be used to check, which kind of card is inserted.   
---|---  
  
•| SD Card operating range: 2.7V...3.6V. So you need a voltage level converter to connect a 5V micro to a SD-card.  
---|---  
  
•| SD cards can be controlled by the six line SD card interface containing the signals: CMD,CLK,DAT0~DAT3 however this is not supported with AVR-DOS.  
---|---  
  
•| AVR-DOS support the SPI interface which can be easily used with the hardware SPI interface of ATMEGA and ATXMEGA. (Software SPI is also supported).  
---|---  
  
•| The SPI mode is active if the CS signal is asserted (negative) during the reception of the reset command (CMD0) which will be automatically handled by AVR-DOS  
---|---  
  
•| The advantage of the SPI mode is reducing the host design in effort.  
---|---  
  
•| With the Chip Select you can also connect several SPI slaves to one SPI interface  
---|---  
  
•| Endurance: Usually SD or SDHC cards can handle typical up to 100,000 writes for each sector. Reading a logical sector is unlimited. Please take care when writing to SD cards in a loop.  
---|---  
  
•| A typical SD Card current consumption should be between 50mA .... 80mA but should not exceed 200mA  
---|---  
  
![sd and microSD pinout](sd and microsd pinout.png)

Picture: Backside of SD/SDHC card and microSD card

SD/SDHC card pin out:

Pin # | Description for SPI mode | Connect to Pin on ATMEGA128 | Connect to Pin on ATXMEGA128A1  
---|---|---|---  
1 | Chip Select (SS) (Active low) | SS (PortB 0) (Active low) | SS (example for SPIC) PortC 4 (Active low)  
2 | DI (Data In) | MOSI (PortB 2) | MOSI (example for SPIC) PortC 5  
3 | GND | GND | GND  
4 | Vdd (Supply Voltage) | Supply Voltage (2.7V...3.6V) | Supply Voltage (2.7V...3.6V)  
5 | Clock | SCK (PortB 1) | SCK (example for SPIC) PortC 7  
6 | GND | GND | GND  
7 | D0 (Data Out) | MISO (PortB 3) | MISO (example for SPIC) PortC 6  
8 | Reserved | \- - - | \- - -  
9 | Reserved | \- - - | \- - -  
  
Depending on the used SD-card (or microSD) socket you can also detect if the card is inserted or ejected (for this you need an additional pin on the micro).

In some cases it is best practise to spend another pin able to switch on and off the power to the SD-card socket (e.g. over a transistor or FET). In this case you can cycle power from the AVR when the sd-card controller hangs.

It is also best practise in some cases when you open a file for append, write the data to it and close it right after this so there is no open file where data could be corrupted by an undefined external event.

microSD card pin out (same as microSDHC pin-out):

Pin # | microSD Description for SPI mode  
---|---  
1 | Reserved  
2 | Chip Select (SS)  
3 | DI (Data In)  
4 | Vdd (Supply Voltage)  
5 | Clock  
6 | GND  
7 | DO (Data Out)  
8 | Reserved  
  
Formatting

![notice](notice.jpg)It turns out that using windows to format a memory card can lead to problems. It is strongly advised to use the special format tool from sdcard.org !

You may download it here : https://www.sdcard.org/downloads/formatter_4/

It is important to set the 'Overwrite Format' option. 

It seems amazing that windows format (quick or full) can give other results but it was extensively tested. 

Example 1 for getting started with an ATMEGA and ATXMEGA with MMCSD_HC.LIB:

```vb
'-------------------------------------------------------------------------------  
' Filename: XMEGA_AVR-DOS_SDHC.BAS  
' Library needed: MMCSD_HC.LIB --> Place MMCSD_HC.LIB in the LIB-Path of BASCOM-AVR installation  
' MMCSD_HC.LIB will be called from config_MMCSD_HC.inc  
' AVR-DOS.Lbx  
' Include file: config_MMCSD_HC.inc (will be called from XMEGA_AVR-DOS_SDHC.BAS)  
' Used ATXMEGA: ATXMEGA128A1  
' Used SPI Port: Port D (you can also use Software SPI)  
'-------------------------------------------------------------------------------  
'  
' File Structure:  
'  
' +-------------------------------------------------+  
' | XMEGA_AVR-DOS_SDHC.BAS | Main  
' +-------------------------------------------------+  
' | |  
' +--------------------+ +----------------------+  
' | config_MMCSD_HC.inc| | Config_AVR-DOS.inc | Include Files  
' +--------------------+ +----------------------+  
' | |  
' +--------------------+ +----------------------+  
' | MMCSD_HC.LIB | | AVR-DOS.Lbx | Libraries  
' +--------------------+ +----------------------+  
'  
'  
' Terminal output of following example (with hardware SPI over Port.D):  
'  
' Used SD-Card: 4GByte SDHC Card  
'  
'  
'(  
  
```
\---Example for using a SDHC-Card with AVR-DOS and XMEGA---  
Starting... SDHC with ATXMEGA....  
  
SD Card Type = SDHC Spec. 2.0 or later  
  
Init File System ... OK --> Btemp1= 0 / Gbdriveerror = 0  
Filesystem = 6  
FAT Start Sector: 8196  
Root Start Sector: 8688  
Data First Sector: 8720  
Max. Cluster Nummber: 62794  
Sectors per Cluster: 128  
Root Entries: 512  
Sectors per FAT: 246  
Number of FATs: 2  
  
  
Write to file done !  
File length = 46  
This is my 1 first Text to File with XMEGA !  
write to file  
Total bytes written: 10200  
Write and Readback test done !  
Dir function demo  
LOGGER.TXT 01\01\01 01:00:00 3120  
MY_FILE.TXT 01\01\01 01:00:00 46  
TEST.TXT 01\01\01 01:00:00 10200  
  
Diskfree = 4018560  
Disksize = 4018752  
  
```vb
')

  
$regfile = "xm128a1def.dat"  
$crystal = 32000000 '32MHz  
$hwstack = 128  
$swstack = 128  
$framesize = 128  
  
  
Config Osc = Disabled , 32mhzosc = Enabled '32MHz  
Config Sysclock = 32mhz '32Mhz  
Config Priority = Static , Vector = Application , Lo = Enabled 'config interrupts  
Enable Interrupts  
  
'=====[ Serial Interface to PC = COM5 ]========================================  
Config Com5 = 57600 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
```
Open "COM5:" For Binary As #2  
```vb
Waitms 1  
  
Print #2 ,  
Print #2 , "---Example for using a SDHC-Card with AVR-DOS and XMEGA---"  
  
'=====[ Global Vars ]==========================================================  
Dim Btemp1 As Byte ' Needed for Fat Drivers  
Dim Input_string As String * 100  
Dim Output_string As String * 100  
Dim File_handle As Byte  
Dim File_name As String * 14  
Dim X As Long  
  
  
  
Print #2 , "Starting... SDHC with ATXMEGA...."  
Print #2 ,  
  
'------------------------------------------------------------------------------  
  
'=====[ Includes ]============================================================  
  
  
$include "config_MMCSD_HC.inc"  
  
Print #2 , "SD Card Type = " ;  
Select Case Mmcsd_cardtype  
Case 0 : Print #2 , "can't init the Card"  
Case 1 : Print #2 , "MMC"  
Case 2 : Print #2 , "SDSC Spec. 1.x "  
Case 4 : Print #2 , "SDSC Spec. 2.0 or later"  
Case 12 : Print #2 , "SDHC Spec. 2.0 or later"  
End Select  
  
Print #2 ,  
  
  
If Gbdriveerror = 0 Then 'from.... Gbdriveerror = Driveinit()  
$include "Config_AVR-DOS.inc" ' Include AVR-DOS Configuration and library  
  
  
Print #2 , "Init File System ... " ;  
```
Btemp1 = Initfilesystem(1) ' Reads the Master boot record and the partition boot record (Sector) from the flash card and initializes the file system  
```vb
'1 = Partitionnumber  
If Btemp1 <> 0 Then  
Print #2 , "Error: " ; Btemp1 ; " at Init file system"  
Else  
Print #2 , " OK --> Btemp1= " ; Btemp1 ; " / Gbdriveerror = " ; Gbdriveerror  
Print #2 , "Filesystem = " ; Gbfilesystem  
Print #2 , "FAT Start Sector: " ; Glfatfirstsector  
Print #2 , "Root Start Sector: " ; Glrootfirstsector  
Print #2 , "Data First Sector: " ; Gldatafirstsector  
Print #2 , "Max. Cluster Nummber: " ; Glmaxclusternumber  
Print #2 , "Sectors per Cluster: " ; Gbsectorspercluster  
Print #2 , "Root Entries: " ; Gwrootentries  
Print #2 , "Sectors per FAT: " ; Glsectorsperfat  
Print #2 , "Number of FATs: " ; Gbnumberoffats  
End If  
  
Print #2 ,  
Print #2 ,  
  
'-------------------------------------------------------------------------  
' Write Text to file  
```
File_handle = Freefile() ' get a file handle  
File_name = "My_file.txt"  
Open File_name For Output As #file_handle ' open file for output with file_handle  
```vb
' If the file exist already, the file will be overwritten !  
Print #file_handle , "This is my 1 first Text to File with XMEGA !"  
```
Close #file_handle  
  
```vb
Print #2 , "Write to file done !"  
  
'-------------------------------------------------------------------------  
'Now we want to read back the text we wrote to file and print it over Serial Interface  
```
File_handle = Freefile()  
Open "My_file.txt" For Input As #file_handle ' we can use a constant for the file too  
Print #2 , "File length = " ; Lof(#file_handle)  
Line Input #file_handle , Input_string ' read a line  
Print #2 , Input_string 'print the line  
Close #file_handle  
  
  
  
  
```vb
'WRITE TO FILE  
Print #2 , "write to file"  
```
File_name = "Test.txt"  
Input_string = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"  
  
  
Open File_name For Output As #10  
  
```vb
While X < 10000 '10000 * 102 Byte / 100 = 10200 Byte  
Print #10 , Input_string  
```
X = X + 100  
Wend  
  
Close #10  
  
  
X = Filelen(file_name)  
```vb
Print #2 , "Total bytes written: " ; X  
  
  
  
'READ FROM FILE  
  
```
Open File_name For Input As #10  
While Eof(#10) = 0  
Line Input #10 , Output_string ' read a line  
```vb
If Input_string <> Output_string Then  
Print #2 , "Buffer Error! near byte: " ; X ; " " ; "[" ; Output_string ; "]"  
Waitms 2000  
End If  
Wend  
```
Close #10  
  
  
```vb
Print #2 , "Write and Readback test done !"  
  
  
  
'-------------------------------------------------------------------------  
'Print the file name which was created before  
Print #2 , "Dir function demo"  
```
Input_string = Dir( "*.*")  
```vb
'The first call to the DIR() function must contain a file mask The * means everything.  
' Print File Names  
While Len(input_string) > 0 ' if there was a file found  
Print #2 , Input_string ; " " ; Filedate() ; " " ; Filetime() ; " " ; Filelen()  
' print file , the date the fime was created/changed , the time and the size of the file  
```
Input_string = Dir() ' get next  
```vb
Wend  
  
'-------------------------------------------------------------------------  
  
Print #2 ,  
Print #2 , "Diskfree = " ; Diskfree()  
Print #2 , "Disksize = " ; Disksize()  
  
End If 'If Gbdriveerror = 0 Then  
  
  
End 'end program

```
Example 1: Following the Config_MMCSD_HC.INC which is included in the main example program:

  
```vb
$nocompile  
  
'-------------------------------------------------------------------------------  
' Config_MMCSD_HC.INC  
' Config File for MMC/SD/SDHC Flash Cards Driver  
' (c) 1995-2025 , MCS Electronics / Vögel Franz Josef  
'-------------------------------------------------------------------------------  
' Place MMCSD_HC.LIB in the LIB-Path of BASCOM-AVR installation  
'  
' you can vary MMC_CS on HW-SPI and all pins on SOFT-SPI, check settings  
'  
' ========== Start of user definable range =====================================  
'  
' Declare here you SPI-Mode  
' using HW-SPI: cMMC_Soft = 0  
```
Const Hardware_spi = 0  
' not using HW_SPI: cMMC_Soft = 1  
Const Software_spi = 1  
  
Const Cmmc_soft = Hardware_spi  
  

```vb
#if Cmmc_soft = 0  
  
' --------- Start of Section for HW-SPI ----------------------------------------  
  
'Port D of ATXMEGA is used in this example as SPI Interface to SD-Card  
  
```
Portd_pin6ctrl = &B00_011_000 'Enable Pullup for MISO Pin  
  
```vb
' Define here Slave Slect (SS) Pin of Hardware SPI  
Config Pind.4 = Output ' define here Pin for CS of MMC/SD Card  
```
Mmc_cs Alias Portd.4  
```vb
Set Mmc_cs  
  
' Define here Slave Slect (SS) Pin of Hardware SPI  
Config Pind.4 = Output ' define here Pin of SPI SS  
```
Spi_ss Alias Portd.4  
```vb
Set Spi_ss ' Set SPI-SS to Output and High por Proper work of  
  
  
  
'FOR XMEGA DEVICES  

#if _xmega = 1  
'SPI Configuration for XMEGA  
'Used Library = $LIB "MMCSD_HC.LIB"  
  
  
'Portd.4 SS --> SD-Card Slave Select  
'Portd.5 MOSI --> SD-Card MISO  
'Portd.6 MISO --> SD-Card MOSI  
'Portd.7 CLK --> SD-Card Clock  
  
Config Spid = Hard , Master = Yes , Mode = 0 , Clockdiv = Clk2 , Data_order = Msb  
```
Open "SPID" For Binary As #14  
Const _mmc_spi = Spid_ctrl  

```vb
#else  
  
' HW-SPI is configured to highest Speed  
Config Spi = Hard , Interrupt = Off , Data Order = Msb , Master = Yes , Polarity = High , Phase = 1 , Clockrate = 4 , Noss = 1  
' Spsr = 1 ' Double speed on ATMega128  
```
Spiinit  

```vb
#endif  
  
' --------- End of Section for HW-SPI ------------------------------------------  
  

#else ' Config here SPI pins, if not using HW SPI  
  
' --------- Start of Section for Soft-SPI --------------------------------------  
  
' Chip Select Pin => Pin 1 of MMC/SD  
Config Pind.4 = Output  
```
Mmc_cs Alias Portd.4  
```vb
Set Mmc_cs  
  
' MOSI - Pin => Pin 2 of MMC/SD  
Config Pind.5 = Output  
Set Pind.5  
```
Mmc_portmosi Alias Portd  
Bmmc_mosi Alias 5  
  
```vb
' MISO - Pin => Pin 7 of MMC/SD  
Config Pind.6 = Input  
```
Mmc_portmiso Alias Pind  
Bmmc_miso Alias 6  
  
```vb
' SCK - Pin => Pin 1 of MMC/SD  
Config Pind.7 = Output  
Set Pind.7  
```
Mmc_portsck Alias Portd  
Bmmc_sck Alias 7  
  
```vb
' --------- End of Section for Soft-SPI ----------------------------------------  
  

#endif  
  
' ========== End of user definable range =======================================  
  
  
'==== Variables For Application ================================================  
Dim Mmcsd_cardtype As Byte ' Information about the type of the Card  
' 0 can't init the Card  
' 1 MMC  
' 2 SDSC Spec. 1.x  
' 4 SDSC Spec. 2.0 or later  
' 12 SDHC Spec. 2.0 or later  
  
Dim Gbdriveerror As Byte ' General Driver Error register  
' Values see Error-Codes  
'===============================================================================  
  
  
  
' ==== Variables for Debug =====================================================  
' You can remove remarks(') if you want check this variables in your application  
Dim Gbdrivestatusreg As Byte ' Driver save here Card response  
' Dim gbDriveErrorReg as Byte at GbdriveStatusReg overlay '  
' Dim gbDriveLastCommand as Byte ' Driver save here Last Command to Card  
Dim Gbdrivedebug As Byte  
' Dim MMCSD_Try As Byte ' how often driver tried to initialized the card  
'===============================================================================  
  
  
'==== Driver internal variables ================================================  
' You can remove remarks(') if you want check this variables in your application  
' Dim _mmcsd_timer1 As Word  
' Dim _mmcsd_timer2 As Word  
'===============================================================================  
  
  
  
' Error-Codes  
```
Const Cperrdrivenotpresent = &HE0  
Const Cperrdrivenotsupported = &HE1  
Const Cperrdrivenotinitialized = &HE2  
  
Const Cperrdrivecmdnotaccepted = &HE6  
Const Cperrdrivenodata = &HE7  
  
Const Cperrdriveinit1 = &HE9  
Const Cperrdriveinit2 = &HEA  
Const Cperrdriveinit3 = &HEB  
Const Cperrdriveinit4 = &HEC  
Const Cperrdriveinit5 = &HED  
Const Cperrdriveinit6 = &HEE  
  
Const Cperrdriveread1 = &HF1  
Const Cperrdriveread2 = &HF2  
  
Const Cperrdrivewrite1 = &HF5  
Const Cperrdrivewrite2 = &HF6  
Const Cperrdrivewrite3 = &HF7  
Const Cperrdrivewrite4 = &HF8  
  
  
  
```vb
$lib "MMCSD_HC.LIB"  
$external _mmc  
' Init the Card  
```
Gbdriveerror = Driveinit()  
  
  
```vb
' you can remark/remove following two Code-lines, if you dont't use MMCSD_GetSize()  
$external Mmcsd_getsize  
Declare Function Mmcsd_getsize() As Long  
  
  
' you can remark/remove following two Code-lines, if you dont't use MMCSD_GetCSD()  
' write result of function to an array of 16 Bytes  
$external Mmcsd_getcsd  
Declare Function Mmcsd_getcsd() As Byte  
  
  
' you can remark/remove following two Code-lines, if you dont't use MMCSD_GetCID()  
' write result of function to an array of 16 Bytes  
$external Mmcsd_getcid  
Declare Function Mmcsd_getcid() As Byte  
  
  
' you can remark/remove following two Code-lines, if you dont't use MMCSD_GetOCR()  
' write result of function to an array of 4 Bytes  
$external Mmcsd_getocr  
Declare Function Mmcsd_getocr() As Byte  
  
  
' you can remark/remove following two Code-lines, if you dont't use MMCSD_GetSDStat  
' write result of function to an array of 64 Bytes  
$external Sd_getsd_status  
Declare Function Sd_getsd_status() As Byte  
  
' check the usage of the above functions in the sample MMCSD_Analysis.bas  
' check also the MMC and SD Specification for the content of the registers CSD, CID, OCR and SDStat

```
Example 1: Following the Config_AVR-DOS.inc which is included in the main example program:

```vb
$nocompile  
' Config File-System for Version 5.5:  
  
' === User Settings ============================================================  
  
' Count of file-handles, each file-handle needs 524 Bytes of SRAM  
```
Const Cfilehandles = 2 ' [default = 2]  
  
```vb
' Handling of FAT-Buffer in SRAM:  
' 0 = FAT- and DIR-Buffer is handled in one SRAM buffer with 561 bytes  
' 1 = FAT- and DIR-Buffer is handled in separate SRAM buffers with 1078 bytes  
' Parameter 1 increased speed of file-handling  
```
Const Csepfathandle = 1 ' [default = 1]  
  
```vb
' Handling of pending FAT and Directory information of open files  
' 0 = FAT and Directory Information is updated every time a data sector of the file is updated  
' 1 = FAT and Directory Information is only updated at FLUSH and SAVE command  
' Parameter 1 increases writing speed of data significantly  
```
Const Cfatdirsaveatend = 1 ' [default = 1]  
  
  
```vb
' Surrounding String with Quotation Marks at the Command WRITE  
' 0 = No Surrounding of strings with quotation.marks  
' 1 = Surrounding of strings with quotation.marks (f.E. "Text")  
```
Const Ctextquotationmarks = 1 ' [default = 1]  
  
  
```vb
' Write second FAT. Windows accepts a not updated second FAT  
' PC-Command: chkdsk /f corrects the second FAT, it overwrites the  
' second FAT with the first FAT  
' set this parameter to 0 for high speed continuing saving data  
' 0 = Second FAT is not updated  
' 1 = Second FAT is updated if exist  
```
Const Cfatsecondupdate = 1 ' [default = 1]  
  
  
```vb
' Character to separate ASCII Values in WRITE - statement (and INPUT)  
' Normally a comma (,) is used. but it can be changed to other values, f.E.  
' to TAB (ASCII-Code 9) if EXCEL Files with Tab separated values should be  
' written or read. This parameter works for WRITE and INPUT  
' Parameter value is the ASSCII-Code of the separator  
' 44 = comma [default]  
' 9 = TAB ' [default = 44]  
```
Const Cvariableseparator = 44  
  
  
  
  
```vb
' === End of User Setting ======================================================  
  
  
  
' === Variables for AVR-DOS ====================================================  
  
' FileSystem Basis Informationen  
Dim Gldrivesectors As Long  
Dim Gbdoserror As Byte  
  
' Master Boot Record  
Dim Gbfilesystem As Byte  
' Partition Boot Record  
Dim Gbfilesystemstatus As Byte  
Dim Glfatfirstsector As Long  
Dim Gbnumberoffats As Byte  
Dim Glsectorsperfat As Long  
Dim Glrootfirstsector As Long  
Dim Gwrootentries As Word  
Dim Gldatafirstsector As Long  
Dim Gbsectorspercluster As Byte  
Dim Glmaxclusternumber As Long  
Dim Gllastsearchedcluster As Long  
  
' Additional info  
Dim Glfs_temp1 As Long  
  
' Block für Directory Handling  
  
Dim Gldirfirstsectornumber As Long  
  
Dim Gwfreedirentry As Word  
Dim Glfreedirsectornumber As Long  
  
Dim Gsdir0tempfilename As String * 11  
Dim Gwdir0entry As Word ' Keep together with next, otherwise change _DIR  
Dim Gldir0sectornumber As Long  
  
Dim Gstempfilename As String * 11  
Dim Gwdirentry As Word  
Dim Gldirsectornumber As Long  
Dim Gbdirbufferstatus As Byte  
Dim Gbdirbuffer(512) As Byte  
```
Const C_filesystemsramsize1 = 594  

```vb
#if Csepfathandle = 1  
Dim Glfatsectornumber As Long  
Dim Gbfatbufferstatus As Byte  
Dim Gbfatbuffer(512) As Byte  
```
Const C_filesystemsramsize2 = 517  

#else  
Const C_filesystemsramsize2 = 0  

```vb
#endif  
  
' File Handle Block  
```
Const Co_filenumber = 0  
Const Co_filemode = 1  
Const Co_filedirentry = 2 : Const Co_filedirentry_2 = 3  
Const Co_filedirsectornumber = 4  
Const Co_filefirstcluster = 8  
Const Co_filesize = 12  
Const Co_fileposition = 16  
Const Co_filesectornumber = 20  
Const Co_filebufferstatus = 24  
Const Co_filebuffer = 25  
Const C_filehandlesize = Co_filebuffer + 513 ' incl. one Additional Byte for 00 as string terminator  
' for direct text reading from File-buffer  
Const C_filehandlesize_m = 65536 - C_filehandlesize ' for use with add immediate word with subi, sbci  
' = minus c_FileHandleSize in Word-Format  
  
Const C_filehandlessize = C_filehandlesize * Cfilehandles  
  
  
Dim Abfilehandles(c_filehandlessize) As Byte  
Const C_filesystemsramsize = C_filesystemsramsize1 + C_filesystemsramsize2 + C_filehandlessize  
  
  
```vb
' End of variables for AVR-DOS ================================================  
  
' Definitions of Constants ====================================================  
  
' Bit definiton for FileSystemStatus  
  
```
Dfilesystemstatusfat Alias 0 : Const Dfilesystemstatusfat = 0 ' 0 = FAT16, 1 = FAT32  
Dfilesystemsubdir Alias 1 : Const Dfilesystemsubdir = 1 ' 0 = Root-Directory, 1 = Sub-Directory  
Const Dmfilesystemsubdir =(2 ^ Dfilesystemsubdir) ' not used yet  
Const Dmfilesystemdirincluster =(2 ^ Dfilesystemstatusfat + 2 ^ Dfilesystemsubdir) ' not used yet  
Dfatsecondupdate Alias 7 : Const Dfatsecondupdate = 7 ' Bit-position for parameter of  
```vb
' Update second FAT in gbFileSystemStatus  
  
  
' Bit Definitions for BufferStatus (FAT, DIR, File)  
  
```
Deof Alias 1 : Const Deof = 1 : Const Dmeof =(2 ^ Deof)  
Deofinsector Alias 2 : Const Deofinsector = 2 : Const Dmeofinsector =(2 ^ Deofinsector)  
Dwritepending Alias 3 : Const Dwritepending = 3 : Const Dmwritepending =(2 ^ Dwritepending)  
Dfatsector Alias 4 : Const Dfatsector = 4 : Const Dmfatsector =(2 ^ Dfatsector) ' For Writing Sector back (FATNumber times)  
Dfileempty Alias 5 : Const Dfileempty = 5 : Const Dmfileempty =(2 ^ Dfileempty)  
  
' New feature for reduce saving  
Dfatdirwritepending Alias 6 : Const Dfatdirwritepending = 6 : Const Dmfatdirwritepending =(2 ^ Dfatdirwritepending)  
Dfatdirsaveatend Alias 7 : Const Dfatdirsaveatend = 7 : Const Dmfatdirsaveatend =(2 ^ Dfatdirsaveatend)  
Dfatdirsaveanyway Alias 0 : Const Dfatdirsaveanyway = 0 : Const Dmfatdirsaveanyway =(2 ^ Dfatdirsaveanyway)  
  
  
  
  
Const Dmeofall =(2 ^ Deof + 2 ^ Deofinsector)  
Const Dmeof_empty =(2 ^ Deof + 2 ^ Deofinsector + 2 ^ Dfileempty)  
  
  
Const Cp_fatbufferinitstatus =(2 ^ Dfatsector)  
Const Cp_dirbufferinitstatus = 0  
  
  

#if Cfatdirsaveatend = 1  
Const Cp_filebufferinitstatus =(2 ^ Dfatdirsaveatend)  

#else  
Const Cp_filebufferinitstatus = 0  

```vb
#endif  
  
  
  

#if Cfatsecondupdate = 0  
```
Const Cp_fatsecondupdate =(2 ^ Dfatsecondupdate)  

#else  
Const Cp_fatsecondupdate = 0  

```vb
#endif  
  
  
' Bit definitions for FileMode (Similar to DOS File Attribut)  
```
Dreadonly Alias 0 : Const Dreadonly = 0  
'Const cpFileReadOnly = &H21 ' Archiv and read-only Bit set  
Const Cpfilewrite = &H20 ' Archiv Bit set  
  
  
```vb
' Error Codes  
  
' Group Number is upper nibble of Error-Code  
' Group 0 (0-15): No Error or File End Information  
```
Const Cpnoerror = 0  
Const Cpendoffile = 1  
  
' Group 1 (17-31): File System Init  
Const Cpnombr = 17  
Const Cpnopbr = 18  
Const Cpfilesystemnotsupported = 19  
Const Cpsectorsizenotsupported = 20  
Const Cpsectorsperclusternotsupported = 21  
Const Cpcountofclustersnotsupported = 22  
  
' Group 2 (32-47): FAT - Error  
Const Cpnonextcluster = 33  
Const Cpnofreecluster = 34  
Const Cpclustererror = 35  
' Group 3 (49-63): Directory Error  
Const Cpnofreedirentry = 49  
Const Cpfileexists = 50  
Const Cpfiledeletenotallowed = 51  
Const Cpsubdirectorynotempty = 52  
Const Cpsubdirectoryerror = 53  
Const Cpnotasubdirectory = 54  
' Group 4 (65-79): File Handle  
Const Cpnofreefilenumber = 65  
Const Cpfilenotfound = 66  
Const Cpfilenumbernotfound = 67  
Const Cpfileopennohandle = 68  
Const Cpfileopenhandleinuse = 69  
Const Cpfileopenshareconflict = 70  
Const Cpfileinuse = 71  
Const Cpfilereadonly = 72  
Const Cpfilenowildcardallowed = 73  
Const Cpfilenumberinvalid = 74 ' Zero is not allowed  
  
' Group 7 (97-127): other errors  
Const Cpfilepositionerror = 97  
Const Cpfileaccesserror = 98  
Const Cpinvalidfileposition = 99  
Const Cpfilesizetogreat = 100  
  
Const Cpdrivererrorstart = &HC0  
  
  
```vb
' Range 224 to 255 is reserved for Driver  
  
' Other Constants  
' File Open Mode / stored in File-handle return-value of Fileattr(FN#, [1])  
```
Const Cpfileopeninput = 1 ' Read  
Const Cpfileopenoutput = 2 ' Write sequential  
'Const cpFileOpenRandom = 4 ' not in use yet  
Const Cpfileopenappend = 8 ' Write sequential; first set Pointer to end  
Const Cpfileopenbinary = 32 ' Read and Write; Pointer can be changed by user  
  
  
' permission Masks for file access routine regarding to the file open mode  
Const Cfilewrite_mode = &B00101010 ' Binary, Append, Output  
Const Cfileread_mode = &B00100001 ' Binary, Input  
Const Cfileseekset_mode = &B00100000 ' Binary  
Const Cfileinputline = &B00100001 ' Binary, Input  
Const Cfileput_mode = &B00100000 ' Binary  
Const Cfileget_mode = &B00100000 ' Binary  
  
' Directory attributs in FAT16/32  
Const Cpfileopenallowed = &B00100001 ' Read Only and Archiv may be set  
Const Cpfiledeleteallowed = &B00100000  
Const Cpfilesearchallowed = &B00111101 ' Do no search hidden Files  
```vb
' Bit 0 = Read Only  
' Bit 1 = Hidden  
' Bit 2 = System  
' Bit 3 = Volume ID  
' Bit 4 = Directory  
' Bit 5 = Archiv  
' Long File name has Bit 0+1+2+3 set  
Dim Lastdosmem As Byte  
  
  
$lib "AVR-DOS.Lbx"

```
\- - - END of EXAMPLE 1 - - -

Example 2: SD and SDHC Card Analysis Example Demo program

(Show the Card Capacity and the Card-Register CSD, CID, OCR and SD_Status):

This example uses: $include "Config_MMCSD_HC.bas" which calls following Libary: $lib "MMCSD_HC.LIB" 

This example is written for ATMEGA but is also working for ATXMEGA devices.

```vb
'-------------------------------------------------------------------------------  
' MMCSD_Analysis.BAS  
' Test MMC / SD Card  
' (c) 1995-2025 , MCS Electronics / Vögel Franz Josef  
'-------------------------------------------------------------------------------  
' Test MMC / SD Card  
' Show the Card Capacity and the Card-Register CSD, CID, OCR and SD_Status  
' First you have to init the Card in the File Config_MMCSD_HC.bas with  
' $Include "Config_MMCSD_HC.bas"  
' All Card registers are written with the MSB first to the Byte-array  
' f.E. CSD(1) contains then MSB (Bit 120-127) of the CSD-Register  
  
$regfile = "M644pdef.dat"  
$crystal = 16000000  
  
$hwstack = 100  
$swstack = 100  
$framesize = 100  
  
  
$baud = 57600  
  
  
  
Config Serialin = Buffered , Size = 20  
Config Clock = Soft  
  
Enable Interrupts  
  
Config Date = Dmy , Separator = .  
Print "Test_Dos_Drive compiled at " ; Version()  
$include "Config_MMCSD_HC.bas"  
  
  
  
  
  
  
Dim Xc As Byte ' for Print - counter  
Dim Xd As Byte ' for Print - Counter  
  
Print "Start of Card Analysis"  
Print "Last Drive-Error-Code = " ; Gbdriveerror  
Print "Gbdrivestatusreg =" ; Gbdrivestatusreg  
  
' Check detected Card Type  
Select Case Mmcsd_cardtype  
Case 1  
Print "MMC-Card detected"  
Case 2  
Print "SD-Card Spec. 1.x detected"  
Case 4  
Print "SD-Card Spec. 2.0 detected"  
Case 12  
Print "SD-Card Spec. 2.0 High Capacity detected"  
Case Else  
Print "No Card detected"  
End Select  
  
If Mmcsd_cardtype > 0 Then  
  
' check the CSD Register  
  
Dim Csd(16) As Byte  
Print "Get CSD"  
```
Csd(1) = Mmcsd_getcsd()  
```vb
If Gbdriveerror <> 0 Then  
Print "Error at reading CSD"  
Else  
For Xc = 1 To 16  
Print Hex(csd(xc)) ; " " ;  
Next  
Print " "  
End If  
  
' Get the Card Capacity from the CSD Register  
  
Dim Mmcsd_size As Long  
Print "Get Card Capacity [KB]"  
```
Mmcsd_size = Mmcsd_getsize()  
```vb
If Gbdriveerror <> 0 Then  
Print "Error at reading CSD"  
Else  
Print "Card Capacity = ; " ; Mmcsd_size ; "kb (1KB=1024 Bytes)"  
End If  
  
' Get the CID Register  
  
Dim Cid(16) As Byte  
Print "Get CID"  
```
Cid(1) = Mmcsd_getcid()  
```vb
If Gbdriveerror <> 0 Then  
Print "Error at reading CID"  
Else  
For Xc = 1 To 16  
Print Hex(cid(xc)) ; " " ;  
Next  
Print " "  
End If  
  
' Get the OCR Register  
  
Dim Ocr(4) As Byte  
Print "Get OCR"  
```
Ocr(1) = Mmcsd_getocr()  
```vb
If Gbdriveerror <> 0 Then  
Print "Error at reading OCR"  
Else  
For Xc = 1 To 4  
Print Hex(ocr(xc)) ; " " ;  
Next  
Print " "  
End If  
  
If Mmcsd_cardtype > 1 Then  
  
' Get the SD_Status Register on SD-Cards  
  
Dim Sd_status(64) As Byte  
Print "Get SD_Status"  
```
Sd_status(1) = Sd_getsd_status()  
```vb
If Gbdriveerror <> 0 Then  
Print "Error at reading SD_Status"  
Else  
For Xc = 1 To 64  
Print Hex(sd_status(xc)) ; " " ;  
```
Xd = Xc Mod 8  
```vb
If Xd = 0 Then  
Print " "  
End If  
Next  
End If  
End If  
End If  
  
  
Print "End of Card Analysis"  
  
End

```
XTINY EXAMPLE

```vb
'--------------------------------------------------------------------------------  
'name : FlashCard-Demo-XTINY.BAS  
'copyright : (c) 1995-2025, MCS Electronics  
'purpose : demonstrates AVR-DOS on XYTINY platform  
'micro : avr128da28  
'suited for demo : no  
'commercial addon needed : yes  
'-------------------------------------------------------------------------------  
' This sample file shows how the AVR-DOS library from Josef Franz Vögel  
' can be used.  
'-------------------------------------------------------------------------------  
$regfile = "AVRX128da28.dat"  
  
$crystal = 24000000 'speed  
$hwstack = 128 'stack  
$swstack = 128  
$framesize = 128  
  
'The AVRX series have more oscillator options  
Config Osc = Enabled , Frequency = 24mhz  
  
'set the system clock and prescaler  
Config Sysclock = Int_osc , Prescale = 1  
  
'set up the COM por/USART connected to PA0 and PA1  
Config Com1 = 115200 , Mode = Asynchroneous , Parity = None , Databits = 8 , Stopbits = 1  
  
$external Waitms ' one of the libs needs the waitms code  
  
Declare Sub Directorylist(pstr1 As String , Byval Pdays As Word) 'declare sub  
  
Config Date = Dmy , Separator = DOT ' the file system uses date and times  
Config Clock = Soft ' real clock installed  
Enable Interrupts  
  
```
Time$ = "12:00:00" : Date$ = "16.04.23" ' set the time and date  
```vb
'when you have a clock, the date and time of the clock will be used  
  
Print "Lib version : " ; Ver()  
  
'include the driver configuration file this file will setup the SPI  
$include "config_MMCSD_HC_XTINY.inc"  
'include specific AVR-DOS settings  
$include "CONFIG_AVR-DOS.inc" ' some constants  
  
' Init Port and Card  
Print "Setup Port and Reset Card ... ";  
  
If Drivecheck() = 0 Then ' we have a card detected  
Print "OK"  
```
_temp1 = Driveinit() ' init the drive  
```vb
Else  
Print "Card not inserted, check Card!"  
End ' end program  
End If  
  
' The card is now setup and the low level card driver routine could be used  
' such as ReadSector, WriteSector etc.  
' We use the AVD-DOS Filesystem which is compatible with DOS/Windows  
' Make sure your CF card is 32MB or bigger. It needs to be formatted with FAT 16  
' Smaller cards can only be formatted with FAT12  
' of course you can also use FAT32  
  
Print "Init File System ... ";  
  
Dim Gbtemp1 As Byte ' scratch byte  
```
Gbtemp1 = Initfilesystem(1) ' we must init the filesystem once  
```vb
If Gbtemp1 > 0 Then  
Print "Error " ; Gbtemp1  
Else  
Print "OK"  
Print "Disksize : " ; Disksize() ' show disk size in bytes  
Print "Disk free: " ; Diskfree() ' show free space too  
End If  
  
  
'dim some test variables  
Dim S As String * 60 , Fl As String * 12 , Ff As Byte  
Dim Sdatetime As String * 18  
```
Fl = "test.txt"  
S = "test this"  
  
```vb
'Now we are getting to it  
'We can specify a file handle with #1 or #2 etc. or we can ask for a free  
'file handle with the FreeFile function. It will return a free handle if there is one.  
  
```
Ff = Freefile() ' get a file handle  
  
'With this file handle we refer to a file  
Open Fl For Output As #ff ' open fikle for output  
```vb
' we need to open a file before we can use the file commands  
' we open it for OUTPUT, INPUT , APPEND or BINARY  
' In this case we open it for OUTPUT because we want to write to the file.  
' If the file existed, the file would be overwritten.  
Print #ff , S ' print some data  
Print #ff , S  
Print #ff , S  
Print #ff , "A constant" ; S  
```
Close #ff ' close file  
  
```vb
'A file opened if OUTPUT mode is convenient to write string data too  
'The next beta will support WRITE too  
  
'We now created a file that contains 3 lines of text.  
'We want to append some data to it  
```
S = "this is appended"  
Open Fl For Append As #150 ' we specify the file number now  
Print #150 , S  
Close #150  
  
  
'Ok we want to check if the file contains the written lines  
Ff = Freefile() ' get file handle  
Open "test.txt" For Input As #ff ' we can use a constant for the file too  
```vb
Print Lof(#ff) ; " length of file"  
Print Fileattr(#ff) ; " file mode" ' should be 1 for input  
Do  
```
LineInput #ff , S ' read a line  
```vb
' line input is used to read a line of text from a file  
Print S ' print on terminal emulator  
Loop Until Eof(ff) <> 0  
'The EOF() function returns a non-zero number when the end of the file is reached  
'This way we know that there is no more data we can read  
```
Close #ff  
  
Ddemo:  
```vb
'Lets have a look at the file we created  
Print "Dir function demo"  
```
S = Dir( "*.*")  
```vb
'The first call to the DIR() function must contain a file mask  
' The * means everything.  
'  
While Len(s) > 0 ' if there was a file found  
Print S ; " " ; Filedate() ; " " ; Filetime() ; " " ; Filelen()  
' print file , the date the fime was created/changed , the time and the size of the file  
```
S = Dir() ' get next  
```vb
Wend  
'Wait 3  
  
'We can use the KILL statement to delete a file.  
'A file mask is not supported  
Print "Kill (delete) file demo"  
```
Kill "test.txt"  
  
S = Dir( "*.TXT") ' check for TXT files  
```vb
While Len(s) > 0  
Print S ; " " ; Filedate() ; " " ; Filetime() ; " " ; Filelen()  
```
S = Dir() ' get next  
```vb
' the next call to the DIR function must not specify the mask so we get the next file  
Wend  
'Wait 3  
  
  
'for the binary file demo we need some variables of different types  
Dim B As Byte , W As Word , L As Long , Sn As Single , Ltemp As Long  
Dim Stxt As String * 10  
```
B = 1 : W = 50000 : L = 12345678 : Sn = 123.45 : Stxt = "test"  
  
'open the file in BINARY mode  
Open "test.biN" For Binary As #2  
Put #2 , B ' write a byte  
Put #2 , W ' write a word  
Put #2 , L ' write a long  
Ltemp = Loc(#2) + 1 ' get the position of the next byte  
```vb
Print Ltemp ; " LOC" ' store the location of the file pointer  
Print Lof(#2) ; " length of file"  
Print Seek(#2) ; " file pointer" ' now you understand difference between loc and seek function  
Print Fileattr(#2) ; " file mode" ' should be 32 for binary  
```
Put #2 , Sn ' write a single  
Put #2 , Stxt ' write a string  
  
Flush #2 ' flush to disk  
Close #2  
  
'now open the file again and write only the single  
Open "test.bin" For Binary As #2  
Seek #2 , Ltemp ' set the filepointer  
Sn = 1.23 ' change the single value so we can check it better  
Put #2 , Sn  
  
L = 1 'specify the file position  
B = Seek(#2 , L) ' reset is the same as using SEEK #2,L  
Get #2 , B ' get the byte  
Get #2 , W ' get the word  
Get #2 , L ' get the long  
Get #2 , Sn ' get the single  
Get #2 , Stxt ' get the string  
Close #2  
  
  
```vb
'now we send to the RS-232 port the values we read back from the file  
Print B ' byte must be 1  
Print W ' word must be 50000  
Print L ' long must be 12345678  
Print Sn ' single must be 1.23  
Print Stxt ' string must be test  
  
  
'we can print to a file like we print to the RS-232  
```
Open "file.tst" For Output As #3  
Print #3 , "This is a test" ; B ; " " ; W ; " " ; L ; " " ; Sn  
Close #3  
  
'read back the data  
Open "file.tst" For Input As #3  
LineInput #3 , S  
Print #1 , S 'send to terminal emulator  
Close #3  
  
  
```vb
'now the good old bsave and bload  
Dim Ar(100) As Byte , I As Byte  
For I = 1 To 100  
```
Ar(i) = I ' fill the array  
```vb
Next  
  
Wait 2  
  
```
W = Varptr(ar(1))  
Bsave "josef.img" , W , 100  
For I = 1 To 100  
Ar(i) = 0 ' reset the array  
Next  
  
Bload "josef.img" , W ' Josef you are amazing !  
  
```vb
For I = 1 To 10  
Print Ar(i) ; " " ;  
Next  
Print  
  
Print "File demo"  
Print Filelen( "josef.img") ; " length" ' length of file  
Print Filetime( "josef.img") ; " time" ' time file was changed  
Print Filedate( "josef.img") ; " date" ' file date  
  
```
Flush ' flush all open files  
```vb
Print "gbDOSerror " ; Gbdoserror  
Print "Finally an advanced dir demo"  
```
S = "*.*" ' return anything  
Directorylist S , 2 ' show all from the last 2 days  
  
S = "write"  
Open "write.dmo" For Output As #2  
Write #2 , S , W , L , Sn ' write is also supported  
Close #2  
  
Open "write.dmo" For Input As #2  
Input #2 , S , W , L , Sn ' write is also supported  
Close #2  
```vb
Print S ; " " ; W ; " " ; L ; " " ; Sn  
  
' For singles take in mind that the result might differ a bit because of conversion  
```
Sn = 123.45  
S = Str(sn) ' create a string  
Print S ' show result of conversion  
Sn = Val(s) ' convert from string to single  
```vb
Print Sn ' show result  
'When storing singles, better use GET/PUT  
  
End  
  
  
  
  
' Read and print Directory and show Filename, Date, Time, Size  
' for all files matching pStr1 and create/update younger than pDays  
Sub Directorylist(pstr1 As String , Byval Pdays As Word)  
```
Local Lfilename As String * 12 ' hold file name for print  
Local Lwcounter As Word , Lfilesizesum As Long ' for summary  
Local Lwnow As Word , Lwdays As Word  
Local Lsec As Byte , Lmin As Byte , Lhour As Byte , Lday As Byte , Lmonth As Byte , Lyear As Byte  
Print "Listing of all Files matching " ; Pstr1 ; " and create/last update date within " ; Pdays ; " days"  
Lwnow = Sysday()  
Lwcounter = 0 : Lfilesizesum = 0  
Lfilename = Dir(pstr1)  
While Lfilename <> ""  
Lsec = Filedatetime()  
Lwdays = Lwnow - Sysday(lday) ' Days between Now and last File Update; uses lDay, lMonth, lYear  
```vb
If Lwdays <= Pdays Then ' days smaller than desired with parameter  
Print Lfilename ; " " ; Filedate() ; " " ; Filetime() ; " " ; Filelen()  
```
Incr Lwcounter : Lfilesizesum = Filelen() + Lfilesizesum  
End If  
Lfilename = Dir()  
```vb
Wend  
Print Lwcounter ; " File(s) found with " ; Lfilesizesum ; " Byte(s)"  
End Sub

```
Some notes. As you can see all included files have the now preferred INC extension.  
Besides the $regfile and code to setup the oscillator and system clock, the code is the same as for other processors. 

The used include file for Xtiny platform differs because the SPI is named different. You best have a look at the Config_MMCSD_HC_XTINY.inc file. 

It can be used for the old AVR, the XMEGA and the Xtiny, MegaX and AVRX.

---

## Edit Copy

With this option, you can copy selected text into the clipboard.

Edit copy shortcut : ![copy](copy.jpg), CTRL+C

---

## Edit Cut

With this option, you can cut selected text into the clipboard.

Edit cut shortcut : ![cut](cut.jpg), CTRL+X

---

## Edit Encrypt Selected Code

This add on option allows you to encrypt portions of your code.

Because the encryption can not be undone, you will get this warning:

![edit_encrypt](edit_encrypt.jpg)

```vb
If you chose YES, the selected code will be encrypted and will result in lines like :

$CRYPT 6288E522B4A1429A6F16D639BFB7405B

$CRYPT 7ABCF89E7F817EB166E03AFF2EB64C4B

$CRYPT 645C88E996A87BF94D34726AA1B1BCCC

$CRYPT 9405555D91FA3B51DEEC4C2186F09ED1

$CRYPT 6D4790DA2ADFF09DE0DA97C594C1B074

```
Only the compiler can decrypt and process these lines. There is no way you can change the $CRYPT lines back into source code !

So make a backup of your code before you use this option. Typically, it will only be used on finished projects.

If the encrypted code contains errors, you will get error messages pointing to the [$CRYPT](crypt.md) lines.

![notice](notice.jpg)This option is not available/enabled by default. You need to buy a license that will unlock this option. Our sales requires your BASCOM serial number too.

---

## Edit Find

With this option, you can search for text in your program.

Text at the current cursor position will automatically be placed in the find dialog box.

All text you search for is saved so the next time you search, you can retrieve the search phrase from a list.

Click the 'Clear History' button to clear the history. This will clear ALL find history from all pull down boxes in both the Find and Replace windows.

![edit_find](edit_find.png)

The following options available:

Option | Description  
---|---  
Case Sensitive | When selected, the case must match. Searching for PRINT will not find pRint. With this option turned off, Print will find print, PRINT, PRinT, etc.  
Whole words only | When selected, only whole words are considered. A whole word is a word that is surrounded by spaces, or that is at the start of a line. Looking for PRINT will find : "Print test" and "print" and "print print". But not "printer"  
Regular expressions | You can use a regular expression to find a match. ^ A circumflex at the start of the string matches the start of a line. $ A dollar sign at the end of the expression matches the end of a line. . A period matches any character. * An asterisk after a string matches any number of occurrences of that string followed by any characters, including zero characters. For example, bo* matches bot, bo and boo but not b. \+ A plus sign after a string matches any number of occurrences of that string followed by any characters except zero characters. For example, bo+ matches boo, and booo, but not bo or be. [ ] Characters in brackets match any one character that appears in the brackets, but no others. For example [bot] matches b, o, or t. [^] A circumflex at the start of the string in brackets means NOT. Hence, [^bot] matches any characters except b, o, or t. [-] A hyphen within the brackets signifies a range of characters. For example, [b-o] matches any character from b through o.  \ A backslash before a wildcard character tells the Code editor to treat that character literally, not as a wildcard. For example, \^ matches ^ and does not look for the start of a line.  
Forward | This is the search direction. By default it will search forward.  Forward means down in this context.  
Backward | This is the search direction. You can use backwards in case you pressed F3 too many times and want to go back to the previous found text.  
Global | All the text of the current editor will be searched.  
Selected text | Only the selected text will be searched.  
So before you press CTRL+F to search for text you can select text and this option will be selected automatic. Otherwise global is selected.  
From cursor | Search from the current cursor position to the end of the code.  
Entire scope | Search from the current cursor position to the end, then search till the start of the cursor position. This will search the entire text.  
  
Find in Files

The Find in Files option can be used to search for text in files.

![find_files](find_files.png)

Option | Description  
---|---  
Case Sensitive | When selected, the case must match. Searching for PRINT will not find pRint. With this option turned off, Print will find print, PRINT, PRinT, etc.  
Whole words only | When selected, only whole words are considered. A whole word is a word that is surrounded by spaces, or that is at the start of a line. Looking for PRINT will find : "Print test" and "print" and "print print". But not "printer"  
Regular expressions | You can use a regular expression to find a match. ^ A circumflex at the start of the string matches the start of a line. $ A dollar sign at the end of the expression matches the end of a line. . A period matches any character. * An asterisk after a string matches any number of occurrences of that string followed by any characters, including zero characters. For example, bo* matches bot, bo and boo but not b. \+ A plus sign after a string matches any number of occurrences of that string followed by any characters except zero characters. For example, bo+ matches boo, and booo, but not bo or be. [ ] Characters in brackets match any one character that appears in the brackets, but no others. For example [bot] matches b, o, or t. [^] A circumflex at the start of the string in brackets means NOT. Hence, [^bot] matches any characters except b, o, or t. [-] A hyphen within the brackets signifies a range of characters. For example, [b-o] matches any character from b through o.  \ A backslash before a wildcard character tells the Code editor to treat that character literally, not as a wildcard. For example, \^ matches ^ and does not look for the start of a line.  
Search all project files | This option will search through all project files. Files considered are $INCLUDE files. Nested $include files are not considered.   
Search all open files | This option will search though all open files. This are loaded files visible in the TABS  
Search in directories | You can specify a custom folder to search for the text.  
Search in current file | This option will restrict the search to the current file.  
  
Edit Find shortcut : ![filefind](filefind.jpg), CTRL+F

---

## Edit Find Next

With this option, you can search again for the last specified search item.

Edit Find Next shortcut : ![find_next16](find_next16.jpg), F3

---

## Edit Fold All Subs and Functions

When Code folding is enabled in [Options, Environment, IDE, Editor](options_environment.md), this options will fold/collapse all sub procedures and functions.

Other structures that can be folded with F11 remain unaltered.

Using SHIFT+F11 or CTRL+ENTER, you can fold/unfold the current block.

Consider this example :

![code_fold1](code_fold1.png)

Both the Sub and For/Next can be folded but the Fold All Subs and Functions option, will only fold the sub :

![code_fold2](code_fold2.png)

See Also

[Edit Unfold All Code](edit_unfold_all_code.md)

---

## Edit Goto

With this option, you can immediately go to a specified line number.

Edit go to line shortcut : ![33_go_jump_icon](33_go_jump_icon.png) ,CTRL+G

---

## Edit Goto Bookmark

With this option, you can jump to a bookmark.

There can be up to 8 bookmarks. Shortcut : CTRL+Q+ x where x can be 1-8

Bookmarks are stored in a file named <project>.BM

---

## Edit Indent Block

With this option, you can indent a selected block of text.

Edit Indent Block shortcut : ![indent](indent.jpg), CTRL+SHIFT+I

---

## Edit Insert ASCII

This option will show a pop up window from which you can select an ASCII character.

![edit_insert_ascii](edit_insert_ascii.png)

In BASCOM you can embed ASCII characters by using brackets embedded with the ASCII code like : {065}

For example : Dim S As String : S="AB{067}"

This is the same as S="AAA"

The pop up lists shows all ASCII values and when you click the OK-button, the brackets are added.

---

## Edit Paste

With this option, you can paste text from the clipboard starting at the current cursor position.

Edit paste shortcut : ![paste](paste.jpg), CTRL+V

---

## Edit Proper Indent

This option will properly indent your code.

Indention is used to make code better readable.

Every structure will be indented. And nested will increase indenting.

This code :

For C = 0 To 100

B = A(c)

```vb
Print "Read " ; C ; ":" ; B ; "/" ; Hex(b)

Waitms 4

Next

```
Will be transformed into :

For C = 0 To 100

B = A(c)

```vb
Print "Read " ; C ; ":" ; B ; "/" ; Hex(b)

Waitms 4

Next

```
And this is a sample with nesting :

```vb
Do

Input "Data to write ? (0-255)" , D

Print "Reading content of EEPROM (via ERAM Byte)"

For C = 0 To 100

```
B = A(c)

```vb
Print "Read " ; C ; ":" ; B ; "/" ; Hex(b)

Waitms 4

Next

Loop

```
When indenting does not work you need to check your code for mistakes. For example for endif instead of End If.

Proper indenting is also required for [proper drawing of indention](edit_show_excluded_code.md).

---

## Edit Redo

With this option, you can redo the last undo.

Edit Redo shortcut : ![redo](redo.jpg), CTRL+SHIFT+Z

---

## Edit Remark Block

With this option, you can Remark or Unremark a selected block of text.

While you can use '( and ') to remark a block of code, you might prefer the old BASIC way using just one ' .

When a remark is found, it will be removed. When there is no remark, it will insert a remark.

---

## Edit Replace

With this option, you can replace selected text in your program.

![edit_replace](edit_replace.png)

All options except 'Replace With' are described under [Edit Find](edit_find.md).

Replace With : this is the new text that will replace the old text.

In version 2087 you can also replace text in files. 

![edit_replace_files](edit_replace_files.png)

The search and replace works similar to Search And Find in Files.

We recommend to make a backup of your project before you use 'Replace All'.

Edit Replace shortcut : ![replace16](replace16.jpg), CTRL+R

---

## Edit Show Dead Code

This option turns on/off marking of 'dead' code.

Dead code is code that does not do a thing and could be removed.

Dead code is shown in Italic and gray but you can change the color and italic.

Dead code is similar to Excluded code with the difference that excluded code is not compiled while dead code is compiled. 

Dead code is a new feature in 2080 and intended to show you which variables or code are not used.

You can decide if the code is really dead, and need to be removed, or not.

Since this is a new feature, you should take care before deleting 'dead code'

![edit_dead_code](edit_dead_code.png)

The example above demonstrates a few dead code elements:

\- the local dead as byte, is not used in the code

\- the function result is assigned twice without that the result is used, this does not make sense

\- the GOTO skips over some code which is never used (print)

See Also

[Edit Show Excluded Code](edit_show_excluded_code.md)

---

## Edit Show Excluded Code

This option turns on/off marking of excluded code.

Excluded code is code that is not compiled as part of the project because conditional compilation parameters exclude the code.

Excluded code is shown in Italic and gray but you can change the default colors.

```vb
For example when using an XMEGA processor, the _XMEGA constant will be set to 1. When the option is turned off, it will show normal like :

  

#if _xmega  
print "XMEGA"  

#else  
print "NORMAL"  

#endif  
  
```
When then option is turned on, the editor will show it like :

```vb
#if _xmega  
print "XMEGA"  

#else  
print "NORMAL"  

#endif  


```
When you have a lot of conditional code it is hard to see which code is executed. When you turn the option on, it is much easier to see.

Check out this example:

![edit_show_excluded_code](edit_show_excluded_code.png)

  
  


In order for this option to work correct, your code should not contain syntax errors. 

See Also

[#IF, #ELSEIF . #ELSE](_if_else_endif.md) , [Show Dead Code](edit_show_dead_code.md)

---

## Edit Toggle Bookmark

With this option, you can set/reset a bookmark, so you can jump in your code with the Edit Go to Bookmark option. Shortcut : CTRL+K + x where x can be 1-8

Bookmarks are stored in a file named <project>.BM

---

## Edit Undo

With this option, you can undo the last text manipulation.

Edit Undo shortcut : ![undo](undo.jpg), CTRL+Z

---

## Edit Unfold All Code

This option will unfold all folded code so all code becomes visible.

See Also

[Edit Fold All Subs and Functions](edit_fold_all_subs_and_functions.md)

---

## Edit Unindent Block

With this option, you can unindent a block.

Edit Unindent Block shortcut : ![outdent](outdent.jpg), CTRL+SHIFT+U

---

## File Close

Close the current program.

The current editor window will be closed. When you have made changes to the program, you will be asked to save the program first. You can then decide to save, cancel, or not to save the changes you have made.

File close shortcut : ![fileclose](fileclose.jpg)

---

## File Exit

With this option, you can leave BASCOM.

If you have made changes to your program, you can save them upon leaving BASCOM.

All of the files you have open, at the moment you choose exit, will be remembered.

The next time you run BASCOM, they will be opened automatically.

File exit shortcut : ![exit](exit.jpg)

---

## File New

This option creates a new window in which you will write your program.

The focus is set to the new window.

You can have multiple windows open at the same time.

Only one window can have the focus. When you execute other functions such as [Simulate](program_simulate.md) or [Program Chip](program_send_to_chip.md), BASCOM will use the files that belong to the current active program. This is in most cases the program which has the focus.

File new shortcut: ![new](new.jpg), CTRL + N

---

## File Open

With this option you can load an existing program from disk.

BASCOM saves files in standard ASCII format. Therefore, if you want to load a file that was made with another editor be sure that it is saved as an ASCII file. Most programs allow you to export the file as a DOS or ASCII file.

Note that you can specify that BASCOM must reformat the file when it opens it with the [Options Environment](options_environment.md) option. This should only be necessary when loading files made with another editor.

File open shortcut : ![fileopen](fileopen.jpg), CTRL+O

---

## File Print

With this option, you can print the current program.

Note that the current program is the program that has the focus.

File print shortcut : ![fileprint](fileprint.jpg), CTRL+P

---

## File Print Preview

With this option, you can preview the current program before it is printed.

Note that the current program is the program that has the focus. 

File print preview shortcut : ![print_prev](print_prev.jpg)

---

## File Project

Originally the IDE was not designed to support projects. Each file you open is a project.

Most chips were not even suited for big projects.

Some projects use a lot of include files. It is a good idea to break up your code in modular tested modules.

You can simply include the modules with [$include](include.md).

In order to make working with a project more convenient, a number of Project options have been added. The Project menu can be found under the File menu. The Project menu has 4 sub menu items and a MRU list(most recent used projects).

When in project mode, the main project file will be compiled. In normal mode, the active window is considered the project and will be compiled. The same is true for the simulator and programmer. 

A simple project explorer has been added that will list all project files. The active project will be shown in blue. The relative path is shown.

![ProjectExplorer](projectexplorer.png)

You can add a new file to the active project. By default the INC extension will be selected. It will be good practice to give included files the INC extension. The main project should have the BAS extension. When you click the ADD button, a file selection dialog will appear. You can select multiple files by using the SHIFT and/or CTRL keys.

When you add a file to a project, it will be added to the project list. When you double click the file in the list it will be selected. Or when it was not loaded before, it will be loaded from disk.

That a file is part of a project collection does not mean that the file will be used or included : you still need to [$INCLUDE](include.md) a file that you want to use in your project.

You can also remove a file from the project. This will not remove or delete the file from disk. The file will only be removed from the project collection. 

Only one file can be the main project. This is the file that will be compiled. The main file is colored in blue.

![notice](notice.jpg)When you updated from a previous version, you need to reset the docking in order to make the Project List window visible. This option you can find under [Options, Environment, IDE](options_environment.md)

Project New

This option will close all files and the current project and will query for a project file name. The file will have the PRJ extension.

Project Open

This option will close all open files and let you select an existing project file. A project file has the PRJ extension.

The PRJ file contains no code, it only contains data about the project files.

All files from the project will be loaded when they were loaded when you closed the project.

The position and size will be set exactly as when you closed. 

![FileprojectOpen](fileprojectopen.png)

Project Save

This option will save all project files. It will also save other opened non-project files.

Project Close

This option will close the active project. This will end the project mode. The project mode is started when you open a PRJ file either with OPEN or by clicking a PRJ file from the MRU menu. 

When you close bascom and you have the Option 'Auto Load All Files' checked, then like usual, all open files will be saved and when you run bascom again, they will all be opened. This might be confusing since you work in normal mode by default. It is recommended to deactivate the 'Auto Load All Files' when working with projects.

In project mode, you can also drag and drop files to the IDE. If they have the BAS or INC extension, they will be added to the project. In normal mode, the file will be opened.

---

## File Save

With this option, you save your current program to disk under the same file name.

The file name is visible in the Windows caption of the edit window.

If the program was created with the [File New](file_new.md) option, you will be asked to name the file first. Use the [File Save As](file_save_as.md) option to give the file another name.

Note that the file is saved as an ASCII file.

File save shortcut : ![filesave](filesave.jpg), CTRL+S

---

## File Save As

With this option, you can save your current program to disk under a different file name.

When you want to make some changes to your program, but you do not want to make changes to the current version you can use the "Save As" option. It will leave your program as it was saved, and will create a new file with a new name so you end up with two copies. You then make changes to the new created file.

Note that the file is saved as an ASCII file. 

File save as shortcut : ![BASC0018_wmf](basc0018_wmf.gif)

---

## Help About

This option shows an about box as shown below.

![about](about.png)

Your serial number is shown on the third line of the about box.

You will need this when you have questions about the product.

The compiler and IDE version numbers are also shown.

When you click the App data dir link, the folder which contains the BASCOM settings will be opened:

![about_data_folder](about_data_folder.png)

It contains the bascom-avr.xml file with all settings and the bascavr.log file. When you need support, you might be asked to email these files.

When you need support, also click the Copy-button. It will copy the following info to the clipboard, which you can paste in your email :

Dont forget that Serial numbers should not be sent to the user list.

Make sure you sent your email to support and not a public list !

Compiler version :1.11.8.3

IDE version :1.11.8.5

Serial number :XX-XXXX-XXXXX

Windows OS :Microsoft Windows XP

Windows SP :Service Pack 2

Explorer :7.0.5730.11

Company :MCS

Owner :Mark Alberts

Windows dir :C:\WINNT

App data dir :C:\Documents and Settings

System dir :C:\WINNT\system32

When you click the support link, your email client will be started and an email to support@mcselec.com will be created.

Click on Ok to return to the editor.

---

## Help Credits

BASCOM was "invented" in 1995. Many users gave feedback and helped with tips, code, suggestions, support, a user list, and of course with buying the software.

The software improved a lot during the last 25 years and will so during the next decade.

While it is impossible to thank everybody there are some people that deserve credits :

•| Peter Maroudas. He wrote and tested the FT80x FTDI display support. FT800 support would not exist without him.  
---|---  
  
•|   
---|---  
  
•| Josef Franz VÃ¶gel. He wrote a significant part of the libraries in BASCOM-AVR. He is also author of AVR-DOS.  
---|---  
  
•| Dr.-Ing. Claus Kuehnel for his book 'AVR RISC' , that helped me a lot when I began to study the AVR chips. Check his website at <http://www.ckuehnel.ch>  
---|---  
  
•| Atmel, who gave permission to use the AVR picture in the start up screen. And for the great tech support. Check their website at <http://www.atmel.com>  
---|---  
  
•| Brian Dickens, who did most of the Beta testing. He also checked the documentation on grammar and spelling errors. (he is not responsible for the spelling errors i added later :-) )  
---|---  
  
•| Jack Tidwell. I used his FP unit for singles. It is the best one available.  
---|---

---

## Help Index

Shows the BASCOM help file.

When you are in the editor window, the current word selected or by the cursor will be used as a keyword.

Notice that when the help window is small, you might need to make the help window bigger to show the whole content.

![notice](notice.jpg)The help contains complete sample code and partial sample code. 

In all cases the samples are shown to give you an idea of the operation. When trying a program you should always use the samples from the SAMPLES directory. These are updated and tested when new versions are published. The (partial) samples are not all updates, only when they contain errors. So the samples from the help might need some small adjustments while the samples form the SAMPLES dir will work at least on the used chip.

---

## Help MCS Forum

This option will start your default Web browser and direct it to [http://www.mcselec.com/index2.php?option=com_forum&Itemid=59](<http://www.mcselec.com/index2.php?option=com_forum&Itemid=59>)

This forum is hosted by MCS Electronics. There are various forums available. You can post your questions there. Do not cross post your questions on multiple forums and to support.

The forum is available for all users : demo or commercial users.

Note that everything you write might be on line for ever. So mind your language.

Users of the commercial version can email MCS support.

The forum allows uploads for code examples, circuits etc.

If you try to abuse the forum or any other part of the MCS web, you will be banned from the site.

![forum](forum.png)

---

## Help MCS Shop

This option will start your default web browser and direct it to :[http://www.mcselec.com/index.php?option=com_phpshop&Itemid=1](<http://www.mcselec.com/index.php?option=com_phpshop&Itemid=1>)

You can order items and pay with PayPal. PayPal will accept most credit cards.

Before you order, it is best to check the [resellers](international_resellers.md) page to find a reseller near you. Resellers can help you in your own language, have all MCS items on stock, and are in the same time zone.

![shop](shop.png)

Before you can order items, you need to create an account.

Read the following about the new website :[ http://www.mcselec.com/index.php?option=com_content&task=view&id=133&Itemid=1](<http://www.mcselec.com/index.php?option=com_content&task=view&id=133&Itemid=1>)

---

## Help Update

The manual update process is explained [here](updates.md).

The Help Update is an automated version.

The DEMO version can not be updated. You can however install the full version into the DEMO folder.

In order to do a successful update you need the following :

\- license validated in the register (https://register.mcselec.com)

\- working internet connection.

\- firewall and anti virus software must allow BASCOM to connect to the internet

When you click Help, Update, the following window will be shown:

![help_update](help_update.png)

You can select if you want to update BasCom or the Add-On's. 

By default BasCom is selected.

BasCom Update

You need to click the START button to start the actual update process.

When there are unsaved files, you will get an error message :

![update_error](update_error.png)

Your work/project must be saved since as soon the update download is finished, the setup will be executed and BASCOM is closed.

When there are no unsaved files, the current version will be checked.

Checking for update...

Current version : 2.0.8.0

Latest version : 2.0.7.8

No newer version found

In this case, there is no newer file and nothing happens. You need to click the CLOSE button to close the Update window. The IDE will not be closed in this case.

If however a newer version exists, it will be downloaded and unzipped in your windows TEMP folder.

After that setup.exe will be executed with admin rights. So you might get a windows security message that setup requires admin rights. 

BASCOM will close automatically so the new version can be installed in the same folder. We recommend however to install each version into a different folder.

There is no need to uninstall an older version first. 

This setup is the same as you used when you installed the software. But of course the latest version.

You can install into the same folder, but you may also install into a new folder. 

When installing into a new folder you must manual install/copy the license file bscavrl.dll into the new folder yourself.

The bscavrl.dll file you get when you purchase bascom. It is either on CD-ROM or in the bascom-avr application folder.

Please notice that this license file is offered during purchase. We do not offer it again in the event you lost it. 

Add On Update

When you chose to update Add On, you can also specify that libraries will be copied after the update. You do this by checking the 'Copy Libs After Update' check box.

The Add on update will check if you have an add on installed. It will then check if there is an update available. Notice that not all add ons you purchased are supported yet. So those you have to manual download/install.

The supported Add Ons :

\- AVRDOS. 

\- I2CSLAVE

\- XTINY

The add on is always ZIPPED and this ZIP file is downloaded to a new SUB folder named ADDONS.

This ADDONS subfolder is created in the BasCom-AVR application folder.

Each Add On is installed into its own sub folder. So for AVRDOS it is installed into ADDONS\AVRDOS

Older versions that might exist are overwritten.

When an Add-On contains a LIB or LBX file, the option 'Copy Libs after update' will be copied to the BasCom-AVR Library folder. The original file will be renamed so you always have a backup. 

You do need write access in the BasCom-AVR application folder and sub folder.

---

## Help Wiki

This option will open the browser at wiki.mcselec.com

The wiki contains the help file, projects and is partial translated into German as well.

When you want to contribute you need to create an account and send an email to [tomi@mcselec.com](<mailto:tomi@mcselec.com>) to get the proper access rights.

---

## Options Communication

With this option, you can modify the communication settings for the terminal emulator.

![options_communication](options_communication.png)

Item | Description  
---|---  
Comport | The communication port of your PC that you use for the terminal emulator.  
Baud rate | The baud rate to use.  
Parity | Parity, default None.  
Data bits | Number of data bits, default 8.  
Stop bits | Number of stop bits, default 1.  
Handshake | The handshake used, default is none.  
Emulation | Emulation used, default TTY and VT100.  
Font | Font type and color used by the emulator.  
Back color | Background color of the terminal emulator.  
Keep TE open | This option will keep the terminal emulator COM port open when you close the window or move the focus away. Some serial programmers which close the COM port when they need to program, will not work in this mode when they use the same COM port.  
Use Existing COM ports | When you select this option, you will get a list with the available COM ports only at places you can select a COM port. When you insert an USB virtual COM port, it will be added to list automatically. Removing virtual COM ports will also update the available COM port list. When you do not select this option you get a list with COM1-COM255.  
  
Note that the baud rate of the terminal emulator and the baud rate setting of the [compiler options](options_compiler_communication.md), must be the same in order to work correctly.

The reason why you can specify them both to be different is that you can use the terminal emulator for other purposes too.

---

## Options Compiler

With this option, you can modify the compiler options.

The following TAB pages are available:

[Options Compiler Chip](options_compiler_chip.md)

[Options Compiler Output](options_compiler_output.md)

[Options Compiler Communication](options_compiler_communication.md)

[Options Compiler I2C , SPI, 1WIRE](options_compiler_i2c__spi__1wire.md)

[Options Compiler LCD](options_compiler_lcd.md)

---

## Options Compiler Communication

![options_compiler_com](options_compiler_com.png)

Options Compiler Communication

Item | Description  
---|---  
Baud rate | Selects the baud rate for the serial communication statements. You can also type in a new baud rate. It is advised to use [$BAUD](baud_1.md) in the source code which overrides this setting.  
Frequency | Select the frequency of the used crystal. You can also type in a new frequency. It is advised to use [$CRYSTAL](crystal_1.md) in the source code which overrides this setting. Settings in source code are preferred since it is more clear.  
  
The settings for the internal hardware UART are:

No parity , 8 data bits , 1 stop bit

Some AVR chips have the option to specify different data bits and different stop bits and parity.

Note that these settings must match the settings of the terminal emulator. In the simulator the output is always shown correct since the baud rate is not taken in consideration during simulation. With real hardware when you print data at 9600 baud, the terminal emulator will show weird characters when not set to the same baud rate, in this example, to 9600 baud.

---

## Options Compiler Output

![options_compiler_output](options_compiler_output.png)

Options Compiler Output

Item | Description  
---|---  
Binary file | Select to generate a binary file. (xxx.bin)  
Debug file | Select to generate a debug file (xxx.dbg)  
Hex file | Select to generate an Intel HEX file (xxx.hex)  
Report file | Select to generate a report file (xxx.rpt)  
Error file | Select to generate an error file (xxx.err)  
AVR Studio object file | Select to generate an AVR Studio object file (xxx.obj) Using the OBJ file you can debug with AVR Studio. This also allows to use tools like ICE. In Studio 6.0 (fixed in 6.1) you need to make these changes in Studio : Locate the file atmelstudio.pkgundef under the installation folder for Atmel. Studio. Remove (or remark) the below lines from the file and save the file.  [$RootKey$\Languages\Language Services\Basic] [$RootKey$\AutomationProperties\TextEditor\Basic]  
Size warning | Select to generate a warning when the code size exceeds the Flash ROM size.  
Swap words | This option will swap the bytes of the object code words. Useful for some programmers. Should be disabled for most programmers. Don't use it with the internal supported programmers.  
Optimize code | This options does additional optimization of the generated code. Since it takes more compile time it is an option.  
Show internal variables | Internal variables are used. Most of them refer to a register. Like _TEMP1 = R24. This option shows these variables in the report.

---

## Options Environment

The Environment TAB has a few TABS of it's own.

Options Environment Editor 

![options_env_editor](options_env_editor.png)

OPTION | DESCRIPTION  
---|---  
Auto Indent | When you press return, the cursor is set to the next line at the current column position.  
Don't change case | When set, the reformat won't change the case of the line after you have edited it. Default is that the text is reformatted so every word begins with upper case.  
Reformat BAS files | Reformat files when loading them into the editor. All lines are reformatted so that multiple spaces are removed. This is only necessary when you are loading files that where created with another editor. Normally you won't need to set this option.  
Reformat code | Reformat code when entered in the editor. The reformat option will change the modified line. For example a = a + 1 will be changed into : a = a + 1 . When you forget a string end marker ", one will be added, and endif will be changed into End If. And finally, ? is changed into Print.  
Smart TAB | When set, a TAB will place the cursor to the column where text starts on the previous line.  
Syntax highlighting | This options highlights BASCOM statements in the editor.  
Show margin | Shows a margin on the right side of the editor. You can specify the position. By default this is 80.  
Comment | The position of the comment. Comment is positioned to the right of your source code. Except when comment is first character of a line.  
TAB-size | Number of spaces that are generated for a TAB.  
Key mapping | Choose default, Classic, Brief or Epsilon.  
No reformat extension | File extensions separated by a space that will not be reformatted when loaded. For example when DAT is entered, opening a DAT file can be done without that it is reformatted.  
Size of new editor window | When a new editor window is created you can select how the windows will be created. Normal or Maximized (full window)  
Line Numbers | Show line numbers in the margin.  
Show Subs/Labels | This option will show sub modules/functions and labels at the top of the editor window in a drop down box. To get more screen space you can disable this option.  
Remove Empty Lines | This option will remove empty lines when you paste data from the clipboard into the editor. When you copy & paste text from the help file (or any other source) you will find that windows inserts empty lines. This option will change two CR+LF into one.   
  
Indention

When indention lines are drawn, you can select the color of each level. The default is gray.

When you move the mouse over an indention line, the tooltip will show the start of the structure.

![edit_indent_tooltip](edit_indent_tooltip.png)

The sample above shows the info for the green indention line. 

Obvious when the code fits into the screen, it is simple to see that the green line belongs to #IF _XMEGA. But when there is a lot of code in the editor, and you can not see all of the code, it can be a big help.

Code Folding

This option activates so called Code Folding. Code Folding allows you to hide/fold portions of your code. 

![options_env_editor_codefold1](options_env_editor_codefold1.png)

The screen shot above shows :

1 \- The Sub DEMO is folded. So you only see Sub Demo in your code. To indicate that the sub is folded there is a marker at the end of the line (3 dots)

Another indicator is the + sign. This means that the node is folded. 

2 \- When you put the cursor above the marker, you get a hint with the folded text/code. 

3 \- The minus means that you can fold that node. When you click the - it will turn into a + and the code is folded. 

This is how it looks when the node at (3) is clicked:

![options_env_editor_codefold2](options_env_editor_codefold2.png)

When folding code, all child code (all levels under the node) will be folded/unfolded as well.

A node is a point in your code that is part of a structure like sub/end sub , function/ end function, for/next, do/loop, while/wend. Remarks , Dim, Const and Config can also be folded.

When you press F11, the current SUB or FUNCTION will be folded/unfolded. The Editor menu also has options to fold/unfold all code.

When you want to fold code that normally would not fold you can use a trick. When you define a constant you can use this for code folding:

Const fold=1

```vb
#IF Fold

print "fold this"

print "end this too"

#ENDIF

```
Conditional compilation is used to fold the code. 

Draw Indention Lines

This option will draw vertical indent lines for structures. 

![editor_draw_indent](editor_draw_indent.png)

Drawing indention lines may result in slower screen painting. Errors in your code might result in wrong painting of the lines.

Options Environment Font

![options_env_ide_font](options_env_ide_font.png)

OPTION | DESCRIPTION  
---|---  
Background color | The background color of the editor window. Choose a color that is the same as your background. In a white room, using white would be best for your eyes.  
Keyword color | The color of the reserved words. Default Navy. The keywords can be displayed in bold too.  
Comment color | The color of comment. Default green. Comment can be shown in Italic too.  
ASM color | Color to use for ASM statements. Default purple.  
HW registers color | The color to use for the hardware registers/ports. Default maroon.  
String color | The color to use for string constants : "test"  
Variable color | The color to use for variables. Default is black.  
User Function Color | The color to use for user SUBS and FUNCTIONS. The default is fuchsia.  
Excluded Code Color | The color to use for Excluded code (code not compiled because of conditional compilation).  
Dead Code Color | The color to use for Dead Code. (code that is not used)  
Editor font | Click on this button to select another font for the editor window. A good choice is Fixedsys.  
Use Monofont | When checked and the selected font is a monofont the font will be drawn with monofont properties. Otherwise it will be shown as non monofont. Use this for compatibility with old bascom versions and fonts.  
Show Hidden Characters | This option will show special characters in the editor. Special characters are characters such as CR and LF. And all characters with an ASCII value above 127. You can use this option to find odd characters in your code which could result in compilation errors.  
Override Windows Font | This setting will override the Windows default font. You can select a font by clicking the IDE system font button. It is recommended to select a font like SEGOU UI, normal, 10 points. This font is used by all forms of the IDE. It is independent of the editor font.   
Big Menu Icons | This option will use bigger icons for the IDE. The normal default size is 16x16. The bigger size is 32x32. This will give better images when you have a high resolution monitor setting.   
  
Options Environment IDE 

![options_ev_ide](options_ev_ide.png)

OPTION | DESCRIPTION  
---|---  
Tool tips | Show tool tips when hovering over form elements such as buttons.  
File location | Click to select a directory where your program files are stored. By default Windows will use the My Documents path.  
Sample Location | Click to select the folder where the SAMPLE files are located. They are either stored in a sub folder of the application, or in a folder under the Documents\MCS Electronics\BASCOM-AVR\samples folder  
Use HTML Help | Chose between old help and CHM Help. CHM is the preferred help file. Since HLP is not supported under Vista, it is advised to switch to CHM/HTML Help. The HLP file is not distributed but using the UpdateWiz you can still download the HLP file.  
Code hints | Select this option to enable code hints. You can get code hints after you have typed a statement that is recognized as a valid statement or function.   
Hint Time | The delay time in mS before a code hint will be shown.  
Hint Color | The background color of the hints.  
Allow multiple Instances | Select this option when you want to run multiple instances of BASCOM. When not enabled, running a second copy will terminate the first instance.  
Auto save on compile | The code is always saved when you compile. When you select this option, the code is saved under the same name. When this option is not selected, you will be prompted for a new filename.  
Auto backup | Check this option to make periodic backups. When checked you can specify the backup time in minutes. The file will also be saved when you press the compiler button.  
History Backup | This option creates a history backup of the source file each time you save it. When you Compile code, the active source will be saved too before compilation and hence it will create a history file as well. The history file is a version of the code saved in the HISTORY folder. This folder is located in the same folder as the main project.  The file will be named <FILE>~yymmdd hhnnss.hst Where <FILE> is the original file name, and yymmdd is the date and hhNNss is the time.   
Auto load last file | When enabled, this option will load the last file that was open into the editor, when you start BASCOM.  
Auto load all files | When enabled, this option will load all files that were open when you closed BASCOM.  
Check for updates | Select this option to check for updates when the IDE is started.  
Show TABS | This option will enable/disable the TAB for multiple windows. While the TAB is convenient to switch between windows, it will also consume screen space. You can disable this option to get more screen space.  
Reset docking | This will reset the dockable windows to the default position.  
Search Find Auto Complete | This option can enable/disable the auto completion in the Find dialog. When it is active and you type some text, based on historical input, the text will be completed. This is not always desired and can be disabled.  
Language | This will set the language in the main menu to the selected language. Not all listed languages are supported/translated yet.  
Clear Do not Ask | Some messages have a 'do not ask again' option. To reset this and thus show the messages, you can click this button.  
Use New Parser | When compiling a project, the main file is searched for some settings like $regfile, $hwstack, $swstack and $framesize. This information is passed to the compiler DLL. This search is fast but simple : it will not work correct when using directives such as : #IF someConditon $regfile = "m88def.dat" #ELSE $regfile = "m2650def.dat" #ENDIF The parser used for the code explorer is capable to get the information but requires more time because it will parse the entire project. So you have the option to choose the old method or the new method. In version 2087 the new parser is made default.  It is good practice to start your project with the required info :  $regfile = "yourmicro.dat" $hwstack=32 ' values shown as sample $swstack=32 $framesize=32 We recommend that you always use 'New Parser' since the old method will be disregarded in a future update. This does mean that your main project code always need to contain the most important settings : $REGFILE, $HWSTACK, $SWSTACK and $FRAMESIZE. These settings override the optional project configuration settings. A future version will not use the configuration file settings since it is best that these settings are stored in the code.  This setting is also required for the [$PROGRAMMER](programmer.md) directive.   
Code Explorer with separate INC files | The Code explorer will put all elements in one tree without file names. Setting this option however will create a tree of elements with all file names under a branch named 'Inc Files'.  ![code_expl_with_sep_inc](code_expl_with_sep_inc.png)![code_expl_without_sep](code_expl_without_sep.png) Code explorer with separate inc files Code explorer without separate inc files  
  
|   
  
  
Options Search

![options_search](options_search.png)

Using the Search and select options you can customize the search and select colors.

You can also enable the option : Search Multi Color and Select Multi Color.

When search multi color is enabled all other matches will be highlighted too.

![multi_search](multi_search.png)

This sample shows what happens when you search for 'serial'. Note that that text is gray because of the 'Dead Code' option.

![options_multi](options_multi.png)

When you enable Select Multi Color, all text you select using the keyboard, mouse, or double click, will be highlighted the usual way. All other occurrences will be highlighted too.

This can be confusing. 

The multi select coloring will do only what the name suggests : it will color the selecting text and all other occurrences. But when you perform an operation like replace, it will only be performed on the active selected text.

Options Environment PDF

![options_env_pdf](options_env_pdf.png)

OPTION | DESCRIPTION  
---|---  
Auto open processor PDF | This option will automatic load the PDF of the selected micro processor in the PDF viewer. The $REGFILE value determines which data sheet is loaded. The PDF must exist otherwise it can not be loaded.  
Open PDF in new sheet | Every time you change the value of the $REGFILE the processor PDF can be shown in the same sheet, or a new sheet can be shown with the PDF. A good option in case your project uses multiple processors.  
Auto save/load project PDF | Load all PDF's when the project is opened that were loaded when the project was closed.  
  
Custom ShortCuts

When you want to define your own short cuts you can create an ini file named shortcuts.ini.

This ini file is just a text file you can create with notepad. Store this file in the BASCOM application folder.

To enable the user shortcuts you need to make an option named : ENABLED with the value -1.

This is an example of the default values

[MENU]

enabled=-1

FileNew=CTRL+N

FileSave=CTRL+S

FilePrint=CTRL+P

EditUndo=CTRL+Z

EditRedo=SHIFT+CTRL+Z

EditCut=CTRL+X

EditCopy=CTRL+C

EditPaste=CTRL+V

EditFind=CTRL+F

EditFindNext=F3

EditReplace=CTRL+R

EditGoto=CTRL+G

EditIndent=SHIFT+CTRL+I

EditUnIndent=SHIFT+CTRL+U

EditUnremarkBlock=CTRL+M

EditProperIndent=CTRL+ALT+P

Compile=F7

SyntaxCheck=CTRL+F7

ProgramShowResult=CTRL+W

ProgramSimulate=F2

ProgramSendToChip=F4

ProgramResetChip=SHIFT+F4

TerminalEmulator=CTRL+T

LCD_Designer=CTRL+L

LibManager=CTRL+I

BatchCompile=CTRL+B

ShowDevMng=CTRL+D

To turn the custom shortcuts off set the ENABLED to 0.

---

## Options Monitor

With this option you can modify the monitor settings.

OPTION | DESCRIPTION  
---|---  
Upload speed | Selects the baud rate used for uploading  
Monitor prefix | String that will be send to the monitor before the upload starts  
Monitor suffix | String that us sent to the monitor after the download is completed.  
Monitor delay | Time in milliseconds to wait after a line has been sent to the monitor.  
Prefix delay | Time in milliseconds to wait after a prefix has been sent to the monitor.

---

## Options Printer

With this option you can modify the printer settings.

![options_printer](options_printer.png)

OPTION | DESCRIPTION  
---|---  
Font | Printer font to use when printing  
Setup | Click to change the printer setup  
Color | Will print in color. Use this only for color printers.  
Wrap lines | Wrap long lines. When not enabled, long lines will be partial shown.  
Print header | Print a header with the filename.  
Line numbers | Will be the line number before each line.  
Syntax | Enable this to use the same syntax highlighting as the editor  
Left margin | The left margin of the paper.  
Right margin | The right margin of the paper.  
Top margin | The top margin of the paper.  
Bottom margin | The bottom margin of the paper.

---

## Options Programmer

With this option you can modify the programmer settings.

![options_programmer](options_programmer.png)

OPTION | DESCRIPTION  
---|---  
Programmer | Select one from the list.  
Play sound | Name of a WAV file to be played when programming is finished. Press the directory button to select a file.  
Erase Warning | Set this option when you want a confirmation when the chip is erased.  
Auto flash | Some programmers support auto flash. Pressing F4 will program the chip without showing the programmer window.  
Auto verify | Some programmers support verifying. The chip content will be verified after programming.  
Upload code and data | Set this option to program both the FLASH memory and the EEPROM memory  
Program after compile | When compilation is successful, the chip will be programmed  
Set focus to terminal emulator | When the chip is programmed, the terminal emulator will be shown  
|   
| Parallel printer port programmers  
LPT address | Port address of the LPT that is connected to the programmer.  
Port delay | An optional delay in uS. It should be 0. But on some systems a delay might be needed.  
|   
| Serial port programmer  
COM port | The com port the programmer is connected to.  
STK500 EXE | The path of stk500.exe. This is the full file location to the files stk500.exe that comes with the STK500.  
USB | For mkII and other Atmel USB programmers you can enter the serial number here. Or you can look it up from the list.  
Baud | Some serial programmers have an optional baud rate you can chose. The usual values are supported. When you want special custom baud rate you can replace the baud rate by creating a file named : progbaud.lst In this text file you can place all the baud rates. For example : 123 300 600 1200 2400 4800 9600 9610 19200 38400 57600 128000 256000 115200 500000 Then save the file. The file must reside in the bascom-avr application folder. The file is loaded when you run bascom. It will depend on your PC hardware/driver if the baud you use will actually work.   
|   
| Other  
Use HEX | Select when a HEX file must be sent instead of the bin file.  
Program | The program to execute. This is your programmer software.  
Parameter | The optional parameter that the program might need. Use {FILE} to insert the binary filename(file.bin) and {EEPROM} to insert the filename of the generated EEP file. When âUse Hexâ is checked the filename (file.hex) will be inserted for {FILE}. In all cases a binary file will be inserted for {EEPROM} with the extension .EEP Use {CHIP} to insert the official device name of the chip. The device name is required by some programmers.  
  
See Also

[Supported programmers](supported_programmers.md)

---

## Options Select Settings File

The options are stored in a file named bascom-avrxxxx.xml

The xxxx represent the version. For example 2083.

When you click Help, About, you can click the XML data link that will show you where the file is stored.

In order to make it possible to use different settings file, you can rename these files. 

You can select the actual settings file using this menu option.

When you select this option, the status bar will show the current selected file.

This file will also be loaded when you run bascom.

A File Dialog will open and show all XML files. You need to select a bascom-avr xml file. 

You can use this option after you have performed an update. Each update will have its own settings file. That way you can use multiple versions that each have their own settings file.

The following dialog window is shown :

![options_select_settings_file](options_select_settings_file.png)

The current option file is show : d:\users\mark\AppData\Roaming\MCS Electronics\bascom-avr2082.xml

This location is also shown when you click the XML data folder link in the Help, About window

At the left you can view all the xml files. 

When you select a file, the COPY and SELECT buttons will be enabled.

By using the COPY button you can make a backup of the selected option file. 

![options_copy](options_copy.png)

You must give the file a different name. When the file is created, it will be shown in the list. 

When you use the SELECT button, you select the new option file. This is reflected at the CURRENT OPTION FILE value in the top of the window.

The CUSTOM location can be used to store your option file at a custom location. You can enter a file and location or use the button to browse to the file.

You need to click the SELECT CUSTOM button to select this file as the new custom option file.

Click the CLOSE button to close the window.

---

## Options Simulator

With this option you can modify the simulator settings.

![options_sim](options_sim.png)

OPTION | DESCRIPTION  
---|---  
Use integrated simulator | Set this option to use BASCOMâs simulator. You can also use AVR Studio by clearing this option.  
Run simulator after compilation | Run the selected simulator after a successful compilation.  
Program | The path with the program name of the external simulator.  
Parameter | The parameter to pass to the program. {FILE}.OBJ will supply the name of the current program with the extension .OBJ to the simulator.

---

## Program Compile

With this option, you compile your current program.

Your program will be saved automatically before being compiled.

The following files will be created depending on the [Option Compiler Settings.](options_compiler.md)

File | Description  
---|---  
xxx.BIN | Binary file which can be programmed into the microprocessor.  
xxx.DBG | Debug file that is needed by the simulator.  
xxx.OBJ | Object file for simulating using AVR Studio. Also needed by the internal simulator.  
xxx.HEX | Intel hexadecimal file, which is needed by some programmers.  
xxx.ERR | Error file. Only created when errors are found.  
xxx.RPT | Report file.  
xxx.EEP | EEPROM image file  
  
If a serious error occurs, you will receive an error message in a dialog box and the compilation will end.

All other errors will be displayed at the bottom of the edit window, just above the status bar.

When you click on the line with the error info, you will jump to the line that contains the error. The margin will also display the ![BASC0033_wmf](basc0033_wmf.gif)sign.

At the next compilation, the error window will disappear or reappear if there are still errors.

See also ['Syntax Check'](program_syntax_check.md) for further explanation of the Error window.

Program compile shortcut: ![BASC0034_wmf](basc0034_wmf.gif), F7

---

## Program Show Result

Use this option to view information concerning the result of the compilation.

See the [Options Compiler Output](options_compiler_output.md) for specifying which files will be created.

The files that can be viewed are "report" and "error".

File show result shortcut : ![BASC0036_wmf](basc0036_wmf.gif),CTRL+W

Information provided in the report:

Info | Description  
---|---  
Report | Name of the program  
Date and time | The compilation date and time.  
Compiler | The version of the compiler.  
Processor | The selected target processor.  
SRAM | Size of microprocessor SRAM (internal RAM).  
EEPROM | Size of microprocessor EEPROM (internal EEPROM).  
ROMSIZE | Size of the microprocessor FLASH ROM.  
ROMIMAGE | Size of the compiled program.  
BAUD | Selected baud rate.  
XTAL | Selected XTAL or frequency.  
BAUD error | The error percentage of the baud rate.  
XRAM | Size of external RAM if available.  
Stack start | The location in memory, where the hardware stack points to. The HW-stack pointer grows downward.  
S-Stacksize | The size of the software stack.  
S-Stackstart | The location in memory where the software stack pointer points to. The software stack pointer grows downward.  
Framesize | The size of the frame. The frame is used for storing local variables.  
Framestart | The location in memory where the frame starts.  
LCD address | The address that must be placed on the bus to enable the LCD display E-line.  
LCD RS | The address that must be placed on the bus to enable the LCD RS-line  
LCD mode | The mode the LCD display is used with. 4 bit mode or 8 bit mode.  
LCD DB7-DB4 | The port pins used for controlling the LCD in pin mode.  
LCD E | The port pin used to control the LCD enable line.  
LCD RS | The port pin used to control the LCD RS line.  
Variable | The variable name and address in memory  
Constant | Constants name and value Some internal constants are : _CHIP : number that identifies the selected chip _RAMSIZE : size of SRAM _ERAMSIZE : size of EEPROM _XTAL : value of crystal _BUILD : number that identifies the version of the compiler _COMPILER : number that identifies the platform of the compiler  
Warnings | This is a list with variables that are dimensioned but not used. Some of them  
EEPROM binary image map | This is a list of all ERAM variables with their value. It is only shown when [DATA](data_2.md) lines are used to create the EEP file. (EEPROM binary image).  
  
When the option : Load Report in IDE, is set, the report will be shown as a text file in the IDE.

---

## Program Simulate

With this option, you can simulate your program. So what exactly is simulating? For BASCOM it means that the generated object code is processed with a virtual AVR processor.

The simulator can simulate the AVR instructions. It can also simulate the hardware for a part. The goal of the simulator is to allow you to debug your code. The goal was not to create 100% virtual AVR hardware.

This means that some hardware is simulated but with different timing. 

You can simulate your programs with AVR Studio or any other Simulator available such as ISIS or you can use the built in Simulator.

The simulator that will be used when you press F2, depends on the selection you made in the Options Simulator TAB. The default is the built in Simulator.

Program Simulate shortcut : ![BASC0037_wmf](basc0037_wmf.gif), F2

To use the built in Simulator the files DBG and OBJ must be selected from the [Options Compiler Output](options_compiler_output.md) TAB.

The OBJ file is the same file that is used by the AVR Studio simulator.

The DBG file contains info about variables and many other info required to simulate a program.

![sim_main](sim_main.png)

The yellow dot means that the line contains executable code. The blue arrow is visible when you start simulating. It will point to the line that will be executed.

The Simulator window is divided into a few sections:

The Toolbar

The toolbar contains the buttons you can press to start an action.

![BASC0039](basc0039.gif)This is the RUN button, it starts a simulation. You can also press F5. The simulation will pause when you press the pause button. It is advised, that you step through your code at the first debug session. When you press F8, you step through the code line by line which is a clearer way to see what is happening.

![BASC0040](basc0040.gif)This is the PAUSE button. Pressing this button will pause the simulation.

![BASC0041](basc0041.gif)This is the STOP button. Pressing this button will stop the simulation. You can't continue from this point, because all of the variables are reset. You need to press the RUN button when you want to simulate your program again.

![BASC0042](basc0042.gif)This is the STEP button. Pressing this button (or F8) will simulate one code line of your BASIC program. The simulator will go to the RUN state. After the line is executed the simulator will be in the PAUSE state. If you press F8 again, and it takes a long time too simulate the code, press F8 again, and the simulator will go to the pause state.

![BASC0043](basc0043.gif)This is the STEP OVER button or SHIFT+F8). It has the same effect as the STEP button, but sub programs are executed completely, and the simulator does not step into the SUB program.

![BASC0044](basc0044.gif)This is the RUN TO button. The simulator will RUN until it gets to the current line. The line must contain executable code. Move the cursor to the desired line before pressing the button.

![BASC0045](basc0045.gif)This button will show the processor registers window.

![sim_registers](sim_registers.png)

The values are shown in hexadecimal format. To change a value, click the cell in the VAL column, and type the new value. When you right click the mouse, you can choose between the Decimal, Hexadecimal and Binary formats.

The register window will show the values by default in black. When a register value has been changed, the color will change into red. Each time you step through the code, all changed registers are marked blue. This way, the red colored value indicate the registers that were changed since you last pressed F8(step code). A register that has not been changed at all, will remain black.

![BASC0047](basc0047.gif)This is the IO button and will show processor Input and Output registers.

![sim_IO](sim_io.png)

The IO window works similar as the Register window.

A right click of the mouse will show a popup menu so you can choose the format of the values.

And the colors also work the same as for the registers : black, value has not been changed since last step(F8). Red : the value was changed the last time your pressed F8. Blue : the value was changed since the begin of simulation. When you press the STOP-button, all colors will be reset to black.

![BASC0049](basc0049.gif)Pressing this button shows the Memory window.

![sim_memory](sim_memory.png)

The values can be changed the same way as in the Register window.

When you move from cell to cell you can view in the status bar which variable is stored at that address.

The SRAM TAB will show internal memory and XRAM memory.

The EEPROM TAB will show the memory content of the EEPROM.

The colors work exactly the same as for the register and IO windows. Since internal ram is cleared by the compiler at startup, you will see all values will be colored blue. You can clear the colors by right clicking the mouse and choosing 'Clear Colors'.

![simulator_refreshvars](simulator_refreshvars.png) The refresh variables button will refresh all variables during a run (F5). When you use the hardware simulator, the LEDS will only update their state when you have enabled this option. Note that using this option will slow down simulation. That is why it is an option. When you use F8 to step through your code you do not need to turn this option on as the variables are refreshed after each step.

![simulator_simtimers](simulator_simtimers.png) When you want to simulate the processors internal timers you need to turn this option on. Simulating the timers uses a lot of processor time, so you might not want this option on in most cases. When you are debugging timer code it is helpful to simulate the timers.

The simulator supports the basic timer modes. As there are many new chips with new timer modes it is possible that the simulator does not support all modes. When you need to simulate a timer the best option may be to use the latest version of AVR Studio and load the BASCOM Object file.

Even AVR Studio may have some flaws, so the best option remains to test the code in a real chip.

![notice](notice.jpg)The TIMER simulation only simulates TIMER0 and 16 bit TIMER1. And only counting/time modes are supported. PWM mode is not simulated. 

![simulator_realterm](simulator_realterm.png) This option allows you to use a real terminal emulator for the serial communication simulation.

Normally the simulator send serial output to the blue window, and you can also enter data that needs to be sent to the serial port.

When you enable the terminal option, the data is sent to the actual serial port, and when serial data is received by the serial port, it will be shown.

![sim_trace](sim_trace.png)This option turns on/off trace information. When enabled, a file with the name of your project will be created with the .TRACELOG extension.

This file will contain the file, line number and source code that is executed. It is intended to check which parts of your code execute.

Under the toolbar section there is a TAB with a number of pages:

VARIABLES

![simulator_vars](simulator_vars.png)

This section allows you to see the value of program variables. You can add variables by double clicking in the Variable-column. A list will pop up from which you can select the variable.

To watch an array variable, type the name of the variable with the index.

During simulation you can change the values of the variables in the Value-column, Hex-column or Bin-column. You must press ENTER to store the changes.

To delete a variable, you can press CTRL+DEL.

To enter more variables, press the DOWN-key so a new row will become visible.

It is also possible to watch a variable by selecting it in the code window, and then pressing enter. It will be added to the variable list automatically.

Notice that it takes time to refresh the variables. So remove variables that do not need to be watched anymore for faster simulation speed.

LOCALS

![simulator_locals](simulator_locals.png)

The LOCALS window shows the variables found in a SUB or FUNCTION. Only local variables are shown. You can not add variables in the LOCALS section.

Changing the value of local variables works the same as in the Variables TAB.

WATCH

![simulator_watch](simulator_watch.png)

The Watch-TAB can be used to enter an expression that will be evaluated during simulation. When the expression is true the simulation is paused.

To enter a new expression, type the expression in the text-field below the Remove button, and press the Add-button.

When you press the Modify-button, the current selected expression from the list will be replaced with the current typed value in the text field.

To delete an expression, select the desired expression from the list, and press the Remove-button.

During simulation when an expression becomes true, the expression that matches will be selected and the Watch-TAB will be shown.

uP

![simulator_up](simulator_up.png)

This TAB shows the value of the microprocessor status register (SREG).

The flags can be changed by clicking on the check boxes.

The software stack, hardware stack, and frame pointer values are shown. The minimum or maximum value that occurred during simulation is also shown. When one of these data areas enter or overlap another one, a stack or frame overflow occurs.

This will be signaled with a pause and a check box.

Pressing the snapshot-button will save a snapshot of the current register values and create a copy of the memory.

You will notice that the Snapshot-button will change to âStopâ

Now execute some code by pressing F8 and press the Snapshot-button again.

A window will pop up that will show all modified address locations.

This can help to determine which registers or memory a statement uses.

![simulator_snapshot](simulator_snapshot.png)

When you write an ISR (Interrupt Service Routine) with the NOSAVE option, you can use this to determine which registers are used and then save only the modified registers.

INTERRUPTS

![simulator_ints](simulator_ints.png)

This TAB shows the interrupt sources. When no ISR's are programmed all buttons will be disabled.

When you have written an ISR (using ON INT...), the button for that interrupt will be enabled. Only the interrupts that are used will be enabled.

By clicking an interrupt button the corresponding ISR is executed.

This is how you simulate the interrupts. When you have enabled 'Sim Timers' it can also trigger the event.

The pulse generator can be used to supply pulses to the timer when it is used in counter mode.

First select the desired pin from the pull down box. Depending on the chip one or more pins are available. Most chips have 2 counters so there will usually be 2 input pins.

Next, select the number of pulses and the desired delay time between the pulses, then press the Pulse-button to generate the pulses.

The delay time is needed since other tasks must be processed as well.

The option âSim timersâ must be selected when you want to simulate timers/counters.

TERMINAL Section

Under the window with the TABS you will find the terminal emulator window. It is the dark blue area.

In your program when you use PRINT, the output will be shown in this window.

When you use INPUT in your program, you must set the focus to the terminal window and type in the desired value.

You can also make the print output go directly to the COM port.

Check the Terminal option to enable this feature.

The terminal emulator settings will be used for the baud rate and COM port.

Any data received by the COM port will also be shown in the terminal emulator window.

Notice that most microprocessors have only 1 UART. The UART0-TAB is used to communicate with tis UART. The UART1-TAB need to be selected in order to view the UART1 output, or to send data to UART1.

In version 2083, UART0-UART3 are simulated. Unavailable UARTS are not shown.

Software UARTS are not supported by the simulator. They can not be simulated.

UART0

UART0 has some specific options. When you right click the mouse you will get a popup menu.

\- Serial Input File. 

This option selects a file with the SI extension. It must be named the same as your main file but having the SI extension. The content will be used as serial data input. Each time the processor checks UART0 it will read a byte fom the file as if it were sent.

\- Load custom serial Input File

This option allows you to select a specific SI file. An Open Dialog will be shown and you can select the file.

\- Copy

This option copies data sent to the simulated terminal. 

\- Paste

This option sends data to the simulated terminal.

\- Log to File

This option creates a file with the LOG extension. It will have the name of your main file with the LOG extension. All data send to the simulated UART terminal will be send to the log file as well.

\- Show in HEX

This option shows output in HEX format between brackets like [45] [6E] etc.

SOURCE Section

Under the Terminal section you find the Source Window.

It contains the source code of the program you are simulating. All lines that contain executable code have a yellow point in the left margin.

You can set a breakpoint on these lines by selecting the line and pressing F9.

By holding the mouse cursor over a variable name, the value of the variable is shown in the status bar.

If you select a variable, and press ENTER, it will be added to the Variable window.

In order to use the function keys (F8 for stepping for example), the focus must be set to the Source Window.

In version 2083, the simulator source window will have the same fonts as the editor window. The source window is read only. You an not change the source code in the simulator!

A blue arrow will show the line that will be executed next.

When you right click a menu will be shown with the following options:

![sim_source_popup](sim_source_popup.png)

Option | Description  
---|---  
Run (F5) | Run code.  
Step /Pause (F8) | Step through code or pause running code  
Step Over (SHIFT+F8) | Step code but step over sub routines and functions..  
Run To (F10) | Run to the current line. This line should have a yellow dot(contains executable code)  
Goto Line (ALT+G). | This option let you chose a line to jump to. Use this with care since it will jump right to the code. This means that some parts of your code are not executed.   
Clear All Breakpoints | This option clears all breakpoints set with F9.  
Toggle breakpoint (F9) | This option will toggle a break point. It will only work on a line with executable code.  
Find (CTRL+F) | Option to find text, similar to the function in the source editor  
Find Next (F3) | Option to find next instance similar to the function in the source editor.  
Show Registers | Option to show/hide internal registers R0-R31  
Show IO | Option to show/hide IO registers  
Show Memory  | Option to show/hide memory content for SRAM and EEPROM  
Log Terminal output | This option let you select a file name for the simulator output log file.  
Clear EEPROM | This option will reset the EEPROM content to empty(FF). This is required sometimes since between sessions the EEPROM content is saved in an EEP file when this option is checked in Options, Simulator, Save EEPROM state. And when you restart simulation the EEP content is read. This option will clear the content.   
  
The hardware simulator.

By pressing the hardware simulation button ![BASC0055](basc0055.gif)the windows shown below will be displayed.

![BASC0056](basc0056.gif)

The top section is a virtual LCD display. It works to display code in PIN mode, and bus mode. For bus mode, only the 8-bit bus mode is supported by the simulator.

Below the LCD display area are LED bars which give a visual indication of the ports.

By clicking an LED it will toggle.

PA means PORTA, PB means PORTB, etc.

IA means PINA, IB means PINB etc. (Shows the value of the Input pins)

It depends on the kind of microprocessor you have selected, as to which ports will be shown.

Right beside the PIN led's, there is a track bar. This bar can be used to simulate the input voltage applied the ADC converter. Note that not all chips have an AD converter. You can set a value for each channel by selecting the desired channel below the track bar.

Next to the track bar is a numeric keypad. This keypad can be used to simulate the GETKBD() function.

When you simulate the Keyboard, it is important that you press/click the keyboard button before simulating the getkbd() line !!!

To simulate the Comparator, specify the comparator input voltage level using Comparator IN0.

Enable Real Hardware Simulation

By clicking the ![BASC0057](basc0057.gif)button you can simulate the actual processor ports in-circuit!

The processor chip used must have a serial port.

In order simulate real hardware you must compile the basmon.bas file.

To do this, follow this example:

Lets say you have the DT006 simmstick, and you are using a 2313 AVR chip.

Open the basmon.bas file and change the line $REGFILE = "xxx" to $REGFILE = "2313def.dat"

Now compile the program and program the chip.

It is best to set the lock bits so the monitor does not get overwritten if you accidentally press F4.

The real hardware simulation only works when the target micro system has a serial port. Most have and so does the DT006.

Connect a cable between the COM port of your PC and the DT006. You probably already have one connected. Normally it is used to send data to the terminal emulator with the PRINT statement.

The monitor program is compiled for 19200 baud. The Options Communication settings must be set to the same baud rate!

The same settings for the monitor program are used for the Terminal emulator, so select the COM port, and the baud rate of 19200.

Power up or reset the DT006. It probably already is powered since you just previously compiled the basmon.bas program and stored it in the 2313.

When you press the real hardware simulation button now the simulator will send and receive data when a port, pin or DDR register is changed.

This allows you to simulate an attached hardware LCD display for example, or something simpler, like an LED. In the SAMPLES dir, you will find the program DT006. You can compile the program and press F2.

When you step through the program the LED's will change!

All statements can be simulated this way but they have to be able to use static timing. Which means that 1-wire will not work because it depends on timing. I2C has a static bus and thus will work.

NOTE: It is important that when you finish your simulation sessions that you click the button again to disable the Real hardware simulation.

When the program hangs it probably means that something went wrong with the serial communication. The only way to escape is to press the Real hardware Simulation ![image1764821748](image1764821748.jpg)button again.

The Real Hardware Simulation is a cost effective way to test attached hardware.

![notice](notice.jpg) The refresh variables button will refresh all variables during a run(F5). When you use the hardware simulator, the LEDS will only update their state when you have enabled this option. Note that using this option will slow down the simulation.

Watchdog Simulation

Most AVR chips have an internal Watchdog. This Watchdog timer is clocked from an internal oscillator. The frequency is approximately 1 MHz. Voltage and temperature variations can have an impact on the WD timer. It is not a very precise timer. So some tolerance is needed when you refresh/reset the WD-timer. The Simulator will warn you when a WD overflow will occur. But only when you have enabled the WD timer.

The status bar

![simulator_sttausbar](simulator_sttausbar.png)

The status bar shows the PC (program counter) and the number of cycles. You can reset the cycles by positioning the mouse cursor on the status bar and then right click. You will then get a pop up menu with the option to reset the cycles. You can also double click the cycles to reset it to 0.

You can use this to determine how much time a program statement takes.

```vb
Do not jump to a conclusion too quick, the time shown might also depend on the value of a variable.

For example, with WAITMS var this might be obvious, but with the division of a value the time might vary too.

```
Start Simulation

To start a simulation the program need to be compiled. So typically you press F7 to compile your code. Make sure that the BIN, DBG and OBJ files are created (Options, Compiler, Output).

When the code is compiled without errors, you can simulate your project. To do so press F2.

By default the simulator is in STOP mode. The status bar will show PC = 0 (program counter) and Cycles = 0. Some instructions use more cycles than other. A NOP for example takes 1 cycle. When the processor has an oscillator running on 8 MHz, and the 8 DIV fuse is set, it means the processor will have a clock of 1 MHz. Meaning that each second, 1 million cycles can be executed. So you could execute a million NOP instructions in 1 second. 

The simulator however is not able to do so. The simulator reads the object data, and decodes the data and simulates the instructions and the hardware. Also, the software need to give time to windows otherwise the code will stall windows and your other programs. 

When the AVR is initialized, the RAM is cleared. This will takes time. So when you press F8 the first time, you will notice that the blue arrow will be visible on the first line of the main project. It depends on the used processor how long it will take till the initialization is done. When done, the simulator will go into PAUSE mode. 

Press F8 again to step through the code. You will notice that the blue arrow will jump only to code with a yellow dot which indicates that the line contains executable code.

DIM statements for example are important for the compiler but do not create code. So these statements will be skipped.

Using the BREAK instruction you can pause the simulator. This is a good way when instead of F8, you use F5 to RUN the code. You can also set a break point using F9. This will be visible with a red dot.

![sim_run2](sim_run2.png)

When your code uses INC modules, the simulator will show the name of the current module.

---

## Program Syntax Check

With this option, your program is checked for syntax errors. No file will be created except for an error file, if an error is found.

Program syntax check shortcut ![BASC0035_wmf](basc0035_wmf.gif), CTRL + F7

When there is an error, an error window will be made visible at the bottom of the screen.

![error ocurred](error ocurred.png)

You can double click the error line to go to the place where the errors is found. Some errors point to a line zero that does not exist. These errors are caused by references to the assembler library and are the result of other errors.

The error window is a dockable window that is docked by default to the bottom of the screen. You can drag it outside this position or double click the caption(Errors) to make it undock :

![error_undocked](error_undocked.png)

Here the panel is undocked. Like most windows you can close it. But the error must be resolved (corrected and syntax checked/recompiled) for this window can be closed !

By double clicking the caption (top space where the name of the window is show) you can dock it back to it's original position. 

When you have closed the window and want to view it again, you can choose the View, Error Panel option from the main menu.

---

## Tools Font Editor

The Font Editor was a Plug in which is now integrated into the Tools menu.

The editor is intended to create Fonts that can be used with Graphical display such as SED1521, KS108, color displays, etc.

When you choose this option the following window will appear:

![font_editor](font_editor.gif)

You can open an existing Font file, or Save a modified file.

The supplied font files are installed in the Samples\lcdgraph folder.

You can copy an image from the clipboard, and you can then move the image up , down, left and right.

When you select a new character, the current character is saved. The suggest button will draw an image of the current selected character.

When you keep the left mouse button pressed, you can set the pixels in the grid. When you keep the right mouse button pressed, you can clear the pixels in the grid.

When you choose the option to create a new Font, you must provide the name of the font, the height of the font in pixels and the width of the font in pixels.

The Max ASCII is the last ASCII character value you want to use. Each character will occupy space. So it is important that you do not choose a value that is too high and will not be used.

When you display normal text, the maximum number is 127 so it does not make sense to specify a value of 255.

A font file is a plain text file. 

Lets have a look at the first few lines of the 8x8 font:

Font8x8:

$asm

.db 1,8,8,0

.db 0,0,0,0,0,0,0,0 ; 

.db 0,0,6,95,6,0,0,0 ; !

The first line contains the name of the font. With the [SETFONT](setfont.md) statement you can select the font. Essential, this sets a data pointer to the location of the font data.

The second line ($ASM) is a directive for the internal assembler that asm code will follow.

All other lines are data lines. 

The third line contains 4 bytes: 1 (height in bytes of the font) , 8 (width in pixels of the font), 8 (block size of the font) and a 0 which was not used before the 'truetype' support, but used for aligning the data in memory. This because AVR object code is a word long.

This last position is 0 by default. Except for 'TrueType' fonts. In BASCOM a TrueType font is a font where every character can have it's own width. The letter 'i' for example takes less space then the letter 'w'. The EADOG128 library demonstrates the TrueType option.

In order to display TT, the code need to determine the space at the left and right of the character. This space is then skipped and a fixed space is used between the characters. You can replace the 0 by the width you want to use. The value 2 seems a good one for small fonts.

All other lines are bytes that represent the character.

Graphical LCD uses 1 byte to set 8 pixels black/white.

The LCD driver will for load the height in bytes i the example this is 1 byte.

Then the driver will load the width in bytes of the character. in the example this is 8. This means that data lines are 8 bytes long. 

And finally the block size in bytes of one character will be loaded. This is simply the first parameter times the second parameter. In the example this is 8 too. The last parameter is loaded to see if TT spacing must be used.

Depending on the ASCII value of the character to show, the driver will located the proper place in the table by multiplying the block size with the ASCII value. This will be added to the start of the table address.

Now the driver will load and write a byte and thus will set 8 pixels.

The pixels are shown from top to bottom like this :

x 

x

x

x

x

x

x

x

Then the next byte will be loaded and send to the lcd.

xy 

xy

xy

xy

xy

xy

xy

xy

and this will repeat for the number of bytes specified. 

Then if the height is more than 1 byte, the next block will be loaded. 

This also means that each font height must be a multiple of 8 pixels.

This restriction is only because writing a full byte is the fastest way to update an LCD.

---

## Tools Graphic Converter

The Graphic converter is intended to convert BMP files into BASCOM Graphic Files (.BGF) that can be used with Graphic LCD displays.

The following dialog box will be shown:

![graphic_converter](graphic_converter.png)

To load a picture click the Load button.

The picture can be maximum 128 pixels high and 240 pixels width.

When the picture is larger it will be adjusted.

You can use your favorite graphic tool to create the bitmaps and use the Graphic converter to convert them into black and white images.

When you click the Save-button the picture will be converted into black and white.

Any non-white color will be converted into black.

The resulting file will have the BGF extension. (bascom graphics format)

You can also paste a picture from the clipboard by clicking the Paste button.

Press the Ok-button to return to the editor.

The picture can be shown with the [ShowPic](showpic.md) statement or the [ShowpicE](showpice.md) statement.

![notice](notice.jpg) The BGF files are RLE encoded to save space.

![notice](notice.jpg) It is important that the font selection 6*8 or 8*8 match the font size in the CONFIG GRAPHLCD. For example :

Config Graphlcd = 240x128 , Dataport = Porta , Controlport = Portc , Ce = 2 , Cd = 3 , Wr = 0 , Rd = 1 , Reset = 4 , Fs = 5 , Mode = 8

In this case you would use 8*8.

When you use your own drawing routine you can also save the pictures uncompressed by setting the Uncompressed check box. The resulting BGF files can not be shown with the showpic or showpicE statements anymore in that case!

The BGF format is made up as following:

•| first byte is the height of the picture  
---|---  
  
•| second byte is the width of the picture  
---|---  
  
•| for each row, all pixels are scanned from left to right in steps of 6 or 8 depending on the font size. The resulting byte in stored with RLE compression  
---|---  
  
The RLE method used is : byte value, AA(hex), repeats.

So a sequence of 5, AA, 10 means that a byte with the value of 5 must be repeated 16 times (hex notation used)

Option | Description  
---|---  
Height | The height in pixels of the image.  
Width | The width in pixels of the image.  
Font | The T6963 supports 6x8 and 8x8 fonts. This is the font select that must match the CONFIG statement. For other displays, use 8*8.  
Type | The size of the display. When the size is not listed, use one with the same width.  
SED Series | If your display is a SEDxxxx chip, select this option.  
Uncompressed | Images are RLE encoded. Select this option when you do not want to compress the image.

---

## Tools LIB Manager

With this option the following window will appear:

![lib_manager](lib_manager.png)

The Libraries are shown in the left pane. When you select a library, the routines that are in the library will be shown in the right pane.

After selecting a routine in the left pane, you can DELETE it with the DELETE button..

Clicking the ADD button allows you to add an ASM routine to the library. The ADD Paste button will add a routine from the clipboard instead of a file on disk.

The COMPILE button will compile the lib into an LBX file. When an error occurs you will get an error. By watching the content of the generated lbx file you can determine the error.

A compiled LBX file does not contain comments and a huge amount of mnemonics are compiled into object code. This object code is inserted at compile time of the main BASIC program. This results in faster compilation time.

The DEMO version comes with the compiled MCS.LIB file which is named MCS.LBX. The ASM source (MCS.LIB) is included only with the commercial edition.

With the ability to create LBX files you can create add on packages for BASCOM and sell them. For example, the LBX files could be distributed for free, and the ASM source could be sold.

Some library examples :

•| MODBUS crc routine for the modbus slave program.  
---|---  
  
•| Glcd.lib contains the graphical LCD asm code  
---|---  
  
Commercial packages available from MCS:

•| I2CSLAVE library  
---|---  
  
•| BCCARD for communication with www.basiccard.com chipcards  
---|---  
  
See Also

[$LIB](lib.md) for writing your own libraries

---

## Tools PDF Update

Use this option to update all Atmel PDF files.

The Atmel data sheets are stored in the \PDF subdirectory.

The following window will be shown :

![pdf_update](pdf_update.png)

There is only one option available : Check. When you click the Check-button, the MCS server will be checked for newer versions of the PDF documents.

You need to make sure that BASCOM is allowed to contact the internet. 

You also need to have port 211 open. This port is used in FTP mode to contact the MCS server.

The MCS server is synchronizing all PDF files each day with the ATMEL server. This means that the copy on the MCS server can be maximum 24 hours old.

The check will read all available DAT files and check if there is a reference to the PDF.

When an item is disabled(grayed) then it means there is no link to the PDF in the DAT file.

During the check the window will look like this :

![pdf_update_check](pdf_update_check.png)

All PDF's that are newer will have a check mark. These need an update.

You can manual unselect or select the PDF's.

In the log window at the bottom of the window you can view which files will be downloaded.

When you want to download the selected files, press the Download-button.

This will close all PDF documents in the PDF viewer. A backup of each PDF file downloaded will be made before it is downloaded. You need to restore it when something goes wrong during the download(server drops the connection for example).

When a document is downloaded, the check mark will be removed.

After all documents are downloaded, they documents are opened again in the PDF viewer.

As of version 2077 the PDF documents are downloaded from the MCS Electronics server.

Previously they were downloaded from Atmels webserver. When Atmel change the file name the link is broken and you can not update the file.

To solve this all files are stored on the MCS server and each day all files are synchronized with atmel so all files are maximum 1 day old.

As of version 2079 the PDF files are downloaded using FTP. This results in a better performance. Just make sure port 411 is open in your firewall for outgoing connections.

---

## Tools Plugin Manager

The Plug in Manager allows you to specify which Plug-in's needs to be loaded the next time you start BASCOM.

![pluginmng](pluginmng.gif)

Just select the plug in's you want to load/use by setting the check box.

The plug in's menu's will be loaded under the Tools Menu.

To add a button to the toolbar, right click the mouse on the menu bar, and choose customize.

When you want to write your own plug in's, contact support@mcselec.com

---

## Tools Resource Editor

The resource editor can be used to edit the resource strings of your application.

The resource editor will create a <project>.BCR file.

The resource editor is part of the Resource Add On, and is only available when you have this add on installed.

The simplest way to get the resources from your application is to create a BCS file using the DUMP option.

Then import them with the resource editor.

![Tools_resource_editor](tools_resource_editor.png)

The following options are available when you right click with the mouse in the resource editor.

Option | Description  
---|---  
Search | Search for a string.  
Find Next | Find next occurrence.  
Delete Row | Delete the current row.  
Add Row | Add a new row for a new string.  
Import | This option will import the BCS file which you can create with the $RESOURCE DUMP option.  
Set Language Name | Change the language name of the current language/column.  
Add Language | Add a new column for a new language.  
Delete Language | Delete the current column (language).  
  
The resource editor is pretty simple. The only task is allow you to edit the various strings. You can also use notepad or Excel to create the BCR file which is explained in the [$RESOURCE](resource.md) topic.

---

## Tools Stack Analyzer

The Stack analyzer helps to determine the proper stack size.

See [$DBG](_dbg.md) for the proper usage of this option.

---

## Tools Terminal Emulator

With this option you can communicate via the RS-232 interface to the microcomputer. The following window will appear:

![terminal_emu](terminal_emu.png)

Information you type and information that the computer board sends are displayed in the same window.

Note that you must use the same baud rate on both sides of the transmission. If you compiled your program with the Compiler Settings at 4800 baud, you must also set the Communication Settings to 4800 baud.

The setting for the baud rate is also reported in the report file.

![notice](notice.jpg)NOTE: The focus MUST be on this window in order to see any data (text, etc) sent from the processor. You will NOT see any data sent by the processor right after a reset. You must use an external hardware reset AFTER the terminal Emulator window is given focus in order to see the data. Using the Reset ![reset_icon](reset_icon.png) shortcut, you will not be able to see any data because pressing the shortcut causes the Terminal emulator to lose focus. This is different than âHyper Terminalâ which always receives data even when the Hyper terminal window does not have focus. Use Hyper terminal if you need to see the program output immediately after programming or reset. Or use the option 'Keep terminal emulator open' from the Options, Communication.

File Upload

Uploads the current program from the processor chip in HEX format. This option is meant for loading the program into a monitor program for example. It will send the current compiled program HEX file to the serial port.

File Escape

Aborts the upload to the monitor program.

File Exit

Closes terminal emulator.

Terminal Clear

Clears the terminal window.

Terminal Open Log

Opens or closes the LOG file. When there is no LOG file selected you will be asked to enter a filename or to select a filename. All info that is printed to the terminal window is captured into the log file. The menu caption will change into 'Close Log' and when you choose this option the file will be closed.

Terminal Send ASCII

This option allows you to send any ASCII character you need to send. Values from 000 to 255 may be entered.

![terminal_sendASCII](terminal_sendascii.png)

Terminal Send Magic number

This option will send 4 bytes to the terminal emulator. The intention is to use it together with the boot loader examples. Some of the boot loader samples check for a number of characters when the chip resets. When they receive 4 'magic' characters after each other, they will start the boot load procedure. This menu options send these 4 magic characters.

Terminal Setting

This options will show the terminal settings so you can change them quickly.

It is the same as [Options, Communication](options_communication.md).

Terminal User Commands

This option will show or hide the toolbar with the user definable command buttons.

There are 16 user definable buttons named CMD1-CMD16. When you hover the mouse cursor above the button, the button data will be shown.

When you right click the mouse above the button, you can enter the data for the button.

Example for CMD4:

![userbutton](userbutton.png)

In the sample above the data "test" will be sent. No carriage return(CR) or line feed(LF) will be sent. If you want to send them as well you need to include them as special characters.

Special characters are entered with their 3 digit ASCII value between brackets : {xxx}

For example to send CR + LF you wend enter {013}{010}

![tools_terminal_user_buttons](tools_terminal_user_buttons.png)

See Also

[Options, Communication](options_communication.md)

---

## View Code Explorer

Action

Shows the Code Explorer Window

![code_explorer](code_explorer.png)

The code explorer shows code elements in a tree. By double clicking an element the cursor will be set to the matching code in the editor.

You can also drag an element into the editor window. 

By clicking the right mouse a pop up menu will allow you to filter out constants and variables (registers) from the definition file.

The following code elements will be shown in the explorer:

\- Aliases. These are the user [ALIAS](alias.md)es. 

\- Assembler. This is for single line asm using !

\- Assembler Block. This is for assembler blocks using $asm .. $end asm. If you add comment after $asm, it will be shown in the tree as well. Example : $asm ; Test 

\- Constants. Both user defined constants ([CONST](const.md)) and constants from the definition file are shown. 

\- Declarations. Subs and Functions are both shown. Each with their own color.

\- Functions. These are the user function implementations.

\- Labels. When labels are used in subs and functions, the sub/functions name is listed first.

\- Macros. These are the user macro's created with [MACRO](macro.md).

\- Subs. These are the user sub implementations.

\- Variables. These are the variables from the user code and definition file. Each shown with their own color. Locals are shown under a branch of the sub/function.

\- CallStack. This is optional. Since it takes time to trace the call stack it is turned off by default. Use right mouse click and the pop up menu to activate it.

The call stack shows a tree of the calls you make to user subs and functions. And each sub/function also shows the user functions it calls. 

When multiple calls are made, three dots are added for each additional call. 

\- Types. Declared types with their members are shown. See TYPE.

\- Information. Processor, free ERAM and SRAM. Estimated $hwstack, $swstack and $framesize. 

![notice](notice.jpg)The calculated stack settings are based on the program call tree and local variables. This is just a tool to give you an idea about stack usage. Not taken into account is the stack required by the assembler routines. This means that you need to add a certain amount to the calculated values. When your code uses interrupts you need to increase the calculated $HWSTACK by 32. Otherwise increase it by 16. The $FRAMESIZE should have a minimum value of 24. Add a value of 16 to $SWSTACK. 

Applications using AVR-DOS should use a minimum of 128 for all stacks. 

A future version will also take the assembler code into account.

When the Code Explorer has the focus, pressing CTRL+F will search in the code explorer and not in the editor.

The code explorer works in a separate thread. It will be updated a few seconds after you have quit typing. 

By making the Code Explorer window invisible, the explorer is deactivated.

The popup menu has the following options:

![code_explorer_popup](code_explorer_popup.png)

Show Register Constants

This option can toggle between showing and hiding the register constants. When register constants are shown the tree can become big.

User constants and register constants are shown in a different color.

Show Register Variables

This option can toggle between showing and hiding the register variables. When register variables are shown the tree can become big.

User variables and register variables are shown in a different color.

Show Call Stack

This option can show the Call Stack. This reveals the nesting of your code.

Show Errors

This option deserves a warning. The option is turned off by default. It can be useful to find errors but it can also point to errors which are not considered an error for the compiler. The compiler has a separate parser. The parser from the IDE is a different new parser. While in 2080 all DAT files are updated, you still can get errors which are no real errors. You might want to report them to support. Please send a small as possible program that will show the error.

Show Unused Items

When this option is turned on, all unused items will be shown in grey. For example :

![code_explorer_unused_items](code_explorer_unused_items.png)

In this sample, _temp1 , so_rx_data and DataPtr are unused or unreferenced. _temp1 is an internal variable and so is DataPtr. They do not occupy any space.

But so_rx_data is a user variable which is not referenced. You could remove or remark it.

Refresh

This option will parse the project and update the code explorer tree. 

Find References

This option can find all references for an item. For example when you go to Variables, and select a variable the option becomes enabled in the menu. After choosing this option, the references will be added to the tree.

![code_explorer_refs](code_explorer_refs.png)

Now by clicking the item you will go to the point in your code where the item is referenced/used.

Show References

This options shows a panel on the bottom of the code explorer tree. When you activate the tooltip keeping SHIFT pressed and hovering an item in the editor, the references panel will be updated with all references of that item. A single click on an item in this list will set the cursor in the IDE to referred item.

Consider this simple piece of code :

```vb
Dim S As Single

Input "s " , S

Print S

```
When pressing SHIFT and hovering the mouse over the variable S , the tooltip will be shown : ![tooltip-s](tooltip-s.png)

The references list will be updated as well. The item in bold points to the definition, in this case the DIM S. 

The following two items in the list point to the INPUT "s ", S and the Print S.

Items shown in red are variables that are assigned. 

The panel can be shown or hidden using the right click menu from the explorer.

RENAMING

When you right an item in the References List you get a pop up menu : RENAME

When you click the RENAME option you will be asked for a new name.

Enter a new name for the item (variable,constant, etc). All occurrences in your project will be replaced. Not only the ones in loaded files but also in included files on disk.

When the new name you provide is already used in the project you will get an error message and the items will not be replaced.

---

## View Error Panel

This option will show the Error panel.

![view_error_empty](view_error_empty.png)

When there are no errors, the list will be empty. You will also be able to close the window.

When there are errors :

![error_panel_error](error_panel_error.png)

You will not be able to close the window until the error is solved and the program is checked/compiled.

The panel is dockable and by default docked to the bottom of the IDE.

When you right click the mouse inside the error panel, a menu will popup with one option : Copy to Clipboard. All data from the error window will be copied to the windows clipboard if you select this option.

---

## View PDF viewer

The PDF viewer is dock able panel which is located by default on the right side of the IDE.

![IDE_pdf](ide_pdf.png)

The viewer itself contains a tree with the topics and the actual PDF viewer.

The tree topics can be searched by right clicking on the tree. Choose 'Search' and enter a search text.

When a topic has sub topics, the topic is bold.

When you have enabled 'Auto open Processor PDF' in Options, Environment, PDF, the data sheet will be automatically loaded when you change the $REGFILE value.

It can be shown in a new sheet or it can replace the current PDF.

![pdf_open](pdf_open.png) | Open a PDF.  
---|---  
![pdf_copy](pdf_copy.png) | Copy selected text to the clipboard. You can not copy from protected PDF documents.  
![pdf_first](pdf_first.png) | First page.  
![pdf_prev](pdf_prev.png) | Previous page.  
![pdf_page](pdf_page.png) | Current page indicator. You can enter a page number to jump to a different page.  
![pdf_next](pdf_next.png) | Next page.  
![pdf_last](pdf_last.png) | Last page.  
![pdf_find](pdf_find.png) | Find text in PDF.  
![pdf_zoomin](pdf_zoomin.png) | Zoom in.  
![pdf_zoomout](pdf_zoomout.png) | Zoom out.  
![pdf_rotate](pdf_rotate.png) | Rotate page to the left and right.  
![pdf_print](pdf_print.png) | Print page(s).  
  
When you right click in the PDF, a pop up menu with the most common options will appear.

In [Options, Environment, PDF](options_environment.md) you can specify how data sheets must be downloaded.

Data sheets can be downloaded automatic. When the $REGFILE is changed and the PDF is not present, you will be asked if the PDF must be downloaded.

If you choose to download, it will be downloaded from the Atmel website.

![as_download_pdf](as_download_pdf.png)

When you click 'Do not show this message again' , you will not be asked anymore if you want to download the Mega32.PDF. You will be asked to download other PDF documents when they do not exist.

During the download you will see a similar window:

![down_pdf](down_pdf.png)

You can also download all newer PDF's from the Atmel website with the option : [Tools, PDF Update](tools_pdf_update.md)

When PDF's are downloaded with the UpdateWiz, they are downloaded from the MCS Electronics website.

---

## View PinOut

The Pin Out viewer is a dock able window that shows the case of the active chip.

The active chip is determined by the value of [$REGFILE](regfile.md).

![pinout](pinout.png)

When you move the mouse cursor over a pin, you will see that the pin will be colored red. At the bottom of the window, a pin description is show. In the sample above you will see that each line has a different color. This means that the pin has multiple alternative functions.

The first blue colored function is as generic IO pin.

The second green colored function is RESET pin.

The third black colored function is PIN change interrupt.

A pin can have one or more functions. Some functions can be used together.

When you move the mouse cursor away, the pin will be colored blue to indicate that you viewed this pin. For example, when you need to look at it again.

You can also search for a pin description. Enter some text and return.

Here is an example when you search the VCC pin :

![pin_viewer_search](pin_viewer_search.png)

When pins are found that have the search phrase in the description, the pin will be colored blue.

By clicking 'Clear Pin HL' you can clear all colored pins.

Some chips might have multiple cases. You can select the case from the package list.

![pin_viwer_packlist](pin_viwer_packlist.png)

When you change from package, all pin colors will be cleared.

When you double click a pin, the pin will be colored green. Another double click will color it red/blue.

When a pin is green, it will not be colored red/blue. The green color serves as a kind of bookmark.

The only exception is the search function. It will make bookmarked green pins, blue too.

Use the right mouse to access a popup menu. This menu allows you to zoom the image to a bigger or smaller size.

Double click the chip to show the chip data.

![pinout_chipdata](pinout_chipdata.png)

When you want to search for a chip, click the 'Chip Search' button.

It will show the following window:

![pinout_chipsearchSpecs](pinout_chipsearchspecs.png)

You can provide criteria such as 2 UARTS. All criteria are OR-ed together. This means that when one of the criteria is met, the chip will be included in the list.

![notice](notice.jpg)Only chips supported by BASCOM will be listed. When a chip has SRAM, and is not supported yet, it will be in the near future since the goal is to support all chips.

When you find an error in the pin description, please send an email to support so it can be corrected.

---

## View Project Files

Action

Shows the Project Explore Window.

![ide_view_project_Explorer](ide_view_project_explorer.png)

The project explorer window is intended to be used in project mode. Project mode is a mode where all files belong to one project. Here you have a main file and optional include files. 

The project explorer is a dock able window. It lists all files assigned to the project. When you double click a file, it will be opened in the editor. 

\- Use the ADD button to add files to the project

\- Use the REMOVE button to remove files from the project. Files you remove are only removed from the project, they are not removed from disk

\- Use SET MAIN to set the main project file. The main project file is the file that is compiled.

---

## View Vertical Splitter

You can split the editor window into two parts. By default you use the horizontal splitter marked with the arrow.

![view_split_1](view_split_1.png)

This will create a split screen :

![view_split_2](view_split_2.png)

With the option Vertical Splitter, you switch between horizontal en vertical splitter.

The splitter is located near the code explorer window.

![view_split_4](view_split_4.png)

This will result in a vertical split window.

![view_split_5](view_split_5.png)

When you chose the vertical splitter option again the window will be split horizontal again.

Notice that in order to show two different code windows you need to open the two windows and use [Tile Vertically](window_tile_vertically.md).

---

## Window Arrange Icons

Arrange the icons of the minimized editor windows.

---

## Window Cascade

Cascade all open editor windows.

---

## Window Minimize All

Minimize all open editor windows.

---

## Window Tile

Tile all open editor windows horizontally.  
  
![tile_horz](tile_horz.png)

---

## Window Tile Vertically

Tile all open editor windows vertically.

![tile_vertc](tile_vertc.png)

---
