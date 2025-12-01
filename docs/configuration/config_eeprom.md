# CONFIG EEPROM

Action

Setup memory mode for EEPROM in XMEGA.

Syntax

CONFIG EEPROM=mode

Remarks

mode | MAPPED, or QUICK. In Xmega, the EEPROM can be mapped into memory so it can be used with pointer operations such as LD,ST,LDS and STS. When EEPROM is mapped, EEPROM memory will start at &H1000. The advantage of mapping the EEPROM is that reading the EEPROM becomes much more simpler.  When you use the BASCOM EEPROM routines, you must include this statement before you use the EEPROM. To maintain compatibility with code and other AVR chips you can still use address 0 for the EEPROM. The library will add an offset of &H1000 to the address.  When you use the QUICK mode, you also use mapped mode but for read operations, the library read routine will not be used but instead the address is internally increased with &H1000 and a normal pointer operation is used. This allows code like : If SomeEEPROMvar = 10000 Then  End If  
---|---  
  
See also

[Memory usage](memory_usage.md)

Example

Config Eeprom = Mapped