import unittest

from day03 import (
    formatData,
    transpose,
    mostCommonBitNumber,
    leastCommonBitNumber,
    powerConsumption,
    o2GeneratorRating,
    co2ScrubberRating,
    lifeSupportRating,
)

with open("day03-example.txt", "r") as f:
    exampledata = f.readlines()

# gamma rate is the binary number 10110, or 22 in decimal
# epsilon rate is 01001, or 9 in decimal
# power consumption, 198


class TestDay03(unittest.TestCase):
    def test_formatdata(self):
        # fmt:off
        og1 = ['000','111','222']
        og2 = ['000\n','111\n','222\n']
        formatted = [[0,0,0],[1,1,1],[2,2,2]]
        # fmt:on
        self.assertEqual(formatData(og1), formatted)
        self.assertEqual(formatData(og2), formatted)

    def test_transpose(self):
        og = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        transposed = [(0, 1, 2), (0, 1, 2), (0, 1, 2)]
        self.assertEqual(transpose(og), transposed)

    def test_mostCommonBitNumber(self):
        self.assertEqual(mostCommonBitNumber(exampledata), "10110")
        self.assertEqual(int(mostCommonBitNumber(exampledata), 2), 22)

    def test_leastCommonBitNumber(self):
        self.assertEqual(leastCommonBitNumber(exampledata), "01001")
        self.assertEqual(int(leastCommonBitNumber(exampledata), 2), 9)

    def test_powerConsumption(self):
        self.assertEqual(powerConsumption(exampledata), 198)

    def test_o2GeneratorRating(self):
        self.assertEqual(o2GeneratorRating(exampledata), "10111")
        self.assertEqual(int(o2GeneratorRating(exampledata), 2), 23)

    def test_co2ScrubberRating(self):
        self.assertEqual(co2ScrubberRating(exampledata), "01010")
        self.assertEqual(int(co2ScrubberRating(exampledata), 2), 10)

    def test_lifeSupportRating(self):
        self.assertEqual(lifeSupportRating(exampledata), 230)


if __name__ == "__main__":
    unittest.main()
