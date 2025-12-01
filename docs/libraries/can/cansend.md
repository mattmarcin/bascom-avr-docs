# CANSEND

Action

Puts the Message Object into Transmit mode and send out data.

Syntax blocking function

status = CANSEND(object, var[,bytes])

Syntax non blocking statement

CANSEND object, var[,bytes]

Remarks

status | The status of sending the frame. This should be 0 if there was no problem. If there is an error it will return 1 or higher. The return value is the CANSTMOB register content with the TX bit cleared.  
---|---  
object | The message object number in the range from 0-14. The MOB must have been configured into the DISABLED mode before CANSEND can be used.   
var | A variable or array which content will be send. The data type of the variable will be used to determine the number of bytes to send.  
bytes | This is an optional value. You can specify how many bytes must be transmitted.   
  
The CANSEND function will disable the TX interrupt and then polls the CANSTMOB register for a change of flags. The TX flag is cleared so that a successful transmission returns a 0.

In case of ACK errors or other errors, a value other then 0 will be returned. Right after the status has changed, the TX and Error interrupt are enabled again and the CAN interrupt routine is executed. You need to reconfigure the MOB in all cases otherwise you can not send new data.

The CANSEND statement will send the data and returns immediately.

The advantage is that your code can continue running other code. Before new data can be sent it must however have been processed. Check out the CAN-elektor-V2.bas example from the samples\CAN folder.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Have a look at [CONFIG CANBUS](config_canbusmode.md) for a full example.

The code below only demonstrates that you MUST configure the MOB again in the interrupt routine.

The code below is taken from the sample you find under CONFIG CANBUS

The \examples\CAN folder contains 2 examples too.

Elseif Canstmob.6 = 1 Then 'transmission ready  
```vb
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK

```
Elseif Canstmob.0 = 1 Then 'ACK ERROR  
```vb
Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No  
' reconfig with value -1 for the current MOB and do not set ID and MASK  


```