case (type x, type y)
when (int, int)
then use ADD
when (int, double)
then promote x to double
     use FADD
when (double, int)
then promote y to double
     use FADD
when (double, double)
then use FADD
when (string, string)
then use string concatenation