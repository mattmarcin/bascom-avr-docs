# GETATKBDRAW

Action

Reads a key from a PC AT keyboard.

Syntax

var = GETATKBDRAW()

Remarks

var | The variable that is assigned with the key read from the keyboard. It may be a byte or a string variable. When no key is pressed a 0 will be returned.  
---|---  
  
The GETATKBDRAW() function needs 2 input pins and a translation table for the keys. You can read more about this at the [CONFIG KEYBOARD](config_keyboard.md) compiler directive.

The GetatkbdRAW function will return RAW data from a PS/2 keyboard or Mouse.

While GetatKBD is intended to wait for pressed keys, GetATkbdRAW just returns raw PS/2 data so you can use your own code to process the data.

See Also

[GETATKBD](getatkbd.md) , [CONFIG KEYBOARD](config_keyboard.md)

Example

See GETATKBD.BAS