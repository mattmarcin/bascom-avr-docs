# View PinOut

The Pin Out viewer is a dock able window that shows the case of the active chip.

The active chip is determined by the value of [$REGFILE](regfile.md).

![pinout](pinout.png)

When you move the mouse cursor over a pin, you will see that the pin will be colored red. At the bottom of the window, a pin description is show. In the sample above you will see that each line has a different color. This means that the pin has multiple alternative functions.

The first blue colored function is as generic IO pin.

The second green colored function is RESET pin.

The third black colored function is PIN change interrupt.

A pin can have one or more functions. Some functions can be used together.

When you move the mouse cursor away, the pin will be colored blue to indicate that you viewed this pin. For example, when you need to look at it again.

You can also search for a pin description. Enter some text and return.

Here is an example when you search the VCC pin :

![pin_viewer_search](pin_viewer_search.png)

When pins are found that have the search phrase in the description, the pin will be colored blue.

By clicking 'Clear Pin HL' you can clear all colored pins.

Some chips might have multiple cases. You can select the case from the package list.

![pin_viwer_packlist](pin_viwer_packlist.png)

When you change from package, all pin colors will be cleared.

When you double click a pin, the pin will be colored green. Another double click will color it red/blue.

When a pin is green, it will not be colored red/blue. The green color serves as a kind of bookmark.

The only exception is the search function. It will make bookmarked green pins, blue too.

Use the right mouse to access a popup menu. This menu allows you to zoom the image to a bigger or smaller size.

Double click the chip to show the chip data.

![pinout_chipdata](pinout_chipdata.png)

When you want to search for a chip, click the 'Chip Search' button.

It will show the following window:

![pinout_chipsearchSpecs](pinout_chipsearchspecs.png)

You can provide criteria such as 2 UARTS. All criteria are OR-ed together. This means that when one of the criteria is met, the chip will be included in the list.

![notice](notice.jpg)Only chips supported by BASCOM will be listed. When a chip has SRAM, and is not supported yet, it will be in the near future since the goal is to support all chips.

When you find an error in the pin description, please send an email to support so it can be corrected.