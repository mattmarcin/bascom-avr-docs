# Keyword Reference

1WIRE  
  
1Wire routines allow you to communicate with Dallas 1wire chips.

[1WRESET](1wreset.md) , [1WREAD](1wread.md) , [1WWRITE](1wwrite.md) , [1WSEARCHFIRST](1wsearchfirst.md) , [1WSEARCHNEXT](1wsearchnext.md) ,[1WVERIFY](1wverify.md) , [1WIRECOUNT](1wirecount.md)

CAN

[CONFIG CANBUSMODE](config_canbusmode.md), [CONFIG CANMOB](config_canmob.md), [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Conditions and Loops

Conditions execute a part of the program depending on a condition being True or False

[IF-THEN-ELSE-END IF](if_then_else_end_if.md) , [WHILE-WEND](while_wend.md) , [ELSE](else.md) , [DO-LOOP](do_loop.md) , [SELECT CASE - END SELECT](select_case_end_select.md) , [FOR-NEXT](for_next.md) , [CONTINUE](continue.md), [REDO](redo.md)

Conditional Compilation

[#IF #ELSE #ELSEIF #ENDIF , VAREXIST](_if_else_endif.md)

Configuration

Configuration commands initialize the hardware to the desired state.

[CONFIG](config.md) , [CONFIG ACI](config_aci.md) , [CONFIG ADC](config_adc.md) , [CONFIG ADCx](config_adca.md) , [CONFIG BCCARD](config_bccard.md) , [CONFIG CLOCK](config_clock.md) , [CONFIG COM1](config_com1.md) , [CONFIG COM2](config_com2.md) , [CONFIG DAC](config_dacx.md) , [CONFIG DATE](config_date.md) , [CONFIG DMXSLAVE](config_dmxslave.md), [CONFIG EEPROM](config_eeprom.md) ,[CONFIG EXTENDED_PORT](config_extended_port.md) , [CONFIG PS2EMU](config_ps2emu.md) , [CONFIG ATEMU](config_atemu.md) , [CONFIG I2CSLAVE](config_i2cslave.md) , [CONFIG INPUT](configinput.md), [CONFIG GRAPHLCD](config_graphlcd.md) , [CONFIG KEYBOARD](config_keyboard.md) , [CONFIG TIMER0](config_timer0.md) , [CONFIG TIMER1](config_timer1.md) , [CONFIG LCDBUS](config_lcdbus.md) , [CONFIG LCDMODE](config_lcdmode.md) , [CONFIG 1WIRE](config_1wire.md) , [CONFIG LCD](config_lcd.md) , [CONFIG OSC](config_osc.md), [CONFIG SERIALOUT](config_serialout.md) , [CONFIG SERIALIN](config_serialin.md) , [CONFIG SPI](config_spi.md) , [CONFIG SPIx](config_spix.md), [CONFIG SYSCLOCK](config_sysclock.md) , [CONFIG LCDPIN](config_lcdpin.md) , [CONFIG PRIORITY](config_priority.md) , [CONFIG SDA](config_sda.md) , [CONFIG SCL](config_scl.md) , [CONFIG DEBOUNCE](config_debounce.md) , [CONFIG WATCHDOG](config_watchdog.md) , [CONFIG PORT , ](config_port.md)[COUNTER0 AND COUNTER1](counter0_and_counter1.md) , [CONFIG TCPIP](config_tcpip.md) , [CONFIG TWISLAVE](config_twislave.md) , [CONFIG SINGLE](configsingle.md) , [CONFIG X10](config_x10.md) , [CONFIG XRAM](configxram.md) , [CONFIG USB](config_usb.md) , [CONFIG DP](config_dp.md) , [CONFIG TCXX](config_tcxx.md) , [CONFIG VPORT](config_vport.md) [CONFIG ERROR](config_error.md) , [CONFIG POWER REDUCTION](config_power_reduction.md),[ CONFIG EVENT_SYSTEM](config_event_system.md) , [CONFIG DMA ](config_dma.md), [CONFIG DMACHx](config_dmachx.md) , [CONFIG SUBMODE](config_submode.md) , [CONFIG POWERMODE](config_powermode.md) , [CONFIG XPIN](config_xpin.md) , [CONFIG FT800](config_ft800.md) , [CONFIG I2CBUS](config_i2cbus.md) , [CONFIG EDMA](config_edma.md) , [CONFIG EDMAx](config_edmax.md) , [CONFIG INPUTBIN](config_inputbin.md) , [CONFIG MODBUS](config_modbus.md) , [CONFIG PORT_MUX](config_port_mux.md) , [CONFIG VREF](config_vref.md) , , [CONFIG TCA](config_tca0.md), [CONFIG TCB](config_tcb0_tcb1.md), [CONFIG TCD](config_tcd0.md) , [CONFIG RC5](config_rc5.md), [CONFIG RC5SEND](config_rc5send.md) ,  [CONFIG VARPTRMODE](config_varptrmode.md)

Conversion

A conversion routine is a function that converts a number or string from one form to another.

[BCD](bcd.md) , [GRAY2BIN](gray2bin.md) , [BIN2GRAY](bin2gray.md) , [BIN](bin.md) , [MAKEBCD](makebcd.md) , [MAKEDEC](makedec.md) , [MAKEINT](makeint.md) , [FORMAT](format.md) , [FUSING](fusing.md) , [BINVAL](binval.md) , [CRC8](crc8.md) , [CRC16](crc16.md) , [CRC16UNI](crc16uni.md) , [CRC32](crc32.md) , [HIGH](high.md) , [HIGHW](highw.md) , [LOW](low.md) , [AESENCRYPT](aesencrypt.md) , [AESDECRYPT](aesdecrypt.md) , [FLIP](flip2.md) , [CRCMB](crcmb.md) , [CRC8UNI](crc8uni.md) , [MANCHESTERDEC](manchesterdec.md), [MANCHESTERENC](manchesterenc.md) , [DESENCRYPT](desencrypt.md) , [DESDECRYPT](desdecrypt.md)

DateTime

Date Time routines can be used to calculate with date and/or times.

[DATE](date.md) , [TIME](time.md) , [DATE$](date_.md) , [TIME$](time_.md) , [DAYOFWEEK](dayofweek.md) , [DAYOFYEAR](dayofyear.md) , [SECOFDAY](secofday.md) , [SECELAPSED](secelapsed.md) , [SYSDAY](sysday.md) , [SYSSEC](syssec.md) , [SYSSECELAPSED](syssecelapsed.md)

Delay

Delay routines delay the program for the specified time.

[WAIT](wait.md) , [WAITMS](waitms.md) , [WAITUS](waitus.md) , [DELAY](delay.md)

Directives

Directives are special instructions for the compiler. They can override a setting from the IDE.

[$ASM](asm.md) , [$BAUD](baud_1.md) , [$BAUD1](_baud1.md) , [$BIGSTRINGS](bigstrings.md) , [$BGF](_bgf.md) , [$BOOT](_boot.md) , [$CRYSTAL](crystal_1.md) , [$DATA](data_1.md) , [$DBG](_dbg.md) , [$DEFAULT](default.md) , [$EEPLEAVE](_eepleave.md) , [$EEPROM](eeprom.md) , [$EEPROMHEX](_eepromhex.md) , [$EEPROMSIZE](eepromsize.md), [$EXTERNAL](external.md) , [$HWSTACK](_hwstack.md) , [$INC](_inc.md) , [$INCLUDE](include.md) , [$INITMICRO](_initmicro.md) , [$LCD](lcd_1.md) , [$LCDRS](lcdrs.md) , [$LCDPUTCTRL](lcdputctrl.md) , [$LCDPUTDATA](lcdputdata.md) , [$LCDVFO](_lcdvfo.md) , [$LIB](lib.md) , [$LOADER](loader.md) , [$LOADERSIZE](loadersize.md) , [$MAP](_map.md) , [$NOCOMPILE](nocompile.md) , [$NOINIT](_noinit.md) , [$NORAMCLEAR](_noramclear.md) , [$NORAMPZ](norampz.md) , [$PROJECTTIME](_projecttime.md), [$PROG](_prog.md) , [$PROGRAMMER](programmer.md) , [$REGFILE](regfile.md) , [$RESOURCE](resource.md) , [$ROMSTART](_romstart.md) [$SERIALINPUT](serialinput.md), [$SERIALINPUT1](_serialinput1.md) , [$SERIALINPUT2LCD](serialinput2lcd.md) , [$SERIALOUTPUT](serialoutput.md) , [$SERIALOUTPUT1](_serialoutput1.md) , [$SIM](sim.md) , [$SWSTACK](_swstack.md) , [$TIMEOUT](_timeout.md) , [$TINY](_tiny.md) , [$WAITSTATE](_waitstate.md) , [$XRAMSIZE](xramsize.md) , [$XRAMSTART](xramstart.md) , [$XA](xa.md) , [$CRYPT](crypt.md) , [$NOTRANSFORM](notransform.md) , [$FILE](file.md) , [$AESKEY](_aeskey.md) , [$XTEAKEY](xteakey.md) , [$STACKDUMP](stackdump.md) ,[ $NOFRAMEPROTECT](noframeprotect.md) , [$FRAMEPROTECT](frameprotect.md) , [$FORCESOFTI2C](forcesofti2c.md) , [$BOOTVECTOR](bootvector.md) , [$REDUCEIVR](_aeskey.md) , [$TYPECHECK](typecheck.md) , [$NOTYPECHECK](notypecheck.md)

File

File commands can be used with AVR-DOS, the Disk Operating System for AVR.

[BSAVE](bsave.md) , [BLOAD](bload.md) , [GET](get.md) , [VER](ver.md) , [DISKFREE](diskfree.md) , [DIR](dir.md) , [DriveReset](drivereset.md) , [DriveInit](driveinit.md) , [LINE INPUT](line_input.md) , [INITFILESYSTEM](initfilesystem.md) , [EOF](eof.md) , [WRITE](write.md) , [FLUSH](flush.md) , [FREEFILE](freefile.md) , [FILEATTR](fileattr.md) , [FILEDATE](filedate.md) , [FILETIME](filetime.md) , [FILEDATETIME](filedatetime.md) , [FILELEN](filelen.md) , [SEEK](seek.md) , [KILL](kill.md) , [DriveGetIdentity](drivegetidentity.md) , [DriveWriteSector](drivewritesector.md) , [DriveReadSector](drivereadsector.md) , [LOC](loc.md) , [LOF](lof.md) , [PUT](put.md) , [OPEN](open.md) , [CLOSE](close.md) , [CHDIR](chdir.md) , [MKDIR](mkdir.md) , [RMDIR](rmdir.md) , [NAME](name.md) , [GETATTR](getattr.md) , [SETATTR](setattr.md) , [CLEARATTR](clearattr.md)

Graphical LCD

Graphical LCD commands extend the normal text LCD commands.

[GLCDCMD](glcdcmd.md) , [GLCDDATA](glcddata.md) , [SETFONT](setfont.md) , [LINE](line.md) , [PSET](pset.md) , [SHOWPIC](showpic.md) , [SHOWPICE](showpice.md) , [CIRCLE](circle.md) , [BOX](box.md) , [RGB8TO16](rgb8to16.md)

I2C

I2C commands allow you to communicate with I2C chips with the TWI hardware or with emulated I2C hardware.

[I2CINIT](i2cinit.md) , [I2CRECEIVE](i2creceive.md) , [I2CSEND](i2csend.md) , [I2CSTART, I2CREPSTART, I2CSTOP,I2CRBYTE,I2CWBYTE](i2start_i2cstop__i2crbyte__i2cwbyte.md)

IO

I/O commands are related to the I/O pins and ports of the processor chip.

[ALIAS](alias.md) , [BITWAIT](bitwait.md) , [TOGGLE](toggle.md) , [RESET](reset.md) , [SET](set.md) , [SHIFTIN](shiftin.md) , [SHIFTOUT](shiftout.md) , [DEBOUNCE](debounce.md) , [PULSEIN](pulsein.md) , [PULSEOUT](pulseout.md)

Micro

Micro statements are specific to the micro processor chip.

[IDLE](idle.md) , [POWER mode](power_mode.md) , [POWERDOWN](powerdown.md) , [POWERSAVE](powersave.md) , [ON INTERRUPT](on_interrupt.md) , [ENABLE](enable.md) , [DISABLE](disable.md) , [START](start.md) , [END](end.md) , [VERSION](version.md) , [CLOCKDIVISION](clockdivision.md) , [CRYSTAL](crystal_2.md) , [STOP](stop.md)

Memory

Memory functions set or read RAM , EEPROM or flash memory.

[ADR](adr___adr2.md) , [ADR2](adr___adr2.md) , [WRITEEEPROM](writeeeprom.md) , [CPEEK](cpeek.md) , [CPEEKH](cpeekh.md) , [PEEK](peek.md) , [POKE](poke.md) , [OUT](out.md) , [READEEPROM](readeeprom.md) , [DATA](data_2.md) , [INP](inp.md) , [READ](read.md) , [RESTORE](restore.md) , [LOOKDOWN](lookdown.md) , [LOOKUP](lookup.md) , [LOOKUPSTR](lookupstr.md) , [LOADADR](loadadr.md) , [LOADLABEL](loadlabel.md) , [LOADWORDADR](loadwordadr.md) , [MEMCOPY](memcopy.md) , [GETREG](getreg.md) , [SETREG](setreg.md) , [VARPTR](varptr.md) , [MEMFILL](memfill.md)

Remote Control

Remote control statements send or receive IR commands for remote control.

[RC5SEND](rc5send.md) , [RC6SEND](rc6send.md) , [GETRC5](getrc5.md) , [SONYSEND](sonysend.md)

RS-232

RS-232 are serial routines that use the UART or emulate a UART.

[BAUD](baud_2.md) , [BAUD1](baud1.md), [BUFSPACE](bufspace.md) , [CLEAR](clear.md), [ECHO](echo.md) , [WAITKEY](waitkey.md) , [ISCHARWAITING](ischarwaiting.md) , [INKEY](inkey.md) , [INPUTBIN](inputbin.md) , [INPUTHEX](inputhex.md) , [INPUT](input.md) , [PRINT](print.md) , [PRINTBIN](printbin.md) , [SERIN](serin.md) , [SEROUT](serout.md) , [SPC](spc.md) , [MAKEMODBUS](makemodbus.md)

SPI

SPI routines communicate according to the SPI protocol with either hardware SPI or software emulated SPI.

[SPIIN](spiin.md) , [SPIINIT](spiinit.md) , [SPIMOVE](spimove.md) , [SPIOUT](spiout.md) , [SPI1IN](spiin.md) , [SPI1INIT](spiinit.md) , [SPI1MOVE](spimove.md) , [SPI1OUT](spiout.md)

String

String routines are used to manipulate strings.

[ASC](asc.md) , [CHARPOS](charpos.md), [UCASE](ucase.md) , [LCASE](lcase.md) , [TRIM](trim.md) , [SPLIT](split.md) , [LTRIM](ltrim.md) , [INSTR](instr.md) , [SPACE](space.md) , [STRING](string.md) , [RTRIM](rtrim.md) , [LEFT](left.md) , [LEN](len.md) , [MID](mid.md) , [RIGHT](right.md) , [VAL](val.md) , [STR](str.md) , [CHR](chr.md) , [CHECKSUM](checksum.md) , [CHECKSUMXOR](checksum.md), [HEX ](hex.md), [HEXVAL](hexval.md) , [QUOTE](quote.md) , [REPLACECHARS](replacechars.md) , [STR2DIGITS](str2digits.md) , [DELCHAR](delchar.md), [DELCHARS](delchars.md) , [INSERTCHAR](insertchar.md) , [JOIN](join.md)

TCP/IP

TCP/IP routines can be used with the W3100/IIM7000/IIM7010/W5100/W5200/W5300 modules.

[BASE64DEC](base64dec.md) , [BASE64ENC](base64enc.md) , [IP2STR](ip2str.md) , [UDPREAD](udpread.md) , [UDPWRITE](udpwrite.md) , [UDPWRITESTR](udpwritestr.md) , [TCPWRITE](tcpwrite.md) , [TCPWRITESTR](tcpwritestr.md) , [TCPREAD](tcpread.md) , [GETDSTIP](getdstip.md) , [GETDSTPORT](getdstport.md) , [SOCKETSTAT](socketstat.md) , [SOCKETCONNECT](socketconnect.md) , [SOCKETLISTEN](socketlisten.md) , [GETSOCKET](getsocket.md) , [SOCKETCLOSE](socketclose.md) , [SETTCP](settcp.md) , [GETTCPREGS](gettcpregs.md) , [SETTCPREGS](settcpregs.md) , [SETIPPROTOCOL](setipprotocol.md) , [TCPCHECKSUM](tcpchecksum.md) , [SOCKETDISCONNECT](socketdisconnect.md) , [SNTP](sntp.md) , [TCPREADHEADER](tcpreadheader.md) , [UDPREADHEADER](udpreadheader.md), [URL2IP](url2ip.md)

Text LCD

Text LCD routines work with normal text based LCD displays.

[HOME](home.md) , [CURSOR](cursor.md) , [UPPERLINE](upperline.md) , [THIRDLINE](thirdline.md) , [INITLCD](initlcd.md) , [LOWERLINE](lowerline.md) , [LCD](lcd_2.md) , [LCDAT](lcdat.md) , [FOURTHLINE](fourthline.md) , [DISPLAY](display.md) , [LCDCONTRAST](lcdcontrast.md) , [LOCATE](locate.md) , [SHIFTCURSOR](shiftcursor.md) , [DEFLCDCHAR](deflcdchar.md) , [SHIFTLCD](shiftlcd.md) , [CLS](cls.md) , [LCDAUTODIM](lcdautodim.md) , [LCDCMD](lcdcmd.md), [LCDDATA](lcddata.md) , [LCDFONT](lcdfont.md)

Trig & Math

Trig and Math routines work with numeric variables.

[ACOS](acos.md) , [ASIN](asin.md) , [ATN](atn.md) , [ATN2](atn2.md) , [EXP](exp.md) , [RAD2DEG](rad2deg.md) , [FRAC](frac.md) , [TAN](tan.md) , [TANH](tanh.md) , [COS](cos.md) , [COSH](cosh.md) , [LOG](log.md) , [LOG10](log10.md) , [ROUND](round.md) , [ABS](abs.md) , [INT](int.md) , [MAX](max.md) , [MIN](min.md) , [SQR](sqr.md) , [SGN ](sgn.md), [POWER](power.md) , [SIN](sin.md) , [SINH](sinh.md) , [FIX](fix.md) , [INCR](incr.md) , [DECR](decr.md) , [DEG2RAD](deg2rad.md) , [CHECKFLOAT](checkfloat.md) , [MOD](mod.md) , [QSIN](qsin.md) , [QCOS](qcos.md) , [AND](and.md), [OR](or.md) , [XOR](xor.md) , [NOT](not.md)

Various

This section contains all statements that were hard to put into another group

[CONST](const.md) , [DBG](dbg.md) , [DECLARE FUNCTION](declare_function.md) , [DEBUG](debug.md), [DECLARE SUB](declare_sub.md) , [DEFXXX](defxxx.md) , [DIM](dim.md) , [DTMFOUT](dtmfout.md) , [EXIT](exit.md) , [ENCODER](encoder.md) , [GETADC](getadc.md) , [GETKBD](getkbd.md) , [GETATKBD](getatkbd.md) , [GETRC](getrc.md) , [GOSUB](gosub.md) , [GOTO](goto.md) , [LOCAL](local.md) ,[ON VALUE](on_value.md) , [POPALL](popall.md) , [PS2MOUSEXY](ps2mousexy.md) , [PUSHALL](pushall.md) , [RETURN](return.md) , [RND](rnd.md) , [ROTATE](rotate.md) , [SENDSCAN](sendscan.md) , [SENDSCANKBD](sendscankbd.md) , [SHIFT](shift.md) , [SOUND](sound.md) , [STCHECK](stcheck.md) , [SUB](sub.md) , [SWAP](swap.md) , [VARPTR](varptr.md) , [X10DETECT](x10detect.md) , [X10SEND](x10send.md) , [READMAGCARD](readmagcard.md) , [REM](rem.md) , [BITS](bits.md) , [BYVAL](byval.md) , [CALL](call.md) , [#IF](_if_else_endif.md) , [#ELSE](_if_else_endif.md) , [#ENDIF](_if_else_endif.md) , [READHITAG](readhitag.md) , [SORT](sort.md) , [XTEADECODE](xteadecode.md) , [XTEAENCODE](xteaencode.md) , [BREAK](break.md) , [COMPARE](compare.md) , [NOP](nop.md) , [SIZEOF](sizeof.md) , [WRITEDAC](writedac.md) , [TYPE](type.md)

RAINBOW WS2812

Rainbow or WS2812 LED statements and functions.

[CONFIG RAINBOW](config_rainbow.md) , [RB_ADDCOLOR](rb_addcolor.md), [RB_ANDCOLOR](rb_andcolor.md), [RB_ORCOLOR](rb_orcolor.md), [RB_SUBCOLOR](rb_subcolor.md), [RB_CLEARSTRIPE](rb_clearstripe.md) , [RB_CLEARCOLORS](rb_clearcolors.md) , [RB_FILL](rb_fill.md) , [RB_FILLCOLORS](rb_fillcolors.md) , [RB_FILLSTRIPE](rb_fillstripe.md) , [RB_SELECTCHANNEL](rb_selectchannel.md), [RB_SEND](rb_send.md), [RB_SETCOLOR](rb_setcolor.md) , [RB_SWAPCOLOR](rb_swapcolor.md) , [RB_ROTATELEFT](rb_rotateleft.md), [RB_ROTATERIGHT](rb_rotateright.md), [RB_SHIFTLEFT](rb_shiftleft.md), [RB_SHIFTRIGHT](rb_shiftright.md) , [RB_CHANGEPIN](rb_changepin.md) , [RB_SETTABLECOLOR](rb_settablecolor.md) , [RB_GETCOLOR](rb_getcolor.md) , [RB_LOOKUPCOLOR](rb_lookupcolor.md) , [RB_COLOR](rb_color.md) , [RB_COPY](rb_copy.md)

FT800-FT801-FT810

[CMD8](cmd8.md) , [CMD16](cmd16.md) , [CMD32](cmd32.md) , [RD8](rd8.md) , [RD16](rd16.md) , [RD32](rd32.md) , [WR8](wr8.md) , [WR16](wr16.md) , [WR32](wr32.md)

XMEGA

[READSIG](readsig.md) , [ATXMEGA](atxmega.md)

XTINY

[XTINY](xtiny.md)

MEGAX

[MEGAX](megax.md)

AVRX

[AVRX](avrx.md)