# BCCARD

BCCARD.LIB is a commercial addon library that is available separately from [MCS Electronics](<http://www.mcselec.com/index.php?page=shop.product_details&flypage=shop.flypage&product_id=33&category_id=6&option=com_phpshop&Itemid=1>).

With the BCCARD library you can interface with the BasicCards from [www.basiccard.com](<http://Www.basiccard.com>)

BasicCards are also available from MCS Electronics

A BasicCard is a smart card that can be programmed in BASIC.

The chip on the card looks like this :

![smartcard](smartcard.gif)

To interface it you need a smart card connector.

In the provided example the connections are made as following:

Smart Card PIN | Connect to  
---|---  
C1 | +5 Volt  
C2 | PORTD.4 , RESET  
C3 | PIN 4 of 2313 , CLOCK  
C5 | GND  
C7 | PORTD.5 , I/O  
  
The microprocessor must be clocked with a 3579545 crystal since that is the frequency the Smart Card is working on. The output clock of the microprocessor is connected to the clock pin of the Smart card.

Some global variables are needed by the library. They are dimensioned automatic by the compiler when you use the CONFIG BCCARD statement.

These variables are:

_Bc_pcb : a byte needed by the communication protocol.

Sw1 and SW2 : both bytes that correspondent to the BasicCard variables SW1 and SW2

The following statements are especially for the BasicCard:

[CONFIG BCCARD](config_bccard.md) to init the library

[BCRESET](bcreset.md) to reset the card

[BCDEF](bcdef.md) to define your function in the card

[BCCALL](bccall.md) to call the function in the card

Encryption is not supported by the library yet.