with open("day10-input.txt", "r") as f:
    data = f.readlines()
data = [x.strip() for x in data]

openingChars = ["(", "[", "{", "<"]
closingChars = [")", "]", "}", ">"]
charsMap = {"(": ")", "[": "]", "{": "}", "<": ">"}
autoCompletePoints = {")": 1, "]": 2, "}": 3, ">": 4}


def separateIncompleteCorrupt(data: list[str]) -> tuple[list[str], list[str]]:
    incompleteLines: list[str] = []
    corruptLines: list[str] = []
    for line in data:
        isCorrupt = False
        stack: list[str] = []
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
            incompleteLines.append(line)
    return incompleteLines, corruptLines


# first illegal character
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
def corruptLineScore(line: str) -> tuple[int, str, str]:
    score = 0
    expectedChar = "a"
    badChar = "*"
    stack: list[str] = []
    for char in line:
        if char in openingChars:
            stack.append(char)
        if char in closingChars:
            openedWith: str = stack.pop()
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


def day10a(data: list[str]) -> int:
    corrupt: list[str] = separateIncompleteCorrupt(data)[1]
    scores: list[int] = []
    for line in corrupt:
        scores.append(corruptLineScore(line)[0])
    return sum(scores)


def closingCharacters(line: str) -> str:
    # [({(<(())[]>[[{[]{<()<>> -> }}]])})]
    stack: list[str] = []
    unpaired: list[str] = []
    for char in line:
        if char in charsMap.keys():
            stack.append(charsMap[char])
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                unpaired.append(charsMap[char])
    stack.reverse()
    return "".join(stack)


# for each character, multiply the total score by 5 and
# then increase the total score by the point value given
# for the character in the following table:
# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
def autoCompleteScore(scorestring: str) -> int:
    score: int = 0
    for char in scorestring:
        score *= 5
        score += autoCompletePoints[char]
    return score


def day10b(data: list[str]) -> int:
    incomplete: list[str] = separateIncompleteCorrupt(data)[0]
    scores: list[int] = [
        autoCompleteScore(closingCharacters(line)) for line in incomplete
    ]
    # sort all of the scores and then take the middle score
    scores.sort()
    middleScore: int = scores[len(scores) // 2]
    return middleScore


if __name__ == "__main__":
    # What is the total syntax error score for those errors?
    print(f"Day10a: {day10a(data)}")  # 369105
    # What is the middle autocomplete score?
    print(f"Day10b: {day10b(data)}")  # 3999363569
