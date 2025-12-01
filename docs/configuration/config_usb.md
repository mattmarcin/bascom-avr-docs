# CONFIG USB

Action

Create settings related to USB.

Syntax

CONFIG USB = dev, Language= lang, Manufact= "man", Product="prod" , Serial="serial"

Remarks

Dev | The possible options are Device and Host. Host is not supported yet.  
---|---  
Lang | A language identifier. &H0409 for US/English  
Man | A string constant with the manufacture name.   
Prod | A string constant with the product name.  
Serial  | A string constant with the serial number.  
  
The above settings determine how your device is displayed by the operating system.

Since these settings end up in flash code space, it is best to chose short names. There is no limit to the length other then the USB specifications impose, but keep it short as possible. Strings in USB are UNI coded. Which mean that a word is used for each character. with normal ASCII coding, only a byte is used for each character.

For a commercial USB device you need to give it a unique VID & PID combination. When you plan to use it at home, this is not needed.

You can buy a Vendor ID (VID) from the USB organization. This cost 2000 $.

As a service MCS offers a PID in the on line shop. This cost little and it gives you a unique Product ID(PID) but with the MCS Electronics VID.

![notice](notice.jpg)Notice that using CONFIG USB will include a file named USBINC.BAS. This file is not part of the BASCOM setup/distribution. It is available as a commercial add on. The add on package includes 3 samples , the include file, and a special activeX for the HID demo.

None of the samples require a driver. A small UB162 module with normal pins is available from the on line shop too.

The first supported USB devices are USB1287, USB162.

See also

NONE

Example

```vb
$regfile = "usb162.dat"

$crystal = 8000000

$baud = 19200

```
Const Mdbg = 1

```vb
Config Clockdiv = 1

Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

```
Const Vendor_id = &H16D0 ' MCS Vendor ID

Const Product_id = &H201D ' MCS product ID, you can buy a VID&PID in the MCS shop

Const Ep_control_length = 32

Const User_conf_size = 41

Const Size_of_report = 53

Const Device_class = 0

Const Device_sub_class = 0

Const Device_protocol = 0

Const Release_number = &H1000

Const Length_of_report_in = 8

Const Length_of_report_out = 8

Const Interface_nb = 0

Const Alternate = 0

Const Nb_endpoint = 2

Const Interface_class = 3 ' HID

Const Interface_sub_class = 0

Const Interface_protocol = 0

Const Interface_index = 0

```vb
Config Com1 = Dummy , Synchrone = 0 , Parity = None , Stopbits = 1 , Databits = 8 , Clockpol = 0

Print "USB GENERIC test"

Declare Sub Usb_user_endpoint_init

Declare Sub Hid_test_hit()

Declare Sub Hid_task()

Declare Sub Hid_task_init()

```
Const Usb_config_attributes_reserved = &H80

Const Usb_config_buspowered = Usb_config_attributes_reserved

Const Usb_config_selfpowered = Usb_config_attributes_reserved Or &H40

Const Usb_config_remotewakeup = Usb_config_attributes_reserved Or &H20

Const Nb_interface = 1

Const Conf_nb = 1

Const Conf_index = 0

Const Conf_attributes = Usb_config_buspowered

Const Max_power = 50 ' 100 mA

Const Interface_nb_mouse = 0

Const Alternate_mouse = 0

Const Nb_endpoint_mouse = 1

Const Interface_class_mouse = 3 ' HID Class

Const Interface_sub_class_mouse = 1 ' Sub Class is Mouse

Const Interface_protocol_mouse = 2 ' Mouse

Const Interface_index_mouse = 0

Const Nb_endpoints = 2 ' number of endpoints in the application including control endpoint

Const Ep_kbd_in = 1 ' Number of the mouse interrupt IN endpoint

Const Ep_hid_in = 1

Const Ep_hid_out = 2

Const Endpoint_nb_1 = Ep_hid_in Or &H80

Const Ep_attributes_1 = 3 ' BULK = 0x02, INTERUPT = 0x03

Const Ep_in_length_1 = 8

Const Ep_size_1 = Ep_in_length_1

Const Ep_interval_1 = 20 ' Interrupt polling interval from host

Const Endpoint_nb_2 = Ep_hid_out

Const Ep_attributes_2 = 3 ' BULK = 0x02, INTERUPT = 0x03

Const Ep_out_length = 8

Const Ep_size_2 = Ep_out_length

