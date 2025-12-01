# RND

Action

Returns a random number.

Syntax

var = RND( limit )

Remarks

Limit | Word that limits the returned random number.  
---|---  
Var | The variable that is assigned with the random number.  
  
The RND() function returns an Integer/Word and needs an internal storage of 2 bytes. (___RSEED). Each new call to Rnd() will give a new positive random number.

![notice](notice.jpg) Notice that it is a software based generated number. And each time you will restart your program the same sequence will be created.

You can use a different SEED value by dimensioning and assigning ___RSEED yourself:

```vb
Dim ___rseed as word : ___rseed = 10234

Dim I as word : I = rnd(10)

```
When your application uses a timer you can assign ___RSEED with the timer value. This will give a better random number.

See also

[CONFIG RND](config_rnd.md)

Example

```vb
'-----------------------------------------------------------------------------------------

'name : rnd.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demo : RND() function

'micro : Mega48

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "m48def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

Dim I As Word ' dim variable

Do

```
I = Rnd(40) 'get random number (0-39)

```vb
Print I 'print the value

Wait 1 'wait 1 second

Loop 'for ever

End

```