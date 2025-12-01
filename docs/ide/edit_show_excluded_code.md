# Edit Show Excluded Code

This option turns on/off marking of excluded code.

Excluded code is code that is not compiled as part of the project because conditional compilation parameters exclude the code.

Excluded code is shown in Italic and gray but you can change the default colors.

```vb
For example when using an XMEGA processor, the _XMEGA constant will be set to 1. When the option is turned off, it will show normal like :

  

#if _xmega  
print "XMEGA"  

#else  
print "NORMAL"  

#endif  
  
```
When then option is turned on, the editor will show it like :

```vb
#if _xmega  
print "XMEGA"  

#else  
print "NORMAL"  

#endif  


```
When you have a lot of conditional code it is hard to see which code is executed. When you turn the option on, it is much easier to see.

Check out this example:

![edit_show_excluded_code](edit_show_excluded_code.png)

  
  


In order for this option to work correct, your code should not contain syntax errors. 

See Also

[#IF, #ELSEIF . #ELSE](_if_else_endif.md) , [Show Dead Code](edit_show_dead_code.md)