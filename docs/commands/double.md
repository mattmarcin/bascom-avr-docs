# DOUBLE

The double.lbx (lib) is written by Josef Franz VÃ¶gel. The library supports the basic operations :

•| Addition (+)  
---|---  
  
•| Subtraction (-)  
---|---  
  
•| Multiplication (*)  
---|---  
  
•| Division (/)  
---|---  
  
•| Val() , INPUT  
---|---  
  
•| Str() , PRINT  
---|---  
  
•| Int()  
---|---  
  
•| Frac()  
---|---  
  
•| Fix()  
---|---  
  
•| Round()  
---|---  
  
•| Conversion from double to single and long  
---|---  
  
•| Conversion from single and long to double  
---|---  
  
The double library uses special Mega instructions not available in all AVR chips. But as the old chips are not manufactured anymore, this should not be a problem.

In version 1.11.9.8 a software multiplication is performed so the trig functions can be used on any chip that has enough internal memory.

In the report file you can find out if your micro supports the HWMUL. the _HWMUL conststant is set to 1 in that case. 

When software multiplication is used, the multiply routine needs more processor cycles. A number of trig functions depend on the multiplication code and as a result, they become more slow too. 

All Trig() functions are supported by the double too!