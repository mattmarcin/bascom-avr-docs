# Options Compiler Communication

![options_compiler_com](options_compiler_com.png)

Options Compiler Communication

Item | Description  
---|---  
Baud rate | Selects the baud rate for the serial communication statements. You can also type in a new baud rate. It is advised to use [$BAUD](baud_1.md) in the source code which overrides this setting.  
Frequency | Select the frequency of the used crystal. You can also type in a new frequency. It is advised to use [$CRYSTAL](crystal_1.md) in the source code which overrides this setting. Settings in source code are preferred since it is more clear.  
  
The settings for the internal hardware UART are:

No parity , 8 data bits , 1 stop bit

Some AVR chips have the option to specify different data bits and different stop bits and parity.

Note that these settings must match the settings of the terminal emulator. In the simulator the output is always shown correct since the baud rate is not taken in consideration during simulation. With real hardware when you print data at 9600 baud, the terminal emulator will show weird characters when not set to the same baud rate, in this example, to 9600 baud.