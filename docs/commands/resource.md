# $RESOURCE

Action

Instruct the compiler to use a special resource file for multi language support.

Syntax

```vb
$RESOURCE [DUMP] "lang1" [, "lang2"]

$RESOURCE ON | OFF

```
Remarks

lang1 | This is the name of the first and default language. You can add a maximum of 8 languages. The names will be used in the resource editor. But they are only intended as a reference. The resource names will not end up in your application. They are used for the column names in the resource editor.  
---|---  
lang2 | The second language. You can add multiple languages separated by a comma. The language must be specified within double quotes.  
ON | This will turn on the languages resource handling. In some cases you need to turn the language handling ON or OFF which is explained later  
OFF | This will turn OFF the language handling  
DUMP | This mode will create a <project>.BCS file which contains all used string constants  
  
Some applications require that the interface is available in multiple languages. You write your application the same way as you always do. 

When it is ready, you can add the $RESOURCE directive to make the application suited for multiple languages. 

The $RESOURCE option will generate a BYTE variable named LANGUAGE. You can change the value in your application. The compiler will take care that the proper string is shown.

But first you need to translate the strings into the languages of your choice.

For this purpose you can use the Resource Editor. The [Resource Editor](tools_resource_editor.md) can import a BCS file (BASCOM String file) which contains the languages and the strings.

You can then add a string for all languages.

So first make sure your application works. Then compile using the $RESOURCE DUMP option.

When you test the languages.bas sample the content will look like this :

"English" , "Dutch" , "German" , "Italian"

"Multi language test"

"This"

" is a test"

"Name "

"Hello "

As you can see, the first line contains the languages. The other lines only contain a string. Each string is only stored once in BASCOM. So even while "Mark" can have multiple meanings, it will only end up once in the BCS file. 

After you have translated the strings, the content of the BCR (BASCOM Resource) file will look like :

"English","Dutch","German","Italian"

"This","Dit","Dies","Questo"

"Name ","Naam","Name","Nome"

"Multi language test","Meertalen test","","Test multilingua"

"Hello ","Hallo","Hallo","Ciao"

" is a test"," is een test","ist ein test","Ã¨ un test"

"mark","Mark","Marcus","Marco"

You may edit this file yourself, using Notepad or you can use the Resource Editor. Untranslated strings will be stored as "". Untranslated strings will be shown in the original language !

Now recompile your project and the compiler will handle every string it will find in the resource file (BCR) in a special way. Strings that are not found in the BCR file, are not processed and handled like normal. For example when you have a PRINT "check this out" , and you did not put that in the BCR file, it will show the same no matter which value the LANGUAGE variable has.

But for each string found in the BCR file, the compiler will show the string depending on the LANGUAGE variable. When one of the languages is not translated, it will show as the original language. 

When LANGUAGE is 0, it will show the first string (the string from the first column). When languages is 1, it will show the string from the second column, and so on.

You must take care that the LANGUAGE variables has a valid value. 

So by switching/changing 1 variable, you can change the language in the entire application. Strings are used for PRINT, LCD and other commands. It will work on every string that is in the BCR file. But that also brings us to the next option.

Image this code :

```vb
If S = "mark" Then

Print "we can not change names"

End If

```
As you can see, we use a string. The code will fail if the string is translated (and is different in each language). You can simply remove the this string from the Resource file. But when you also need the word "mark" in the interface, you have a problem. For this purpose you can turn off the resource handling using $RESOURCE OFF

The compiler will then not process the code following the directive with the special resource handling.

And when you are done, you can turn the resource handling on again using $RESOURCE ON.

See also

[Resource Editor](tools_resource_editor.md)

Example

```vb
'------------------------------------------------------------------------------

' language.bas

' (c) 1995-2025 , MCS Electronics

'This example will only work with the resource add on

'resources are only needed for multi language applications

'By changing the LANGUAGE variable all strings used will be shown in the proper language

'------------------------------------------------------------------------------

$regfile = "m88def.dat"

$crystal = 8000000

$baud = 19200

'a few steps are needed to create a multi language application

'STEP 1, make your program as usual

'STEP 2, generate a file with all string resources using the $RESOURCE DUMP directive

'$resource Dump , "English" , "Dutch" , "German" , "Italian" 'we will use 4 languages

'STEP 3, compile and you will find a file with the BCS extesion

'STEP 4, use Tools, Resource Editor and inport the resources

'STEP 5, add languages, translate the original strings

'STEP 6, compile your program this time with specifying the languages without the DUMP option

$resource "English" , "Dutch" , "German" , "Italian"

'this must be done before you use any other resource !

'in this sample 4 languages are used

'this because all resources found are looked up in the BCR file(BasCom Resource)

Dim S As String * 20

Dim B As Byte

Print "Multi language test"

Do

Print "This" ;

```
S = " is a test" : Print S

```vb
Input "Name " , S

Print "Hello " ; S

'now something to look out for !

'all string data not found in the BCR file is not resourced. so there is no problem with the following:

If S = "mark" Then

Print "we can not change names"

End If

'but if you want to have "mark" resourced for another sentence you have a problem.

'the solution is to turn off resourcing

$resource Off

Print "mark"

If S = "mark" Then

Print "we can not change names"

End If

$resource On

```
Language = Language + 1

```vb
If Language > 3 Then Language = 0

Loop

```