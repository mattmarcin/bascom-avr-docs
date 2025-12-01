# $NORAMCLEAR

Action

Instruct the compiler to not generate initial RAM clear code.

Syntax

$NORAMCLEAR

Remarks

Normally the SRAM is cleared in the initialization code. When you don't want the SRAM to be cleared(set to 0) you can use this directive.

Because all variables are automatically set to 0 or ""(strings) without the $NORAMCLEAR, using $NORAMCLEAR will set the variables to an unknown value. That is, the variables will probably set to FF but you cannot count on it.

When you have a battery back upped circuit, you do not want to clear the RAM at start up. So that would be a situation when you could use $NORAMCLEAR.

See also

[$NOINIT](_noinit.md)