import time
import functools


def timefunc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Function {func.__name__} took {run_time} seconds to execute")
        return value

    return wrapper
