# $CRYPT

Action

This directive marks encrypted BASIC code.

Syntax

$CRYPT data

Remarks

In some cases you might want to share only portions of your code. The IDE can encrypt your code, and the compiler can process this encrypted code.

AES encryption is used. You do need a commercial add on to use the encryption. The $crypt command can be processed by all bascom editions starting from version 2.0.5.0. So you only need an add on when you want to encrypt the code. 

![notice](notice.jpg)Once encrypted, you can NOT DECRYPT into source code! Thus make a BACKUP of your source code before you encrypt the code. 

See also

[Edit Encrypt Selected Code](edit_encrypt_selected_code.md)

Example

```vb
$CRYPT 6288E522B4A1429A6F16D639BFB7405B

$CRYPT 7ABCF89E7F817EB166E03AFF2EB64C4B

$CRYPT 645C88E996A87BF94D34726AA1B1BCCC

$CRYPT 9405555D91FA3B51DEEC4C2186F09ED1

$CRYPT 6D4790DA2ADFF09DE0DA97C594C1B074

```