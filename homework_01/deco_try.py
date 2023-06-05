"""Decorator testing fulfilled here"""
from functools import wraps

DISABLE = False


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


@do_thrice
@count_calls
def say_hi():
    """Prints Hi!"""
    print("Hi!")


@count_calls
def catalan_rec(n):
    """Catalan number finder"""
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_rec(i) * catalan_rec(n - i - 1)
    return res


def main():
    """Executes all functions"""
    say_hi()
    print(say_hi.__dict__)
    print(say_hi.__wrapped__.__dict__)
    print(say_hi.__wrapped__.calls)
    print(say_hi.__doc__, say_hi.__name__)
    print(catalan_rec(n=7))
    print(catalan_rec.__dict__)
    print(catalan_rec.calls)


if __name__ == '__main__':
    main()