Const Ep_interval_2 = 20 ' interrupt polling from host

```vb
Config Usb = Device , Language = &H0409 , Manufact = "MCS" , Product = "MCSHID162" , Serial = "MC0001"

'Dim some user vars

Dim Usb_kbd_state As Byte , Usb_key As Byte , Usb_data_to_send As Byte

Dim Dummy As Byte , Dummy1 As Byte , Dummy2 As Byte

Print "task init"

```
Usb_task_init

Hid_task_init

Do

Usb_task

Hid_task

```vb
'you can call your sub program here

Loop

'nothing needed to init

Sub Hid_task_init()

'nothing

end sub

'HID task must be checked regular

Sub Hid_task()

If Usb_connected = 1 Then ' Check USB HID is enumerated

```
Usb_select_endpoint Ep_hid_out ' Get Data Repport From Host

If Ueintx.rxouti = 1 Then ' Is_usb_receive_out())

Dummy1 = Uedatx : Print "Got : " ; Dummy1

Dummy2 = Uedatx : Print "Got : " ; Dummy2

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Dummy = Uedatx : Print "Got : " ; Dummy

Usb_ack_receive_out

```vb
End If

If Dummy1 = &H55 And Dummy2 = &HAA Then ' Check if we received DFU mode command from host

```
Usb_detach ' Detach Actual Generic Hid Application

```vb
Waitms 500

Goto &H1800 'goto bootloader

'here you could call the bootloader then

End If

```
Usb_select_endpoint Ep_hid_in ' Ready to send these information to the host application

If Ueintx.txini = 1 Then ' Is_usb_in_ready())

Uedatx = 1

Uedatx = 2

Uedatx = 3

Uedatx = 4

Uedatx = 5

Uedatx = 6

Uedatx = 7

Uedatx = 8

Usb_ack_fifocon ' Send data over the USB

```vb
End If

End If

End Sub

Function Usb_user_read_request(type As Byte , Request As Byte) As Byte

#if Mdbg

Print "USB_USER_READ_REQ"

#endif

```
Usb_string_type = Uedatx 'Usb_read_byte();

Usb_descriptor_type = Uedatx 'Usb_read_byte();

Usb_user_read_request = 0

```vb
Select Case Request

Case Get_descriptor:

Select Case Usb_descriptor_type

Case Report : Call Hid_get_report()

```
Usb_user_read_request = 1

Case Hid : Call Hid_get_hid_descriptor()

Usb_user_read_request = 1

Case Else

Usb_user_read_request = 0

```vb
End Select

Case Set_configuration:

Select Case Usb_descriptor_type

Case Set_report : Call Hid_set_report()

```
Usb_user_read_request = 1

Case Else

Usb_user_read_request = 0

```vb
End Select

Case Get_interface:

'// usb_hid_set_idle();

```
Call Usb_hid_get_interface()

Usb_user_read_request = 1

Case Else

Usb_user_read_request = 0

```vb
End Select

End Function

'usb_init_device.

'This function initializes the USB device controller and

'configures the Default Control Endpoint.

Sub Usb_init_device()

#if Usbfunc

```
Usb_select_device

```vb
#endif

#if Usbfunc

If Usbsta.id = 1 Then 'is it an USB device?

#endif

```
Uenum = Ep_control ' select USB endpoint

If Ueconx.epen = 0 Then ' usb endpoint not enabled yet

Call Usb_configure_endpoint(ep_control , Type_control , Direction_out , Size_32 , One_bank , Nyet_disabled)

```vb
End If

#if Usbfunc

End If

#endif

End Sub

Sub Usb_user_endpoint_init(byval Nm As Byte)

```
Call Usb_configure_endpoint(ep_hid_in , Type_interrupt , Direction_in , Size_8 , One_bank , Nyet_enabled)

Call Usb_configure_endpoint(ep_hid_out , Type_interrupt , Direction_out , Size_8 , One_bank , Nyet_enabled)

End Sub

Usb_dev_desc:

Data 18 , Device_descriptor 'size and device_descriptor

Data 0 , 2 'Usb_write_word_enum_struc(USB_SPECIFICATION)

Data Device_class , Device_sub_class ' DEVICE_CLASS and DEVICE_SUB_CLASS

Data Device_protocol , Ep_control_length ' device protol and ep_control_length

Data Vendor_id% ' Usb_write_word_enum_struc(VENDOR_ID)

