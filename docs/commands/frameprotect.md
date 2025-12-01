# $FRAMEPROTECT

Action

This directive will enable or disable interrupt frame protection.

Syntax

$FRAMEPROTECT = value

Remarks

Value must be a constant expression that evaluates to false (0) or true (<>0).

By default the frame protection is off. 

When a user function/sub passes parameters with byval, a copy is created and passed to the user sub/function.

When an interrupt is executed, and it calls user sub/functions with parameters passed with byval, the values can get corrupted. 

When activated, the compiler disables interrupts before passing variables, and enables interrupts (when they were enabled) inside the user sub/function. This ensures that the values can not get corrupted from an interrupt which is calling other user sub/functions. 

When you do not call user sub/functions from inside your interrupt you can omit the $frameprotect directive or set it to 0 in order to reduce code.

In version 2075 the compiler had frame protection as a default, and the $NOFRAMEPROTECT served as an override. While you can still use $NOFRAMEPROTECT, it is off by default in 2076 to the preferred switch is $FRAMEPROTECT = 0|1

When you activate frame protection the internal constant named _FPROTECT will be set to 1. 

When you have a user function that calls an ASM library, you must include code to restore the I-flag.

The bcd.lib user lib sample demonstrates this with this code :

#IF _FPROTECT

Out sreg,r3 ; restore I flag

#ENDIF

See also

[$NOFRAMEPROTECT](noframeprotect.md)

Example

```vb
'************************************************  
' TESTING THE FRAME PARAMETER PASSING  
' UNDER HEAVY INTERRUPT LOAD  
'************************************************  
  
' file: frame_pass_test.bas  
  
$regfile = "m88def.dat"  
$crystal = 8000000  
$hwstack = 100  
$swstack = 100  
$framesize = 100  
  
$noframeprotect ' in this sample, disabling the frame protection will result in errors

$frameprotect=0 ' from version 2076, this is the preferred method  
  
Dim Ww As Word , Www As Word , Wwww As Word  
Declare Sub Stack_checking(byval Identifier As Integer )  
  
$baud = 19200  
```
Open "com1:" For Binary As #1  
  
Const T0_idozito = 100  
```vb
Config Timer0 = Timer , Prescale = 1024 '256 --> 4.096 msec egység, 1024 --> 16.384 msec  
On Ovf0 Timer0_interrupt  
Enable Timer0  
```
Start Timer0  
Load Timer0 , T0_idozito  
  
```vb
' These routines are called under the timer interrupt  
Declare Sub Under_it_pass_1(byval Inpar1_uit As Word )  
Declare Sub Under_it_pass_2(byval Inpar2_uit As Word )  
Declare Sub Test()  
' These routines are called in the main loop  
Declare Sub Inmain_test_routine_1(byval Im1_par1 As Word , Byval Im1_par2 As Word , Byval Im1_par3 As Word , Byval Im1_par4 As Word , Byval Im1_par5 As Word , Byval Im1_par6 As Word )  
Declare Sub Inmain_test_routine_2(byval Im2_par1 As Word , Byval Im2_par2 As Word , Byval Im2_par3 As Word , Byval Im2_par4 As Word , Byval Im2_par5 As Word , Byval Im2_par6 As Word )  
Declare Sub Inmain_test_routine_3(byval Im3_par1 As Word , Byval Im3_par2 As Word , Byval Im3_par3 As Word , Byval Im3_par4 As Word , Byval Im3_par5 As Word , Byval Im3_par6 As Word )  
  
' Routine-1 parameters are stored here  
Dim Dim1_p1 As Word  
Dim Dim1_p2 As Word  
Dim Dim1_p3 As Word  
Dim Dim1_p4 As Word  
Dim Dim1_p5 As Word  
Dim Dim1_p6 As Word  
  
' Routine-3 parameters are stored here  
Dim Dim3_p1 As Word  
Dim Dim3_p2 As Word  
Dim Dim3_p3 As Word  
Dim Dim3_p4 As Word  
Dim Dim3_p5 As Word  
Dim Dim3_p6 As Word  
  
```
Program_begins_here:  
```vb
Enable Interrupts  
Print #1 , "PROGRAM BEGIN"  
Do  
```
Call Inmain_test_routine_1(&Haaaa , &HAAAA , &HAAAA , &HAAAA , &HAAAA , &HAAAA )  
  
Call Inmain_test_routine_2(&Haaaa , &HAAAA , &HAAAA , &HAAAA , &HAAAA , &HAAAA )  
  
