# CONFIG SERVOS

Action

Configures how much servoâs will be controlled.

Syntax

```vb
CONFIG SERVOS = X , ServoN = Portb.0 , Reload = rl [, INTERVAL=t] 

CONFIG SERVOS = X , ServoN = Portb.0 , MODE=mode , PRESCALE=pre

```
Syntax Xmega

CONFIG SERVOS = X , ServoN = Portb.0 , MODE=mode , TIMER= tmr, PRESCALE=pre

Remarks

Servoâs need a variable pulse in order to operate. The CONFIG SERVOS directive will set up a byte array with the servo pulse width values and will initialize an ISR that uses TIMER0.

X | The number of servoâs you want to control. Each used servo will use one byte of SRAM.  
---|---  
servoN | The port pin the servo is attached too. N represents a value between 1 and 10. When you specify that you will use multiple servo's you need to specify a pin for each servo. Like : config servos=3, servo1=portb.0, servo2=portb.2, servo3=portC.4  
reload | The reload value for the ISR in uS. This is the overflow rate of the timer. So when 100 is used, it means that each 100 uS an interrupt will occur to update the servo variables.  
Interval | The update interval. Using the interval option will result in using alternative servo code optimized for servos.  
Mode | The normal default modes use software PWM with a relatively high frequency. This will give a big processor load since the timer ISR is executed many times. It allows to create create precise pulses in small steps. But when controlling a simple RC servo, it is also possible to use a lower refresh rate which will result in lower processor load.  MODE=SERVO will work for normal AVR and XMEGA. You do not need to specify the interval or reload value.   
Prescale | The prescale value is calculated so that the 8 bit timer interrupt is executed every 2 ms. Inside the interrupt, the servo pin is made high for the value of the servo() array. Then the next time inside the ISR, the pin is set low for the reset of the time. It depends on the processor frequency if you get a good range. In the report you can find the used prescale value as a constant named _SERVO_PRESCALER. When you do not get a full servo swing, you might want to try a higher prescale value. The prescale parameter overrides the automatic calculation.  
Timer | This is for XMEGA only. Specify the name of the timer that will be used in interrupt mode.  
  
PWM MODE

When you use for example :

Config Servos = 2 , Servo1 = Portb.0 , Servo2 = Portb.1 , Reload = 10

The internal ISR will execute every 10 uS.

An arrays named SERVO() will be created and it can hold 2 bytes : servo(1) and servo(2).

By setting the value of the servo() array you control how long the positive pulse will last. After it has reached this value it will be reset to 0.

The reload value should be set to 10. After 20 mS, a new pulse will be generated.

You can use other reload values but it will also mean that the repeat value will change.

The PORT pins specified must be set to work as an output pin by the user.

CONFIG PINB.0 = OUTPUT

Will set a pin to output mode.

The CONFIG SERVOS only works with servo's that rotate 180 degrees. These are the servo's found in RC models.

There are also continuous rotation servos which work different. The servo code will NOT work on these servos.

Alternative Servocode

When using the INTERVAL option, you can use alternative code which is optimized for servo's.(this is however not the MODE=SERVO)

You should use a RELOAD value of 100 in that case and an interval of 100 should be used for best results.

Using a reload of 100 uS will give more time to the main application. This does give lower resolution but this is not a problem for most model servos. With an interval of 100, the refresh will be done in 100x100 us which results in 10 mS.

The following test code was used:

Config Servos = 2 , Servo1 = Portd.7 , Servo2 = Portb.1 , Reload = 100 , Interval = 100

Servo(1) = 10

Servo(2) = 5

```vb
Enable Interrupts

Do

For J = 8 To 16

```
Servo(1) = J

```vb
Waitms 5000 ' some time to check if the servo is stable

Next

Waitms 5000

Loop

```
SERVO mode

The MODE=SERVO can be used for normal AVR and XMEGA. It results in a lower processor load.

XMEGA

The Xmega has several timers. You must specify the timer to be used. 

The Xmega has 16 bit timers and instead of a byte array, a word array is created for the servo values.

The Xmega can also create pulses with it's timers without the need of interrupts. But this mode demands that you use fixed CCx pins. The software servo pulse mode, allows you to chose any pin.

Resources used

TIMER0 is used to create the ISR. Xmega will use TCxx.

NOTE

The servo() value is not absolute. It will depend on the processor clock. This means that these values might need an adjustment when you alter the $crystal value.

Example PWM mode

