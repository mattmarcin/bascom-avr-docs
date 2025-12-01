# CONFIG SUBMODE

Action

This option sets how the compiler deals with Subs, Functions and Declarations.

Syntax

CONFIG SUBMODE = NEW|OLD

Remarks

When the SUBMODE option is not configured, the default 'OLD' will be used.

This is the old mode used in versions up to 2070.

This old mode demands that you DECLARE a function or sub, before you call/use it.

It also binds in the sub/function at the same location as in your code.

When working with $include files, this requires that you insert an $include file with the SUBS/FUNCTIONS at the end of your code, and that you insert an $include file with the DECLARE statements at the start of your code.

Or you can put the DECLARE and actual implementation in one file and use a GOTO to jump over the Sub/Function code.

```vb
For example consider this code :

print "code here"

Sub test()

print

End Sub

```
When using the OLD method, this will give problems since the code will run into the Sub test, without it actual being called.

We can solve that like this by placing the sub/functions after the END statement:

```vb
print "code here"

END

Sub test()

print

End Sub

```
or we can use a GOTO:

```vb
print "code here"

GOTO skip

Sub test()

print

End Sub

```
skip:

print "more code here"

When you use CONFIG SUBMODE=NEW, most behaviour is changed :

\- there is no need to DECLARE a sub/function before you call it. But, the actual sub/function code must be placed before the actual call!

\- only the used sub/functions are included

\- the compiled sub/function code is placed after the main program. this is something you do not need to worry about.

\- you can $include the modules without a GOTO to jump over the code because code is stored automatically after the END statement.

\- sub/functions behave like macro's : only when used they are included

\- Any Dead code or Un-used code will not be Compiled!

This means you can $Include a file with all your collection of Sub or Functions and the Compiler will determine which items are to be used during Compilation saving you unnecessary wastage of Flash space.

See also

[DECLARE SUB](declare_sub.md), [SUB](sub.md), [DECLARE FUNCTION](declare_function.md) , [CALL](call.md)

Example

  
```vb
$regfile = "m88def.dat"  
$crystal = 8000000  
config submode=new  
  
declare sub test1() ' not required  
  
sub test2() ' this sub is not used and will not be compiled  
print "test2"  
end sub  
  
function myfunc() as byte ' called from test1  
```
myfunc = 1  
```vb
end function  
  
sub test1()  
print "test1"  
print myfunc() ' uses myfunc  
end sub  
  
print "test"  
```
test1 ' call test1  
end '12