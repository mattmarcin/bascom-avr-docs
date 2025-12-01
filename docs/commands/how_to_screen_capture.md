# How to Screen Capture

How to Screen Capture

There is nothing better than been able to produce nice Screen captures from your Graphics Display (instead of using a camera) when wanting to write a manual or a help file explaining the different screen operations/features at what they do.

The process is quite simple to implement into your program generating a Screen capture output. You can use the supplied code or you can modify the code and produce your own version.

```vb
If you look at FT800 Capture.Bas it demonstrates the Screen capture using two routines. 

Sub ScreenShot: is a demo originally from James Bowman (Gameduino2) which takes a snapshot and just outputs the data via Serial (which you have to write your own PC serial capture program).

Sub ScreenShot2: is the same as above except it uses additional control codes for handshaking and stopping the program. A sample PC (Windows) program called Capture FT800.exe demonstrate the capture process which when successful produces a BMP file. 

```
Capture FT800.exe waits for a ACK to acknowledge a ready to receive message so transmission can start, once transfer begins and then finishes it receives a EOT acknowledge end of transmission., Additional to this if the user wants to stop/quit transmission the program will send an ESC character to notify the hardware to stop sending data .

The easiest way to begin is to add Screenshot.inc to your code:

```vb
$Include "FT800.inc"  
$Include "FT800_Functions.inc"  
  
$Include "ScreenShot.inc" ' ç==== add this line 

Then decide where in your program you want to call ScreenShot2 so it can start the capturing process (working with Capture FT800.exe). 

```
This example itâs called at the end of the program:

  
Do  
Demo  
Loop

ScreenShot2  
  
End

This sample is called within a certain code area, straight after the screen is displayed.

ClearScreen  
ColorRGB 255, 255, 255  
BitmapSource RAM_G  
BitmapLayout Header_Format(1+_base), Header_Stride(1+_base), Header_Height(1+_base)  
BitmapSize NEAREST, Border, Border, Header_Width(1+_base), Header_Height(1+_base)  
Begin_G BITMAPS ' start drawing bitmaps  
Const DA = FT_DispWidth / 4  
Ln1 = Header_Width(1+_base) / 2  
Const DB = FT_DispHeight / 2  
Ln2 = Header_Height(1+_base) / 2  
BMoffsetx = DA - Ln1  
BMoffsety = DB - Ln2  
Vertex2II BMoffsetx, BMoffsety, 0, 0  
UpdateScreen

ScreenShot2

Using the Capture FT800.exe:

Note: when possible use the highest baud rate possible to decrease the wait time of receiving transmission. Donât forget to make sure the Hardware baud rate matches the Capture FT800 baud rate! (it wonât time time out if wrong).

![](embim2.png)

1)| Chose your Comm port  
---|---  
  
2)| Select the Baud rate of your Hardware  
---|---  
  
3)| You can either enter a filename or it can prompt you at the end of the capture.  
---|---  
  
4)| Press Start when ready, if successful you will see a message.  
---|---