from utils import importTXTFile

data = importTXTFile("day01-input.txt", int)


def countDepthIncreases(data):
    count = 0
    current = data[0]
    for x in data:
        if x > current:
            count += 1
        current = x
    return count


def countDepthIncreasesInThrees(data):
    count = 0
    current = data[0] + data[1] + data[2]
    for i, x in enumerate(data):
        if 0 <= i < len(data) - 2:
            windowsum = data[i] + data[i + 1] + data[i + 2]
            if windowsum > current:
                count += 1
            current = windowsum
    return count


print(f"Day01a: {countDepthIncreases(data)}")
print(f"Day01b: {countDepthIncreasesInThrees(data)}")
