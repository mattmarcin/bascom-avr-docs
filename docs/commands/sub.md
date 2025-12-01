# SUB

Action

Defines a Sub procedure.

Syntax

SUB Name[(var1 , â¦ )]

Remarks

Name | Name of the sub procedure, can be any non-reserved word.  
---|---  
var1 | The name of the optional parameter(s).  
  
You must end each subroutine with the END SUB statement.

You can copy the DECLARE SUB line and remove the DECLARE statement. This ensures that you have the right parameters.

You can also use CONFIG SUBMODE=NEW and only write the implementation. In that case you do not need to write the DECLARATION.

See Also

[FUNCTION](declare_function.md) , [CALL](call.md) , [CONFIG SUBMODE](config_submode.md) , [EXIT](exit.md)

See the [DECLARE SUB](declare_sub.md) topic for more details.