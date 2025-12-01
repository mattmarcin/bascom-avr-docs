# CANRECEIVE

Action

Receives data from a received CAN frame and stores it into a variable.

Syntax

numrec = CANRECEIVE(var [, bytes])

Remarks

numrec | Number of bytes received.  
---|---  
var | The variable into which the received data is stored. This must be a numeric variable or array. Version 2076 supports strings as well.  
bytes | This is an optional parameter and specifies the number of bytes to retrieve.  
  
The compiler will use the data type of the variable to determine how many bytes need to be retrieved. So when you use a variable that was [DIM](dim.md)ensioned as a long, an attempt will be made to read 4 bytes.

The CANRECEIVE function operates on the current selected Message Object which is selected with CANSELPAGE.

The CANRECEIVE function is intended to be used inside the CAN interrupt routine.

After you have retrieved the data from the received CAN frame, the Message Object is free to be used again. You MUST configure it again in order to receive a new interrupt.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Breceived = Canreceive(porta) ' read the data and store in PORTA  
```vb
Print #2 , "Got : " ; Breceived ; " bytes" ' show what we received  
Print #2 , Hex(porta)  
Config Canmob = -1 , Bitlen = 11 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK

```