Data Product_id% ' Usb_write_word_enum_struc(PRODUCT_ID)

Data Release_number% ' Usb_write_word_enum_struc(RELEASE_NUMBER)

Data Man_index , Prod_index ' MAN_INDEX and PROD_INDEX

Data Sn_index , Nb_configuration ' SN_INDEX and NB_CONFIGURATION

Usb_conf_desc:

Data 9 , Configuration_descriptor ' length , CONFIGURATION descriptor

Data User_conf_size% ' total length of data returned

Data Nb_interface , Conf_nb ' number of interfaces for this conf. , value for SetConfiguration resquest

Data Conf_index , Conf_attributes ' index of string descriptor , Configuration characteristics

Data Max_power ' maximum power consumption

Data 9 , Interface_descriptor 'length , INTERFACE descriptor type

Data Interface_nb , Alternate 'Number of interface , value to select alternate setting

Data Nb_endpoint , Interface_class 'Number of EP except EP 0 ,Class code assigned by the USB

Data Interface_sub_class , Interface_protocol 'Sub-class code assigned by the USB , Protocol code assigned by the USB

Data Interface_index 'Index Of String Descriptor

Data 9 , Hid_descriptor 'length , HID descriptor type

Data Hid_bdc% , 8 ' Binay Coded Decimal Spec. release , Hid_country_code

Data Hid_class_desc_nb , Hid_descriptor_type 'Number of HID class descriptors to follow , Report descriptor type

Data Size_of_report% 'HID KEYBOARD LENGTH

Data 7 , Endpoint_descriptor ' Size Of This Descriptor In Bytes , ENDPOINT descriptor type

Data Endpoint_nb_1 , Ep_attributes_1 ' Address of the endpoint ,Endpoint's attributes

Data Ep_size_1% ' Maximum packet size for this EP , Interval for polling EP in ms

Data Ep_interval_1

Data 7 , Endpoint_descriptor ' Size Of This Descriptor In Bytes , ENDPOINT descriptor type

Data Endpoint_nb_2 , Ep_attributes_2 ' Address of the endpoint , Endpoint's attributes

Data Ep_size_2% ' Maximum packet size for this EP

Data Ep_interval_2 ' Interval for polling EP in ms

Usb_hid_report:

Data &H06 , &HFF , &HFF ' 04|2 , Usage Page (vendordefined?)

Data &H09 , &H01 ' 08|1 , Usage (vendordefined

Data &HA1 , &H01 ' A0|1 , Collection (Application)

' // IN report

Data &H09 , &H02 ' 08|1 , Usage (vendordefined)

Data &H09 , &H03 ' 08|1 , Usage (vendordefined)

Data &H15 , &H00 ' 14|1 , Logical Minimum(0 for signed byte?)

Data &H26 , &HFF , &H00 ' 24|1 , Logical Maximum(255 for signed byte?)

Data &H75 , &H08 ' 74|1 , Report Size(8) = field size in bits = 1 byte

Data &H95 , Length_of_report_in ' 94|1:ReportCount(size) = repeat count of previous item

Data &H81 , &H02 ' 80|1: IN report (Data,Variable, Absolute)

' // OUT report

Data &H09 , &H04 ' 08|1 , Usage (vendordefined)

Data &H09 , &H05 ' 08|1 , Usage (vendordefined)

Data &H15 , &H00 ' 14|1 , Logical Minimum(0 for signed byte?)

Data &H26 , &HFF , &H00 ' 24|1 , Logical Maximum(255 for signed byte?)

Data &H75 , &H08 ' 74|1 , Report Size(8) = field size in bits = 1 byte

Data &H95 , Length_of_report_out ' 94|1:ReportCount(size) = repeat count of previous item

Data &H91 , &H02 ' 90|1: OUT report (Data,Variable, Absolute)

' // Feature report

Data &H09 , &H06 ' 08|1 , Usage (vendordefined)

Data &H09 , &H07 ' 08|1 , Usage (vendordefined)

Data &H15 , &H00 ' 14|1 , LogicalMinimum(0 for signed byte)

Data &H26 , &HFF , &H00 ' 24|1 , Logical Maximum(255 for signed byte)

Data &H75 , &H08 ' 74|1 , Report Size(8) =field size in bits = 1 byte

Data &H95 , &H04 ' 94|1:ReportCount

Data &HB1 , &H02 ' B0|1: Feature report

Data &HC0 ' C0|0 , End Collection