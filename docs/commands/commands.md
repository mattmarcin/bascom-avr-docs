# Commands

Summary of Command Groups

Setting Graphics State  
---  
[AlphaFunc](alphafunc.md) | Set the alpha test function  
[BitmapHandle](bitmaphandle.md) | Set the bitmap handle  
[BitmapLayout](bitmaplayout.md) | Set the source bitmap memory format and layout for the current handle  
[BitmapSize](bitmapsize.md) | Set the screen drawing of bitmaps for the current handle  
[BitmapSource](bitmapsource.md) | Set the source address for bitmap graphics  
[BitmapTransformA-F](bitmaptransform.md) | Set the components of the bitmap transform matrix  
[BlendFunc](blendfunc.md) | Set pixel arithmetic  
[Cell](cell.md) | Set the bitmap cell number for the VERTEX2F command  
[Clear_B](clear_b.md) | Clear buffers to preset values  
[ClearColorA](clearcolora.md) | Set clear value for the alpha channel  
[ClearColorRGB](clearcolorrgb.md) | Set clear values for red, green and blue channels  
[ClearStencil](clearstencil.md) | Set clear value for the stencil buffer  
[ClearTag](cleartag.md) | Set clear value for the tag buffer  
[Color_A](color_a.md) | Set the current color alpha  
[ColorMask](colormask.md) | Enable or disable writing of color components  
[ColorRGB](colorrgb.md) , [ColorRBGdw](colorrgbdw.md) | Set the current color red, green and blue  
[LineWidth](linewidth.md) | Set the line width  
[PointSize](pointsize.md) | Set point size  
[RestoreContext](restorecontext.md) | Restore the current graphics context from the context stack  
[SaveContext](savecontext.md) | Push the current graphics context on the context stack  
[ScissorSize](scissorsize.md) | Set the size of the scissor clip rectangle  
[ScissorXY](scissorxy.md) | Set the top left corner of the scissor clip rectangle  
[StencilFunc](stencilfunc.md) | Set function and reference value for stencil testing  
[StencilMask](stencilmask.md) | Control the writing of individual bits in the stencil planes  
[StencilOp](stencilop.md) | Set stencil test actions  
[Tag](tag.md) | Set the current tag value  
[TagMask](tagmask.md) | Control the writing of the tag buffer  

Commands that begin and finish the display list  
[Begin_G](begin_g.md) | Start drawing a graphics primitive  
[End_G](end_g.md) | Finish drawing a graphics primitive  
[CmdDlStart](cmddlstart.md) | Start a New Display List  

Commands to draw graphic objects  
[CmdText](cmdtext.md) | Draw Text  
[CmdButton](cmdbutton.md) | Draw a Button  
[CmdClock](cmdclock.md) | Draw an analog clock  
[CmdBgColor](cmdbgcolor2.md) | Set the background color  
[CmdFgColor](cmdfgcolor.md) | Set the foreground color  
[CmdGradColor](cmdgradcolor.md) | Set the 3D effects for CmdButton and CmdKeys highlight color  
[CmdGauge](cmdgauge.md) | Draw a gauge  
[CmdGradient](cmdgradient.md) | Draw a smooth color gradient  
[CmdKeys](cmdkeys.md) | Draw a row of keys  
[CmdProgress](cmdprogress.md) | Draw a progress bar  
[CmdScrollbar](cmdscrollbar.md) | Draw a scroll bar  
[CmdSlider](cmdslider.md) | Draw a slider  
[CmdDial](cmddial.md) | Draw a rotary dial control  
[CmdToggle](cmdtoggle.md) | Draw a toggle switch  
[CmdNumber](cmdnumber.md) | Draw a decimal number  

Drawing Actions  
[Vertex2f](vertex2f.md) | Supply a vertex with fractional coordinates  
[Vertex2ii](vertex2ii.md) | Supply a vertex with positive integer coordinates  
[CmdSetFont](cmdsetfont.md) | Set up a custom font  
[CmdTrack](cmdtrack.md) | Track touches for a graphic object  

