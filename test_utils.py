import unittest

from utils import importTXTFile, transpose


class TestUtils(unittest.TestCase):
    def test_importdata(self):
        data = importTXTFile("day01-example.txt", int)
        self.assertListEqual(data, [199, 200, 208, 210, 200, 207, 240, 269, 260, 263])

    def test_transpose(self):
        og = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        transposed = [(0, 1, 2), (0, 1, 2), (0, 1, 2)]
        self.assertEqual(transpose(og), transposed)


if __name__ == "__main__":
    unittest.main()
