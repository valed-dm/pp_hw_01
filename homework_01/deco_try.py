DISABLE = True


def disable(func):
    """
    Disable a decorator by re-assigning the decorator's name
    to this function. For example, to turn off memoization:
    # >>> memo = disable
    """
    return func


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


if DISABLE:
    do_twice = disable


@do_twice
def say_hi():
    print("Hi!")


def main():
    """Executes all functions"""
    say_hi()


if __name__ == '__main__':
    main()
