# $NOINIT

Action

Instruct the compiler to generate code without initialization code.

Syntax

$NOINIT

Remarks

```vb
$NOINIT is only needed in rare situations. It will instruct the compiler not to add initialization code. But that means that you need to write your own code then.

$NOINIT was added in order to support boot loaders. But the new $LOADER directive can better be used as it does not require special ASM knowledge.

```
See also

[$LOADER](loader.md)

Example

NONE