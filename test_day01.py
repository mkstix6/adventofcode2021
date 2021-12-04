import unittest

from utils import importTXTFile
from day01 import countDepthIncreases, countDepthIncreasesInThrees

exampledata = importTXTFile('day01-example.txt', int)

class TestDay01(unittest.TestCase):

    def test_countDepthIncreases(self):
        self.assertEqual(countDepthIncreases(exampledata), 7)

    def test_countDepthIncreasesInThrees(self):
        self.assertEqual(countDepthIncreasesInThrees(exampledata), 5)

if __name__ == '__main__':
    unittest.main()
