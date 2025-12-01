# CONFIG DMXSLAVE

Action

Configures the DMX-512 slave.

Syntax

CONFIG DMXSLAVE = com, Channels=nchannels, DmxStart = nstart, Store=nstore

Remarks

com | The UART you want to use for the communication with the DMX-512 bus. This depends on the micro processor. In most cases this is COM1.   
---|---  
Channels | A numeric constant that defines the maximum number of channels you can receive. When you like to process all DMX data, you need to use 512 since 512 is the maximum. When you make a simple device a number of 8 would be sufficient.  
DmxStart | The slave starting address. This is 1 by default. You will receive data starting at address 'Start'.  
Store | The number of bytes you will receive and store.  
  
You must chose the crystal/oscillator speed in a way that 250000 baud will give no errors. Typical 4, 8 and 16 MHz will work fine.

When you want to be sure, check the compiler report. It should have 0% error.

Since the DMX slave is running in interrupt mode on the background, you must ENABLE interrupts.

The serial interrupts used, is enabled by the CONFIG DMXSLAVE command.

So how does this work? When you configure the DMXSLAVE, it will receive data in interrupt mode. It will store the data into a byte arrays named _DMX_RECEIVED

The first byte stored into this array is the value for address 'DMXSTART' : the address you defined with DMXSTART.

The number of bytes stored in the array depends on the 'STORE' setting. 

Example : Config Dmxslave = Com1 , Channels = 16 , DmxStart = 3 , Store = 1 

This will setup an array _DMX_RECEIVED that can hold 16 bytes. So the maximum value for STORE would be 16 too. In the example our address is 3, and we store only address 3. 

We can dynamic change the DMXSTART address and the number of bytes to get !

For this purpose you can change the automatic generated internal variables _DMX_ADDRESS and _DMX_CHANNELS_TOGET

_DMX_ADDRESS defines the starting address. And _DMX_CHANNELS_TOGET defines the number of bytes to store after the address matches.

All platforms are supported. 

See also

NONE

Example

```vb
'-----------------------------------------------------------------

' dmx-receive.bas

' (c) 1995-2025 MCS Electronics

' this sample demonstates receiving a DMX datastream in the background

'-----------------------------------------------------------------

'we use a chip with 2 UARTS so we can print some data

$regfile = "m162def.dat"

'you need to use a crystal that can generate a good 250 KHz baud

'For example 8 Mhz, 16 or 20 Mhz

$crystal = 8000000

'define the stack

$hwstack = 40

$swstack = 32

$framesize = 32

'these are the pins we use. COM1/UART1 is used for the DMX data

' TX RX

' COM1 PD.1 PD.0 DMX

' COM2 PB.3 PB.2 RS-232

Config Dmxslave = Com1 , Channels = 16 , DMXstart = 3 , Store = 1

'this will set up the code. an array named _dmx_channels will contain the data

'the channels will define the size. So when you want to receive data for 8 channels, you set it to 8.

'the maximum size is 512 for retrieving all data

'START defines the starting address. By default it is 1. Thus the array will be filled starting at address 3 in the example

'STORE defines how many bytes you want to store

'By default, 1 channel is read. But you can alter the variable _dmx_channelels_toget to specify how many bytes you want to receive

'So essential you need to chose how many bytes you like to receive. Most slaves only need 1 - 3 bytes. It would be a waste of space to define more channels then,

'Then you set the slave address with the variable : _dmx_address , which is also set by the optional [START]

'And finally you chose how many bytes you want to receive that start at the specified address. You do this by setting the _dmx_channels_toget variable.

'Example :

' Config Dmxslave = Com1 , Channels = 16 , Start = 300 , Store = 4

' this would store the bytes from address 300 - 303. the maximum would be 315 since channels is set to 16

' Config Dmxslave = Com1 , Channels = 8 , Start = 1 , Store = 8

' this would store the bytes from address 1 - 8. the maximum would be 8 since channels is set to 8

Config Com2 = 19200 , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

```
Open "COM2:" For Binary As #1

```vb
Print #1 , "MCS DMX-512 test"

'since DMX data is received in an ISR routine, you must enable the global interrupts

Enable Interrupts

Dim J As Byte

Do

If Inkey(#1) = 32 Then ' when you press the space bar

For J = 1 To _dmx_channels ' show the data we received

Print #1 , _dmx_received(j) ; " " ;

Next

Print #1,

```
Elseif Inkey(#1) = 27 Then 'you ca dynamic change the start address and the channels

```vb
Input #1 , "start " , _dmx_address

Input #1 , "channels " , _dmx_channels_toget

End If

Loop

'typical you would read a DIP switch and use the value as the address

End

```