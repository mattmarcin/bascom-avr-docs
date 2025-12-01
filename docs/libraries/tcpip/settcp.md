# SETTCP

Action

Configures or reconfigures the TCP/IP chip.

Syntax

SETTCP MAC , IP , SUBMASK , GATEWAY

Remarks

MAC | The MAC address you want to assign to the ethernet chip. The MAC address is a unique number that identifies your chip. You must use a different address for every W3100A chip in your network. Example : 123.00.12.34.56.78 You need to specify 6 bytes that must be separated by dots. The bytes must be specified in decimal notation.  
---|---  
IP | The IP address you want to assign to the ethernet chip. The IP address must be unique for every ethernet chip in your network. When you have a LAN, 192.168.0.10 can be used. 192.168.0.x is used for LANâs since the address is not an assigned internet address.  
SUBMASK | The sub mask you want to assign to the W3100A. The sub mask is in most cases 255.255.255.0  
GATEWAY | This is the gateway address of the ethernet chip. The gateway address you can determine with the IPCONFIG command at the command prompt : C:\>ipconfig Windows 2000 IP Configuration Ethernet adapter Local Area Connection 2: Connection-specific DNS Suffix . : IP Address. . . . . . . . . . . . : 192.168.0.3 Subnet Mask . . . . . . . . . . . : 255.255.255.0 Default Gateway . . . . . . . . . : 192.168.0.1 Use 192.168.0.1 in this case.  
  
The CONFIG TCPIP statement may be used only once.

When you want to set the TCP/IP settings dynamically for instance when the settings are stored in EEPROM, you can not use constants. For this purpose, SETTCP must be used.

SETTCP can take a variable or a constant for each parameter.

When you set the TCP/IP settings dynamically, you do not need to set them with CONFIG TCPIP. In the CONFIG TCPIP you can use the NOINIT parameter so that the MAC and IP are not initialized which saves code.

See also

[GETSOCKET](getsocket.md) , [SOCKETCONNECT](socketconnect.md), [SOCKETSTAT](socketstat.md) , [TCPWRITE](tcpwrite.md), [TCPWRITESTR](tcpwritestr.md), [TCPREAD](tcpread.md), [SOCKETCLOSE](socketclose.md) , [SOCKETLISTEN](socketlisten.md) , [CONFIG TCPIP](config_tcpip.md) , [SOCKETDISCONNECT](socketdisconnect.md) , [GETTCPREGS](gettcpregs.md) , [SETTCPREGS](settcpregs.md)

Example

See the DHCP.BAS example from the BASCOM Sample dir.