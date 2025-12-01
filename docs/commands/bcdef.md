# BCDEF

Action

Defines a subroutine name and itâs parameters in BASCOM so it can be called in the BasicCard.

Syntax

BCDEF name([param1 , paramn])

Remarks

name | The name of the procedure. It may be different than the name of the procedure in the BasicCard but it is advised to use the same names.  
---|---  
Param1 | Optional you might want to pass parameters. For each parameter you pass, you must specify the data type. Supported data types are byte, Integer, Word, Long, Single and String  
  
![notice](notice.jpg)This statements uses BCCARD.LIB, a library that is available separately from MCS Electronics.

BCDEF Calc(string)

Would define a name âCalcâ with one string parameter.

When you use strings, it must be the last parameter passed.

BCDEF name(byte,string)

BCDEF does not generate any code. It only informs the compiler about the data types of the passed parameters.

See Also

[CONFIG BCCARD](config_bccard.md) , [BCCALL](bccall.md) , [BCRESET](bcreset.md)

Partial Example

Bcdef Calc(string)