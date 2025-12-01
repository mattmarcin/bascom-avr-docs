# CANID

Action

Returns the ID from the received CAN frame.

Syntax

value = CANID()

Remarks

The CANID function can return a 11 bit or 29 bit ID. You need to assign it to a WORD or DWORD variable. 

The CANID functions works at the current selected MOB and is typically used inside the CAN interrupt.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Dim _canid As Dword

_canid = Canid() ' read the identifier