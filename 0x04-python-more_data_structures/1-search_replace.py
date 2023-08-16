#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new = []
    for mem in my_list:
        if mem == search:
            new.append(replace)
        else:
            new.append(mem)
    return new
