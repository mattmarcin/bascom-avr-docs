# AVR-DOS File System

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