import unittest

from day03 import powerConsumption, mostCommonBitNumber, leastCommonBitNumber

with open("day03-example.txt", "r") as f:
    exampledata = f.readlines()

# gamma rate is the binary number 10110, or 22 in decimal
# epsilon rate is 01001, or 9 in decimal
# power consumption, 198


class TestDay03(unittest.TestCase):
    def test_powerConsumption(self):
        self.assertEqual(powerConsumption(exampledata), 198)

    def test_mostCommonBitNumber(self):
        self.assertEqual(mostCommonBitNumber(exampledata), "10110")
        self.assertEqual(int(mostCommonBitNumber(exampledata), 2), 22)

    def test_leastCommonBitNumber(self):
        self.assertEqual(leastCommonBitNumber(exampledata), "01001")
        self.assertEqual(int(leastCommonBitNumber(exampledata), 2), 9)


if __name__ == "__main__":
    unittest.main()
