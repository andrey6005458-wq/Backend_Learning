from typing import Callable
import time
from functools import wraps


def param_timer_deco(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Программа спала {round(end - start, 2)} секунд")
        return result

    return wrapper


@param_timer_deco
def my_func(sleep_time: int):
    """Уважаемый Дмитрий, будет ли сегодня стрим по Warcraft?"""
    time.sleep(sleep_time)
    return 12345


print(my_func(3))
print(my_func.__doc__)
print(my_func.__name__)
