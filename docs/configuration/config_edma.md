# CONFIG EDMA

Action

Configures the enhanced direct memory access (DMA) module of the XMEGA.

Syntax

CONFIG EDMA=enabled|disabled, DOUBLEBUF=db, CPM=cpm , CHM=chm

Remarks

DMA | By default the DMA is disabled. Use ENABLED to enable the module.   
---|---  
db | DOUBLE BUFFER This options will set the double buffer mode. By default is is DISABLED. To allow for continuous transfer, two channels can be interlinked so that the second takes over the transfer when the first is finished and vice versa. This is called double buffering. When a transmission is completed for the first channel, the second channel is enabled. When a request is detected on the second channel, the transfer starts and when this is completed the first channel is enabled again Modes : \- DISABLED : No double buffer enabled \- CH01 : Double buffer enabled on channel0/1 \- CH23 : Double buffer enabled on channel2/3 \- CH01CH23 : Double buffer enabled on channel0/1 and channel2/3  
cpm | Channel Priority Mode If several channels request data transfer at the same time a priority scheme is available to determine which channel is allowed to transfer data. Application software can decide whether one or more channels should have a fixed priority or if a round robin scheme should be used. A round robin scheme means that the channel that last transferred data will have the lowest priority Modes : RR : Round Robin CH0RR123 : Channel0 > Round Robin (Channel 1, 2 and 3) CH01RR23 : Channel0 > Channel1 > Round Robin (Channel 2 and 3) CH0123 : Channel0 > Channel1 > Channel2 > Channel3  
chm | Channel Mode The channel mode selects the mode. Possible options for channel mode are : PER0123 : 4 peripheral channels 0,1,2,3 STD0 : 1 standard channel, 2 peripheral channels 2,3 STD2 : 2peripheral channels 0,1, 1 standard channel 2 STD02 : 2 standard channels 0,2  
  
You also need to set the individual EDMA channels using CONFIG EDMACHx. 

See also

[CONFIG DMACHx](config_dmachx.md) , [START DMACHx](start.md) , [CONFIG DMA](config_dma.md) , [CONFIG EDMAx](config_edmax.md)

Example

See [CONFIG DMACHx](config_dmachx.md)