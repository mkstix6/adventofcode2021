from collections import Counter

with open("day03.txt", "r") as f:
    data = f.readlines()


def powerConsumption(data):
    return int(mostCommonBitNumber(data), 2) * int(leastCommonBitNumber(data), 2)


def mostCommonBitNumber(data):
    # format data into lists of integers for later handling
    intLists = [[int(y) for y in word.strip()] for word in data]
    # transpose
    charAtIndexCollections = list(zip(*intLists))
    # count most common in each list
    mostCommons = [
        Counter(group).most_common(1)[0][0] for group in charAtIndexCollections
    ]
    # convert to result format
    binaryString = "".join(str(num) for num in mostCommons)
    return binaryString


def leastCommonBitNumber(data):
    mostCommonsBinary = mostCommonBitNumber(data)
    intList = [int(y) for y in mostCommonsBinary]
    leastCommons = [1 if x == 0 else 0 for x in intList]
    # convert to result format
    binaryString = "".join(str(num) for num in leastCommons)
    return binaryString


print(f"Day03a: {powerConsumption(data)}")
