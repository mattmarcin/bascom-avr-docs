# CmdInterrupt

Action

Trigger an Interrupt Int_CmdFlag

Syntax

CmdInterrupt ms

Remarks

ms | Delay before interrupt triggers, in milliseconds. The interrupt is guaranteed not to fire before this delay. If ms is zero, the Interrupt fires immediately.  
---|---  
  
When the co-processor engine executes this command, it triggers Interrupt Int_CmdFlag