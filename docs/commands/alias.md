# ALIAS

Action

Indicates that the variable can be referenced with another name.

Syntax

newvar ALIAS oldvar

Remarks

oldvar | Name of the variable such as PORTB.1  
---|---  
newvar | New name of the variable such as direction  
  
Aliasing port pins can give the pin names a more meaningful name. For example, when your program uses 4 different pins to control 4 different relays, you could name them portb.1, portb.2, portb.3 and portb.4.

But it would be more convenient to refer to them as relais1, relais2, relais3 and realais4.

When you later on change your PCB and decide that relays 4 must be connected to portD.4 instead of portb.4, you only need to change the ALIAS line, and not your whole program.

See also

[CONST](const.md)

Example

```vb
'-------------------------------------------------------------------------------

'copyright : (c) 1995-2025, MCS Electronics

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'purpose : demonstrates ALIAS

'-------------------------------------------------------------------------------

$regfile = "m48def.dat"

$crystal = 4000000 ' 4 MHz crystal

```
Const On = 1

Const Off = 0

Config Portb = Output

Relais1 Alias Portb.1

Relais2 Alias Portb.2

Relais3 Alias Portd.5

Relais4 Alias Portd.2

Set Relais1

Relais2 = 0

Relais3 = On

Relais4 = Off

End