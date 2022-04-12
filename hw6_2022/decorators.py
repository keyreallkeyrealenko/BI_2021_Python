import time
import random


def measure_time(func):
    """This is a decorator function. It is a syntactic sugar to return a time of execution
    instead of real value."""

    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start

    return inner_function


@measure_time
def get_min():
    """This function return min of a list"""
    return min([i for i in range(1, 5000000)])


def function_logging(func):
    """This is a decorator function, it expands standard functionality with logging info"""

    def inner_func(*args, **kwargs):
        if not args and not kwargs:
            print(f'Function {func.__name__} is called with no arguments')
        elif args and not kwargs:
            print(f'Function {func.__name__} is called with positional arguments: {args}')
        elif kwargs and not args:
            print(f'Function {func.__name__} is called with keywords arguments: ', end='')
            my_str = ''
            for key, value in kwargs.items():
                my_str += f'{key}={value}, '
            print(my_str[:-2])
        else:
            print(f'Function {func.__name__} is called with positional arguments: {args} and keywords arguments: ',
                  end='')
            my_str = ''
            for key, value in kwargs.items():
                my_str += f'{key}={value}, '
            print(my_str[:-2])
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} returns output as type {type(result).__name__}')
        return result

    return inner_func


""""This block-1 is just to check function_logging decorator"""


@function_logging
def func1():
    return set()


@function_logging
def func2(a, b, c):
    return (a + b) / c


@function_logging
def func3(a, b, c, d=4):
    return [a + b * c] * d


@function_logging
def func4(a=None, b=None):
    return {a: b}


"""The end of the block-1"""


def russian_roulette_decorator(probability=None, return_value=None):
    """The decorator. It changes return value of function to *return_value with given *probability"""

    def decorator(func):
        def inner_func(*args, **kwargs):
            val = random.random()
            if val <= probability:
                return return_value
            else:
                return func(*args, **kwargs)

        return inner_func

    return decorator


@russian_roulette_decorator(probability=0.2, return_value='OOOOPPPPPSSSS')
def get_randint(min_val, max_val):
    return random.randint(min_val, max_val)


def main():
    # First task
    print(get_min(), end='\n\n')
    # Second task
    print(func1(), end='\n\n')
    print(func2(1, 2, 3), end='\n\n')
    print(func3(1, 2, c=3, d=2), end='\n\n')
    print(func4(a=None, b=float("-inf")), end='\n\n')
    # Third task
    for _ in range(10):
        print(get_randint(2, 10))


if __name__ == '__main__':
    main()
