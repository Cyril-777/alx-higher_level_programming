#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {key: x for key, x in a_dictionary.items() if x != value}
