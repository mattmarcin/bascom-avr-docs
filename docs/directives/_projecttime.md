# $PROJECTTIME

Action

This directive will keep track of time you spend on the source.

Syntax

$PROJECTTIME

Remarks

Keeping track of project time is the only purpose of this directive. It will be ignored by the compiler. 

When the IDE finds the $PROJECTTIME directive, it will count the minutes you spend on the code.

Each time you save the code, the updated value will be shown.

The IDE will automatic insert the value after $PROJECTTIME. 

So how does this work?

When you type, you start a timer. When there are no keystrokes for 2 minutes, this process stops. It is started automatic as soon as you start typing. 

So when you type a character each minute, each minute will be counted a a full minutes of work.

The time is counted and shown in minutes. 

While you can edit the value in the source, it will be changed as soon as you save the source. 

See also

NONE

Example

$PROJECTTIME