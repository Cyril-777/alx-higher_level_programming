#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numo = 0
    deno = 0
    for score, weight in my_list:
        numo += score * weight
        deno += weight
    return (numo / deno)
