import numpy as np


def importTXTFile(filename, dtype=int):
    return np.loadtxt(filename, dtype=dtype).tolist()


def transpose(matrix):
    return list([list(a) for a in zip(*matrix)])
