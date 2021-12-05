import re
from functools import reduce
from utils import transpose

with open("day04.txt", "r") as f:
    data = f.readlines()


def extractFullSequence(data):
    return [int(num) for num in data[0].strip().split(",")]


def extractBoards(data):
    boards = []
    for x in range(2, len(data), 6):
        board = []
        for y in range(5):
            board.append([int(num) for num in re.split(" +", data[x + y].strip())])
        boards.append(board)
    return boards


# The score of the winning board can now be calculated.
# Start by finding the sum of all unmarked numbers on that board;
# in this case, the sum is 188.
# Then, multiply that sum by the number that was just called
# when the board won, 24, to get the final score, 188 * 24 = 4512.
def computeScore(board, sequence) -> int:
    # sum of all unmarked numbers on that board
    remainingNums = board.copy()
    remainingNums = reduce(lambda acc, curr: acc + curr, remainingNums)
    for num in sequence:
        if num in remainingNums:
            remainingNums.remove(num)
    remainingSum = sum(remainingNums)
    # the number that was just called
    last = int(sequence[-1])
    return remainingSum * last


def boardHasBingo(board, sequence) -> bool:
    # extract board bingo lines
    lines = []
    for row in board:
        lines.append(list(row))
    transposedBoard = transpose(board)
    for row in transposedBoard:
        lines.append(list(row))
    # cross of sequence numbers in lines
    for num in sequence:
        for line in lines:
            if num in line:
                line.remove(num)
    # examine if any lines have bingo
    for line in lines:
        if len(line) == 0:
            return True
    return False


def checkBoardsForBingo(boards, sequence):
    results = [boardHasBingo(board, sequence) for board in boards]
    if True in results:
        return results.index(True)
    else:
        return False


def findWinningScore(data):
    boards = extractBoards(data)
    sequence = extractFullSequence(data)
    calledNumbers = []
    winBoardIndex = False
    while winBoardIndex is False:
        calledNumbers.append(sequence.pop(0))
        winBoardIndex = checkBoardsForBingo(boards, calledNumbers)
    return computeScore(boards[winBoardIndex], calledNumbers)


def findLastPlaceScore(data):
    boards = extractBoards(data)
    sequence = extractFullSequence(data)
    calledNumbers = []
    winBoardIndex = False
    lastBoard = False
    while len(boards) > 0:
        calledNumbers.append(sequence.pop(0))
        winBoardIndex = checkBoardsForBingo(boards, calledNumbers)
        while winBoardIndex is not False:
            # Remove win board from list
            lastBoard = boards.pop(winBoardIndex)
            # Check if there are any other joint winners this round
            winBoardIndex = checkBoardsForBingo(boards, calledNumbers)
    # Only one board should remain
    return computeScore(lastBoard, calledNumbers)


print(f"Day04a: {findWinningScore(data)}")
print(f"Day04b: {findLastPlaceScore(data)}")
