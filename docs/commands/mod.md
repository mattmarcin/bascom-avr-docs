# MOD

Action

Calculates the remainder of a division.

Syntax

var1 = var2 MOD var3

Remarks

var1 | Variable that will be assigned with the modules of var2 and var3.  
---|---  
var2 | A numeric variable to take the modules from  
var3  | The modulus  
  
The MOD operation is similar to the division operation(/). But while a division returns the number of times a number can be divided, the MOD returns the remainder.

For example : 21 MOD 3 will result in 0 since 7x3=21. There will be no remainder.

But 22 MOD 3 will result in 1 since 22-(7x3)=1

In BASCOM, the variable you assign determines which kind of math will be used. When you have 2 word variables you want to get the modulus from, you have to assign a word variable too.

When you assign a byte, byte math will be used.

Floating Point

When using singles or doubles, the MOD uses this equivalent code :

Dim A as single, B as single, c as single, d as single

a = 13 : b = 2.7 'sample

c = a MOD b

d = a - FIX(a / b) * b

See also

[Language Fundamentals](language_fundamentals.md)

Example

```vb
Dim L As Long , L2 As Long  
For L = 1 To 1000  
```
L2 = L Mod 100  
```vb
If L2 = 0 Then ' multiple of 100  
Print L  
End If  
Next  


```