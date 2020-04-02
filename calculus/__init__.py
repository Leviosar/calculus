__version__ = '0.1.0'

import time

from typing import Callable, Tuple


def benchmark(function: Callable, label: str, args: Tuple):
    """
    General benchmarking function, receives a callable and it's arguments
    run the callable with the given args and returns the approximated time
    the function took to run
    """
    initial = time.time()
    function(**args)
    end = time.time()
    return (end - initial)


def integral(function: Callable, limits: Tuple[int, int], n: int):
    """
    Simple defined integral calculation using classic mathematical definition
    function: Callable -> int, the integral to be calculated
    limits: Tuple[int, int], upper and lower integration bounds
    n: int, number of iterations the algorythm will make to approximate value
    """

    upper_limit, lower_limit = (
        max(int(limits[0]), int(limits[1])),
        min(int(limits[0]), int(limits[1]))
    )

    deltaI = (upper_limit - lower_limit) / n
    area = 0
    i = lower_limit

    while i < upper_limit:
        try:
            area += deltaI * function(i)
            i += deltaI
        except ZeroDivisionError:
            break

    return area
