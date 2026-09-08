import numpy as np
import pandas as pd


def values(func, start, end, step):
    index = np.arange(start, end + step, step)
    return pd.Series(map(func, index), index=index, dtype='float64')


def min_extremum(data):
    return min(data[data == min(data)].index)


def max_extremum(data):
    return max(data[data == max(data)].index)


data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))