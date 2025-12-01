# $LIB

Action

Informs the compiler about the used libraries.

Syntax

$LIB "libname1" [, "libname2"]

Remarks

Libname1 is the name of the library that holds ASM routines that are used by your program. More filenames can be specified by separating the names by a comma.

The specified libraries will be searched when you specify the routines to use with the $EXTERNAL directive.

The search order is the same as the order you specify the library names.

The MCS.LBX will be searched last and is always included so you don't need to specify it with the $LIB directive.

Because the MCS.LBX is searched last you can include duplicate routines in your own library. These routines will be used instead of the ones from the default MCS.LBX library. This is a good way when you want to enhance the MCS.LBX routines. Just copy the MCS.LIB to a new file and make the changes in this new file. When we make changes to the library your changes will be preserved.

Creating your own LIB file

A library file is a simple ASCII file. It can be created with the BASCOM editor, notepad or any other ASCII editor.

When you use BASCOM, make sure that the LIB extension is added to the Options, Environment, Editor, "No reformat extension".

This will prevent the editor to reformat the LIB file when you open it.

The file must include the following header information. It is not used yet but will be later.

copyright = Your name

www = optional location where people can find the latest source

email = your email address

comment = AVR compiler library

libversion = the version of the library in the format : 1.00

date = date of last modification

statement = A statement with copyright and usage information

The routine must start with the name in brackets and must end with the [END].

The following ASM routine example is from the MYLIB.LIB library.

[test]

Test:

ldd r26,y+2 ; load address of X

ldd r27,y+3

ld r24,x ; get value into r24

Inc r24 ; value + 1

St x,r24 ; put back

ldd r26,y+0 ; address of Y

ldd r27,y+1

st x,r24 ; store

ret ; ready

[END]

After you have saved your library in the LIB subdirectory you must compile it with the [LIB Manager](tools_lib_manager.md). Or you can include it with the LIB extension in which case you donât have to compile it.

About the assembler.

When you reference constants that are declared in your basic program you need to put a star(*) before the line.

' Basic Program

CONST myconst = 7

' asm lib

* sbi portb, myconst

By adding the *, the line will be compiled when the basic program is compiled. It will not be changed into object code in the LBX file.

When you use constants you need to use valid BASIC constants:

Ldi r24,12

Ldi r24, 1+1

Ldi r24, &B001 ; binary basic

Ldi r24,0b001 ; binary

Ldi r24,&HFF ; hex basic

Ldi r24,$FF ; hex

Ldi r24,0xFF ; hex

Other syntax is NOT supported.

See also

[$EXTERNAL](external.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

'In order to let this work you must put the mylib.lib file in the LIB dir

'And compile it to a LBX

'-------------------------------------------------------------------------

'define the used library

$lib"mylib.lbx"

'you can also use the original ASM :

'$LIB "mylib.LIB"

'also define the used routines

$external Test

'this is needed so the parameters will be placed correct on the stack

Declare Sub Test(byval X Asbyte , Y Asbyte)

'reserve some space

Dim Z As Byte

'call our own sub routine

```
Call Test(1 , Z)

```vb
'z will be 2 in the used example

End

```