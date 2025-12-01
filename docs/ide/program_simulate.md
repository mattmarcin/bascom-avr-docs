# Program Simulate

With this option, you can simulate your program. So what exactly is simulating? For BASCOM it means that the generated object code is processed with a virtual AVR processor.

The simulator can simulate the AVR instructions. It can also simulate the hardware for a part. The goal of the simulator is to allow you to debug your code. The goal was not to create 100% virtual AVR hardware.

This means that some hardware is simulated but with different timing. 

You can simulate your programs with AVR Studio or any other Simulator available such as ISIS or you can use the built in Simulator.

The simulator that will be used when you press F2, depends on the selection you made in the Options Simulator TAB. The default is the built in Simulator.

Program Simulate shortcut : ![BASC0037_wmf](basc0037_wmf.gif), F2

To use the built in Simulator the files DBG and OBJ must be selected from the [Options Compiler Output](options_compiler_output.md) TAB.

The OBJ file is the same file that is used by the AVR Studio simulator.

The DBG file contains info about variables and many other info required to simulate a program.

![sim_main](sim_main.png)

The yellow dot means that the line contains executable code. The blue arrow is visible when you start simulating. It will point to the line that will be executed.

The Simulator window is divided into a few sections:

The Toolbar

The toolbar contains the buttons you can press to start an action.

![BASC0039](basc0039.gif)This is the RUN button, it starts a simulation. You can also press F5. The simulation will pause when you press the pause button. It is advised, that you step through your code at the first debug session. When you press F8, you step through the code line by line which is a clearer way to see what is happening.

![BASC0040](basc0040.gif)This is the PAUSE button. Pressing this button will pause the simulation.

![BASC0041](basc0041.gif)This is the STOP button. Pressing this button will stop the simulation. You can't continue from this point, because all of the variables are reset. You need to press the RUN button when you want to simulate your program again.

![BASC0042](basc0042.gif)This is the STEP button. Pressing this button (or F8) will simulate one code line of your BASIC program. The simulator will go to the RUN state. After the line is executed the simulator will be in the PAUSE state. If you press F8 again, and it takes a long time too simulate the code, press F8 again, and the simulator will go to the pause state.

![BASC0043](basc0043.gif)This is the STEP OVER button or SHIFT+F8). It has the same effect as the STEP button, but sub programs are executed completely, and the simulator does not step into the SUB program.

![BASC0044](basc0044.gif)This is the RUN TO button. The simulator will RUN until it gets to the current line. The line must contain executable code. Move the cursor to the desired line before pressing the button.

![BASC0045](basc0045.gif)This button will show the processor registers window.

![sim_registers](sim_registers.png)

The values are shown in hexadecimal format. To change a value, click the cell in the VAL column, and type the new value. When you right click the mouse, you can choose between the Decimal, Hexadecimal and Binary formats.

The register window will show the values by default in black. When a register value has been changed, the color will change into red. Each time you step through the code, all changed registers are marked blue. This way, the red colored value indicate the registers that were changed since you last pressed F8(step code). A register that has not been changed at all, will remain black.

![BASC0047](basc0047.gif)This is the IO button and will show processor Input and Output registers.

![sim_IO](sim_io.png)

The IO window works similar as the Register window.

A right click of the mouse will show a popup menu so you can choose the format of the values.

And the colors also work the same as for the registers : black, value has not been changed since last step(F8). Red : the value was changed the last time your pressed F8. Blue : the value was changed since the begin of simulation. When you press the STOP-button, all colors will be reset to black.

![BASC0049](basc0049.gif)Pressing this button shows the Memory window.

![sim_memory](sim_memory.png)

The values can be changed the same way as in the Register window.

When you move from cell to cell you can view in the status bar which variable is stored at that address.

The SRAM TAB will show internal memory and XRAM memory.

The EEPROM TAB will show the memory content of the EEPROM.

The colors work exactly the same as for the register and IO windows. Since internal ram is cleared by the compiler at startup, you will see all values will be colored blue. You can clear the colors by right clicking the mouse and choosing 'Clear Colors'.

![simulator_refreshvars](simulator_refreshvars.png) The refresh variables button will refresh all variables during a run (F5). When you use the hardware simulator, the LEDS will only update their state when you have enabled this option. Note that using this option will slow down simulation. That is why it is an option. When you use F8 to step through your code you do not need to turn this option on as the variables are refreshed after each step.

