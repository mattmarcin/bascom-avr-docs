# $ASM

Action

Start of inline assembly code block.

Syntax

$ASM

Remarks

Use $ASM together with $END ASM to insert a block of assembler code in your BASIC code. You can also precede each line with the ! sign.

See also the chapter [Mixing BASIC and Assembly](mixing_asm_and_basic.md) and [assembler mnemonics](assembler_mnemonics.md)

Example

Dim C As Byte

Loadadr C , X 'load address of variable C into register X

$asm

Ldi R24,1 ; load register R24 with the constant 1

St X,R24 ; store 1 into variable c

```vb
$end Asm

Print C

End

```