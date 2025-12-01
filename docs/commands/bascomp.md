# BASCOMP

BASCOMP.EXE is a command line compiler utility.

It can be called from your own favorite editor when using linux. Or when compiling projects from a batch file.

The bascomp.exe utility must be placed in the same folder as bascavr.exe.

It depends on the bascom-avr license dll and the basc-avr.dll compiler DLL.

It also depends on the DAT files and the LIB folder with the libraries.

For this reason the files is best placed into the bascom-avr application folder.

Change in 2085

The utility used to work by passing the chip ID. But since some processors are binary compatible and share the same ID this could result in problems.

bascomp requires only one parameter : the source file you want to compile. When the path contains spaces you need to enclose it in double quotes.

Example : bascomp "c:\some folder\mycode example.bas"

bascomp will read the source and extract info about the dat file and stack. Specifically it will look for $regfile, $hwstack,$swstack and $framesize

If these settings are not found you need to provide them using SS for $softstack, HW for $hwstack and FR for $framesize

Example : bascomp "myfile.bas" HW=64

This would use a $hwstack of 64 bytes. Note that even if your source would contain a different value, a value of 64 would be used.

In order to override the processor dat file, you need to use the new DEVICE parameter. It accepts only the official processor name.

Example : bascomp "myfile.bas" device=atmega88

When you specify a device name that does not exist, a list will be shown with all device names.

The command line utility will set the DOS errorcode to 0 when no error is found, or to a non zero value when there is a problem.

Parameters 

HW | Hardware stack ($hwstack)  
---|---  
FR | Frame size ($framesize)  
SS | Soft stack ($swstack)  
DEVICE | Device name. Stored in the DAT files with the name device= The name is not case sensitive.  
  
This is a list of device names which will change when new DAT files are added.

available devices:

AT90S1200

AT90S2313

AT90S2323

AT90S2333

AT90S2343

AT90S4414

AT90S4433

AT90S4434

AT90S8515

AT90S8535

AT86RF401

AT90PWM1

AT90PWM216

AT90PWM3

ATtiny12

ATtiny13

ATtiny13A

ATtiny15

ATtiny1634

ATtiny167

ATtiny20

ATtiny22

ATtiny2313

ATtiny2313A

ATtiny24

ATtiny24A

ATtiny25

ATtiny26

ATtiny261

ATtiny4313

ATtiny43U

ATtiny44

ATtiny441

ATtiny45

ATtiny461

ATtiny48

ATtiny828

ATtiny84

ATtiny841

ATtiny85

ATtiny861

ATtiny87

ATtiny88

ATtiny1604

ATtiny1606

ATtiny1607

ATtiny1614

ATtiny1616

ATtiny1617

ATtiny202

ATtiny204

ATtiny212

ATtiny214

ATtiny3216

ATtiny3217

ATtiny402

ATtiny404

ATtiny406

ATtiny412

ATtiny414

ATtiny1416

ATtiny417

ATtiny804

ATtiny806

ATtiny807

ATtiny814

ATtiny816

ATtiny817

AVR128DB28

AVR128DB32

AVR128DB64

AVR64DB32

ATMega103

ATMega1280

ATMega128

ATMega1281

ATMEGA1284

ATMEGA1284P

AT90CAN128

ATMega128

ATMega128RFA1

ATMEGA161

ATmega162

ATMEGA163

ATMEGA164A

ATMEGA164PA

ATMEGA164P

ATMega165A

ATMega165

ATmega168

ATmega168PA

ATmega168PB

ATmega168P

ATmega169A

ATmega169

ATmega169PA

ATmega169P

ATmega16A

ATmega16

ATMEGA16M1

ATMEGA16U2

ATMEGA16U4

ATMega2560

ATMega2561

ATMEGA323

ATMEGA324A

ATMEGA324PA

ATMEGA324PB

ATMEGA324P

ATMEGA3250A

ATMEGA3250PA

ATMEGA3250P

ATMEGA325

ATmega328

ATmega328PB

ATmega328P

ATmega329

ATMEGA32A

ATMEGA32C1

AT90CAN32

ATMEGA32

ATMEGA32M1

ATMEGA32U2

ATMEGA32U4

ATmega406

ATmega48

ATmega48PA

ATmega48PB

ATmega48P

ATmega603

ATMega640

ATMEGA644A

ATMEGA644

ATMEGA644PA

ATMEGA644P

ATMEGA6450P

ATMEGA645

ATmega6490

ATmega649A

ATmega649

ATmega649P

ATMEGA64C1

AT90CAN64

atmega64

ATMEGA64M1

ATmega8515

ATmega8535

ATmega88A

ATmega88

ATmega88PA

ATmega88PB

ATmega88P

ATmega8A

ATmega8

ATMEGA8U2

ATmega4808

ATmega4809

AT90USB1286

AT90USB1287

AT90USB162

AT90USB646

AT90USB82

ATXMega128A1

ATXMega128A1U

ATXMega128A3

ATXMega128A3U

ATxmega128A4U

ATxmega128B1

ATxmega128B3

ATXMega128C3

ATXMega128D3

ATxmega128D4

ATxmega16A4

ATxmega16D4

ATxmega16E5

ATXMega192A3

ATXMega192A3U

ATXMega192D3

ATXMega256A3B

ATXMega256A3BU

ATXMega256A3

ATXMega256A3U

ATXMega256D3

ATxmega32A4

ATxmega32A4U

ATXMega32C4

ATxmega32D4

ATxmega32E5

ATXMega384C3

ATXMega64A1

ATXMega64A3

ATXMega64A3U

ATxmega64A4U

ATXMega64D3

ATxmega64D4

ATxmega8E5