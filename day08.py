from collections import Counter

with open("day08-input.txt", "r") as f:
    data = f.readlines()
data = [x.strip() for x in data]

digitSegmentCounts = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
}


def countOutputFor1478(data):
    total = 0
    uniques = {
        "1": 2,
        "4": 4,
        "7": 3,
        "8": 7,
    }
    # Each row of data extract the input and output parts then sort every string's characters alphabetically
    for [input, output] in [
        [["".join(sorted(z)) for z in x.split(" ")] for x in row.split(" | ")]
        for row in data
    ]:
        charStrings = uniques.copy()
        for name, count in charStrings.items():
            for x in input:
                if len(x) == count:
                    charStrings[name] = x
        for x in output:
            if x in charStrings.values():
                total += 1
    return total


def rowOutputValue(dataRow):
    total = 0
    uniques = {
        "1": 2,
        "4": 4,
        "7": 3,
        "8": 7,
    }
    confirmedNumberStrings = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
    }
    digitSegmentMap = {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
    }
    properDigitSegments = {
        "0": "abcefg",
        "1": "cf",
        "2": "acdeg",
        "3": "acdfg",
        "4": "bcdf",
        "5": "abdfg",
        "6": "abdefg",
        "7": "acf",
        "8": "abcdefg",
        "9": "abcdfg",
    }
    properSegmentOccurrences = {
        "a": 8,
        "b": 6,
        "c": 8,
        "d": 7,
        "e": 4,
        "f": 8,
        "g": 7,
    }
    [input, output] = [x.split(" ") for x in dataRow.split(" | ")]
    # Sort all strings
    input = set(["".join(sorted(x)) for x in input])
    output = ["".join(sorted(x)) for x in output]
    # Find the unique length items
    for name, count in uniques.items():
        for x in input:
            if len(x) == count:
                uniques[name] = x
    confirmedNumberStrings = confirmedNumberStrings | uniques
    # Count up input character occurrence for later
    charsCount = Counter("".join(input))
    # Find segment A
    digitSegmentMap["a"] = list(filter(lambda x: x not in uniques["1"], uniques["7"]))[
        0
    ]
    # Find segment E
    digitSegmentMap["e"] = list(filter(lambda item: item[1] == 4, charsCount.items()))[
        0
    ][0]
    # Find number 9
    confirmedNumberStrings["9"] = "abcdefg".replace(digitSegmentMap["e"], "")
    # Find number 0
    confirmedNumberStrings["0"] = filter(
        lambda sixChars: confirmedNumberStrings["1"],
        filter(lambda item: len(item) == 6, input),
    )
    return total


def sumOutputValues(data):
    total = 0
    for dataRow in data:
        total += rowOutputValue(dataRow)
    return total


# In the output values, how many times do digits 1, 4, 7, or 8 appear?
print(f"Day08a: {countOutputFor1478(data)}")  # 532
# What do you get if you add up all of the output values?
print(f"Day08b: {sumOutputValues(data)}")  # ???
