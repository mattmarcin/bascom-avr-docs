# EUROTIMEDATE

The CONFIG CLOCK statement for using the asynchrony timer of the 8535, M163, M103 or M128 (and others) allows you to use a software based clock. See [TIME$](time_.md) and [DATE$](date_.md).

By default the date format is in MM/DD/YY.

By specifying:

[$LIB](lib.md) "EURODATETIME.LBX"

The DATE$ will work in European format : DD-MM-YY

Note that the eurotimedate library should not be used anymore. It is replaced by the [DATETIME](datetime.md) library which offers many more features.