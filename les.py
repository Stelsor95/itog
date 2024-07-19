import logging
import os
from typing import Callable


def decor(func: Callable):
    my_format = '{msg}'
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="./logles2.log", filemode="w", encoding="utf-8",
                         level=logging.INFO, style="{", format=my_format)
    def wrapper (*args, **kwargs):
        result = str (func (*args, **kwargs))
        logger.info(f"result: {result}, *args: {args}, *kwargs: {kwargs}")
        return result
    return wrapper

@decor
def factorial (x):
    f = 1
    for i in range (2, x+1):
        f *= i
    return f

# ----- БЛОК ЗАПУСКА ---------------------

print(factorial (5))
print(factorial (10))
print(factorial (15))
print(factorial (x=5))
print(factorial (15))
print(factorial (15))
print(factorial (15))
print(factorial (x = 10))
print(factorial (x = 0))