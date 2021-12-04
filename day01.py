import numpy as np
from utils import importTXTFile

data = importTXTFile('day01.txt', int)

def countDepthIncreases(data):
    count = 0
    current = data[0]
    for x in data:
        if x > current:
            count+=1
        current = x
    return count

print (countDepthIncreases(data))
