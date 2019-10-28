from pyfoster.funcs.logging_func import logfunc
from pyfoster.funcs.timing_func import timefunc


@logfunc
def zero_div(a, b=0):
    return a // b

print(zero_div(5))
