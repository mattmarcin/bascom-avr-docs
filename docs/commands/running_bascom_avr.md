# Running BASCOM-AVR

After you have installed BASCOM, you will find a program entry under MCS Electronics\BASCOM-AVR

Double-click the BASCOM-AVR icon ![bascom-icon](bascom-icon.png) to run BASCOM.

The following window will appear. (If this is your first run, the edit window will be empty.)

![bascomide](bascomide.png)

The most-recently opened file will be loaded automatically. Like most Windows programs, there is a menu and a toolbar. The toolbar can be customized. To do this, place the mouse cursor right beside the 'Help' menu.

Then right-click. You can turn on/off the toolbars or you can choose 'Customize'.

This will show the following window:

![toolbar_cust](toolbar_cust.png)

You have the option to create new Toolbars or the reset the toolbars to the default.

To place a new button on a menu bar, select the 'Commands' TAB.

![toolbar_commands](toolbar_commands.png)

In the example above, the Program Category has been selected and at the right pane, all buttons that belong to the Program-category are shown.

You can now select a button and drag & drop it to the Toolbar. To remove a button from the Toolbar, you drag it out of the Toolbar and release the left mouse button.

On the Options-TAB you can further customize the Toolbar:

![setup_options](setup_options.png)

To preserve screen space there are no large icons available.

Option | Description  
---|---  
Menus show recent used commands first | With this option the IDE will learn the menu options you use. It will show only the most used menu options. The idea is that you can find your option quicker this way.  
Show full menus after a short delay | This option will show the remaining menu options after short delay so you do not need to click another menu option to show all menu options.  
Reset my usage data | This option will reset the data the IDE has collected about your menu choices.  
Show Tool tips on toolbars | This option is on by default and it will show a tool tip when you hold the mouse cursor above a toolbar button  
Show shortcut keys in Tool tips | This option is on by default and it will show the shortcut in the tool tip. For example CTRL+C for the Copy button.  
  
The Editor

The editor supports syntax highlighting. Code you enter can be reformatted automatically.

When you press CTRL+J you can select a template. A template is a small piece of code that can be inserted automatically.

When you press CTRL+J you can select a template or you can type the template name and press CTRL+J. If there is only one template starting with that name, the template will be inserted. Otherwise the options are shown.

![editor_templates](editor_templates.png)

Templates are stored in the file bascavr.tpl

When you press SHIFT and move the mouse cursor over a variable, constant or other element you will get a tool tip with info.

![editor_tooltip](editor_tooltip.png)

In the sample above the variable 's' was selected and the tool tip shows that it is a string with a length of 16 bytes in the modules crc8-16-32.bas

Intellisense

The editor has built in intellisense. 

It is important that your code contains the $REGFILE directive like : $REGFILE = "M88def.dat". 

When you press CTRL+SPACE you get a list of statements, sub routines, functions, labels, asm registers, etc. This list depends on the place of the cursor in the code.

\- At the start of a line you will get a list like : ![intel_sol](intel_sol.png). You can select a value from the list and press enter to insert it into the code.

\- When you type a letter of some letters like pr ![intel_pr](intel_pr.png) Here you can see the position is set to the first item that starts with PR : PRINT

\- After PRINT when a variable is expected : ![intel_var](intel_var.png) Here you get functions, variables and constants

\- After CONFIG ![intel_config](intel_config.png) Here you get a list of all CONFIG statements. 

\- After CONFIG param (the = sign). ![intel_configParam](intel_configparam.png) Here you get a lost of parameter values.

\- After GOTO, GOSUB ![intel_gotogosub](intel_gotogosub.png) Here you get a list with labels.

\- After CALL ![intel_call](intel_call.png) Here you get a lost with sub routines.

\- Inside $ASM-$END ASM ![intel_asm](intel_asm.png) Here you get a list of ASM mnemonics. 

\- After ASM mnemonic ![intel_asm_prm](intel_asm_prm.png) Here you get a list of registers.

PLEASE NOTICE : 

\- intellisense is considered a beta function. It is subject to change. It will only work when there are no syntax errors.

\- values for CONFIG might not be shown. This is because all these values need to be present in the DAT files. And each processor has specific options. 

Select Text

Selection of text can be done by double clicking the text, by holding SHIFT down and moving the cursor or you can select a block of text by pressing the ALT key and dragging the mouse cursor.

![edit_select_textblock](edit_select_textblock.png)

TABS

When you have loaded multiple files, each file will be shown in a TAB. The active TAB can be closed or dragged to a new position. When a file is modified the TAB caption will be shown in red.

![editor_tabs](editor_tabs.png)

SHIFT + MOUSE

When you move the mouse cursor to the TAB caption you will see the full path of the loaded file.

When you press the SHIFT key and move the mouse cursor you can get information in a tool tip.

For example when you hover over an indention line :

![edit_indention_mouse](edit_indention_mouse.png)

The tooltip shows info about the structure. So you know that the green line belongs to While Unseen > 0

When we hover over a code element like CH :

![edit_intelli_dim](edit_intelli_dim.png)

This time since CH is a variable. the data type is shown.

In 2084 String constants will be shown with their length. 

The Reference window will list all referenced variables :

![edit_reference_window](edit_reference_window.png)

When you click an item, the cursor will be changed automatically.

Custom Configuration

You can load a custom configuration file by specifying the filename as a parameter.

This allows you to run different versions of the software with different setting/option files.

The configuration file has the XML extension. It can be found by clicking the XML data folder link in the Help, About window.

By default bascom uses the file : \Users\<USER>\AppData\Roaming\MCS Electronics\bascom-avrXXXX.xml

The XXXX is the version. For example 2082. 

When you want to use a custom file we would recommend to store it in the bascom-avr application folder. This way you can run multiple versions of bascom, all with their own settings.

The name of the settings file must be provided as a parameter to BasCom. For example to use a settings file named mysettings.xml :

bascavr.exe mysettings.xml

When BasCom is started it will check if the provided file exists and will load the settings of that file.

If the files does not exist, the normal setting file ise used. 

The reason for unique file names is that once in a while a menu option is added. That is no problem when you update, but when you want to use the xml with an older file you could get errors because of non existing menus.