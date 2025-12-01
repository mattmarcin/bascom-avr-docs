# $DBG

Action

Enables debugging output to the hardware UART.

Syntax

$DBG

Remarks

Calculating the hardware, software and frame space can be a difficult task.

With $DBG the compiler will insert characters for the various spaces.

To the Frame space 'F' will be written. When you have a frame size of 4, FFFF will be written.

To the Hardware space 'H' will be written. If you have a hardware stack space of 8, HHHHHHHH will be written to this space.

To the software space 'S' will be written. If you have a software stack space of 6, SSSSSS will be written.

The idea is that when a character is overwritten, it is being used. So by watching these spaces you can determine if the space is used or not.

With the DBG statement a record is written to the HW UART. The record must be logged to a file so it can be analyzed by the stack analyzer.

Make the following steps to determine the proper values:

•| Make the frame space 40, the soft stack 20 and the HW stack 50  
---|---  
  
•| Add $DBG to the top of your program  
---|---  
  
•| Add a DBG statement to every Subroutine or Function  
---|---  
  
•| Open the terminal emulator and open a new log file. By default it will have the name of your current program with the .log extension  
---|---  
  
•| Run your program and notice that it will dump information to the terminal emulator  
---|---  
  
•| When your program has executed all sub modules or options you have build in, turn off the file logging and turn off the program  
---|---  
  
•| Choose the Tools Stack analyzer option  
---|---  
  
•| A window will be shown with the data from the log file  
---|---  
  
•| Press the Advise button that will determine the needed space. Make sure that there is at least one H, S and F in the data. Otherwise it means that all the data is overwritten and that you need to increase the size.  
---|---  
  
•| Press the Use button to use the advised settings.  
---|---  
  
As an alternative you can watch the space in the simulator and determine if the characters are overwritten or not.

The DBG statement will assign an internal variable named ___SUBROUTINE

Because the name of a SUB or Function may be 32 long, this variable uses 33 bytes!

___SUBROUTINE will be assigned with the name of the current SUB or FUNCTION.

When you first run a SUB named Test1234 it will be assigned with Test1234

When the next DBG statement is in a SUB named Test, it will be assigned with Test.

The 234 will still be there so it will be shown in the log file.

![tool_stack](tool_stack.gif)

Every DBG record will be shown as a row.

The columns are:

Column | Description  
---|---  
Sub | Name of the sub or function from where the DBG was used  
FS | Used frame space  
SS | Used software stack space  
HS | Used hardware stack space  
Frame space | Frame space  
Soft stack | Soft stack space  
HW stack | Hardware stack space  
  
The Frame space is used to store temp and local variables.

It also stores the variables that are passed to subs/functions by value.

Because PRINT , INPUT and the FP num<>String conversion routines require a buffer, the compiler always is using 24 bytes of frame space.

When the advise is to use 2 bytes of frame space, the setting will be 24+2=26.

For example when you use : print var, var need to be converted into a string before it can be printed or shown with LCD.

An alternative for the buffer would be to setup a temp buffer and free it once finished. This gives more code overhead.

In older version of BASCOM the start of the frame was used for the buffer but that gave conflicts when variables were printed from an ISR.

See also

[DBG](dbg.md)