#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Recall python decorators"""
from functools import wraps, reduce

DISABLE = False


def disable(func):
    """
    Disable a decorator by re-assigning the decorator's name
    to this function. For example, to turn off memoization:
    # >>> memo = disable
    """
    return func


def decorator(func):
    """
    Decorate a decorator so that it inherits the docstrings
    and stuff from the function it's decorating.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def count_calls(func):
    """Decorator that counts calls made to the function decorated."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def memo(func):
    """
    Memoize a function so that it caches all return values for
    faster future lookups.
    """
    cache = {}

    @wraps(func)
    def helper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return helper


def memo_kwargs(func):
    """Keep a cache of previous function calls"""

    @wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = {}
    return wrapper_cache


def n_ary(func):
    """
    Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x.
    i.e. = functools.reduce
    """

    @wraps(func)
    def wrapper_reduce(*args):
        return reduce(func, [*args])

    return wrapper_reduce


def trace():
    """Trace calls made to function decorated.

    @trace("____")
    def fib(n):
        ....

    >>> fib(3)
     --> fib(3)
    ____ --> fib(2)
    ________ --> fib(1)
    ________ <-- fib(1) == 1
    ________ --> fib(0)
    ________ <-- fib(0) == 1
    ____ <-- fib(2) == 2
    ____ --> fib(1)
    ____ <-- fib(1) == 1
     <-- fib(3) == 3

    """
    return


if DISABLE:
    decorator = disable
    count_calls = disable
    memo = disable
    n_ary = disable
    trace = disable


@count_calls
@memo_kwargs
@n_ary
def addition(a, b):
    """Sum docstring"""
    return a + b


@count_calls
@memo_kwargs
@n_ary
def multiplication(a, b):
    """Multiply docstring"""
    return a * b


@count_calls
# @trace("####")
@memo
def fibonacci(n):
    """Fibonacci docstring"""
    return 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Executes all functions"""
    print(addition(4, 3))
    print(addition(4, 3, 2))
    print(addition(4, 3))
    print(addition(2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(addition.__doc__)
    print("addition was called", addition.calls, "times")

    print(multiplication(4, 3))
    print(multiplication(4, 3, 2))
    print(multiplication(4, 3, 2, 1))
    print(multiplication.__doc__)
    print("multiplication was called", multiplication.calls, "times")

    print("fibonacci(5) =", fibonacci(5))
    print("fibonacci(10) =", fibonacci(10))
    print(fibonacci.__doc__)
    print(fibonacci.calls, 'fibonacci calls made')


if __name__ == '__main__':
    main()
