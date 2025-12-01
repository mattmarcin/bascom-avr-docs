# ATXMEGA32E5

\- The XMEGA E series requires that you reset the interrupt yourself. For example : TCC4_INTflags.0=1 'clear OV flag 

\- The ERASE_APP NVM command (&H20) erases the complete flash, thus the boot space included. Use &H25 instead to erase and write a page.

\- There is a fixed map for the virtual ports : 

VPORT0 - Virtual port A

VPORT1 - Virtual port C

VPORT2 - Virtual port D

VPORT3 - Virtual port R

\- CONFIG XPIN slewrate is for the whole port, not for an individual pin

![atxmega8E5_16E5_32E5](atxmega8e5_16e5_32e5.png)