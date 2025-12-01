# View Show Allert Window

Action

Shows the Alert Windows when available.

An alert window can contain various info. In version 2086 it is limited to show when COM ports are added or removed.

When you use a CDC device (virtual COM port) and you plug the device, depending on settings and hub/usb port a new COM number will be assigned.

In the lower right of the screen an alert window/message will appear. It will not have focus and it will fade away after some time.

Below are 2 examples. One when a new COM port is found. And one when that same COM port is removed.

![alert_show_new_com](alert_show_new_com.png)

![show_alert_com_removed](show_alert_com_removed.png)

The X on the alert window can be used to close the window.

The X on the bottom can be used to Delete the window.

When you close a window, it will exist until BasCom is closed.

For this reason the 'View Show Alert Windows option exists : you can show the old alerts.

A new alert is always added after the last message. So in this example the first message was the NEW com port. 

And when the cable was pulled, the second alert was added. 

When multiple alert windows exist, you can use << and >> to scroll through them.