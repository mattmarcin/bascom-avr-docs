# $VERSION

Action

This compiler directive stores version information.

Syntax

$VERSION V,S,R

Remarks

Version info is important information. If you need to maintain source code, it will make it easy to identify the code.

$VERSION has 3 parameters. These must be numeric digits. Each time you compile your code, the release number is increased.

You can use Version(2) to print this information. $version 1,2,3 will be printed as 1.2.3

The compiler will create three internal constants named _VERSION_MAJOR, _VERSION_MINOR and _VERSION_BUILD with the specified values.

For example when $version is set to : $VERSION 1,2,3

_VERSION_MAJOR will become 1 , _VERSION_MINOR will become 2 and _VERSION_BUILD will become 3.

See also

[VERSION](version.md)

Example

```vb
$version 1,2,3

Print Version(2)

```