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


def do_twice(func):
    """Decorator calls func twice"""

    @wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


if DISABLE:
    do_twice = disable


@do_twice
def say_hi():
    """Prints Hi!"""
    print("Hi!")


def main():
    """Executes all functions"""
    say_hi()
    print(say_hi.__doc__, say_hi.__name__)


if __name__ == '__main__':
    main()
