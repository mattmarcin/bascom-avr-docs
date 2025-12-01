# CONFIG EXTENDED_PORT

Action

Configures compiler to generate warning or error when transforming extended port register.

Syntax

CONFIG EXTENDED_PORT = WARNING|ERROR

Remarks

A lot of AVR chips have so called extended registers. When the AVR was designed the designers did not set aside enough space for the hardware registers. A number of instructions work only with the lower 32 addresses, and a number only work on registers with an address till &H3F.

SRAM memory was moved up and the space after &H5F was used for registers. These are extended registers.

For these chips, the SRAM starts at &H100 or higher. 

Because INP, OUT, SBI, SBI, SBIC, SBIS, etc. will not work on these extended registers, the compiler changes this automatic when needed. When INP or OUT is used, this is not a problem. LDS or STS can be used with the same register.

But an instruction like SBIC that will test a pin , needs a temporarily register. Register R23 is used for this.

When you write your own ASM you might want to get a warning or an error. For this purpose you can use CONFIG EXTENDED_PORT.

When you use WARNING there will be a warning in the report file. When you use ERROR, you will get an error and your code will not compile.

See also

NONE