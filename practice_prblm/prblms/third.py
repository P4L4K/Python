#default values
def fun_default(a,b=90):
    print(" value of a: ",a)
    print(" value of b: ",b)

fun_default(b=50,a="Monika")
fun_default(a="lalit")

#if the default value is not given and still we did not pass value(argument) for the parameter : error
#if we give the arguments without specifying its parameters : arguments will be assigned on the first comes  first served basis
fun(50,"hey")
fun() # error as value for a is not defined by default
