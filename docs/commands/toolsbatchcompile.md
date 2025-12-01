# Tools Batch Compile

The Batch Compiler is intended to compile multiple files.

Shortcut : CTRL+B

The Batch compile option was added for internal test usage. It is used by MCS to test the provided test samples.

The following window is shown :

![batch_compile](batch_compile.png)

There are a number of menu options.

File Load Batch

Load an earlier created and saved batch file list from disk.

File Save Batch

Save a created list of files to disk

When you have composed a list with various files it is a good idea to save it for later re usage.

File Save Result

Save the batch compile log file to disk. A file named batchresult.txt will be saved in the BASCOM application directory.

File Exit

Close window

Batch Compile

Compile the checked files. By default all files you added are checked. During compilation all files that were compiled without errors are unchecked.

![batchcomp2](batchcomp2.png)

This screen print shows that $inc.bas could not be compiled.

And that array.bas was not yet compiled.

Batch Add Files

Add files to the list. You can select multiple *.BAS files that will be added to the list.

Batch Add Dir

Add a directory to the list. All sub directories will be added too. The entire directory and the sub directories are searched for *.BAS files. They are all added to the list.

Batch Clear List

Clear the list of files.

Batch Clear Good

Remove the files that were compiled without error. You will keep a list with files that compiled with an error.

All results are shown in an error list at the bottom of the screen.

When you double click an item, the file will be opened by the editor.

See Also

[$NOCOMP](nocompile.md)