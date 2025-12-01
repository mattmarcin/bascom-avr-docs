# CANSELPAGE

Action

Selects the Message Object index or page.

Syntax

CANSELPAGE index

Remarks

All 15 message objects share the same registers. With CANSELPAGE you select the index of the MOB you want to access.

The index is a constant or variable in the range of 0-14.

You should save and restore the CANPAGE register when changing the index. This is shown in the CAN [example](config_canbusmode.md).

See also

[CONFIG CANBUS](config_canbusmode.md) , [CONFIG CANMOB](config_canmob.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANGETINTS](cangetints.md)

Example