Call Inmain_test_routine_3(&Haaaa , &HAAAA , &HAAAA , &HAAAA , &HAAAA , &HAAAA )  
```vb
Loop  
  
' All the three routines always gets all parameters as &hAAAA, if they see anything else, they print an error  
' routine_1 stores to DIM area and checks the stored values  
' routine 2 check immediately the incoming parameters  
' routine_3 completely identical to routine_1, except the parameter passing protection  
'  
  
Sub Inmain_test_routine_1(byval Im1_par1 As Word , Byval Im1_par2 As Word , Byval Im1_par3 As Word , Byval Im1_par4 As Word , Byval Im1_par5 As Word , Byval Im1_par6 As Word )  
```
Dim1_p1 = Im1_par1 : Dim1_p2 = Im1_par2 : Dim1_p3 = Im1_par3 : Dim1_p4 = Im1_par4 : Dim1_p5 = Im1_par5 :

Dim1_p6 = Im1_par6  
If Dim1_p1 <> &HAAAA Or Dim1_p2 <> &HAAAA Or Dim1_p3 <> &HAAAA Or Dim1_p4 <> &HAAAA Or Dim1_p5 <> &HAAAA _

Or Dim1_p6 <> &HAAAA Then  
```vb
Print #1 , " PAR ERROR R1 " ; Hex(dim1_p1 ) ; " " ; Hex(dim1_p2 ) ; " " ; Hex(dim1_p3 ) ; " " ;  
Print #1 , Hex(dim1_p4 ) ; " " ; Hex(dim1_p5 ) ; " " ; Hex(dim1_p6 )  
End If  
End Sub  
  
Sub Inmain_test_routine_2(byval Im2_par1 As Word , Byval Im2_par2 As Word , Byval Im2_par3 As Word , Byval Im2_par4 As Word , Byval Im2_par5 As Word , Byval Im2_par6 As Word )  
If Im2_par1 <> &HAAAA Or Im2_par2 <> &HAAAA Or Im2_par3 <> &HAAAA Or Im2_par4 <> &HAAAA Or Im2_par5 <> &HAAAA Or _ Im2_par6 <> &HAAAA Then  
Print #1 , " PAR ERROR R2 " ; Hex(im2_par1 ) ; " " ; Hex(im2_par2 ) ; " " ; Hex(im2_par3 ) ; " " ;  
Print #1 , Hex(im2_par4 ) ; " " ; Hex(im2_par5 ) ; " " ; Hex(im2_par6 )  
End If  
End Sub  
  
Sub Inmain_test_routine_3(byval Im3_par1 As Word , Byval Im3_par2 As Word , Byval Im3_par3 As Word , Byval Im3_par4 As Word , Byval Im3_par5 As Word , Byval Im3_par6 As Word )  
```
Dim3_p1 = Im3_par1 : Dim3_p2 = Im3_par2 : Dim3_p3 = Im3_par3 : Dim3_p4 = Im3_par4 : Dim3_p5 = Im3_par5 :

Dim3_p6 = Im3_par6  
If Dim3_p1 <> &HAAAA Or Dim3_p2 <> &HAAAA Or Dim3_p3 <> &HAAAA Or Dim3_p4 <> &HAAAA Or Dim3_p5 <> &HAAAA Or _

Dim3_p6 <> &HAAAA Then  
```vb
Print #1 , " PAR ERROR R3 " ; Hex(dim3_p1 ) ; " " ; Hex(dim3_p2 ) ; " " ; Hex(dim3_p3 ) ; " " ;  
Print #1 , Hex(dim3_p4 ) ; " " ; Hex(dim3_p5 ) ; " " ; Hex(dim3_p6 )  
End If  
End Sub  
  
Dim Under_it_store_1 As Word  
Dim Under_it_store_2 As Word  
  
' these two routines are called under timer IT  
' They don't do much, except use the frame for parameter passing  
  
Sub Under_it_pass_1(byval Inpar1_uit As Word )  
```
Under_it_store_1 = Inpar1_uit  
```vb
End Sub  
  
Sub Under_it_pass_2(byval Inpar2_uit As Word )  
```
Under_it_store_2 = Inpar2_uit  
```vb
End Sub  
  
' Timer IT calling two routines which use the frame  
  
```
Timer0_interrupt:  
Load Timer0 , T0_idozito  
Call Under_it_pass_1(&H5555 )  
Call Under_it_pass_2(&H3333 )  
```vb
Return  
  
  
End  
  
  


```