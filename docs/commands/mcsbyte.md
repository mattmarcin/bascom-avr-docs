# MCSBYTE

The numeric<>string conversion routines are optimized when used for byte, integer,word and longs.

When do you use a conversion routine ?

\- When you use STR() , VAL() or HEX().

\- When you print a numeric variable

\- When you use INPUT on numeric variables.

To support all data types the built in routines are efficient in terms of code size.

But when you use only conversion routines on bytes there is a overhead.

The mcsbyte.lib library is an optimized version that only support bytes.

Use it by including : $LIB "mcsbyte.lbx" in your code.

Note that LBX is a compiled LIB file. In order to change the routines you need the commercial edition with the source code(lib files). After a change you should compile the library with the [library manager](tools_lib_manager.md).

See also

[mcsbyteint.lib](mcsbyteint.md)