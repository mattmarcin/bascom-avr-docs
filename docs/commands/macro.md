# MACRO

Action

This statement allow you to define a Macro.

Syntax

MACRO name

macrodef

END MACRO

Remarks

name | The name of the macro. Each macro need to have a unique name.  
---|---  
macrodef | The code you want to have inserted when you use the macro.  
  
Macro's must be defined before they can be used. When a macro is defined but not used in your code, it will not be compiled. You can use $INCLUDE to include a large number of macro's.

When the compiler encounters the name of a defined macro, it will insert the defined code at that place. While it looks similar to a sub routine, there are differences. A sub routine for example is called and has a RETURN(RET).

See also

[SUB](sub.md) , [GOSUB](gosub.md)

Example

Macro Usb_reset_data_toggle

Ueconx.rstdt = 1

End Macro

Macro Usb_disable_stall_handshake

Ueconx.stallrqc = 1

End Macro

Macro Set_power_down_mode

Smcr = 0

Smcr = Bits(se , Sm1)

sleep

End Macro

Usb_reset_data_toggle ' this will insert UECONRX.RSTD=1

Set_power_down_mode ' this will insert the following code

Smcr = 0

Smcr = Bits(se , Sm1)

sleep