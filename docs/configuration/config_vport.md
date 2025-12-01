# CONFIG VPORT

Action

Maps an XMEGA port to a virtual port.

Syntax

CONFIG VPORT0 = port [, VPORT1=port, VPORT2=port, VPORT3=port]

Remarks

VPORT | There are 4 virtual port registers. When setting up these registers, you need to use VPORTx, where X is 0,1,2 or 3, indicating the virtual port. The virtual port itself is accesed via it's registers PORTy, PINy and DDRy where Y is a 0,1 ,2 or 3.  The normal ports have named like PORTA, PORTB, etc. A virtual port will access the same port but using a different register.  
---|---  
port | The last letter of the real port name. For example A for PORTA, B for PORTB, C for PORTC etc.  
  
![notice](notice.jpg)You must specify multiple virtual ports on one CONFIG line. You should not split up the lines in multiple statements because a new CONFIG VPORT will write a new value, erasing the previous setting. When you need to configure 2 virtual ports, put them on one config line like : Config VPort0 = D , VPort1 = E

When you split the command like :

```vb
Config VPort0 = D 

Config VPort1 = E

```
The second config will erase the setting of the first config. 

![notice](notice.jpg)Some processors like the ones from the E5 series have a fixed relation. These chips have virtual port registers (port,ddr,pin) and do not need a CONFIG VPORT).For the E5 this relation is :

PORT0 - Virtual port A

PORT1 - Virtual port C

PORT2 - Virtual port D

PORT3 - Virtual port R

All ports in the Xmega are located in the extended address area. This space can only be accessed with instructions like LDS,STS, LD and ST.

Special bit instructions only work on the lower IO-registers. 

Xmega example :

again:

Lds r24, PINA ; read port input value

sbrs r24,7 ; skip next instruction if bit 7 is set (1)

rjmp again ; try again

Now the same code for a normal AVR

again:

sbis PINA,7 ; skip if pina.7 is set

rjmp again

Not only less code is required, but the LDS takes 3 cycles

With the virtual mapping, you can access any PORT register (PORT,PIN and DDR) via it's virtual name PORT0, PIN0 or DDR0.

Since there are 4 virtual mapping registers, you can define PORT0, PORT1, PORT2 and PORT3.

When you write to PORTn, the compiler can use the smaller/quicker code. 

Devices like graphical LCD can benefit from this. 

XTINY

Xtiny also have virtual port registers. And these are fixed as well. There is no config required. The benefit of the virtual port is again that it is located in lower memory so shorter/faster assembly instructions are possible.

We would recommend to use the virtual port names. 

See Also

[CONFIG PORT](config_port.md)

Example

```vb
'-----------------------------------------------------------------  
' (c) 1995-2025, MCS  
' Mapping Real Ports to Virtual Ports.bas  
' This sample demonstrates mapping ports to virtual ports  
' based on MAK3's sample  
'-----------------------------------------------------------------  
  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 40  
$framesize = 40  
  
'include the following lib and code, the routines will be replaced since they are a workaround  
$lib "xmega.lib"  
$external _xmegafix_clear  
$external _xmegafix_rol_r1014  
  
'first enable the osc of your choice  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
  
Print "Map VPorts"  
'map portD to virtual port0, map portE to virtual port1, map portC to virtual port2  
'map portR to virtual port 3  
Config VPort0 = D , VPort1 = E , VPort2 = C , VPort3 = R  
  
'Each virtual port is available as PORT0, PORT1, PORT2 and PORT3  
' data direct is available as DDR0 , DDR1, DDR2 and DDR3  
' PIN input is available as PIN0 , PIN1, PIN2 and PIN3  
  
'The advantage of virtual port registers is that shorter asm instruction can be used which also use only 1 cycle  
Dim Var As Byte  
  
  
'Real Port Direction  
```
Ddr1 = &B0000_0000 ' Port E = INPUT  
Ddr0 = &B1111_1111 ' Port D = OUTPUT  
  
  
```vb
'Continously copy the value from PORTE to PORTD using the virtual ports.  
Do  
```
Var = Pin1 'Read Virtual Port 0  
Port0 = Var 'Write Virtual Port 1  
```vb
Loop  
  
End 'end program

```