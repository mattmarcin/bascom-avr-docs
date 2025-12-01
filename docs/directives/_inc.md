# $INC

Action

Includes a binary file in the program at the current position.

Syntax

$INC label , size | nosize , "file"

Remarks

Label | The name of the label you can use to refer to the data.  
---|---  
Nosize | Specify either nosize or size. When you use size, the size of the data will be included. This way you know how many bytes you can retrieve.  
File | Name of the file which must be included.  
  
Use RESTORE to get a pointer to the data. And use READ, to read in the data.

The $INC statement is an alternative for the DATA statement.

While DATA works ok for little data, it is harder to use on large sets of data.

See Also

[RESTORE](restore.md), [DATA](data_2.md) , [READ](read.md)

Example

```vb
$regfile = "m48def.dat"

$crystal = 4000000

$baud = 19200

$hwstack = 16

$swstack = 16

$framesize = 16

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Dim Size As Word , W As Word , B As Byte

```
Restore L1 ' set pointer to label

Read Size ' get size of the data

```vb
Print Size ; " bytes stored at label L1"

For W = 1 To Size

```
Read B : Print Chr(b);

```vb
Next

End

'include some data here

$inc L1 , Size , "c:\test.bas"

'when you get an error, insert a file you have on your system

```