![simulator_simtimers](simulator_simtimers.png) When you want to simulate the processors internal timers you need to turn this option on. Simulating the timers uses a lot of processor time, so you might not want this option on in most cases. When you are debugging timer code it is helpful to simulate the timers.

The simulator supports the basic timer modes. As there are many new chips with new timer modes it is possible that the simulator does not support all modes. When you need to simulate a timer the best option may be to use the latest version of AVR Studio and load the BASCOM Object file.

Even AVR Studio may have some flaws, so the best option remains to test the code in a real chip.

![notice](notice.jpg)The TIMER simulation only simulates TIMER0 and 16 bit TIMER1. And only counting/time modes are supported. PWM mode is not simulated. 

![simulator_realterm](simulator_realterm.png) This option allows you to use a real terminal emulator for the serial communication simulation.

Normally the simulator send serial output to the blue window, and you can also enter data that needs to be sent to the serial port.

When you enable the terminal option, the data is sent to the actual serial port, and when serial data is received by the serial port, it will be shown.

![sim_trace](sim_trace.png)This option turns on/off trace information. When enabled, a file with the name of your project will be created with the .TRACELOG extension.

This file will contain the file, line number and source code that is executed. It is intended to check which parts of your code execute.

Under the toolbar section there is a TAB with a number of pages:

VARIABLES

![simulator_vars](simulator_vars.png)

This section allows you to see the value of program variables. You can add variables by double clicking in the Variable-column. A list will pop up from which you can select the variable.

To watch an array variable, type the name of the variable with the index.

During simulation you can change the values of the variables in the Value-column, Hex-column or Bin-column. You must press ENTER to store the changes.

To delete a variable, you can press CTRL+DEL.

To enter more variables, press the DOWN-key so a new row will become visible.

It is also possible to watch a variable by selecting it in the code window, and then pressing enter. It will be added to the variable list automatically.

Notice that it takes time to refresh the variables. So remove variables that do not need to be watched anymore for faster simulation speed.

LOCALS

![simulator_locals](simulator_locals.png)

The LOCALS window shows the variables found in a SUB or FUNCTION. Only local variables are shown. You can not add variables in the LOCALS section.

Changing the value of local variables works the same as in the Variables TAB.

WATCH

![simulator_watch](simulator_watch.png)

The Watch-TAB can be used to enter an expression that will be evaluated during simulation. When the expression is true the simulation is paused.

To enter a new expression, type the expression in the text-field below the Remove button, and press the Add-button.

When you press the Modify-button, the current selected expression from the list will be replaced with the current typed value in the text field.

To delete an expression, select the desired expression from the list, and press the Remove-button.

During simulation when an expression becomes true, the expression that matches will be selected and the Watch-TAB will be shown.

uP

![simulator_up](simulator_up.png)

This TAB shows the value of the microprocessor status register (SREG).

The flags can be changed by clicking on the check boxes.

The software stack, hardware stack, and frame pointer values are shown. The minimum or maximum value that occurred during simulation is also shown. When one of these data areas enter or overlap another one, a stack or frame overflow occurs.

This will be signaled with a pause and a check box.

Pressing the snapshot-button will save a snapshot of the current register values and create a copy of the memory.

You will notice that the Snapshot-button will change to âStopâ

Now execute some code by pressing F8 and press the Snapshot-button again.

A window will pop up that will show all modified address locations.

This can help to determine which registers or memory a statement uses.

![simulator_snapshot](simulator_snapshot.png)

When you write an ISR (Interrupt Service Routine) with the NOSAVE option, you can use this to determine which registers are used and then save only the modified registers.

INTERRUPTS

![simulator_ints](simulator_ints.png)

This TAB shows the interrupt sources. When no ISR's are programmed all buttons will be disabled.

When you have written an ISR (using ON INT...), the button for that interrupt will be enabled. Only the interrupts that are used will be enabled.

By clicking an interrupt button the corresponding ISR is executed.

This is how you simulate the interrupts. When you have enabled 'Sim Timers' it can also trigger the event.

The pulse generator can be used to supply pulses to the timer when it is used in counter mode.

First select the desired pin from the pull down box. Depending on the chip one or more pins are available. Most chips have 2 counters so there will usually be 2 input pins.

Next, select the number of pulses and the desired delay time between the pulses, then press the Pulse-button to generate the pulses.

The delay time is needed since other tasks must be processed as well.

The option âSim timersâ must be selected when you want to simulate timers/counters.

TERMINAL Section

Under the window with the TABS you will find the terminal emulator window. It is the dark blue area.

In your program when you use PRINT, the output will be shown in this window.

