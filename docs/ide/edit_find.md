# Edit Find

With this option, you can search for text in your program.

Text at the current cursor position will automatically be placed in the find dialog box.

All text you search for is saved so the next time you search, you can retrieve the search phrase from a list.

Click the 'Clear History' button to clear the history. This will clear ALL find history from all pull down boxes in both the Find and Replace windows.

![edit_find](edit_find.png)

The following options available:

Option | Description  
---|---  
Case Sensitive | When selected, the case must match. Searching for PRINT will not find pRint. With this option turned off, Print will find print, PRINT, PRinT, etc.  
Whole words only | When selected, only whole words are considered. A whole word is a word that is surrounded by spaces, or that is at the start of a line. Looking for PRINT will find : "Print test" and "print" and "print print". But not "printer"  
Regular expressions | You can use a regular expression to find a match. ^ A circumflex at the start of the string matches the start of a line. $ A dollar sign at the end of the expression matches the end of a line. . A period matches any character. * An asterisk after a string matches any number of occurrences of that string followed by any characters, including zero characters. For example, bo* matches bot, bo and boo but not b. \+ A plus sign after a string matches any number of occurrences of that string followed by any characters except zero characters. For example, bo+ matches boo, and booo, but not bo or be. [ ] Characters in brackets match any one character that appears in the brackets, but no others. For example [bot] matches b, o, or t. [^] A circumflex at the start of the string in brackets means NOT. Hence, [^bot] matches any characters except b, o, or t. [-] A hyphen within the brackets signifies a range of characters. For example, [b-o] matches any character from b through o.  \ A backslash before a wildcard character tells the Code editor to treat that character literally, not as a wildcard. For example, \^ matches ^ and does not look for the start of a line.  
Forward | This is the search direction. By default it will search forward.  Forward means down in this context.  
Backward | This is the search direction. You can use backwards in case you pressed F3 too many times and want to go back to the previous found text.  
Global | All the text of the current editor will be searched.  
Selected text | Only the selected text will be searched.  
So before you press CTRL+F to search for text you can select text and this option will be selected automatic. Otherwise global is selected.  
From cursor | Search from the current cursor position to the end of the code.  
Entire scope | Search from the current cursor position to the end, then search till the start of the cursor position. This will search the entire text.  
  
Find in Files

The Find in Files option can be used to search for text in files.

![find_files](find_files.png)

Option | Description  
---|---  
Case Sensitive | When selected, the case must match. Searching for PRINT will not find pRint. With this option turned off, Print will find print, PRINT, PRinT, etc.  
Whole words only | When selected, only whole words are considered. A whole word is a word that is surrounded by spaces, or that is at the start of a line. Looking for PRINT will find : "Print test" and "print" and "print print". But not "printer"  
Regular expressions | You can use a regular expression to find a match. ^ A circumflex at the start of the string matches the start of a line. $ A dollar sign at the end of the expression matches the end of a line. . A period matches any character. * An asterisk after a string matches any number of occurrences of that string followed by any characters, including zero characters. For example, bo* matches bot, bo and boo but not b. \+ A plus sign after a string matches any number of occurrences of that string followed by any characters except zero characters. For example, bo+ matches boo, and booo, but not bo or be. [ ] Characters in brackets match any one character that appears in the brackets, but no others. For example [bot] matches b, o, or t. [^] A circumflex at the start of the string in brackets means NOT. Hence, [^bot] matches any characters except b, o, or t. [-] A hyphen within the brackets signifies a range of characters. For example, [b-o] matches any character from b through o.  \ A backslash before a wildcard character tells the Code editor to treat that character literally, not as a wildcard. For example, \^ matches ^ and does not look for the start of a line.  
Search all project files | This option will search through all project files. Files considered are $INCLUDE files. Nested $include files are not considered.   
Search all open files | This option will search though all open files. This are loaded files visible in the TABS  
Search in directories | You can specify a custom folder to search for the text.  
Search in current file | This option will restrict the search to the current file.  
  
Edit Find shortcut : ![filefind](filefind.jpg), CTRL+F