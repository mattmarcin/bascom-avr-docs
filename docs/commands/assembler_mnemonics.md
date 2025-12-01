# Assembler mnemonics

BASCOM supports the mnemonics as defined by Atmel.

The Assembler accepts mnemonic instructions from the instruction set.

A summary of the instruction set mnemonics and their parameters is given here. For a detailed description of the Instruction set, refer to the AVR Data Book.

Mnemonics | Operands | Description | Operation | Flags | Clock  
---|---|---|---|---|---  
ARITHMETIC AND LOGIC INSTRUCTIONS |  |  |  |  |   
ADD | Rd, Rr | Add without Carry | Rd = Rd + Rr | Z,C,N,V,H | 1  
ADC | Rd, Rr | Add with Carry | Rd = Rd + Rr + C | Z,C,N,V,H | 1  
SUB | Rd, Rr | Subtract without Carry | Rd = Rd â Rr | Z,C,N,V,H | 1  
SUBI | Rd, K | Subtract Immediate | Rd = Rd â K | Z,C,N,V,H | 1  
SBC | Rd, Rr | Subtract with Carry | Rd = Rd - Rr - C | Z,C,N,V,H | 1  
SBCI | Rd, K | Subtract Immediate with Carry | Rd = Rd - K - C | Z,C,N,V,H | 1  
AND | Rd, Rr | Logical AND | Rd = Rd Â· Rr | Z,N,V | 1  
ANDI | Rd, K | Logical AND with Immediate | Rd = Rd Â· K | Z,N,V | 1  
OR | Rd, Rr | Logical OR | Rd = Rd v Rr | Z,N,V | 1  
ORI | Rd, K | Logical OR with Immediate | Rd = Rd v K | Z,N,V | 1  
EOR | Rd, Rr | Exclusive OR | Rd = Rd Ã Rr | Z,N,V | 1  
COM | Rd | Ones Complement | Rd = $FF - Rd | Z,C,N,V | 1  
NEG | Rd | Twos Complement | Rd = $00 - Rd | Z,C,N,V,H | 1  
SBR | Rd,K | Set Bit(s) in Register | Rd = Rd v K | Z,N,V | 1  
CBR | Rd,K | Clear Bit(s) in Register | Rd = Rd Â· ($FFh - K) | Z,N,V | 1  
INC | Rd | Increment | Rd = Rd + 1 | Z,N,V | 1  
DEC | Rd | Decrement | Rd = Rd - 1 | Z,N,V | 1  
TST | Rd | Test for Zero or Minus | Rd = Rd Â· Rd | Z,N,V | 1  
CLR | Rd | Clear Register | Rd = Rd Ã Rd | Z,N,V | 1  
SER | Rd | Set Register | Rd = $FF | None | 1  
ADIW Adiw r24, K6 | Rdl, K6 | Add Immediate to Word | Rdh:Rdl = Rdh:Rdl + K | Z,C,N,V,S | 2  
SBIW Sbiw R24,K6 | Rdl, K6 | Subtract Immediate from Word | Rdh:Rdl = Rdh:Rdl - K | Z,C,N,V,S | 2  
MUL | Rd,Rr | Multiply Unsigned | R1, R0 = Rd * Rr | C | 2 *  
BRANCH INSTRUCTIONS |  |  |  |  |   
RJMP | K | Relative Jump | PC = PC + k + 1 | None | 2  
IJMP |  | Indirect Jump to (Z) | PC = Z | None | 2  
JMP | K | Jump | PC = k | None | 3  
RCALL | K | Relative Call Subroutine | PC = PC + k + 1 | None | 3  
ICALL |  | Indirect Call to (Z) | PC = Z | None | 3  
CALL | K | Call Subroutine | PC = k | None | 4  
RET |  | Subroutine Return | PC = STACK | None | 4  
RETI |  | Interrupt Return | PC = STACK | I | 4  
CPSE | Rd,Rr | Compare, Skip if Equal | if (Rd = Rr) PC = PC + 2 or 3 | None | 1 / 2  
CP | Rd,Rr | Compare | Rd - Rr | Z,C,N,V,H, | 1  
CPC | Rd,Rr | Compare with Carry | Rd - Rr - C | Z,C,N,V,H | 1  
CPI | Rd,K | Compare with Immediate | Rd - K | Z,C,N,V,H | 1  
SBRC | Rr, b | Skip if Bit in Register Cleared | If (Rr(b)=0) PC = PC + 2 or 3 | None | 1 / 2  
SBRS | Rr, b | Skip if Bit in Register Set | If (Rr(b)=1) PC = PC + 2 or 3 | None | 1 / 2  
SBIC | P, b | Skip if Bit in I/O Register Cleared | If(I/O(P,b)=0) PC = PC + 2 or 3 | None | 2 / 3  
SBIS | P, b | Skip if Bit in I/O Register Set | If(I/O(P,b)=1) PC = PC + 2 or 3 | None | 2 / 3  
BRBS | s, k | Branch if Status Flag Set | if (SREG(s) = 1) then PC=PC+k + 1 | None | 1 / 2  
BRBC | s, k | Branch if Status Flag Cleared | if (SREG(s) = 0) then PC=PC+k + 1 | None | 1 / 2  
BREQ | K | Branch if Equal | if (Z = 1) then PC = PC + k + 1 | None | 1 / 2  
BRNE | K | Branch if Not Equal | if (Z = 0) then PC = PC + k + 1 | None | 1 / 2  
BRCS | K | Branch if Carry Set | if (C = 1) then PC = PC + k + 1 | None | 1 / 2  
BRCC | K | Branch if Carry Cleared | if (C = 0) then PC = PC + k + 1 | None | 1 / 2  
BRSH | K | Branch if Same or Higher | if (C = 0) then PC = PC + k + 1 | None | 1 / 2  
BRLO | K | Branch if Lower | if (C = 1) then PC = PC + k + 1 | None | 1 / 2  
BRMI | K | Branch if Minus | if (N = 1) then PC = PC + k + 1 | None | 1 / 2  
BRPL | K | Branch if Plus | if (N = 0) then PC = PC + k + 1 | None | 1 / 2  
BRGE | K | Branch if Greater or Equal, Signed | if (N V= 0) then PC = PC+ k + 1 | None | 1 / 2  
BRLT | K | Branch if Less Than, Signed | if (N V= 1) then PC = PC + k + 1 | None | 1 / 2  
BRHS | K | Branch if Half Carry Flag Set | if (H = 1) then PC = PC + k + 1 | None | 1 / 2  
BRHC | K | Branch if Half Carry Flag Cleared | if (H = 0) then PC = PC + k + 1 | None | 1 / 2  
BRTS | K | Branch if T Flag Set | if (T = 1) then PC = PC + k + 1 | None | 1 / 2  
BRTC | K | Branch if T Flag Cleared | if (T = 0) then PC = PC + k + 1 | None | 1 / 2  
BRVS | K | Branch if Overflow Flag is Set | if (V = 1) then PC = PC + k + 1 | None | 1 / 2  
BRVC | K | Branch if Overflow Flag is Cleared | if (V = 0) then PC = PC + k + 1 | None | 1 / 2  
BRIE | K | Branch if Interrupt Enabled | if ( I = 1) then PC = PC + k + 1 | None | 1 / 2  
BRID | K | Branch if Interrupt Disabled | if ( I = 0) then PC = PC + k + 1 | None | 1 / 2  
DATA TRANSFER INSTRUCTIONS |  |  |  |  |   
MOV | Rd, Rr | Copy Register | Rd = Rr | None | 1  
LDI | Rd, K | Load Immediate | Rd = K | None | 1  
LDS | Rd, k | Load Direct | Rd = (k) | None | 2  
LD | Rd, X | Load Indirect | Rd = (X) | None | 2  
LD | Rd, X+ | Load Indirect and Post-Increment | Rd = (X), X = X + 1 | None | 2  
LD | Rd, -X | Load Indirect and Pre-Decrement | X = X - 1, Rd =(X) | None | 2  
LD | Rd, Y | Load Indirect | Rd = (Y) | None | 2  
LD | Rd, Y+ | Load Indirect and Post-Increment | Rd = (Y), Y = Y + 1 | None | 2  
LD | Rd, -Y | Load Indirect and Pre-Decrement | Y = Y - 1, Rd = (Y) | None | 2  
LDD | Rd,Y+q | Load Indirect with Displacement | Rd = (Y + q) | None | 2  
LD | Rd, Z | Load Indirect | Rd = (Z) | None | 2  
LD | Rd, Z+ | Load Indirect and Post-Increment | Rd = (Z), Z = Z+1 | None | 2  
LD | Rd, -Z | Load Indirect and Pre-Decrement | Z = Z - 1, Rd = (Z) | None | 2  
LDD | Rd, Z+q | Load Indirect with Displacement | Rd = (Z + q) | None | 2  
STS | k, Rr | Store Direct | (k) = Rr | None | 2  
ST | X, Rr | Store Indirect | (X) = Rr | None | 2  
ST | X+, Rr | Store Indirect and Post-Increment | (X) = Rr, X = X + 1 | None | 2  
ST | -X, Rr | Store Indirect and Pre-Decrement | X = X - 1, (X) = Rr | None | 2  
ST | Y, Rr | Store Indirect | (Y) = Rr | None | 2  
ST | Y+, Rr | Store Indirect and Post-Increment | (Y) = Rr, Y = Y + 1 | None | 2  
ST | -Y, Rr | Store Indirect and Pre-Decrement | Y = Y - 1, (Y) = Rr | None | 2  
STD | Y+q,Rr | Store Indirect with Displacement | (Y + q) = Rr | None | 2  
ST | Z, Rr | Store Indirect | (Z) = Rr | None | 2  
ST | Z+, Rr | Store Indirect and Post-Increment | (Z) = Rr, Z = Z + 1 | None | 2  
ST | -Z, Rr | Store Indirect and Pre-Decrement | Z = Z - 1, (Z) = Rr | None | 2  
STD | Z+q,Rr | Store Indirect with Displacement | (Z + q) = Rr | None | 2  
LPM |  | Load Program Memory | R0 =(Z) | None | 3  
IN | Rd, P | In Port | Rd = P | None | 1  
OUT | P, Rr | Out Port | P = Rr | None | 1  
PUSH | Rr | Push Register on Stack | STACK = Rr | None | 2  
POP | Rd | Pop Register from Stack | Rd = STACK | None | 2  
BIT AND BIT-TEST INSTRUCTIONS |  |  |  |  |   
LSL | Rd | Logical Shift Left | Rd(n+1) =Rd(n),Rd(0)= 0,C=Rd(7) | Z,C,N,V,H | 1  
LSR | Rd | Logical Shift Right | Rd(n) = Rd(n+1), Rd(7) =0, C=Rd(0) | Z,C,N,V | 1  
ROL | Rd | Rotate Left Through Carry | Rd(0) =C, Rd(n+1) =Rd(n),C=Rd(7) | Z,C,N,V,H | 1  
ROR | Rd | Rotate Right Through Carry | Rd(7) =C,Rd(n) =Rd(n+1),CÂ¬Rd(0) | Z,C,N,V | 1  
ASR | Rd | Arithmetic Shift Right | Rd(n) = Rd(n+1), n=0..6 | Z,C,N,V | 1  
SWAP | Rd | Swap Nibbles | Rd(3..0) Â« Rd(7..4) | None | 1  
BSET | S | Flag Set | SREG(s) = 1 | SREG(s) | 1  
BCLR | S | Flag Clear | SREG(s) = 0 | SREG(s) | 1  
SBI | P, b | Set Bit in I/O Register | I/O(P, b) = 1 | None | 2  
CBI | P, b | Clear Bit in I/O Register | I/O(P, b) = 0 | None | 2  
BST | Rr, b | Bit Store from Register to T | T = Rr(b) | T | 1  
BLD | Rd, b | Bit load from T to Register | Rd(b) = T | None | 1  
SEC |  | Set Carry | C = 1 | C | 1  
CLC |  | Clear Carry | C = 0 | C | 1  
SEN |  | Set Negative Flag | N = 1 | N | 1  
CLN |  | Clear Negative Flag | N = 0 | N | 1  
SEZ |  | Set Zero Flag | Z = 1 | Z | 1  
CLZ |  | Clear Zero Flag | Z = 0 | Z | 1  
SEI |  | Global Interrupt Enable | I = 1 | I | 1  
CLI |  | Global Interrupt Disable | I = 0 | I | 1  
SES |  | Set Signed Test Flag | S = 1 | S | 1  
CLS |  | Clear Signed Test Flag | S = 0 | S | 1  
SEV |  | Set Twos Complement Overflow | V = 1 | V | 1  
CLV |  | Clear Twos Complement Overflow | V = 0 | V | 1  
SET |  | Set T in SREG | T = 1 | T | 1  
CLT |  | Clear T in SREG | T = 0 | T | 1  
SHE |  | Set Half Carry Flag in SREG | H = 1 | H | 1  
CLH |  | Clear Half Carry Flag in SREG | H = 0 | H | 1  
NOP |  | No Operation |  | None | 1  
SLEEP |  | Sleep |  | None | 1  
WDR |  | Watchdog Reset |  | None | 1  
  
|  | XMEGA ONLY |  |   
|   
  
LAC |  | Load and clear RAM loc |  | None | 2  
LAT |  | Load and toggle RAM loc |  | None | 2  
LAS |  | Load and set RAM loc |  | None | 2  
XCH |  | Exchange RAM loc |  | None | 2  
  
* ) Not available in base-line microcontrollers

The Assembler is not case sensitive.

The operands have the following forms:

Rd: R0-R31 or R16-R31 (depending on instruction)

Rr: R0-R31

b: Constant (0-7)

s: Constant (0-7)

P: Constant (0-31/63)

K: Constant (0-255)

k: Constant, value range depending on instruction.

q: Constant (0-63)

Rdl: R24, R26, R28, R30. For ADIW and SBIW instructions