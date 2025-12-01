# CmdGetPtr

Action

Get the end memory address of inflated data.

Syntax

CmdGetPtr result

Remarks

result | The end address of decompressed data done by [CmdInflate](cmdinflate.md). The starting address of decompressed data as was specified by [CmdInflate](cmdinflate.md), while the end address of decompressed data can be retrieved by this command. It is one out parameter and can be passed in as any value with [CmdGetPtr](cmdgetptr.md) to RAM_CMD.   
---|---