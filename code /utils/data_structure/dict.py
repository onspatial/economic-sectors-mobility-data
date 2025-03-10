def get_sliced_list_dict(dict,start,end):
    sliced_dict = {}
    for key in dict:
        sliced_dict[key] = dict[key][start:end]
    return sliced_dict

