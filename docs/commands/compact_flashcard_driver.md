# Compact FlashCard Driver

The compact flash card driver library is written by Josef Franz VÃ¶gel. He can be contacted via the BASCOM user list.

Josef has put a lot of effort in writing and especially testing the routines.

Josef nor MCS Electronics can be held responsible for any damage or data loss of your CF-cards.

Compact flash cards are very small cards that are compatible with IDE drives. They work at 3.3V or 5V and have a huge storage capacity.

The Flash Card Driver provides the functions to access a Compact Flash Card.

At the moment there are six functions:

[DriveCheck](drivecheck.md), [DriveReset](drivereset.md) , [DriveInit](driveinit.md) , [DriveGetIdentity](drivegetidentity.md) , [DriveWriteSector](drivewritesector.md) , [DriveReadSector](drivereadsector.md)

The Driver can be used to access the Card directly and to read and write each sector of the card or the driver can be used in combination with a file-system with basic drive access functions.

Because the file system is separated from the driver you can write your own driver.

This way you could use the file system with a serial EEPROM for example.

```vb
For a file system at least the functions for reading (DriveReadSector / _DriveReadSector) and writing (DriveWriteSector / _DriveWriteSector) must be provided. The preceding under slash _ is the label of the according asm-routine. The other functions can, if possible implemented as a NOP â Function, which only returns a No-Error (0) or a Not Supported (224) Code, depending, what makes more sense.

For writing your own Driver to the AVR-DOS File system, check the ASM-part of the functions-description.

```
Error Codes:

Code | Compiler â Alias | Remark  
---|---|---  
0 | CpErrDriveNoError | No Error  
224 | cpErrDriveFunctionNotSupported | This driver does not supports this function  
225 | cpErrDriveNotPresent | No Drive is attached  
226 | cpErrDriveTimeOut | During Reading or writing a time out occurred  
227 | cpErrDriveWriteError | Error during writing  
228 | cpErrDriveReadError | Error during reading  
  
At the [MCS Web AN](<http://www.mcselec.com/index.php?option=com_content&task=view&id=87&Itemid=57>) section you can find the application note 123.

More info about Compact Flash you can find at :

<http://www.sandisk.com/download/Product%20Manuals/cf_r7.pdf>

A typical connection to the micro is shown below.

![cfcard](cfcard.gif)