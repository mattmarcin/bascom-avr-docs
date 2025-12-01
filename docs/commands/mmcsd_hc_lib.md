# MMCSD_HC.LIB

The MMCSD_HC.LIB is an MMC SD-HC card driver library.

See the AVR-DOS topic for an example.

There is an optional constant you can set in your code :

CONST _CS_EXTENDED_PORT=1

You need to set this constant when using a normal AVR chip with the CS pin connected to an extended port. We recommend to use a normal port which allows the CBI/SBI instructions but some times it is required to use an extended port like PORTF on an MEGA2560. Since the extended port needs a register to read-alter-write a bit, the register R23 need to be saved in the lib. When you define the constant and give it a value of 1, the register is preserved.

You can always set this directive, it will only create unneeded code when using normal ports. 

In version 2086 the LIB has been modified and this constant is no longer required or used.

Using MMC/SD card on a SPI bus with multiple devices

The MMC specification requires that clock pulses are sent to the MMC card with the CS line disabled !!!

It means that when another device is active, the clock pulses can confuse or even corrupt the card.

The solution is to use either a bus driver with tri-state , or to use a dedicated pin for the clock lines.

With XMega there are multiple SPI buses possible. 

With normal AVR you can use HW SPI for the MMC, and use SHIFTIN/SHIFTOUT for the other SPI devices.