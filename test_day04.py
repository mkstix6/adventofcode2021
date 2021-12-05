import unittest

from day04 import (
    extractFullSequence,
    extractBoards,
    computeScore,
    boardHasBingo,
    checkBoardsForBingo,
    findWinningScore,
    findLastPlaceScore,
)

with open("day04-example.txt", "r") as f:
    exampledata = f.readlines()

with open("day04.txt", "r") as f:
    realdata = f.readlines()


class TestDay04(unittest.TestCase):
    def test_extractFullSequence(self):
        # fmt:off
        fullSequence = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
        # fmt:on
        self.assertEqual(extractFullSequence(exampledata), fullSequence)

    def test_extractBoards(self):
        # fmt:off
        boards = [[[22, 13, 17, 11, 0],[8, 2, 23, 4, 24],[21, 9, 14, 16, 7],[6, 10, 3, 18, 5],[1, 12, 20, 15, 19]],[[3, 15, 0, 2, 22],[9, 18, 13, 17, 5],[19, 8, 7, 25, 23],[20, 11, 10, 24, 4],[14, 21, 16, 12, 6]],[[14, 21, 17, 24, 4],[10, 16, 15, 9, 19],[18, 8, 23, 26, 20],[22, 11, 13, 6, 5],[2, 0, 12, 3, 7]]]
        # fmt:on
        self.assertEqual(extractBoards(exampledata), boards)

    def test_computeScore01(self):
        # fmt:off
        board = [[1,2,3],[4,5,6],[7,8,9]]
        partialSequence = [1,2,3]
        # fmt:on
        self.assertEqual(computeScore(board, partialSequence), 117)

    def test_computeScore02(self):
        # fmt:off
        board = [[14,21,17,24,4],[10,16,15,9,19],[18,8,23,26,20],[22,11,13,6,5],[2,0,12,3,7]]
        partialSequence = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]
        # fmt:on
        self.assertEqual(computeScore(board, partialSequence), 4512)

    def test_boardHasBingo(self):
        # fmt:off
        board = [[1,2,3],[4,5,6],[7,8,9]]
        partialSequenceA = [1,2,3]
        partialSequenceB = [1,9,3]
        partialSequenceC = [1,4,7]
        partialSequenceD = [1,5,9]
        partialSequenceE = [9,8,7]
        # fmt:on
        self.assertEqual(boardHasBingo(board, partialSequenceA), True)
        self.assertEqual(boardHasBingo(board, partialSequenceB), False)
        self.assertEqual(boardHasBingo(board, partialSequenceC), True)
        self.assertEqual(boardHasBingo(board, partialSequenceD), False)
        self.assertEqual(boardHasBingo(board, partialSequenceE), True)

    def test_checkBoardsForBingoSuccess(self):
        # fmt:off
        boards = [[[22, 13, 17, 11, 0],[8, 2, 23, 4, 24],[21, 9, 14, 16, 7],[6, 10, 3, 18, 5],[1, 12, 20, 15, 19]],[[3, 15, 0, 2, 22],[9, 18, 13, 17, 5],[19, 8, 7, 25, 23],[20, 11, 10, 24, 4],[14, 21, 16, 12, 6]],[[14, 21, 17, 24, 4],[10, 16, 15, 9, 19],[18, 8, 23, 26, 20],[22, 11, 13, 6, 5],[2, 0, 12, 3, 7]]]
        partialSequence = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]
        # fmt:on
        successBoard = checkBoardsForBingo(boards, partialSequence)
        self.assertEqual(successBoard, 2)

    def test_checkBoardsForBingoFail(self):
        # fmt:off
        boards = [[[22, 13, 17, 11, 0],[8, 2, 23, 4, 24],[21, 9, 14, 16, 7],[6, 10, 3, 18, 5],[1, 12, 20, 15, 19]],[[3, 15, 0, 2, 22],[9, 18, 13, 17, 5],[19, 8, 7, 25, 23],[20, 11, 10, 24, 4],[14, 21, 16, 12, 6]],[[14, 21, 17, 24, 4],[10, 16, 15, 9, 19],[18, 8, 23, 26, 20],[22, 11, 13, 6, 5],[2, 0, 12, 3, 7]]]
        partialSequence = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21]
        # fmt:on
        noSuccess = checkBoardsForBingo(boards, partialSequence)
        self.assertEqual(noSuccess, False)

    def test_findWinningScore(self):
        self.assertEqual(findWinningScore(exampledata), 4512)

    def test_findWinningScore_RealAnswer(self):
        self.assertEqual(findWinningScore(realdata), 82440)  # answer day04a confirmed

    def test_findLastPlaceScore(self):
        self.assertEqual(findLastPlaceScore(exampledata), 1924)

    def test_findLastPlaceScore_RealAnswer(self):
        self.assertEqual(findLastPlaceScore(realdata), 20774)  # answer day04b confirmed


if __name__ == "__main__":
    unittest.main()
