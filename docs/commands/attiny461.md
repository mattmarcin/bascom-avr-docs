# ATTINY461

This page is intended to show the outline of the chip and to provide additional information that might not be clear from the data sheet.

![attiny261_461_861](attiny261_461_861.png)

The processor has only one PCINT interrupt. But there are two PCINT interrupt masks to serve all the PCINTx pins. Most processors have their own interrupt for each PCINT mask register so you have better control over the different pins which caused the interrupt.

Since there is only one interrupt, the [ENABLE](enable.md) and [DISABLE](disable.md) statements, set/reset both the PCIE0 and PCIE1 flags in the GIMSK register. You still have to set the PCMSK0 and PCMSK1 registers to specify which bits can cause a PCINT interrupt.