with open("day09-input.txt", "r") as f:
    data = f.readlines()
data = [[int(y) for y in x.strip()] for x in data]


def sumOfTheRiskLevelsOfAllLowPoints(data):
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            v = data[i][j]
            u = 999999999
            d = 999999999
            l = 999999999
            r = 999999999
            if i > 0:
                u = data[i - 1][j]
            if i < len(data) - 1:
                d = data[i + 1][j]
            if j > 0:
                l = data[i][j - 1]
            if j < len(data[i]) - 1:
                r = data[i][j + 1]
            if u > v and d > v and l > v and r > v:
                sum += 1 + data[i][j]
    return sum


# What is the sum of the risk levels of all low points on your heightmap?
print(f"Day09a: {sumOfTheRiskLevelsOfAllLowPoints(data)}")  # 545
#
# print(f"Day09b: {xxx(data)}")  # ???