When you use INPUT in your program, you must set the focus to the terminal window and type in the desired value.

You can also make the print output go directly to the COM port.

Check the Terminal option to enable this feature.

The terminal emulator settings will be used for the baud rate and COM port.

Any data received by the COM port will also be shown in the terminal emulator window.

Notice that most microprocessors have only 1 UART. The UART0-TAB is used to communicate with tis UART. The UART1-TAB need to be selected in order to view the UART1 output, or to send data to UART1.

In version 2083, UART0-UART3 are simulated. Unavailable UARTS are not shown.

Software UARTS are not supported by the simulator. They can not be simulated.

UART0

UART0 has some specific options. When you right click the mouse you will get a popup menu.

\- Serial Input File. 

This option selects a file with the SI extension. It must be named the same as your main file but having the SI extension. The content will be used as serial data input. Each time the processor checks UART0 it will read a byte fom the file as if it were sent.

\- Load custom serial Input File

This option allows you to select a specific SI file. An Open Dialog will be shown and you can select the file.

\- Copy

This option copies data sent to the simulated terminal. 

\- Paste

This option sends data to the simulated terminal.

\- Log to File

This option creates a file with the LOG extension. It will have the name of your main file with the LOG extension. All data send to the simulated UART terminal will be send to the log file as well.

\- Show in HEX

This option shows output in HEX format between brackets like [45] [6E] etc.

SOURCE Section

Under the Terminal section you find the Source Window.

It contains the source code of the program you are simulating. All lines that contain executable code have a yellow point in the left margin.

You can set a breakpoint on these lines by selecting the line and pressing F9.

By holding the mouse cursor over a variable name, the value of the variable is shown in the status bar.

If you select a variable, and press ENTER, it will be added to the Variable window.

In order to use the function keys (F8 for stepping for example), the focus must be set to the Source Window.

In version 2083, the simulator source window will have the same fonts as the editor window. The source window is read only. You an not change the source code in the simulator!

A blue arrow will show the line that will be executed next.

When you right click a menu will be shown with the following options:

![sim_source_popup](sim_source_popup.png)

Option | Description  
---|---  
Run (F5) | Run code.  
Step /Pause (F8) | Step through code or pause running code  
Step Over (SHIFT+F8) | Step code but step over sub routines and functions..  
Run To (F10) | Run to the current line. This line should have a yellow dot(contains executable code)  
Goto Line (ALT+G). | This option let you chose a line to jump to. Use this with care since it will jump right to the code. This means that some parts of your code are not executed.   
Clear All Breakpoints | This option clears all breakpoints set with F9.  
Toggle breakpoint (F9) | This option will toggle a break point. It will only work on a line with executable code.  
Find (CTRL+F) | Option to find text, similar to the function in the source editor  
Find Next (F3) | Option to find next instance similar to the function in the source editor.  
Show Registers | Option to show/hide internal registers R0-R31  
Show IO | Option to show/hide IO registers  
Show Memory  | Option to show/hide memory content for SRAM and EEPROM  
Log Terminal output | This option let you select a file name for the simulator output log file.  
Clear EEPROM | This option will reset the EEPROM content to empty(FF). This is required sometimes since between sessions the EEPROM content is saved in an EEP file when this option is checked in Options, Simulator, Save EEPROM state. And when you restart simulation the EEP content is read. This option will clear the content.   
  
The hardware simulator.

By pressing the hardware simulation button ![BASC0055](basc0055.gif)the windows shown below will be displayed.

![BASC0056](basc0056.gif)

The top section is a virtual LCD display. It works to display code in PIN mode, and bus mode. For bus mode, only the 8-bit bus mode is supported by the simulator.

Below the LCD display area are LED bars which give a visual indication of the ports.

By clicking an LED it will toggle.

PA means PORTA, PB means PORTB, etc.

IA means PINA, IB means PINB etc. (Shows the value of the Input pins)

It depends on the kind of microprocessor you have selected, as to which ports will be shown.

Right beside the PIN led's, there is a track bar. This bar can be used to simulate the input voltage applied the ADC converter. Note that not all chips have an AD converter. You can set a value for each channel by selecting the desired channel below the track bar.

Next to the track bar is a numeric keypad. This keypad can be used to simulate the GETKBD() function.

When you simulate the Keyboard, it is important that you press/click the keyboard button before simulating the getkbd() line !!!

To simulate the Comparator, specify the comparator input voltage level using Comparator IN0.

Enable Real Hardware Simulation

