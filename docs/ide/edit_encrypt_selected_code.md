# Edit Encrypt Selected Code

This add on option allows you to encrypt portions of your code.

Because the encryption can not be undone, you will get this warning:

![edit_encrypt](edit_encrypt.jpg)

```vb
If you chose YES, the selected code will be encrypted and will result in lines like :

$CRYPT 6288E522B4A1429A6F16D639BFB7405B

$CRYPT 7ABCF89E7F817EB166E03AFF2EB64C4B

$CRYPT 645C88E996A87BF94D34726AA1B1BCCC

$CRYPT 9405555D91FA3B51DEEC4C2186F09ED1

$CRYPT 6D4790DA2ADFF09DE0DA97C594C1B074

```
Only the compiler can decrypt and process these lines. There is no way you can change the $CRYPT lines back into source code !

So make a backup of your code before you use this option. Typically, it will only be used on finished projects.

If the encrypted code contains errors, you will get error messages pointing to the [$CRYPT](crypt.md) lines.

![notice](notice.jpg)This option is not available/enabled by default. You need to buy a license that will unlock this option. Our sales requires your BASCOM serial number too.