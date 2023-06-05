"""Decorator testing fulfilled here"""
import tracemalloc
from functools import wraps
from time import perf_counter

DISABLE = False


def measure_performance(func):
    """Measure performance of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10 ** 6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10 ** 6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-" * 40}')
        tracemalloc.stop()
        # return "string from wrapper return clause"
        return func(*args, **kwargs)

    return wrapper


def disable(func):
    """
    Disable a decorator by re-assigning the decorator's name
    to this function. For example, to turn off memoization:
    # >>> memo = disable
    """
    return func


def count_calls(func):
    """Decorator that counts calls made to the function decorated."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        # print(f'{func.__name__} was called {wrapper.calls} times')
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def memoize_factorial(f):
    """Memorizes factorial"""
    memory = {}

    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]

    return inner


def memo(func):
    """
    Memoize a function so that it caches all return values for
    faster future lookups.
    """
    cache = {}

    def helper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return helper


class Memoize:
    """
    Memoize a function so that it caches all return values for
    faster future lookups.
    """

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def do_thrice(func):
    """Decorator calls func thrice."""

    @wraps(func)
    def wrapper_do_thrice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_thrice


if DISABLE:
    do_thrice = disable


@measure_performance
@do_thrice
@count_calls
def say_hi():
    """Prints Hi!"""
    print("Hi!")


@count_calls
@memo
def catalan_rec(n):
    """Catalan number finder"""
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_rec(i) * catalan_rec(n - i - 1)
    return res


@count_calls
@memo
def facto(num):
    """Factorial calculation"""
    if num == 1:
        return 1

    return num * facto(num - 1)


def main():
    """Executes all functions"""
    print("-" * 80)
    say_hi()
    print(say_hi.__dict__)
    print(say_hi.__wrapped__.__dict__)
    print(say_hi.__wrapped__.__wrapped__.__dict__)
    print(say_hi.__wrapped__.__wrapped__.calls)
    print(say_hi.__doc__, say_hi.__name__)
    print("-" * 80)
    print(catalan_rec(7))
    print(catalan_rec.__dict__)
    print(catalan_rec.calls)
    print(catalan_rec.__doc__, catalan_rec.__name__)
    print("-" * 80)
    print(facto(5))
    print(facto.calls)
    print("-" * 80)


if __name__ == '__main__':
    main()
