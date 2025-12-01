# View Code Explorer

Action

Shows the Code Explorer Window

![code_explorer](code_explorer.png)

The code explorer shows code elements in a tree. By double clicking an element the cursor will be set to the matching code in the editor.

You can also drag an element into the editor window. 

By clicking the right mouse a pop up menu will allow you to filter out constants and variables (registers) from the definition file.

The following code elements will be shown in the explorer:

\- Aliases. These are the user [ALIAS](alias.md)es. 

\- Assembler. This is for single line asm using !

\- Assembler Block. This is for assembler blocks using $asm .. $end asm. If you add comment after $asm, it will be shown in the tree as well. Example : $asm ; Test 

\- Constants. Both user defined constants ([CONST](const.md)) and constants from the definition file are shown. 

\- Declarations. Subs and Functions are both shown. Each with their own color.

\- Functions. These are the user function implementations.

\- Labels. When labels are used in subs and functions, the sub/functions name is listed first.

\- Macros. These are the user macro's created with [MACRO](macro.md).

\- Subs. These are the user sub implementations.

\- Variables. These are the variables from the user code and definition file. Each shown with their own color. Locals are shown under a branch of the sub/function.

\- CallStack. This is optional. Since it takes time to trace the call stack it is turned off by default. Use right mouse click and the pop up menu to activate it.

The call stack shows a tree of the calls you make to user subs and functions. And each sub/function also shows the user functions it calls. 

When multiple calls are made, three dots are added for each additional call. 

\- Types. Declared types with their members are shown. See TYPE.

\- Information. Processor, free ERAM and SRAM. Estimated $hwstack, $swstack and $framesize. 

![notice](notice.jpg)The calculated stack settings are based on the program call tree and local variables. This is just a tool to give you an idea about stack usage. Not taken into account is the stack required by the assembler routines. This means that you need to add a certain amount to the calculated values. When your code uses interrupts you need to increase the calculated $HWSTACK by 32. Otherwise increase it by 16. The $FRAMESIZE should have a minimum value of 24. Add a value of 16 to $SWSTACK. 

Applications using AVR-DOS should use a minimum of 128 for all stacks. 

A future version will also take the assembler code into account.

When the Code Explorer has the focus, pressing CTRL+F will search in the code explorer and not in the editor.

The code explorer works in a separate thread. It will be updated a few seconds after you have quit typing. 

By making the Code Explorer window invisible, the explorer is deactivated.

The popup menu has the following options:

![code_explorer_popup](code_explorer_popup.png)

Show Register Constants

This option can toggle between showing and hiding the register constants. When register constants are shown the tree can become big.

User constants and register constants are shown in a different color.

Show Register Variables

This option can toggle between showing and hiding the register variables. When register variables are shown the tree can become big.

User variables and register variables are shown in a different color.

Show Call Stack

This option can show the Call Stack. This reveals the nesting of your code.

Show Errors

This option deserves a warning. The option is turned off by default. It can be useful to find errors but it can also point to errors which are not considered an error for the compiler. The compiler has a separate parser. The parser from the IDE is a different new parser. While in 2080 all DAT files are updated, you still can get errors which are no real errors. You might want to report them to support. Please send a small as possible program that will show the error.

Show Unused Items

When this option is turned on, all unused items will be shown in grey. For example :

![code_explorer_unused_items](code_explorer_unused_items.png)

In this sample, _temp1 , so_rx_data and DataPtr are unused or unreferenced. _temp1 is an internal variable and so is DataPtr. They do not occupy any space.

But so_rx_data is a user variable which is not referenced. You could remove or remark it.

Refresh

This option will parse the project and update the code explorer tree. 

Find References

This option can find all references for an item. For example when you go to Variables, and select a variable the option becomes enabled in the menu. After choosing this option, the references will be added to the tree.

![code_explorer_refs](code_explorer_refs.png)

Now by clicking the item you will go to the point in your code where the item is referenced/used.

Show References

This options shows a panel on the bottom of the code explorer tree. When you activate the tooltip keeping SHIFT pressed and hovering an item in the editor, the references panel will be updated with all references of that item. A single click on an item in this list will set the cursor in the IDE to referred item.

Consider this simple piece of code :

```vb
Dim S As Single

Input "s " , S

Print S

```
When pressing SHIFT and hovering the mouse over the variable S , the tooltip will be shown : ![tooltip-s](tooltip-s.png)

The references list will be updated as well. The item in bold points to the definition, in this case the DIM S. 

The following two items in the list point to the INPUT "s ", S and the Print S.

Items shown in red are variables that are assigned. 

The panel can be shown or hidden using the right click menu from the explorer.

RENAMING

When you right an item in the References List you get a pop up menu : RENAME

When you click the RENAME option you will be asked for a new name.

Enter a new name for the item (variable,constant, etc). All occurrences in your project will be replaced. Not only the ones in loaded files but also in included files on disk.

When the new name you provide is already used in the project you will get an error message and the items will not be replaced.