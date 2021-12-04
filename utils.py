import numpy as np

def importTXTFile(filename, dtype=int):
    return np.loadtxt(filename, dtype=dtype).tolist()
