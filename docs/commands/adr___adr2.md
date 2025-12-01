# ADR ,  ADR2

Action

Create label address.

Syntax

ADR  label

ADR2  label

Remarks

label | The name of a label.  
---|---  
  
The AVR uses WORD addresses. ADR will create the word address. To find a byte in memory, you need to multiply by 2. For this purpose ADR2 is available. It will create the address of the label multiplied by 2.

Using ADR2 you can use tables. The sample program demonstrates this together with some more advanced ASM code.

The sample includes ADR2.LIB. This lib contains a special version of _MoveConst2String .

The normal routine in MCS.LIB will stop printing once a null byte (zero) is encountered that indicates the end of a string.

But for the sample program, we may not change the address, so the address is restored when the null byte is found.

See Also

NONE

Example

```vb
'===============================================================================

' This is an example of how to create an interactive menu system supporting

' sub-menus and support routines using the !ADR and !ADR2 statements

'===============================================================================

$regfile = "M644def.dat"

$crystal = 8000000

$hwstack = 64 ' specify the hardware stack depth

$swstack = 64 ' specify the software stack depth

$framesize = 64 ' specify the framesize (local stack depth)

$lib "adr2.lib"

'-------------------------------------------------------------------------------

Dim Menupointer As Word

Dim Actionpointer As Word

Dim Entries As Byte

Dim Dummy As Byte

Dim Message As String * 32

Dim Local1 As Byte

Dim Local_loop1 As Byte

```
Const Menu_id = &HAA ' sub-menu ID byte

Const Routine_id = &H55 ' service routine ID byte

'-------------------------------------------------------------------------------

Restore Main_menu ' point to the start of the 'main' menu

! sts {MenuPointer}, R8 ' }

! sts {MenuPointer + 1}, R9 ' } store the pointer to the start of the menu

Display_new_menu:

! lds R8, {MenuPointer} ' }

! lds R9, {MenuPointer + 1} ' } restore the pointer to the start of the menu

Read Entries ' get the number of entries in the menu including the title

```vb
Print

For Local_loop1 = 1 To Entries

```
Read Message ' read the message

```vb
Print Message ' send it to the console

Next

```
Read Dataptr ' get the pointer to the menu's action table

! sts {ActionPointer}, R8 ' }

! sts {ActionPointer + 1}, R9 ' } store the pointer to the start of the menu's action list

```vb
Input "Entry ? " , Local1 ' ask the user which menu entry

If Local1 = 0 Then ' is it valid ?

Goto Display_new_menu ' if not, re-display the menu

End If

If Local1 => Entries Then ' is it valid ?

Goto Display_new_menu ' if not, re-display the menu

End If

```
! lds R8,{ActionPointer} ' }

! lds R9,{ActionPointer + 1} ' } restore the pointer to the menu's action list

```vb
If Local1 <> 1 Then

For Local_loop1 = 2 To Local1 '

```
! ldI R30,4 ' }

! clr R1 ' }

! add R8,R30 ' }

! adc R9,R1 ' }

```vb
Next ' } calculate the location of the selected entry's function ID

End If

```
Read Local1 ' get the menu entry's function ID

Read Dummy ' to handle the uP expecting WORDS in DATA statements

If Local1 = Menu_id Then ' did the user select an entry that points to another menu ?

Read Dataptr

! sts {MenuPointer}, R8 ' }

! sts {MenuPointer + 1}, R9 ' } store the start of the menu

```vb
Goto Display_new_menu

End If

```
Read Dataptr ' get the address of this entry's support routine

! movw R30,R8

! icall ' pass control to the entry's support routine

```vb
Goto Display_new_menu ' re-display the last menu displayed

'-------------------------------------------------------------------------------

' Test support routines

'-------------------------------------------------------------------------------

```
Hello_message:

```vb
Print

Print "You asked to print 'Hello'" ' confirmation that Menu Entry 3 was selected

Return

```
2nd_menu_1st_entry_routine:

```vb
Print

Print "You selected Entry 1 of the 2nd menu" ' confirmation that Menu Entry 1 was selected

Return

```
2nd_menu_2nd_entry_routine:

```vb
Print

Print "You selected Entry 2 of the 2nd menu" ' confirmation that Menu Entry 2 was selected

Return

```
3rd_menu_1st_entry_routine:

```vb
Print

Print "You selected Entry 1 of the 3rd menu" ' confirmation that Menu Entry 1 was selected

Return

```
3rd_menu_2nd_entry_routine:

```vb
Print

Print "You selected Entry 2 of the 3rd menu" ' confirmation the Menu Entry 2 was selected

Return

End

'===============================================================================

' Data Statements

'===============================================================================

$data

'-------------------------------------------------------------------------------

' Main Menu

'-------------------------------------------------------------------------------

```
Main_menu:

Data 4 ' number of entries in the menu including title

Data "MAIN MENU" ' } menu title

Data "1. Go to Menu 2" ' } 1st menu entry

Data "2. Go to Menu 3" ' } 2nd menu entry

Data "3. Print 'Hello' message" ' } 3rd menu entry

Adr2 Mainmenu_supporttable ' point to this menu support table

'-------------------------------------------------------------------------------

Mainmenu_supporttable:

Data Menu_id ' identify this menu entry as a menu

Adr2 Second_menu ' address of next menu

Data Menu_id ' identify this menu entry as a menu

Adr2 Third_menu ' address of next menu

Data Routine_id ' identify this menu entry as support routine

Adr Hello_message ' address of the support routine

```vb
'-------------------------------------------------------------------------------

' Second Menu

'-------------------------------------------------------------------------------

```
Second_menu:

Data 4 ' number of entries in the menu

Data "SECOND MENU" ' } menu title

Data "1. 2nd Menu Entry #1" ' } 1st menu entry

Data "2. 2nd Menu Entry #2" ' } 2nd menu entry

Data "3. Go to previous menu" ' } 3rd menu entry

Adr2 Secondmenu_supporttable ' point to this menu support table

'-------------------------------------------------------------------------------

Secondmenu_supporttable:

Data Routine_id ' identify this menu entry as a support routine

Adr 2nd_menu_1st_entry_routine ' support routine for 1st menu entry

Data Routine_id ' identify this menu entry as a support routine

Adr 2nd_menu_2nd_entry_routine ' support routine for 2nd menu entry

Data Menu_id ' identify this menu entry as a menu

Adr2 Main_menu ' support routine for 3rd menu entry

```vb
'-------------------------------------------------------------------------------

' Third Menu

'-------------------------------------------------------------------------------

```
Third_menu:

Data 4 ' number of entries in the menu

Data "THIRD MENU" ' } menu title

Data "1. 3rd Menu Entry #1" ' } 1st menu entry

Data "2. 3rd Menu Entry #2" ' } 2nd menu entry

Data "3. Go to previous menu" ' } 3rd menu entry

Adr2 Thirdmenu_supporttable ' point to this menu support table

'-------------------------------------------------------------------------------

Thirdmenu_supporttable:

Data Routine_id ' identify this menu entry as a support routine

Adr 3rd_menu_1st_entry_routine ' support routine for 1st menu entry

Data Routine_id ' identify this menu entry as a support routine

Adr 3rd_menu_2nd_entry_routine ' support routine for 2nd menu entry

Data Menu_id ' identify this menu entry as a menu

Adr2 Main_menu ' support routine for 3rd menu entry