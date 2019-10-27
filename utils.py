import functools
import logging
import sys 
import os

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs.log')

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)


# logfunc
 def logfunc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
        except Exception as e:
            logging.exception(f'An Error Occured in {func.__name__} function. Check the logs')
            value = None
        return value

    return wrapper
