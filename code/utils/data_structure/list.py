import time


def remove(input_list, string):
    for item in input_list:
        if string in item:
            input_list.remove(item)
    return input_list


def get_intersection(input_list1, input_list2, count=False, verbose=False):
    if verbose:
        print(f"input_list1: {input_list1}")
        print(f"input_list2: {input_list2}")
    intersection = []
    input_list2_copy = input_list2.copy()
    for item in input_list1:
        if item in input_list2_copy:
            intersection.append(item)
            input_list2_copy.remove(item)
    if verbose:
        print(f"intersection: {intersection}")
        # print(f'input_list1: {input_list1}')
        # print(f'input_list2: {input_list2}')
        time.sleep(10)
    if (len(input_list2) > 0) and (len(intersection) > 0):
        assert len(input_list2) == len(input_list2_copy) + len(intersection), "Intersection is not correct"
    if count:
        return len(intersection)
    return intersection


def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def shuffle(input_list, seed=None):
    import random

    if seed is not None:
        random.seed(seed)
    random.shuffle(input_list)
    return input_list


def reverse(input_list):
    return input_list[::-1]


def get_section(input_list, section, max_section=10):
    length = len(input_list)
    section_size = length // max_section
    print(f"length: {length} section_size: {section_size}")
    if section == max_section - 1:
        return input_list[section_size * (section - 1) :]
    else:
        return input_list[section_size * (section - 1) : section_size * section]


def merge_lists(list):
    merged_list = []
    for l in list:
        if l is not None:
            merged_list += l
    return merged_list


if __name__ == "__main__":
    input_list1 = ["a", "b", "c", "d", "c"]
    input_list2 = ["j"]  # ['c', 'd', 'e', 'f']
    print(get_intersection(input_list1, input_list2))
    print(input_list1)
    print(input_list2)
