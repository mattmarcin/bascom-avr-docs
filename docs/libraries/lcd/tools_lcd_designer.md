# Tools LCD Designer

With this option you can design special characters for LCD-text displays.

The following window will appear:

![lcd_designer](lcd_designer.png)

The LCD-matrix has 7x5 points. The bottom row is reserved for the cursor but can be used.

You can select a point by clicking the left mouse button. If a cell was selected it will be unselected.

Clicking the Set All button will set all points.

Clicking the Clear All button will clear all points.

When you are finished you can press the Ok button : a statement will be inserted in your active program-editor window at the current cursor position. The statement looks like this :

Deflcdchar ?,1,2,3,4,5,6,7,8

You must replace the ?-sign with a character number ranging from 0-7.

The eight bytes define how the character will appear. So they will be different depending on the character you have drawn.

See Also

[Font Editor](font_editor.md)