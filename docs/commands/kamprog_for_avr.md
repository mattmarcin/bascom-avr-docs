# KamProg for AVR

KamProg for AVR is an USB programmer from Kamami.

You need to install the software that comes with the KamProg.

You can download the software from the web site of the manufacturer or from MCS Electronics web shop Kamprog product page.

KamProg can be used with BASCOM but also with AVR Studio.

BASCOM will use the KamProg software to either automatic or manual program the chip.

The Kamprog programmer works on Vista32 and Vista64 and requires no special drivers. It has also been tested with Win7 and Win8 and Win8.1

The KamProg programmer is available from MCS Electronics webshop.

When you use Auto program, you will see a small progress window while the processor is programmed.

When you chose manual program, you will see a familiar window, known from USB-ISP.

![kamprog](kamprog.png)

When the source code is compiled and the BIN file exists, it is loaded automatic into the buffer.

When an EEPROM image file exists (EEP), it is loaded too into the EEPROM buffer. When it does not exist you will see a warning which you can ignore.

When the target device is not read yet, the CHIP will be unidentified which is marked as ???.

In the status bar you can see the loaded file, and the size of the file. Notice that 16000 will be shown as 16 KB. 

You can select the EEPROM-TAB to view the EEPROM image. Memory locations can be altered. Select a cell, and type a new value. Then press ENTER to confirm. You can immediately see the new value. 

When you select the Lock and Fusebits-TAB the lock and fuse bits will be read.

![kamprog_lockfuse](kamprog_lockfuse.png)

As soon the target chip is determined, the chip name is shown under the tool bar.

The FLASH size and EEPROM size are shown too.

When you alter a lock or fuse bit, the corresponding Write-button will be enabled. You need to click it to write the new value. The lock and fuse bits are read again so you can see if it worked out.

The lock and fuse bits shown will depend on the used chip. Every chip has different fuse bits. Some fuse bits can not be altered via the serial programming method. For example the fuse bit 'enable serial downloading' can not be changed using the serial programming method.

Fuse bits of interest are : the clock divider and the oscillator fuse bits. When you select a wrong oscillator fuse bit (for example you select an external oscillator) the chip can not programmed anymore until you connect such an external oscillator! Of course a simple 555 chip can generate a clock signal you can use to 'wake' a locked chip. 

Once you have all settings right, you can press the 'Write PRG' button which will insert some code into your program at the current cursor position. This is the $PROG directive. 

For example : $prog &HFF , &HED , &HD0 , &HFF 

When you compile your program with the [$PROG](_prog.md) directive it will generate a PRG file with the lock and fuse bit settings. 

```vb
If you then auto program(see later) a chip, it will use these settings. 

$PROG is great to load the right lock and fuse bits into a new chip. But be careful : do not enable $PROG till you are done with development. Otherwise programming will be slow because of the extra reading and writing steps. 

```
The following menu options are available: 

Option | Description  
---|---  
File |   
  
Exit | Close programmer.  
  
|   
  
Buffer |   
  
Clear | Clear buffer. Will put a value of 255 (FF hex) into each memory location. When the FLASH-TAB has the focus, the FLASH buffer will be cleared. When the EEPROM-TAB has the focus, the EEPROM buffer will be cleared. 255 is the value of an empty memory location.  
Load from File | This will shown an open file dialog so you can select a binary file (BIN)  
  
| The file is loaded into the buffer.  
Save to File | Will save the current buffer to a file.  
Reload | Reloads the buffer from the file image.  
  
|   
  
Chip |   
  
Identify | Will attempt to read the signature of the chip. When the signature is unknown(no DAT file available) or there is no chip or other error, you will get an error. Otherwise the chip name will be shown.  
Write buffer to chip | This will write the active buffer(FLASH or EEPROM) into the chip.  
Read chipcode | When the chip lock bit is not set you can read the FLASH or EEPROM into the buffer.  
Blank check | Check if the chip FLASH or EEPROM is empty.   
Erase | Erases the chip FLASH. It depends on the fusebits if the EEPROM is erased too. Normally the EEPROM is erased too but some chip have a fuse bit to preserve EEPROM when erasing the chip. A chip MUST be erased before it can be programmed.  
Verify | Checks if the buffer matches the chip FLASH or EEPROM.  
Auto program | This will eraser, and program the FLASH and EEPROM and if $PROG is used, it will set the lock and fusebits too.   
  
In the toolbar you can also alter the ISP clock frequency. 

![notice](notice.jpg)The clock frequency should not be higher than a quarter of the oscillator frequency.

This means that a chip with an internal 8 MHz oscillator which has the 8-divider fuse enabled, will have a clock frequency of 1 Mhz.

The programming clock may not exceed 250 KHz in that case.