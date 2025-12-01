# Options Compiler LCD

![image632224065](image632224065.jpg)

Options Compiler LCD

Item | Description  
---|---  
LCD type | The LCD display used.  
Bus mode | The LCD can be operated in BUS mode or in PIN mode. In PIN mode, the data lines of the LCD are connected to the processor port pins. In BUS mode the data lines of the LCD are connected to the data lines of the BUS. Select 4 when you have only connect DB4-DB7. When the data mode is 'pin' , you should select 4.  
Data mode | Select the mode in which the LCD is operating. In PIN mode, individual processor pins can be used to drive the LCD. In BUS mode, the external data bus is used to drive the LCD.  
LCD address | In BUS mode you must specify which address will select the enable line of the LCD display. For the STK200, this is C000 = A14 + A15.  
RS address | In BUS mode you must specify which address will select the RS line of the LCD display. For the STK200, this is 8000 = A15  
Enable | For PIN mode, you must select the processor pin that is connected to the enable line of the LCD display.  
RS | For PIN mode, you must select the processor pin that is connected to the RS line of the LCD display.  
DB7-DB4 | For PIN mode, you must select the processor pins that are connected to the upper four data lines of the LCD display.  
Make upper 3 bits high in LCD designer | Some displays require that for setting custom characters, the upper 3 bits must be 1. Should not be used by default.  
  
It is advised to use the CONFIG LCD command. This way the settings are stored in your source code and not in the separate CFG file.