Commands to operate on memory  
[CmdMemCRC](cmdmemcrc.md) | Compute a CRC-32 for memory  
[CmdMemZero](cmdmemzero.md) | Write zero to a block of memory  
[CmdMemSet](cmdmemset.md) | Fill memory with a byte value  
[CmdMemWrite](cmdmemwrite.md) | Write bytes into memory  
[CmdMemCpy](cmdmemcpy.md) | Copy a block of memory  
[CmdAppend](cmdappend.md) | Append memory to display list  
[CmdGetPtr](cmdgetptr.md) | Get the End memory address of inflated data  

Commands for loafing image data into FT80x memory  
[CmdInflate](cmdinflate.md) | Decompress data into memory  
[CmdLoadImage](cmdloadimage.md) | Load a JPEG image  

Commands for setting the bitmap transform matrix  
[CmdLoadIdentity](cmdloadidentity.md) | Set the current matrix to identity  
[CmdTranslate](cmdtranslate.md) , [CmdTranslateP](cmdtranslatep.md) | Apply a translation to the current matrix  
[CmdScale](cmdscale.md) | Apply a scale to the current matrix  
[CmdRotate](cmdrotate.md) , [CmdRotateA](cmdrotatea.md) | Apply a rotation to the current matrix  
[CmdSetMatrix](cmdsetmatrix.md) | Write the current matrix as a bitmap transform  
[CmdGetMatrix](cmdgetmatrix.md) | Retrieves the current matrix coefficients  
  
|   
  
Execution control  
[Jump](jump.md) | Execute commands at another location in the display list  
[Macro_R](macro_r.md) | Execute a single command from a macro register  
[Call_C](call_c.md) | Execute a sequence of commands at another location in the display list  
[Return_C](return_c.md) | Return from a previous CALL command  
[Display_E](display_e.md) | End the display list  
[CmdSwap](cmdswap.md) | Swap de current display list  

Other Commands  
[CmdColdStart](cmdcoldstart.md) | Set co-processor engine state to default values  
[CmdInterrupt](cmdinterrupt.md) | Trigger interrupt INT_CMDFLAG  
[CmdRegRead](cmdregread.md) | Read a register value  
[CmdCalibrate](cmdcalibrate.md) | Execute the touch screen calibration routine  
[CmdSpinner](cmdspinner.md) | Start an animated spinner  
[CmdStop](cmdstop.md) | Stop any spinner, screensaver or sketch  
[CmdScreenSaver](cmdscreensaver.md) | Start an animated screen saver  
[CmdSketch](cmdsketch.md) | Start a continuous sketch update  
[CmdSnapshot](cmdsnapshot.md) | Take a snapshot of the current screen  
[CmdLogo](cmdlogo.md) | Play device logo animation  
  
Co-Processor Engine commands

![clip0104](clip0104.png)

BASCOM high level commands

  
|   
  
---|---  
[ClearScreen](clearscreen.md) | Clears the LCD with a black background  
[UpdateScreen](updatescreen.md) | Executes the commands in FIFO and refreshes LCD  
[WaitCmdFifoEmpty](waitcmdfifoempty.md) | Waits for execution of commands in FIFO buffer  
[CMDFTSTACK](cmdftstack.md) | Send data from the soft stack  
[CMD8](cmd8.md) | Send a byte to the FT800 graphic processor.  
[CMD16](cmd16.md) | Send a word to the FT800 graphic processor.  
[CMD32](cmd32.md) | Send a dword to the FT800 graphic processor.  
[WR8](wr8.md) | Write an address and a byte parameter to the FT800.  
[WR16](wr16.md) | Write an address and a word parameter to the FT800.  
[WR32](wr32.md) | Write an address and a dword parameter to the FT800.  
  
Errors

The FTERROR byte variable contains 4 flags you can examine.

FtError.0 = WaitCmdFifoEmpty Sub when Overflowed

FtError.1 = WaitCmdFifoEmpty Sub when TimeOut

FtError.2 = FreeSpaceFt Sub when OverFlowed

FtError.3 = FreeSpaceFt Sub when TimeOut