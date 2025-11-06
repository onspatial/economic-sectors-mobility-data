import re


def is_match(string, pattern, regex=False):
    if regex:
        return re.match(pattern, string)
    return pattern in string
