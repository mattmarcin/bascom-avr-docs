# ATXMEGA128A1

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet. 

![atxmega128](atxmega128.png)

Question: The DVDSON FUSE BIT the ATxmega A MANUAL says that for characterization data on VDROP and tSD consult the device data sheet.  
(Device: ATXMEGA128A1 RevH). But I can't find this Information in the datasheet ?  
  
Answer: The voltage spike detector has been removed from the latest revision of the XMEGA A manual.  
This is because we have, unfortunately, not been able to validate the spike detector fully.  
  
Question: The calibration byte in the production signature row show 0xFF and 0x00 for the ADC Calibration byte. Are these really the calibration values ?  
Errata of Rev H don't show something from calibration bytes. (Device: ATXMEGA128A1 RevH)  
  
Answer: Yes this is a known issue with ATXMEGA128A1 RevH. We will be fixing up this  
issue in the later version of the device.  
  
You should write the code for loading the calibration registers in the  
firmware so that when we fix it in the later version you do not have to fix  
the code. Also loading it now will not cause any problem in the ADC  
operation.