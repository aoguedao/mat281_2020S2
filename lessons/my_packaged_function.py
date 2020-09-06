import math


def pkg_abs_diff_floor(x, y):
    """ Retorna la diferencia entera entre dos valores."""
    diff = abs(x - y)
    value = math.floor(diff)
    return value