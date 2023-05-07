import math
import time

from main import Sort
from numpy.random import randint


def round_sigfigs(num: int, sigfigs: int) -> float:
    "Rounds to :param sigfigs: significant digits of a number"
    if abs(num) < 1:
        return 0
    return round(num, -int(math.floor(math.log10(abs(num))) - (sigfigs - 1)))

def runtime(func, arr: list) -> None:
    """
    Measures runtime of :param func:

    :param func: function to be timed
    :type func: callable
    """
    start = time.time()
    func(arr)
    end = time.time()

    res = round_sigfigs(end-start, 3)
    return res

sort = Sort()

# check to see if algorithms sort the array correctly
small_arr = randint(0, 10, size=10)
print(sort.quicksort(small_arr), sort.bubblesort(small_arr), sep="\n")

# measure runtime of algorithms
large_arr = randint(0, 1_000, size=10_000)
print(f"Ran in: {runtime(sort.quicksort, large_arr)} seconds(s)")
print(f"Ran in: {runtime(sort.bubblesort, large_arr)} seconds(s)")