# $BIGSTRINGS

Action

Instruct the compiler to use big strings.

Syntax

$BIGSTRINGS

Remarks

By default each string has a maximum length of 254 bytes. A null character is used to mark the end of a string.

When a longer string is needed, the compiler can not use bytes for passing the length. A word is needed to hold the length.

The $BIGSTRINGS directive will include the bigstrings.lbx and will handle all string routines different when parameters are passed which influence the length. 

The alternative library contains modified(overloaded) routines for code not compatible with big strings.

The following string routines support $BIGSTRINGS:

[ASC](asc.md)

[CHARPOS](charpos.md)

[CRC8](crc8.md)

[DELCHAR](delchar.md)

[DELCHARS](delchars.md)

[GET](get.md)

[INPUT LCD , INPUT SERIAL](input.md)

[INSERTCHAR](insertchar.md)

[INSTR](instr.md)

[LCASE](lcase.md)

[LEFT](left.md)

[LEN](len.md)

[LTRIM](ltrim.md)

[MID](mid.md) function

[MID](mid.md) statement

[PUT](put.md)

[QUOTE](quote.md)

[RIGHT](right.md)

[RTRIM](rtrim.md)

[SPACE](space.md)

[STRING](string.md)

[TRIM](trim.md)

[UCASE](ucase.md)

See also

[DIM](dim.md)

Example

$BIGSTRINGS