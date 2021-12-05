from collections import Counter

with open("day03.txt", "r") as f:
    data = f.readlines()


def formatData(data):
    return [[int(y) for y in word.strip()] for word in data]


def transpose(matrix):
    return list(zip(*matrix))


def mostCommonBitNumber(data):
    # format data into lists of integers for later handling
    intLists = formatData(data)
    # transpose
    charAtIndexCollections = transpose(intLists)
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


def powerConsumption(data):
    return int(mostCommonBitNumber(data), 2) * int(leastCommonBitNumber(data), 2)


# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
def o2GeneratorRating(data) -> str:
    index = 0
    ifEqualCountsPerfer = 1
    while len(data) > 1:
        charIndexGroups = transpose(formatData(data))
        mostCommon, countMostCommon = Counter(charIndexGroups[index]).most_common(1)[0]
        # Case: check against equal count
        if countMostCommon == len(charIndexGroups[index]) / 2:
            mostCommon = ifEqualCountsPerfer
        data = [x for x in data if int(x[index]) == mostCommon]
        index += 1
    return data[0].strip()


# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
def co2ScrubberRating(data) -> str:
    index = 0
    ifEqualCountsPerfer = 0
    while len(data) > 1:
        charIndexGroups = transpose(formatData(data))
        leastCommon, countLeastCommon = Counter(charIndexGroups[index]).most_common()[
            -1
        ]
        # Case: check against equal count
        if countLeastCommon == len(charIndexGroups[index]) / 2:
            leastCommon = ifEqualCountsPerfer
        data = [x for x in data if int(x[index]) == leastCommon]
        index += 1
    return data[0].strip()


def lifeSupportRating(data) -> int:
    return int(o2GeneratorRating(data), 2) * int(co2ScrubberRating(data), 2)


print(f"Day03a: {powerConsumption(data)}")
print(f"Day03b: {lifeSupportRating(data)}")
