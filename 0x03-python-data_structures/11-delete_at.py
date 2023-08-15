#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    tmp = []
    tmp.extend(my_list[:idx])
    tmp.extend(my_list[idx + 1:])
    my_list.clear()
    my_list.extend(tmp)
    return my_list
