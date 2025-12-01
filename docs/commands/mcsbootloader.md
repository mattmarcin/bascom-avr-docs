# MCS Bootloader

The MCS Boot loader is intended to be used with the [$LOADER](loader.md) sample for normal AVR and XMega. For Xtiny, MegaX and AVRX check the [$ROMSTART](_romstart.md) topic.

It uses the X-modem Checksum protocol to upload the binary file. It works very quick.

The Boot loader sample can upload both normal flash programs and EEPROM images.

The Boot loader sends a byte with value of 123 to the AVR Boot loader. This boot loader program then enter the boot loader or will jump to the reset vector (0000) to execute the normal flash program.

When it receives 124 instead of 123, it will upload the EEPROM.

When you select a BIN file the flash will be uploaded. When you select an EEP file, the EEPROM will be uploaded.

The Boot loader has some specific options.

![mcsbootloader](mcsbootloader.jpg)

BOOTSIZE

You can choose the boot size which is 1024 for the BASCOM $LOADER example.

Since this space is used from the normal flash memory, it means your application has 1024 less words for the main application. (A word is 2 byte, so 2KB less)

The XMEGA has a separate boot space so for Xmega you can set the value to 0.

RESET

The boot loader is started when the chip is reset. Thus you need to reset the chip after you have pressed F4(program). But when you have connected the DTR line to the chip reset (with a MAX232 buffer) you can reset the chip automatically. You do need to set the 'Reset via DTR' option then. You can also chose to use the RTS line. When your program does not use the boot vector or needs a special sequence to activate the loader, you can chose the soft reset. To send ASCII characters you can embed them between brackets {}. For example {065} will be sent as the character A or byte with value 65.

CLOSE

By choosing 'Close programmer window when ready' the window will be closed when the loader returns 0.

In all other cases it will remain opened so you can look at a possible cause.

EEP

If an EEP (EEPROM image file) exists, the loader can send this file instead of the flash binary file. If you enable this option, you will be asked if you want to send the EEP instead of the BIN file.

After you have pressed F4 to following window will appear :

![MCS-bootloader](mcs-bootloader.jpg)

As you can see the loader sends a byte with value of 123.

You need to reset the chip, and then you will see that the loader returned 123 which means it received the value.

It will start the upload and you see a progress bar. After the loader is ready, you see a finish code of 0.

A finish code of 0 means that all wend well.

Other finish codes will not close the window even if this option is enabled.

You need to manual close the window then.

ERROR CODES

-6001 - Bad format in file name

-6002 - file not found

-6003 - file not found in folder

-6004 - folder not found

-6005 - canceled

-6006 - time out

-6007 - protocol error

-6008 - too many errors

-6009 - block sequence error

-6016 - session aborted 

The most likely error is -6006 when the bootloader is not present or does not respond timely after the initial handshake. Increase the $timeout in the boot loader in that case.