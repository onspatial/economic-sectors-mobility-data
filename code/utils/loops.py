def product(*args):
    args = check_input(*args)
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def check_input(*args):
    output = ()
    for arg in args:
        if type(arg) is not list:
            output += ([arg],)
        else:
            output += (arg,)
    return output
