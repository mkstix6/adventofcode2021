with open("day10-input.txt", "r") as f:
    data = f.readlines()
data = [x.strip() for x in data]

openingChars = ["(", "[", "{", "<"]
closingChars = [")", "]", "}", ">"]


def extractCorruptInput(data):
    goodLines = []
    corruptLines = []
    for line in data:
        isCorrupt = False
        stack = []
        for char in line:
            if char in openingChars:
                stack.append(char)
            if char in closingChars:
                openedWith = stack.pop()
                if openingChars.index(openedWith) != closingChars.index(char):
                    isCorrupt = True
        if isCorrupt:
            corruptLines.append(line)
        else:
            goodLines.append(line)
    return goodLines, corruptLines


# first illegal character
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
def corruptLineScore(line):
    score = 0
    expectedChar = "a"
    badChar = "*"
    stack = []
    for char in line:
        if char in openingChars:
            stack.append(char)
        if char in closingChars:
            openedWith = stack.pop()
            if openingChars.index(openedWith) != closingChars.index(char):
                expectedChar = closingChars[openingChars.index(openedWith)]
                badChar = char
                break
    if badChar == ")":
        score = 3
    if badChar == "]":
        score = 57
    if badChar == "}":
        score = 1197
    if badChar == ">":
        score = 25137
    return score, expectedChar, badChar


def day10a(data):
    good, corrupt = extractCorruptInput(data)
    # scores = [[tuple[0] for tuple in corruptLineScore(line)] for line in corrupt]
    scores = []
    for line in corrupt:
        scores.append(corruptLineScore(line)[0])
    return sum(scores)


if __name__ == "__main__":
    # What is the total syntax error score for those errors?
    print(f"Day10a: {day10a(data)}")  # 369105
    # ###
    # print(f"Day10b: {XXX(data)}")  # ???
