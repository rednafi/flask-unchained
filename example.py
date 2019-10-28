from pyfoster.funcs.func_logger import logfunc
from pyfoster.funcs.func_timer import timefunc

import sys
import pyfoster


@logfunc
def zero_div(a, b=0):
    return a // b

print(zero_div(5))
