#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Recall python decorators"""

DISABLE = False


def disable(func):
    """
    Disable a decorator by re-assigning the decorator's name
    to this function. For example, to turn off memoization:
    # >>> memo = disable
    """
    return func


def decorator():
    """
    Decorate a decorator so that it inherits the docstrings
    and stuff from the function it's decorating.
    """
    return


def count_calls():
    """Decorator that counts calls made to the function decorated."""
    return


def memo():
    """
    Memoize a function so that it caches all return values for
    faster future lookups.
    """
    return


def n_ary():
    """
    Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x.
    """
    return


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


@memo
@count_calls
@n_ary
def addition(a, b):
    """Sum"""
    return a + b


@count_calls
@memo
@n_ary
def multiplication(a, b):
    """Multiply"""
    return a * b


@count_calls
# @trace("####")
@memo
def fibonacci(n):
    """Some doc"""
    return 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Executes all functions"""
    print(addition(4, 3))
    # print(addition(4, 3, 2))
    print(addition(4, 3))
    print("foo was called", addition.calls, "times")

    print(multiplication(4, 3))
    # print(multiplication(4, 3, 2))
    # print(multiplication(4, 3, 2, 1))
    print("bar was called", multiplication.calls, "times")

    print(fibonacci.__doc__)
    fibonacci(3)
    print(fibonacci.calls, 'calls made')


if __name__ == '__main__':
    main()
