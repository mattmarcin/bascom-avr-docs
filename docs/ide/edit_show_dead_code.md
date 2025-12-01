# Edit Show Dead Code

This option turns on/off marking of 'dead' code.

Dead code is code that does not do a thing and could be removed.

Dead code is shown in Italic and gray but you can change the color and italic.

Dead code is similar to Excluded code with the difference that excluded code is not compiled while dead code is compiled. 

Dead code is a new feature in 2080 and intended to show you which variables or code are not used.

You can decide if the code is really dead, and need to be removed, or not.

Since this is a new feature, you should take care before deleting 'dead code'

![edit_dead_code](edit_dead_code.png)

The example above demonstrates a few dead code elements:

\- the local dead as byte, is not used in the code

\- the function result is assigned twice without that the result is used, this does not make sense

\- the GOTO skips over some code which is never used (print)

See Also

[Edit Show Excluded Code](edit_show_excluded_code.md)