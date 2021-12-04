import unittest

from utils import importTXTFile


class TestUtils(unittest.TestCase):
    def test_importdata(self):
        data = importTXTFile("day01-example.txt", int)
        self.assertListEqual(data, [199, 200, 208, 210, 200, 207, 240, 269, 260, 263])


if __name__ == "__main__":
    unittest.main()
