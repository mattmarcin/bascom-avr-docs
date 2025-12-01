# CANGETINTS

Action

Reads the CAN interrupt registers and store into the _CAN_MOBINTS word variable.

Syntax

CANGETINTS

Remarks

This statement is intended to be used in the CAN Interrupt routine. It will read the CAN interrupt registers and stores it into a word variable.

Multiple Message Objects can cause an interrupt at the same time. This means that all message objects need to be checked for a possible interrupt.

In the example this is done with a For Next loop.

Cangetints ' read all the interrupts into variable _can_mobints

```vb
For _can_int_idx = 0 To 14 ' for all message objects  
If _can_mobints._can_int_idx = 1 Then ' if this message caused an interrupt

```
Canselpage _can_int_idx ' select message object  


The loop checks all bits and if a message object interrupt has been set, the message object will be selected with CANSELPAGE. 

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md)

Example