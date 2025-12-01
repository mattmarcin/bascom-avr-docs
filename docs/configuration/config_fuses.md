# CONFIG FUSES

Action

This configuration option sets the value of Xtiny,MegaX and AVRX fuses and lock bits.

Syntax

CONFIG FUSES=ON|OFF, LOCK=ON|OFF,FUSEx=f,urowx=u 

Remarks

The MCS UPDI programmer can insert the current fuse values into the code. You can also create the values yourself.

FUSES | ON or OFF.  ON - When programming the specified fuses will be programmed. OFF- When programming there will be no automatic programming When the CONFIG FUSES is inserted the value will also be set to OFF. So you must manually change it to ON.   
---|---  
LOCK | ON or OFF. ON - When ON and FUSES=ON, the lock bit will be programmed when the processors is programmed.  OFF- When programming the LOCK bits will be ignored. Thus the processor will not be locked.  When CONFIG FUSES is inserted the value will be set to OFF. So you need to manually set it to ON when you want the processor to be locked. Please take in mind that when the processor is locked you can not program it any longer. You need to use the UNLOCK option.  
FUSEx | The x is in the range from 0 to 7 depending on the processor. Some processors might have even more fuses.   
f | The value the fuse is set too. This is a numeric constant.   
UROWx | The x is in the range from 0 to 31 or less/more depending on the processor.  Userrow fuses can be set by the user. They can be read in your code by their register.   
  
The Xtiny/MegaX/AVRX platform has a lot of fuses. 

The advised method of getting the proper CONFIG FUSES :

\- set the fuses using the programmer Lock & Fuses TAB. 

\- do not set the lock byte. 

\- when satisfied, set the cursor at the proper place in your code

\- click the WRITE CONFIG button.

For example :

![mcs_updi_lock_fuse](mcs_updi_lock_fuse.png)

This will create this line of code : Config Fuses=Off,Lock=OFF,Fuse0=&H00,Fuse1=&H00,Fuse2=&H00,Fuse5=&HC9,Fuse6=&H00,Fuse7=&H00,Fuse8=&H00

As you can see, a fuse will only be listed when the value differs from the value 255 (&HFF)

See also

[$PROG](_prog.md)

Example

Config Fuses=Off,Lock=OFF,Fuse0=&H00,Fuse1=&H00,Fuse2=&H00,Fuse5=&HC9,Fuse6=&H00,Fuse7=&H00,Fuse8=&H00