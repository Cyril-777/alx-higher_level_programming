#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for i, x in a_dictionary.items():
            if x == value:
                del a_dictionary[i]
                break

    return (a_dictionary)
