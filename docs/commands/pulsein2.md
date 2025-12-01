# PULSEIN

The full version includes a lib named pulsein.lib. It overloads the [PULSEIN](pulsein.md) statement. This special lib allows to set a custom timeout and delay.

You need to add the following to your code :

const cPulseIn_Timeout = 0 'This is the default timeout value. When you increase the value you will get a shorter time out period.

```vb
dim bPulseIn_Delay as byte : bPulseIn_Delay = 10 'For 10 uS units , the default is 1

$lib "pulsein.lib" 'include the lib to overload the function

```
The library is compatible with the default lib.