By clicking the ![BASC0057](basc0057.gif)button you can simulate the actual processor ports in-circuit!

The processor chip used must have a serial port.

In order simulate real hardware you must compile the basmon.bas file.

To do this, follow this example:

Lets say you have the DT006 simmstick, and you are using a 2313 AVR chip.

Open the basmon.bas file and change the line $REGFILE = "xxx" to $REGFILE = "2313def.dat"

Now compile the program and program the chip.

It is best to set the lock bits so the monitor does not get overwritten if you accidentally press F4.

The real hardware simulation only works when the target micro system has a serial port. Most have and so does the DT006.

Connect a cable between the COM port of your PC and the DT006. You probably already have one connected. Normally it is used to send data to the terminal emulator with the PRINT statement.

The monitor program is compiled for 19200 baud. The Options Communication settings must be set to the same baud rate!

The same settings for the monitor program are used for the Terminal emulator, so select the COM port, and the baud rate of 19200.

Power up or reset the DT006. It probably already is powered since you just previously compiled the basmon.bas program and stored it in the 2313.

When you press the real hardware simulation button now the simulator will send and receive data when a port, pin or DDR register is changed.

This allows you to simulate an attached hardware LCD display for example, or something simpler, like an LED. In the SAMPLES dir, you will find the program DT006. You can compile the program and press F2.

When you step through the program the LED's will change!

All statements can be simulated this way but they have to be able to use static timing. Which means that 1-wire will not work because it depends on timing. I2C has a static bus and thus will work.

NOTE: It is important that when you finish your simulation sessions that you click the button again to disable the Real hardware simulation.

When the program hangs it probably means that something went wrong with the serial communication. The only way to escape is to press the Real hardware Simulation ![image1764821748](image1764821748.jpg)button again.

The Real Hardware Simulation is a cost effective way to test attached hardware.

![notice](notice.jpg) The refresh variables button will refresh all variables during a run(F5). When you use the hardware simulator, the LEDS will only update their state when you have enabled this option. Note that using this option will slow down the simulation.

Watchdog Simulation

Most AVR chips have an internal Watchdog. This Watchdog timer is clocked from an internal oscillator. The frequency is approximately 1 MHz. Voltage and temperature variations can have an impact on the WD timer. It is not a very precise timer. So some tolerance is needed when you refresh/reset the WD-timer. The Simulator will warn you when a WD overflow will occur. But only when you have enabled the WD timer.

The status bar

![simulator_sttausbar](simulator_sttausbar.png)

The status bar shows the PC (program counter) and the number of cycles. You can reset the cycles by positioning the mouse cursor on the status bar and then right click. You will then get a pop up menu with the option to reset the cycles. You can also double click the cycles to reset it to 0.

You can use this to determine how much time a program statement takes.

```vb
Do not jump to a conclusion too quick, the time shown might also depend on the value of a variable.

For example, with WAITMS var this might be obvious, but with the division of a value the time might vary too.

```
Start Simulation

To start a simulation the program need to be compiled. So typically you press F7 to compile your code. Make sure that the BIN, DBG and OBJ files are created (Options, Compiler, Output).

When the code is compiled without errors, you can simulate your project. To do so press F2.

By default the simulator is in STOP mode. The status bar will show PC = 0 (program counter) and Cycles = 0. Some instructions use more cycles than other. A NOP for example takes 1 cycle. When the processor has an oscillator running on 8 MHz, and the 8 DIV fuse is set, it means the processor will have a clock of 1 MHz. Meaning that each second, 1 million cycles can be executed. So you could execute a million NOP instructions in 1 second. 

The simulator however is not able to do so. The simulator reads the object data, and decodes the data and simulates the instructions and the hardware. Also, the software need to give time to windows otherwise the code will stall windows and your other programs. 

When the AVR is initialized, the RAM is cleared. This will takes time. So when you press F8 the first time, you will notice that the blue arrow will be visible on the first line of the main project. It depends on the used processor how long it will take till the initialization is done. When done, the simulator will go into PAUSE mode. 

Press F8 again to step through the code. You will notice that the blue arrow will jump only to code with a yellow dot which indicates that the line contains executable code.

DIM statements for example are important for the compiler but do not create code. So these statements will be skipped.

Using the BREAK instruction you can pause the simulator. This is a good way when instead of F8, you use F5 to RUN the code. You can also set a break point using F9. This will be visible with a red dot.

![sim_run2](sim_run2.png)

When your code uses INC modules, the simulator will show the name of the current module.