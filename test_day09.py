import unittest

from day09 import (
    sumOfTheRiskLevelsOfAllLowPoints,
    multiplyTogetherTheSizesOfTheThreeLargestBasins,
)

# fmt:off
exampleInput = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"
# fmt:on
class TestDay09(unittest.TestCase):
    def test_sumOfTheRiskLevelsOfAllLowPoints(self):
        self.assertEqual(sumOfTheRiskLevelsOfAllLowPoints(exampleInput), 15)

    def test_multiplyTogetherTheSizesOfTheThreeLargestBasins(self):
        self.assertEqual(
            multiplyTogetherTheSizesOfTheThreeLargestBasins(exampleInput), 1134
        )


if __name__ == "__main__":
    unittest.main()
