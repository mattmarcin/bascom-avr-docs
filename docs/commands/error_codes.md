# Error Codes

The following table lists errors that can occur.

Error | Description  
---|---  
1 | Unknown statement  
2 | Unknown structure EXIT statement  
3 | WHILE expected  
4 | No more space for IRAM BIT  
5 | No more space for BIT  
6 | . expected in filename  
7 | IF THEN expected  
8 | BASIC source file not found  
9 | Maximum 128 aliases allowed  
10 | Unknown LCD type  
11 | INPUT, OUTPUT, 0 or 1 expected  
12 | Unknown CONFIG parameter  
13 | CONST already specified  
14 | Only IRAM bytes supported  
15 | Wrong data type  
16 | Unknown Definition  
17 | 9 parameters expected  
18 | BIT only allowed with IRAM or SRAM  
19 | STRING length expected (DIM S AS STRING * 12 ,for example)  
20 | Unknown DATA TYPE  
21 | Out of IRAM space  
22 | Out of SRAM space  
23 | Out of XRAM space  
24 | Out of EPROM space  
25 | Variable already dimensioned  
26 | AS expected  
27 | parameter expected  
28 | IF THEN expected  
29 | SELECT CASE expected  
30 | BIT's are GLOBAL and can not be erased  
31 | Invalid data type  
32 | Variable not dimensioned  
33 | GLOBAL variable can not be ERASED  
34 | Invalid number of parameters  
35 | 3 parameters expected  
36 | THEN expected  
37 | Invalid comparison operator  
38 | Operation not possible on BITS  
39 | FOR expected  
40 | Variable can not be used with RESET  
41 | Variable can not be used with SET  
42 | Numeric parameter expected  
43 | File not found  
44 | 2 variables expected  
45 | DO expected  
46 | Assignment error  
47 | UNTIL expected  
50 | Value doesn't fit into INTEGER  
51 | Value doesn't fit into WORD  
52 | Value doesn't fit into LONG  
60 | Duplicate label  
61 | Label not found  
62 | SUB or FUNCTION expected first  
63 | Integer or Long expected for ABS()  
64 | , expected  
65 | device was not OPEN  
66 | device already OPENED  
68 | channel expected  
70 | BAUD rate not possible  
71 | Different parameter type passed then declared  
72 | Getclass error. This is an internal error.  
73 | Printing this FUNCTION not yet supported  
74 | 3 parameters expected  
80 | Code does not fit into target chip  
81 | Use HEX(var) instead of PRINTHEX  
82 | Use HEX(var) instead of LCDHEX  
85 | Unknown interrupt source  
86 | Invalid parameter for TIMER configuration  
87 | ALIAS already used  
88 | 0 or 1 expected  
89 | Out of range : must be 1-4  
90 | Address out of bounds  
91 | INPUT, OUTPUT, BINARY, or RANDOM expected  
92 | LEFT or RIGHT expected  
93 | Variable not dimensioned  
94 | Too many bits specified  
95 | Falling or rising expected for edge  
96 | Pre scale value must be 1,8,64,256 or 1024  
97 | SUB or FUNCTION must be DECLARED first  
98 | SET or RESET expected  
99 | TYPE expected  
100 | No array support for IRAM variables  
101 | Can't find HW-register  
102 | Error in internal routine  
103 | = expected  
104 | LoadReg error  
105 | StoreBit error  
106 | Unknown register  
107 | LoadnumValue error  
108 | Unknown directive in device file  
109 | = expected in include file for .EQU  
110 | Include file not found  
111 | SUB or FUNCTION not DECLARED  
112 | SUB/FUNCTION name expected  
113 | SUB/FUNCTION already DECLARED  
114 | LOCAL only allowed in SUB or FUNCTION  
115 | #channel expected  
116 | Invalid register file  
117 | Unknown interrupt  
126 | NEXT expected.  
129 | ( or ) missing.  
200 | .DEF not found  
201 | Low Pointer register expected  
202 | .EQU not found, probably using functions that are not supported by the selected chip  
203 | Error in LD or LDD statement  
204 | Error in ST or STD statement  
205 | } expected  
206 | Library file not found  
207 | Library file already registered  
210 | Bit definition not found  
211 | External routine not found  
212 | LOW LEVEL, RISING or FALLING expected  
213 | String expected for assignment  
214 | Size of XRAM string 0  
215 | Unknown ASM mnemonic  
216 | CONST not defined  
217 | No arrays allowed with BIT/BOOLEAN data type  
218 | Register must be in range from R16-R31  
219 | INT0-INT3 are always low level triggered in the MEGA  
220 | Forward jump out of range  
221 | Backward jump out of range  
222 | Illegal character  
223 | * expected  
224 | Index out of range  
225 | () may not be used with constants  
226 | Numeric of string constant expected  
227 | SRAM start greater than SRAM end  
228 | DATA line must be placed after the END statement  
229 | End Sub or End Function expected  
230 | You can not write to a PIN register  
231 | TO expected  
232 | Not supported for the selected micro  
233 | READ only works for normal DATA lines, not for EPROM data  
234 | ') block comment expected first  
235 | '( block comment expected first  
236 | Value does not fit into byte  
238 | Variable is not dimensioned as an array  
239 | Invalid code sequence because of AVR hardware bug  
240 | END FUNCTION expected  
241 | END SUB expected  
242 | Source variable does not match the target variable  
243 | Bit index out of range for supplied data type  
244 | Do not use the Y pointer  
245 | No arrays supported with IRAM variable  
246 | No more room for .DEF definitions  
247 | . expected  
248 | BYVAL should be used in declaration  
249 | ISR already defined  
250 | GOSUB expected  
251 | Label must be named SECTIC  
252 | Integer or Word expected  
253 | ERAM variable can not be used  
254 | Variable expected  
255 | Z or Z+ expected  
256 | Single expected  
257 | "" expected  
258 | SRAM string expected  
259 | \- not allowed for a byte  
260 | Value larger than string length  
261 | Array expected  
262 | ON or OFF expected  
263 | Array index out of range  
264 | Use ECHO OFF and ECHO ON instead  
265 | offset expected in LDD or STD like Z+1  
266 | TIMER0, TIMER1 or TIMER2 expected  
267 | Numeric constant expected  
268 | Param must be in range from 0-3  
269 | END SELECT expected  
270 | Address already occupied  
322 | Data type not supported with statement  
323 | Label too long  
324 | Chip not supported by I2C slave library  
325 | Pre-scale value must be 1,8,32,128,256 or 1024  
326 | #ENDIF expected  
327 | Maximum size is 255  
328 | Not valid for SW UART  
329 | FileDateTime can only be assigned to a variable  
330 | Maximum value for OUT is &H3F  
332 | $END ASM expected  
334 | ') blockcomment end expected  
335 | Use before DIM statements  
336 | Could not set specified CLOCK value  
337 | No more space for labels  
338 | AS expected  
339 | Bytes to read may not be 0.  
340 | Variable is used as CONSTANT  
341 | OFFSET Error, contact MCS  
342 | OFFSET not allowed, too many locals used  
343 | Variable not supported with this function/statement  
344 | Program will overwrite bootloader  
345 | UART not available for the selected micro  
346 | External interrupt not supported or no settings found in DAT file  
347 | External interrupt mode not supported or found in DAT file  
349 | Setting not supported or not found in DAT file  
350 | Interrupt needs return  
351 | Not supported yet.  
352 | ALIAS can not be CONST or DIMMED variable  
353 | Reserved word may not be used  
354 | Previous Macro definition must be ended first  
355 | Macro previously defined  
356 | String constant size exceeded  
357 | Too many constants, increase resource languages  
358 | .DEF error, already defined  
359 | Operation not allowed on register  
360 | PRESCALE can not be used in COUNTER mode  
361 | Member expected  
362 | SBIC or SBIS was used followed by IN, OUT, SBIC, SBIS, SBI or CBI that also need to be converted.  
363 | No more room for EPROM DATA Index  
364 | Name not allowed, is used by constant/variable  
365 | Function not allowed in PRINT  
366 | Bit value out or range  
367 | Function name not allowed  
368 | Name used by label  
369 | Duplicate label name used by const or variable  
370 | Out of Flash memory  
371 | Function not allowed  
372 | SE entry missing in DAT file  
373 | Re-Configuration not allowed  
374 | . not allowed.  
375 | Duplicate definition  
376 | Config not found  
377 | Unexpected non numeric characters found  
378 | CAN BAUD not possible  
379 | Syntax error  
380 | Array<>Non Array mismatch  
381 | CONFIG RC5 not found  
382 | variable does not match FOR  
383 | Register range must be within [R16-R23]  
384 | Register range must be within [R16-R31]  
385 | Register must be even within [R0-R30]  
386 | Register R0 expected  
387 | IO address must be in range [0-31]  
388 | Bit number must be in range [0-7]  
389 | Constant out of range [0-65535]  
390 | Float not allowed for index  
391 | JTAG can not be disabled  
392 | Invalid operator  
393 | UART is fixed  
394 | Unsupported data type for BYREG  
395 | Index out of range  
396 | Delay not possible with selected frequency. Use WAITMS  
397 | .ORG exceeds PC  
398 | Single or Double expected  
399 | ASM reserved word not allowed  
400 | No structure found for REDO  
401 | No structure found for CONTINUE  
402 | MULTI-DIM not supported for specified page address  
403 | Integer Numeric constant expected  
404 | Mode not possible  
405 | SRAM DAT FILE ERROR  
406 | Insufficient $FRAMESPACE  
407 | Channel not defined  
408 | Invalid channel  
409 | END TYPE expected  
410 | TYPE expected  
411 | MEMBER already exists  
500 | XTINY LICENSE Required  
  
|   
  
998,999 | DEMO/BETA only supports 4096 bytes of code  
9999 | Illegal version. Please remove this illegal crack. You will not always get this message or error. When bascom finds traces of an illegal version it will generated random bugs in your code which are hard to find. It can also show this error.  Only download software from the mcselec.com server.  
  
Other error codes are internal ones. Please report them to support@ when you encounter them.

The Code explorer can give different errors. Here is a table with errors and how you can modify your code.

Config Lcd = 16 * 2  | Config Lcd = 16X2  | Change the * into an X  
---|---|---  
Cursor Off Noblink | Cursor Off , Noblink | Add a comma