from inspect import getfullargspec


def arg_tuple(func, *args, **kwargs):
    """Return a normalised tuple of arguments from args and kwargs

    This function checks that `func(*args, **kwargs)` is a valid function call,
    then converts all the non-keyword arguments to keyword arguments.  It then
    discards any supplied arguments that are equal to their default values
    (since they are unnecessary) and finally it sorts the arguments into
    alphabetical order by name.  The arguments are then retuend as a tuple of
    tuples, where each tuple is a pair containing the name of the argument
    followed by the value given.

    If `func` takes a variable number of arguments, any unnamed arguments will
    be included as a list with a name beginning with an asterisk.

    Parameters
    ----------
    func : function
        Function such that `func(*args, **kwargs)` is a valid call.
    args : list
        List of non-keyword arguments to be passed to `func`.
    kwargs : dict
        Dictionary of keyword arguments to be passed to `func`.

    Examples
    --------
    Tuple of arguments to built-in function `len`:

    >>> len('hello world')
    11
    >>> arg_tuple(len, 'hello world')
    (('obj', 'hello world'),)

    Tuple of arguments to user-defined function, with default argument being
    discarded:

    >>> def sum_of_three(x, a, m=2):
    ...     return x + a + m
    >>> sum_of_three(10, m=2, a=15)
    27
    >>> arg_tuple(sum_of_three, 10, m=2, a=15)
    (('a', 15), ('x', 10))

    """

    kwargs = kwargs.copy()

    spec = getfullargspec(func)

    # Check for too many arguments
    if len(args) > len(spec.args):
        if spec.varargs is None:
            func(*args, **kwargs)  # throws TypeError with useful message
        else:
            kwargs['*' + spec.varargs] = args[len(spec.args):]  # add varargs

    # Convert args to kwargs
    kwargs.update(dict(zip(spec.args, args)))

    # Remove any default arguments
    if spec.defaults is not None:
        for (arg, val) in zip(spec.args[-len(spec.defaults):], spec.defaults):
            if kwargs.get(arg) == val:
                kwargs.pop(arg)
    if spec.kwonlydefaults is not None:
        for arg in spec.kwonlydefaults:
            if kwargs.get(arg) == spec.kwonlydefaults[arg]:
                kwargs.pop(arg)

    # Return as a tuple
    out = tuple(sorted(kwargs.items()))
    return out
