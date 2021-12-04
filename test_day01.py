import unittest

from utils import importTXTFile
from day01 import countDepthIncreases

class TestDay01(unittest.TestCase):

    def test_countDepthIncreases(self):
        data = importTXTFile('day01-example.txt', int)
        self.assertEqual(countDepthIncreases(data), 7)

if __name__ == '__main__':
    unittest.main()
