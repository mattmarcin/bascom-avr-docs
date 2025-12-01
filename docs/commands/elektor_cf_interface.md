# Elektor CF-Interface

The popular Electronics magazine Elektor, published an article about a CF-card interface. This interface was connected to an 89S8252. This interface can be used and will use little pins of the micro.

Note that because of the FAT buffer requirement, it is not possible to use a 8051 micro.,

At this moment, only the Mega128 and the Mega103 AVR microâs are good chips to use with AVR-DOS.

You can use external memory with other chips like the Mega162.

![cf-elektor](cf-elektor.gif)

Changes of the hardware pins is possible in the file Config_FlashCardDrive_EL_PIN.bas.

The default library is FlashCardDrive.lib but this interface uses the library FlashCardDrive_EL_PIN.lib.

See also: [AVR-DOS File System](avr_dos_file_system.md)