```vb
'-----------------------------------------------------------------------------------------

'name : servos.bas

'copyright : (c) 1995-2025, MCS Electronics

'purpose : demonstrates the SERVO option

'micro : 90S2313

'suited for demo : yes

'commercial addon needed : no

'-----------------------------------------------------------------------------------------

$regfile = "2313def.dat" ' specify the used micro

$crystal = 4000000 ' used crystal frequency

$baud = 19200 ' use baud rate

$hwstack = 32 ' default use 32 for the hardware stack

$swstack = 10 ' default use 10 for the SW stack

$framesize = 40 ' default use 40 for the frame space

'Servo's need a pulse in order to operate

'with the config statement CONFIG SERVOS we can specify how many servo's we

'will use and which port pins are used

'A maximum of 14 servos might be used

'The SERVO statements use one byte for an interrupt counter and the TIMER0

'This means that you can not use TIMER0 anymore

'The reload value specifies the interval of the timer in uS

'Config Servos = 2 , Servo1 = Portb.0 , Servo2 = Portb.1 , Reload = 10

Config Servos = 1 , Servo1 = Portb.0 , Reload = 10

'as an option you can use TIMER1

'Config Servos = 2 , Servo1 = Portb.0 , Servo2 = Portb.1 , Reload = 10 , Timer = Timer1

'we use 2 servos with 10 uS resolution(steps)

'we must configure the port pins used to act as output

Config Portb = Output

'finally we must turn on the global interrupt

Enable Interrupts

'the servo() array is created automatic. You can used it to set the

'time the servo must be on

```
Servo(1) = 10 '10 times 10 = 100 uS on

```vb
'Servo(2) = 20 '20 times 10 = 200 uS on

Do

Loop

Dim I As Byte

Do

For I = 0 To 100

```
Servo(1) = I

```vb
Waitms 1000

Next

For I = 100 To 0 Step -1

' Servo(1) = I

Waitms 1000

Next

Loop

End

```
Example SERVO mode

```vb
'-----------------------------------------------------------------------------------  
' (c) 1995-2025, MCS Electronics  
' servos-timer0.bas  
'-----------------------------------------------------------------------------------  
$regfile = "m88def.dat"  
$crystal = 8000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
  
  
Config Com1 = 19200 , Parity = None , Stopbits = 1 , Databits = 8  
Print "Servo test"  
  
Config Servos = 2 , Mode = Servo , Servo1 = Portb.0 , Servo2 = Portb.1  
'Config Servos = 2 , Mode = Servo , Servo1 = Portb.0 , Servo2 = Portb.1 , Prescale= 256  
  
' you need to chose SERVO mode for lowest system resources  
Enable Interrupts ' you must enable interrupts since timer 0 is used in interrupt mode  
  
  
Dim Key As Byte  
'notice that servo() array is a byte array, which is created automatic  
  
Do  
```
Key = Inkey() ' get data from serial port  
If Key = "l" Then 'left  
Servo(1) = 100  
Servo(2) = 100  
Elseif Key = "m" Then ' middle  
Servo(1) = 170  
Servo(2) = 170  
Elseif Key = "r" Then ' right  
Servo(1) = 255  
Servo(2) = 255  
Elseif Key <> 0 Then ' enter user value  
Input "Servo1 " , Servo(1)  
Servo(2) = Servo(1)  
```vb
End If  
Loop

```
Example XMEGA SERVO mode

```vb
'-----------------------------------------------------------------------------------  
' (c) 1995-2025, MCS Electronics  
' xmega-servo.bas  
'-----------------------------------------------------------------------------------  
$regfile = "xm128a1def.dat"  
$crystal = 32000000  
$hwstack = 64  
$swstack = 64  
$framesize = 64  
  
  
Config Osc = Enabled , 32mhzosc = Enabled  
  
'configure the systemclock  
Config Sysclock = 32mhz , Prescalea = 1 , Prescalebc = 1_1  
  
Config Com1 = 19200 , Mode = Asynchroneous , Parity = None , Stopbits = 1 , Databits = 8  
Print "Servo test"  
  
Config Servos = 2 , Mode = Servo , Timer = Tcc0 , Servo1 = Portb.0 , Servo2 = Portb.1  
' you need to chose SERVO mode and you must provide the name of the timer that will be used for the system tick  
Enable Interrupts ' you must enable interrupts since timer TCC0 is used in interrupt mode  
  
  
Dim Key As Byte  
'notice that servo() array is a word array, which is created automatic  
  
Do  
```
Key = Inkey() ' get data from serial port  
If Key = "l" Then 'left  
Servo(1) = 12800  
Servo(2) = 12800  
Elseif Key = "m" Then ' middle  
Servo(1) = 19200  
Servo(2) = 19200  
Elseif Key = "r" Then ' right  
Servo(1) = 40000  
Servo(2) = 40000  
Elseif Key <> 0 Then ' enter user value  
Input "Servo1 " , Servo(1)  
Servo(2) = Servo(1)  
```vb
End If  
Loop

```