# CANBAUD

Action

Sets the baud rate of the CAN bus.

Syntax

CANBAUD = value

Remarks

All devices on the CAN bus need to have the same baud rate. The value must be a constant. The baud rate depends on the used crystal. The compiler uses the $CRYSTAL value to calculate the CAN baud rate. Higher baud rates require a higher system clock.

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

Canbaud = 125000 ' use 125 KB