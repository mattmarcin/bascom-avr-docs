# UPDI Programmer

The MCS UPDI programmer is a serial based programmer.

You need to select 115200 BAUD and the COM port which is connected to the UPDI interface.

In version 2084 you can select up to 225000 baud. This is the maximum recommended baud from microchip with the default clock.

In version 2086 the maximum baud of 1600000 is supported. Notice that only DA/DB processors support this speed.

The UPDI interface is very simple : all you need is a TX, RX and a resistor.

Connect TX from the PC UART to a 4K7 resistor. The other side of the resistor is connected to the PC RX and to the UPDI pin of the processor.

We use DTR to switch the TX and RX from the PC to the processor. This allows to use the PC COM port to be used for serial communication and as a UPDI programmer.

Note : some modules will not give proper signals. A 1K resistor will bring better results.

![notice](notice.jpg)Please notice that you need a MAX232 or other level converter between the PC communication pins to create the proper voltage level! Like the circuit shown below.

The programmer works similar as the other supported programmers : you can program the FLASH, EEPROM and the fuse/lock bytes

In version 2083 you can also write the fuse bytes. 

![updi-programmer](updi-programmer.png)

When you change the values of a fuse the WRITE-FUSES button will be enabled. 

When you change the value of the LOCK fuse, the WRITE-LOCK bits button will be enabled.

When you change the value of the user fuses, the WRITE USER ROW button will be enabled.

When you write the fuses, the fuse values will be re-read (refreshed). And the same for the other fuses. 

See CONFIG FUSES for information on how to automatic program fuse bytes.

Programmer Options

The MCS UPDI programmer has a number of options:

![mcsupdioptions](mcsupdioptions.png)

Since this is a serial programmer you need to select the COM port. 

The BAUD also need to be selected.

115200 should always work

22500 also should work for all processors

The maximum speed for the XTINY platform is 900.000 (900 KB)

The maximum speed for the MEGAX platform is also 900 KB

The maximum speed for the AVRX (DA/DB) platform is 1.600.000 (1.6 MB)

The timeout can best be set to 50.

Then there is an option to control what the DTR and RTS pins should do.

You can chose :

\- NONE : DTR/RTS is not used

\- program/data : DTR/RTS is used to switch between programming and normal mode. This way you can use a MUX and use the same TX/RX pins of your serial port for programming and data

\- HV program : DTR/RTS is used to generate a pulse on the UPDI pin. You should include some circuit that inserts 12V using DTR line.

Since you have 2 pins you can chose DTR for switch between program/data and RTS for the 12V pulse.

![unlock](unlock.png)

The UPDI prgrammer also has a Chip Unlock option. When the chip is locked, you need this option to fully erase the chip.

A typical connection for the UPDI programmer :

![updi-prog-sch](updi-prog-sch.png)

A MAX232 level converter will convert the RS232 levels to 5V.

The TX from the PC/max232 is connected with a 4K7(or 1K) resistor to the UPDI pin.

The RX from the PC/max232 is connected directly to the UPDI pin.

you can also use an USB virtual com port chip such as the FT232 or CP2102.

Using a serial port just for programming is a bit of a waste. Often you also like to have serial communications.

So a more practical programmer will switch the TX/RX lines between the UPDI pin and the TX-RX USART pins of the processor.

![updi-prog-mux](updi-prog-mux.png)

Notice that the USB circuit shown is not complete, you should check it with the chip of your choice like FT232RL, CP2102, etc. The main purpose of the USB part is to show the TX/RX and DTR pins.

The TX pin and RX pins are connected to a 4053 switch. This is an analog switch. The DTR line selects the XYZ-0 or XYZ-1 side of the switch. 

The UPDI pin is also connected to a MUX switch. This simple circuit now switches between the UPDI mode and the TX and RX pins of the processor.

The BASCOM-UPDI programmer will automatically switch the DTR line.

Some processors have a dedicated UPDI pin. Other processors share this pin with a normal IO pin.

The RESET pin can also be dedicated or shared. When shared you must program the RESET function since this is not enabled by default.

A virtual USB COM port is used most likely since a DB-9 serial connector is not found on most modern PC/laptop.

FT232/CP2102

We have tested using the CP2102 but FT232 should also work. As user EDC found out the FT232 requires some driver changes.  
\- Buffers need to be changed from 4096 to 64

\- Latency need to be set from 16 to 2

For more information : [mcs forum](<https://www.mcselec.com/index2.php?option=com_forum&Itemid=59&page=viewtopic&p=82271#82271>)

User Feedback about USB chips

MCP2221A:

1.1 Bascom AVR does not work with the chipset MCP2221A.... no matter of every change in the circuit or in the UART-settings.

UMFT230XB-01:

Works but very slow

See also the info from EDC listed above.

CP2102 (MCS chip of choice)

\- works perfect!

FT232RL

It works but it programs slow.

See also EDC settings.

CH340G

works perfect & fast

Comment from other user:

CH340 doesn't work.

FT232 works perfectly. 

This is of course contradicting. Could be the driver, other settings? 

MCS UPDI programmer is considered a nice free alternative to program the processor. 

For better results you best get the Microchip SNAP programmer. 

See Also

[Using a BOOTLOADER](using_a_bootloader.md) , MCS SNAP Programmer