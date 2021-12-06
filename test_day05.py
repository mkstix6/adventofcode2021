import unittest

from day05 import (
    ingestInput,
    fieldSize,
    constructEmptyField,
    fieldFromInstructions,
    fieldFromInstructionsWithDiagonals,
    countDoublePlusPoints,
    analyseInputForDoublePoints,
    analyseInputForDoublePointsWithDiagonals,
)

with open("day05-example.txt", "r") as f:
    exampledata = f.readlines()

with open("day05-input.txt", "r") as f:
    realdata = f.readlines()

# fmt:off
exampleInstructionList = [[0,9,5,9],[8,0,0,8],[9,4,3,4],[2,2,2,1],[7,0,7,4],[6,4,2,0],[0,9,2,9],[3,4,1,4],[0,0,8,8],[5,5,8,2]]
exampleFieldLayout = [[0,0,0,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0,0],[0,1,1,2,1,1,1,2,1,1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[2,2,2,1,1,1,0,0,0,0]]
exampleFieldLayoutWithDiagonals = [[1,0,1,0,0,0,0,1,1,0],[0,1,1,1,0,0,0,2,0,0],[0,0,2,0,1,0,1,1,1,0],[0,0,0,1,0,2,0,2,0,0],[0,1,1,2,3,1,3,2,1,1],[0,0,0,1,0,2,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,1,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,1,0],[2,2,2,1,1,1,0,0,0,0]]
# fmt:on


class TestDay05(unittest.TestCase):
    def test_ingestInput(self):
        self.assertEqual(ingestInput(exampledata), exampleInstructionList)

    def test_fieldSize(self):
        self.assertEqual(fieldSize(exampleInstructionList), (10, 10))

    def test_constructEmptyField(self):
        self.assertEqual(constructEmptyField(1, 1), [[0]])
        self.assertEqual(constructEmptyField(2, 2), [[0, 0], [0, 0]])
        self.assertEqual(constructEmptyField(3, 3), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(constructEmptyField(2, 3), [[0, 0], [0, 0], [0, 0]])
        self.assertEqual(constructEmptyField(3, 2), [[0, 0, 0], [0, 0, 0]])

    def test_fieldFromInstructions(self):
        self.assertEqual(
            fieldFromInstructions(exampleInstructionList), exampleFieldLayout
        )

    def test_fieldFromInstructionsWithDiagonals(self):
        self.assertEqual(
            fieldFromInstructionsWithDiagonals(exampleInstructionList),
            exampleFieldLayoutWithDiagonals,
        )

    def test_countDoublePlusPoints(self):
        self.assertEqual(countDoublePlusPoints(exampleFieldLayout), 5)

    def test_analyseInputForDoublePoints(self):
        self.assertEqual(analyseInputForDoublePoints(exampledata), 5)
        self.assertEqual(
            analyseInputForDoublePoints(realdata), 5306
        )  # answer day05a confirmed

    def test_analyseInputForDoublePointsWithDiagonals(self):
        self.assertEqual(analyseInputForDoublePointsWithDiagonals(exampledata), 12)
        self.assertEqual(
            analyseInputForDoublePointsWithDiagonals(realdata), 17787
        )  # answer day05a confirmed


if __name__ == "__main__":
    unittest.main()
