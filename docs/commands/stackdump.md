# $STACKDUMP

Action

Makes the compiler hook up the reset vector and includes code, which allows to get a dump of the stack residing in SRAM.

Syntax

$stackdump

Preface

Using $stackdump presumes certain knowledge of assembler code, i.e. reading and understanding disassembled code. On the other hand it's possible that an user, who has little to no experience in assembly reading, simply uses $stackdump, while an assembly-experienced user evaluates the dumped result. This allows sharing of experience, knowledge and active debugging of difficult code via Internet, without having actual hardware available.

Remarks

Additional code in Bascom-Basic is used to put out the content of the saved stack to whatever target, in the provided example code the dump is written to the serial interface, however any other reasonable target for receiving the dump is feasible. For example, a dump can be saved to EEProm also, the user is free to modify the target himself.

Function

After each reset an AVR micrcontroller executes the reset-vector, the $stackdump code hooks this vector and executes a small routine, which saves a certain amount of stack to a protected memory range. This is possible, as SRAM memory keeps its content even after a reset. After saving the stack, a routine is executed which clears SRAM, excluding the previously saved range. In the following it's save to put out the saved stack content by

regular Bascom code. Without $stackdump this can't be done, as a) the stack would be destroyed by normal SRam-clearing code, and b) because every Bascom-code modifies, i.e overwrite the stack itself.

Usage

Stack can contain two types of data, 1) data, i.e. saved registers and 2) return addresses, which were pushed on

the stack by previous calls. The most interesting is the latter, as it can point to faulty code. If followed these

return addresses (which of course needs also some guesswork to distinguish it apart from saved registers), it's

possible to find out interrupting code, and this way difficult to find bugs.

Options

Depending whether the stack pointer is intact at reset, one of the two options can be used:

Ignore_SP = 1

Ignore_SP = 0

If a hard-rest occurs, for example by a watchdog reset, the stack pointer is reset to its default values, and this way can't be used to determine the stack pointers last position. For this case Ignore_SP = 1 is useful.

In this mode the amount of bytes given by Stck_siz_sav beginning from stack end is saved. This can be used for tracking down randomly occurring resets by whatever reasons. Be aware that without knowing the stack pointers last position, it's much harder to find out the last executed call, but it's still possible.

In contrary, if a soft reset occurs, the stack pointer is likely intact and the the option Ignore_SP = 0 is useful.

Here the stack is saved from the stack pointers last position to the amount of Stck_siz_sav bytes till ramend/stack-end. In case ram-end comes first, only the stack range between stack pointer and ram-end is saved.

The method using Ignore_SP = 0 is useful to redirect any interrupt to the reset vector by writing:

```vb
On interrupt_xy my_isr NOSAVE

Enable interrupt_xy

Enable Interrupts

'...

```
my_isr:

!jmp 0

```vb
return

If using an external interrupt, for example INT0 for my_isr, a signal on INT0 will create the stack dump, pointing to code executed at occurrence of the signal. This works like an on-chip hardware debugger. In certain chips a watchdog timer interrupt is available, this interrupt can be used and a watchdog timeout will then create a dump.

```
Notice: Previous mentioned functionality for Ignore_SP = 0 needs enabled interrupts. In case these special, or also global interrupts get disabled by code, it will fail. But also a disabled interrupt can point to the source of a bug. Using Ignore_SP = 1 will work in any case, but with said restrictions.

Closing note

$stackdump can only increase the chance to trap down a nasty bug or do some special type debugging. It's for sure no cure-all type of tool. Because of certain restrictions given by AVR hardware it can't be universal.