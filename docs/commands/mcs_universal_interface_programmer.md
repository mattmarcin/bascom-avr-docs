# MCS Universal Interface Programmer

The MCS Universal Interface programmer allows you to customize the pins that are used for the ISP interface. The file prog.settings stores the various interfaces.

The content :

;how to use this file to add support for other programmers

;first create a section like [newprog]

; then enter the entries:

; BASE= $hexaddress

; MOSI= address in form of BASE[+offset] , bit [,inverted]

; CLOCK= same as MOSI

; RESET=same as MOSI

; MISO=same as MOSI

; The bit is a numer that must be written to set the bit

; for example 128 to set bit 7

; Optional is ,INVERTED to specify that inverse logic is used

; When 128 is specified for the bit, NOT 128 will be written(127)

[FUTURELEC]

;tested and ok

BASE=$378

MOSI=BASE+2,1,inverted

CLOCK=BASE,1

RESET=BASE,2

MISO=BASE+1,64

[sample]

;tested and ok

BASE=$378

MOSI=BASE,1

CLOCK=BASE,8

RESET=BASE,4

MISO=BASE+1,128,INVERTED

[stk200]

;tested and ok

BASE=$378

MOSI=BASE,32

CLOCK=BASE,16

RESET=BASE,128

MISO=BASE+1,64

Four programmers are supported : Futurelec, Sample and STK200/STK300 and WinAVR/ SP12.

To add your own programmer open the file with notepad and add a new section name. For the example I will use stk200 that is already in the file.

[stk200]

The LPT base address must be specified. For LPT1 this is in most cases $378. $ means hexadecimal.

The pins that are needed are MOSI, CLOCK, RESET and MISO.

Add the pin name MOSI =

After the pin name add the address of the register. For the STK200 the data lines are used so BASE must be specified. After the address of the register, specify the bit number value to set the pin high. Pin 0 will be 1, pin 1 would be 2, pin 2 would be 4 etc. D5 is used for the stk so we specify 32.

When the value is set by writing a logic 0, also specify, INVERTED.

After you have specified all pins, save the file and restart BASCOM.

Select the Universal Programmer Interface and select the entry you created.

After you have selected an entry save your settings and exit BASCOM. At the next startup of BASCOM, the settings will be used.

The following picture shows the LPT connector and the relation of the pins to the LPT registers.

![lptcon](lptcon.gif)

Always add your entry to the bottom of the file and email the settings to support@mcselec.com so it can be added to BASCOM.