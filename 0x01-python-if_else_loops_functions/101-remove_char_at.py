#!/usr/bin/python3
def remove_char_at(str, n):
    strt = ""
    i = 0
    for c in str:
        if i != n:
            strt += c
        i += 1
    return strt
