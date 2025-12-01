# QSIN

Action

Returns the sinus of an integer

Syntax

var = QSIN( source )

Remarks

Var | A numeric integer variable that is assigned with sinus of variable source.  
---|---  
source | The integer variable to get the sinus of.  
  
Integer SIN and COS use a lookup table to determine the Sinus or Co sinus. Qsin and Qcos are used by some of the FT800 routines.

![qsin](qsin.png)

The sinus of angle α is shown above. At 0 degrees the value on the y-ax is 0 and at 90 degrees, the value is at its maximum on the Y-ax. In the first quadrant of the circle (1) sinus will have a positive number as a result. In quadrant 2 of the circle, the sinus goes from the maximum value down to 0 and the result is a positive number as well.

In quadrant 3 and 4 of the circle, we will get a negative number as a result since the result is below the x-ax.

The QSIN works with integers which have a range from -32768 to 32767. This means that for the quadrant 1 and 2 we can use a value between 0 and 32767. In degrees we would use a value between 0 and 180. This means that each degree has a value of 182 (32767/180). 

The negative values are reserved for quadrant 3 and 4. 

Instead of integers you can also use a word variable.

The following simple sample will show the input and output values.

```vb
Dim Iii As Integer , I2 As Integer , W As Word

For W= 0 To 65535 Step 182

```
Iii = W ' for usage as an integer

I2 = Qsin(iii) ' get the value of W/III

```vb
Print W; " " ; Iii ; " " ; I2

Next

```
This will give the output :

W III QSIN 

0 0 0

182 182 571

364 364 1143

546 546 1713

728 728 2284

910 910 2854

1092 1092 3423

1274 1274 3992

1456 1456 4558

1638 1638 5124

1820 1820 5687

\--snip--

15470 15470 32640

15652 15652 32685

15834 15834 32720

16016 16016 32745

16198 16198 32760

16380 16380 32766

16562 16562 32761

16744 16744 32746

16926 16926 32721

17108 17108 32687

17290 17290 32643

17472 17472 32588

17654 17654 32523

17836 17836 32448

18018 18018 32364

18200 18200 32270

18382 18382 32166

18564 18564 32053

18746 18746 31929

18928 18928 31796

19110 19110 31653

19292 19292 31500

19474 19474 31339

19656 19656 31166

19838 19838 30986

20020 20020 30794

20202 20202 30595

20384 20384 30386

20566 20566 30167

20748 20748 29939

20930 20930 29702

21112 21112 29456

21294 21294 29202

21476 21476 28938

21658 21658 28666

21840 21840 28384

22022 22022 28095

22204 22204 27796

22386 22386 27489

22568 22568 27173

22750 22750 26850

\--snip--

32214 32214 1738

32396 32396 1168

32578 32578 596

32760 32760 25

32942 -32594 -546

33124 -32412 -1118

33306 -32230 -1688

33488 -32048 -2259

33670 -31866 -2829

33852 -31684 -3398

\--snip --

48230 -17306 -32638

48412 -17124 -32683

48594 -16942 -32719

48776 -16760 -32744

48958 -16578 -32760

49140 -16396 -32766

49322 -16214 -32761

49504 -16032 -32747

49686 -15850 -32723

49868 -15668 -32688

50050 -15486 -32645

50232 -15304 -32590

50414 -15122 -32526

50596 -14940 -32452

50778 -14758 -32368

50960 -14576 -32275

51142 -14394 -32171

51324 -14212 -32058

51506 -14030 -31934

51688 -13848 -31802

51870 -13666 -31659

52052 -13484 -31507

52234 -13302 -31346

52416 -13120 -31174

52598 -12938 -30994

52780 -12756 -30803

52962 -12574 -30604

53144 -12392 -30395

\--snip--

63154 -2382 -7417

63336 -2200 -6859

63518 -2018 -6299

63700 -1836 -5737

63882 -1654 -5173

64064 -1472 -4608

64246 -1290 -4042

64428 -1108 -3473

64610 -926 -2904

64792 -744 -2334

64974 -562 -1764

65156 -380 -1193

65338 -198 -621

65520 -16 -50

![qsin_excel](qsin_excel.png)

When we feed the output in Excel we can create the graph above, showing a perfect sinus.

See Also

[QCOS](qcos.md)

Example

NONE