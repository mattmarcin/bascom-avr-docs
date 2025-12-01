# INITLCD

Action

Initializes the LCD display.

Syntax

INITLCD

Remarks

The LCD display is initialized automatic at start up when LCD statements are used by your code.

This is done by a call to _LCD_INIT.

If you include the INITLCD statement in your code, the automatic call is disabled and the _LCD_INIT is called at the place in your code where you put the INITLCD statement. (initlcd is translated into a call to _init_lcd).

Why is this useful? 

•| In an environments with static electricity, the display can give strange output.  
---|---  
  
You can initialize the display then once in a while. When the display is initialized, the display content is cleared also.

•| The LCD routines depend on the fact that the WR pin of the LCD is connected to ground. But when you connect it to a port pin, you must first set the logic level to 0 and after that you can initialize the display by using INITLCD  
---|---  
  
•| Xmega chips need a stable oscillator. This is done with some CONFIG statements. The INITLCD should be placed after these commands. And since the Xmega by default has a slow internal oscillator, without using INITLCD at the proper location, your application would start slow. See the explanation below.  
---|---  
  
•| So in short you have more control when the LCD is initialized.  
---|---  
  
![notice](notice.jpg)The [CONFIG LCDPIN](config_lcdpin.md) has an option to use the WR pin, and use the busy flag of the display. If you have enough pins, this is the best mode. 

![notice](notice.jpg)The XMEGA has a built in internal oscillator that runs at a relative slow speed. If your code sets the speed to 32 MHz and you also include the $crystal=32000000 directive, you will notice a delay in the start of the code. This is caused by the fact that the delay routines are calculated with the 32 Mhz frequency, but the actual oscillator speed is 1 or 2 MHz.

There are 2 solutions possible. 

\- you can use $crystal=1000000 and then after you have set up the clock speed with CONFIG OSC, you can use another $CRYSTAL directive with the new speed.

\- you use $INITMICRO and put the CONFIG OSC in the _INIT_MICRO code. This will ensure that the micro will run at the specified speed early as possible.

ASM

The generated ASM code :

Rcall _Init_LCD

See also

[LCD](lcd_1.md) , [CONFIG LCDPIN](config_lcdpin.md)

Example

NONE