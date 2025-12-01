# CONFIG CANMOB

Action

Configures one of the 15 CAN Message OBjects.

Syntax

CONFIG CANMOB=mob,BITLEN=bitlen,IDTAG=tag,IDMASK=mask,MSGOBJECT=mode,MSGLEN=msglen,AUTOREPLY=reply , CLEARMOB=clrmob

Remarks

mob | The mob(message object) is a number or variable with a range from 0-14. Number 15 is reserved by Atmel. There are 15 message objects you can use but only one set of registers. The CANPAGE register is used to select the proper MOB. This is all handled by the compiler. Internally, the mob you pass will set the CANPAGE register. When you use a value of -1 , the configuration is done on the current selected MOB (or CANPAGE). A reconfigure does not need to set the IDTAG and IDMASK again.  While you can use a constant or variable, you can not use a variable with a value of -1 to reconfigure the mob. A reconfigure requires a constant of -1.  
---|---  
bitlen | The CAN controller supports CAN messages with 11 bit ID's and with 29 bit ID's. And ID is an identifier. The lowest ID has the highest priority. Using 11 bit ID's has the advantage that it takes less time and as a result, you could send more messages. Just like with traffic, the bus capacity is limited. The baud rate and the message length all play a role. Valid values are 11 and 29. You can use a constant or variable. Using variables will increase code.   
idtag | The IDTAG is the identifier you assign to the message object. When the MOB is used for transmitting, the IDTAG is used for the CAN ID.  When the MOB is used for receiving, the IDTAG is used as a filter. Each time a message is sent or received, an interrupt is generated. This will interrupt the main process. For efficient usage, you need to set the IDTAG to filter only the ID's of interest. The IDMASK can be used together with the IDTAG to create a range. You can use a constant or variable to define the IDTAG. Using a variable will increase code.  
mask | The IDMASK is only used when the MOB is used in receiving mode.  It must be used together with IDTAG to create a range where the MOB will respond to. The following examples are for CAN rev A with 11 bit ID's. Example 1: you only want to filter ID &H0317. In this case you set the IDTAG to &H317. The IDMASK need to be set to &HFFFF in this case. A '1' for a bit in IDMASK means that the corresponding '1' in IDTAG is checked. When set a bit in IDMASK to '0' it means the corresponding bit in IDTAG can have any value. Full filtering: to accept only ID = 0x317 in part A. \- ID MSK = 111 1111 1111 b \- ID TAG = 011 0001 0111 b Example 2: you want to filter ID &H310-&H317. You can set the IDTAG to &H310 and the IDMASK to &HFFF8. The last 3 bits are set to 0 this way which means that &H310 is valid, but so is &H311, &H312, etc. Partial filtering: to accept ID from 0x310 up to 0x317 in part A. \- ID MSK = 111 1111 1000 b \- ID TAG = 011 0001 0xxx b Example 3: you want to filter from &H0000 to &H7FF. This means you need to respond to all messages. The IDMASK need to be set to 0. It will not matter to which value you set IDTAG since all 11 bits of IDMASK are set to 0. No filtering: to accept all ID from 0x000 up to 0x7FF in part A. \- ID MSK = 000 0000 0000 b \- ID TAG = xxx xxxx xxxx b You can use a constant or variable to define the IDMASK. Using a variable will increase code.  
mode | The mode in which the MOB will be used. \- DISABLED (0). The MOB is free to be used. \- TRANSMIT (1). The MOB data will be transmitted. \- RECEIVE (2). The MOB will wait for a message that matches the ID and MASK. \- RECEIVE_BUFFERED (3). This mode can be used to receive multiple frames. The CANSEND function will use the TRANSMIT mode. You should chose the DISABLED mode when configuring the MOB for transmission. Instead of the mentioned parameter names, you can also use a variable to set the mode. This variable must have a value between 0 and 3.  
msglen | This is the message length of the message in bytes. In receive mode you set it to the number of bytes you expect. The CANRECEIVE function will return the number of bytes read.  When the MOB is used for transmitting, it will define the length of the data. The length can also be 0 to send frames without data. The msglen can be a constant or variable. The maximum number of bytes that can be sent or received is 8.  
reply | This option can set ENABLED or DISABLED. If you use a variable, a 0 will disable auto reply, a 1 will enable auto reply. Auto reply can be used to reply to a remote frame. A remote frame is a frame without data. Since a remote frame has no data, you can reuse the MOB to send data as a reply to a remote frame.  
clrmob | By default all registers of a MOB are cleared when you configure the MOB. When you reconfigure the MOB, or want to respond to an auto reply, you do not want to clear the MOB. In such a case you can use CLEARMOB=NO to prevent clearing of the registers.  
  
While CONFIG CANMOB can dynamically set up the MOB (using variables instead of constants), it will increase code. So use a constant if possible.

See also

[CONFIG CANBUSMODE](config_canbusmode.md) , [CANBAUD](canbaud.md), [CANRESET](canreset.md), [CANCLEARMOB](canclearmob.md), [CANCLEARALLMOBS](canclearallmobs.md), [CANSEND](cansend.md), [CANRECEIVE](canreceive.md) , [CANID](canid.md), [CANSELPAGE](canselpage.md), [CANGETINTS](cangetints.md)

Example

```vb
Config Canmob = 0 , Bitlen = 11 , Idtag = &H0120 , Idmask = &H0120 , Msgobject = Receive , Msglen = 1 , Autoreply = Disabled 'first mob is used for receiving data  
Config Canmob = 1 , Bitlen = 11 , Idtag = &H0120 , Msgobject = Disabled , Msglen = 1 ' this mob is used for sending data

Config Canmob = -1 , Bitlen = 11 , Msgobject = Disabled , Msglen = 1 , Clearmob = No ' reconfig with value -1 for the current MOB and do not set ID and MASK

```