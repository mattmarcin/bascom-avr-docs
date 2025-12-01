# MODBUS Slave/Server

The MODBUS protocol is used a lot in the industry. With the MODBUS add-on, you can create a slave or server. 

This add-on is a MODBUS server-RTU that implements function 03,06 and 16.(decimal) 

We use the term master and slave to indicate that there is at least one master, and that there is at least one slave device that will respond. 

A slave could be a master too. Another term is client/server. The server is the MODBUS device that will respond to the client. It is the same as master/slave and thus slave=server and master=client. 

Like a web server, the server does not initiate the communication. It simply waits for data and when it is addressed, it will respond.

When it is not addressed, it should not respond. When it is addressed, it should process the data and send a response. 

A client sends the following data : server address, function, data, checksum

The server address is a byte , the function code is a byte too. The data depends on the function and the checksum is a 16 bit CRC checksum. 

MODBUS uses the term registers for the data. A register is 16 bit width. You can pass words or integers with a single register. 

In order to send a long, single, double or string, you need to send multiple registers.

There are a lot of functions defined in the MODBUS protocol. The add-on implements the functions that are most suited for an own MODBUS server device.

These functions are :

•| 03 : read (multiple) register(s)  
---|---  
  
•| 06 : write a single register  
---|---  
  
•| 16 : write multiple registers  
---|---  
  
If needed you can add other functions yourself. The implemented functions should be sufficient however.

Constants

There are a few constants that you might need to change. 

Registersize : this constant defines how many registers can be processed. For example if a client asks to return 10 registers with function 03, you should set this constant to 10.

The reason for the constant is that RAM space is limited. And each register need storage space (2 bytes for each register) thus we do not want to take more bytes then needed.

Mdbg : this can be used for debugging. The add-on uses a Mega162 since it has 2 UARTS. One UART can be used for debugging. You need to set mdbg to a non-zero value to enable debugging to the serial port.

RS232-RS485

The protocol can be used with RS-232 and RS-485 and TCP/IP, etc. The add-on can be used with RS-232 and RS-485.

RS-485 half duplex needs a data direction pin. It is defined in the source like this :

Rs485dir Alias Portb.1

Config Rs485dir = Output

Rs485dir = 0

'Config Print1 = Portb.1 , Mode = Set

You can remark or remove the mark depending on the mode you need.

For testing, RS-232 is most simple.

TIMER

A timer is used to detect the start of a frame. With RTU (binary data) a silence of 3.5 characters is needed between frames. A frame is a complete MODBUS message.

A timer is used to detect such a silence. The statement : GENRELOAD , is used to generate the proper timer divisor and timer reload values. GENRELOAD will only work on TIMER0 and TIMER1. You pass the names of the constants which are free to chose, and in the sample are named _RL and _TS, and these constant values will be calculated and assigned to constants by the compiler. 

The TM_FRAME constant is the time of 4 characters. When the timer reaches this value it will overflow and execute the ISR_TMR0 interrupt. The interrupt routine will set the start state since now the server can expect an address.

In the TM_FRAME calculation the baud rate value is used. In the add on this is 9600. When you use a different value, you need to change the constant here as well.

Server Address

The server address need to be set. The MBSLAVE variable need to be set by you. Optional, you could change the variable into a constant. 

But when you use a DIP switch for example to set the address, it is better to use a variable.

Event mode

The MODBUS handeling is coded into a state machine and executed as a task. You can call the Modbustask() in your code yourself in the main program loop, or you can have it called in the interrupt of the buffered serial input routine. 

The sample uses the last option :

Config Serialin1 = Buffered , Size = 50 , Bytematch = All

Notice that BYTEMATCH = ALL is used so the Serial1bytereceived routine is called for every received byte. If the state is right, the modbustask code is executed and otherwise, the data is read to remove it from the buffer. Since there can be multiple slaves, the data will keep coming and we may only handle the data when we are addressed.

Functions

Each function that is requested will call a sub routine. 

Function 03 (read registers) : Sub Modbus03(addr3 As Word , Idx3 As Byte , Wval3 As Word) 

addr3 contains the address that was passed by the client. 

Idx3 contains an index in case multiple registers are read. It is 1 for the first register, 2 for the second, etc.

With these 2 values you can fill the wval3 value. 

In the sample, a select case is used to send different values. 

You should NOT change the addr3 and idx3 values ! There variables are passed by reference and changes will corrupt the data.

Notice that the function is called for each register. When the client want to read 2 word registers, the sub routine is called twice.

Function 06(write register) Sub Modbus06(addr3 As Word , Wval3 As Word) 

Addr3 contains the address that was passed by the client.

wval3 contains a word value passed by the client.

You can use the address to change some variable in your code.

Function 16 (write multiple registers) Sub Modbus16w(addr3 As Word , Idx As Byte , Bw As Word) 

Addr3 contains the address send by the client.

Idx contain the index to a word register.

Bw contains the value that was send.

Notice that the sub routine is called for each register. You can use the address and index to alter the proper variable in your code.

For functions that are not implemented, an error response will be sent.