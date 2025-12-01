# X10SEND

Action

Sends a house and key code with the X10 protocol.

Syntax

X10SEND house , code

Remarks

House | The house code in the form of a letter A-P. You can use a constant, or you can use a variable  
---|---  
Code | The code or function to send. This is a number between 1-32.  
  
The X10SEND command needs a TW-523 interface.

Only ground, TX and Zero Cross, needs to be connected for transmission.

Use CONFIG X10 to specify the pins.

X10 is a popular protocol used to control equipment via the mains. A 110 KHz signal is added to the normal 50/60 Hz , 220/110 V power.

Notice that experimenting with 110V-240V can be very dangerous when you do not know exactly what you are doing !!!

In the US, X10 is very popular and wide spread. In Europe it is hard to get a TW-523 for 220/230/240 V.

I modified an 110V version so it worked for 220V. On the Internet you can find modification information. But as noticed before, MODIFY ONLY WHEN YOU UNDERSTAND WHAT YOU ARE DOING.

A bad modified device could result in a fire, and your insurance will most likely not pay. A modified device will not pass any CE, or other test.

When the TW-523 is connected to the mains and you use the X10SEND command, you will notice that the LED on the TW-523 will blink.

The following table lists all X10 codes.

Code value | Description  
---|---  
1-16 | Used to address a unit. X10 can use a maximum of 16 units per house code.  
17 | All units off  
18 | All lights on  
19 | ON  
20 | OFF  
21 | DIM  
22 | BRIGHT  
23 | All lights off  
24 | Extended ode  
25 | Hail request  
26 | Hail acknowledge  
27 | Preset dim  
28 | Preset dim  
29 | Extended data analog  
30 | Status on  
31 | Status off  
32 | Status request  
  
At www.x10.com you can find all X10 information. The intension of BASCOM is not to learn you everything about X10, but to show you how you can use it with BASCOM.

See also

[CONFIG X10](config_x10.md) , [X10DETECT](x10detect.md) , [X10SEND](x10send.md)

Example

See [X10DETECT](x10detect.md)