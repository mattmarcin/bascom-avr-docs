# CmdSketch

Action

Start a continuous sketch update.

Syntax FT800

CmdSketch x, y, w, h, ptr, format

Syntax FT801

CmdSketch x, y, w, h, ptr, format , freq

Remarks

x | x-coordinate of sketch area top-left, in pixels  
---|---  
y | y-coordinate of sketch area top-left, in pixels  
w | Width of sketch area, in pixels  
h | Height of sketch area, in pixels  
ptr | Base address of sketch bitmap  
format | Format of sketch bitmap, either L1 or L8  
freq | The oversampling frequency. The typical value is 1500 to make sure the lines are connected smoothly. The value zero means no oversampling operation.  
  
FT800

Please note that update frequency of bitmap data in graphics memory depends on sampling frequency of ADC built-in circuit of FT800, which is up to 1000 Hz.

FT801

CmdSketch - Capacitive touch specific sketch This command has the same functionality as CmdSketch except it has done the optimization for a Capacitive Touch Panel.

Because Capacitive Touch Panels have lower sampling frequencies (around 100 Hz) to report the coordinates, the sketch functionality updates less frequently compared to resistive touch. CmdSketch introduces a linear interpolation algorithm to provide a smoother effect when drawing the output line.

After the sketch command, the co-processor engine continuously samples the touch inputs and paints pixels into a bitmap, according to the touch (x, y). This means that the user touch inputs are drawn into the bitmap without any need for MCU work. 

Command [CmdStop](cmdstop.md) stops the sketch process.

Note that only one of [CmdSketch](cmdsketch.md), [CmdScreenSaver](cmdscreensaver.md) or [CmdSpinner](cmdspinner.md) can be active at one time.

Example

' see demo - FT800 Sketch.bas also FT800 Demo4.bas (SUB Sketch)