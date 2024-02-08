import functools
import time


def no_change(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def boilerplate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value

    return wrapper


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
