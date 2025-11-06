def display(src):
    if isinstance(src, list):
        print_list(src)
    elif isinstance(src, dict):
        print_dict(src)
    else:
        print(src)


def print_list(src):
    for item in src:
        print(item)


def print_dict(src):
    for key, value in src.items():
        print(key, value)
