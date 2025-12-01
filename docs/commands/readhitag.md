# READHITAG

Action

Read HITAG RFID transponder serial number.

Syntax

result = READHITAG(var) 

Remarks

result | A numeric variable that will be 0 if no serial number was read from the transponder. It will return 1 if a valid number was read.  
---|---  
  
RFID is used for entrance systems, anti theft, and many other applications where a wireless chip is an advantage over the conventional magnetic strip and chip-card. 

The HITAG series from Philips(NXP) is one of the oldest and best available. The HTRC110 chip is a simple to use chip that can read and write transponders. Each transponder chip has a 5 byte(40 bits) unique serial number.

The only disadvantage of the HTRC110 is that you need to sign an NDA in order to get the important documents and 8051 example code.

When the transponder is held before the coil of the receiver, the bits stream will be modulated with the bit values. Just like RC5, HITAG is using Manchester encoding. This is a simple and reliable method used in transmission systems.

Manchester encoding is explained very well at the [Wiki](<http://en.wikipedia.org/wiki/Manchester_code>) Manchester page.

![manchester_encoding](manchester_encoding.png)

The image above is copied from the Wiki. 

There are 2 methods to decode the bits. You can detect the edges of the bits and sample on 3/4 of the bit time.

Another way is to use a state machine. The state machine will check the length between the edges of the pulse. It will start with the assumption that there is a (1). Then it will enter the MID1 state. If the next pulse is a long pulse, we have received a (0). When it received a short pulse, we enter the start1 state. Now we need to receive a short space which indicated a (1), otherwise we have an invalid state. When we are in the MID0 state, we may receive a long space(1) or a short space. All others pulses are invalid and lead to a restart of the pulse state(START).

Have a look at the image above. Then see how it really works. We start with assuming a (1). We then receive a long pulse so we receive a (0). Next we receive a long space which is a (1). And again a long pulse which is a (0) again. Then we get a short space and we are in start1 state. We get a short pulse which is a (0) and we are back in MID0 state. The long space will be a (1) and we are in MID1 state again. etc.etc. When ever we receive a pulse or space which is not defined we reset the pulse state machine.

![manchester_decoding](manchester_decoding.png)

At 125 KHz, the bit time is 512 uS. A short pulse we define as halve a bit time which is 256 uS.

We use a 1/4 of the bit time as an offset since the pulses are not always exactly precise.

So a short bit is 128-384(256-128 - 256+128 ) uS. And a long bit is 384-640 uS (512-128 - 512+128).

We use TIMER0 which is an 8 bit timer available in all AVR's to determine the time. 

Since most micro's have an 8 MHz internal clock, we run the program in 8 MHz. It depends on the pre scaler value of the timer, which value are used to determine the length between the edges.

You can use 64 or 256. The generated constants are : _TAG_MIN_SHORT, _TAG_MAX_SHORT , _TAG_MIN_LONG and _TAG_MAX_LONG. 

We need an interrupt to detect when an edge is received. We can use the INTx for this and configure the pin to interrupt when a logic level changes. Or we can use the PIN interrupt so we can use more pins.

The sample contains both methods. 

It is important that the ReadHitag() functions needs a variable that can store 5 bytes. This would be an array.

And you need to check the _TAG constants above so that they do not exceed 255. 

When you set up the interrupt, you can also use it for other tasks if needed. You only need to call the _checkhitag routine in the subroutine. And you need to make sure that the additional code you write does not take up too much time.

When you use the PCINT interrupt it is important to realize that other pins must be masked off. The PCMSK register may have only 1 bit enabled. Otherwise there is no way to determine which pin was changed. 

EM4095

The EM4095 is similar to the HTRC110. The advantage of the EM4095 is that it has a synchronized clock and needs no setup and less pins.

The EM4095 library uses the same method as the RC5 decoding : the bit is sampled on 3/4 of the bit length. The parity handling is the same. The EM4095 decoding routine is smaller then the HTRC110 decoding library.

A reference design for the EM4095 will be available from MCS.

See also

[READMAGCARD](readmagcard.md) , [CONFIG HITAG](config_hitag.md)

Example

See [CONFIG HITAG ](config_hitag.md)for 2 examples.