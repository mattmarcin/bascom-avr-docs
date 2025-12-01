# CmdLoadImage

Action

Load a JPEG image.

Syntax

CmdLoadImage ptr, options

Remarks

ptr | Destination address  
---|---  
options | By default, option OPT_RGB565 means the loaded bitmap is in RGB565 format.  Option OPT_MONO means the loaded bitmap to be monochrome, in L8 format. The command appends Display List commands to set the source, layout and size of the resulting image. Option OPT_NODL prevents this - nothing is written to the display list.  OPT_NODL can be OR'ed with OPT_MONO or OPT_RGB565.  
  
The data byte should immediately follow in the command buffer. If the number of bytes is not a multiple of 4, then 1, 2 or 3 bytes

should be appended to ensure 4-byte alignment of the next command. These padding bytes can have any value.

The application on the host processor has to parse the JPEG header to get the properties of the JPEG image and decide to decode. Behavior is unpredictable in cases of non baseline jpeg images or the output data generated is more than the RAM_G size.

Example

' See demos - FT800 Demo2.bas, FT800 LoadImage.bas