with open("day08-input.txt", "r") as f:
    data = f.readlines()


digitSegmentCounts = {
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
    targets = {
        "1": 2,
        "4": 4,
        "7": 3,
        "8": 7,
    }
    for [input, output] in [
        [y.strip().split(" ") for y in row.split(" | ")] for row in data
    ]:
        # Sort all strings
        input = ["".join(sorted(x)) for x in input]
        output = ["".join(sorted(x)) for x in output]
        charStrings = targets.copy()
        for name, count in charStrings.items():
            for x in input:
                if len(x) == count:
                    charStrings[name] = x
        for x in output:
            if x in charStrings.values():
                total += 1
    return total


# In the output values, how many times do digits 1, 4, 7, or 8 appear?
print(f"Day08a: {countOutputFor1478(data)}")  # 532
# What do you get if you add up all of the output values?
# print(f"Day08b: {PARTB(data)}")  # ???
