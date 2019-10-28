import functools
import logging
import sys
import os


def create_logger(log_path: str = "logs/logs.log") -> logging.Logger:

    # create folder
    if not os.path.exists(log_path):
        os.mkdir("logs")

    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_path)

    console_handler.setLevel(logging.WARNING)
    file_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# calling the logger
logger = create_logger()


# logfunc
def logfunc(_func=None, logger=logger):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                # log the exception
                err = "There was an exception in  "
                err += func.__name__
                logger.exception(err)

                # re-raise the exception
                raise

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)



