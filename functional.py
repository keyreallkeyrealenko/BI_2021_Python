def unpack_args(*args):
    """It is a helper function. It finds container in *args and functions.
     And return it as container and args respectively"""
    for arg in args:
        # Find container and functions and assign it to container and args variables respectively
        try:
            iter(arg)
            container = arg
            args = tuple(filter(lambda x: x != arg, args))
        except TypeError:
            continue
    if isinstance(container, dict):
        # If container was a dict type, we have to work with values
        container = container.values()
    return container, args


def sequential_map(*args):
    """This function works with following with built-in containers (tuple,list,dict,set,string).
    It returns a container on which functions were applied one by one in a given order."""
    container, args = unpack_args(*args)
    # Apply functions to container
    for func in args:
        container = list(map(func, container))
    return container


def consensus_filter(*args):
    """This function works with following with built-in containers (tuple,list,dict,set,string).
        It returns a filtered container on which functions were applied one by one in a given order."""
    container, args = unpack_args(*args)
    # Apply functions to container
    for func in args:
        container = list(filter(func, container))
    return container


def red(function, iterable):
    """It is a helper function. It replaces reduce function from functools module(it works a bit slower)"""
    value = iterable[0]
    for element in iterable[1:]:
        value = function(value, element)
    return value


def conditional_reduce(*args):
    """As previous functions first it uses unpack_args function to assign variables correctly.Then it
    filters values of a container and applies the second function to get a result"""
    container, args = unpack_args(*args)
    filtered_container = list(filter(args[0], container))
    result = red(args[1], filtered_container)
    return result


def func_chain(*funcs):
    """This function takes multiple functions as arguments and returns their execution one by one.
       It can take many **args to execute functions on them."""

    def chained(*args):
        for func in funcs:
            args = tuple(func(arg) for arg in args)
        if len(args) == 1:
            args = args[0]
        return args

    return chained


def main():
    pass
    # print(sequential_map())
    # print(consensus_filter())
    # print(conditional_reduce())
    # my_chain = func_chain()
    # print(my_chain())


if __name__ == '__main__':
    main()
