import unittest

from day02 import submarineDestination, submarineDestinationWithAim

with open("day02-example.txt", "r") as f:
    exampledata = f.readlines()


class TestDay02(unittest.TestCase):
    def test_submarineDestination(self):
        result = submarineDestination(exampledata)
        self.assertEqual(result["horizontal"], 15)
        self.assertEqual(result["depth"], 10)
        self.assertEqual(result["horizontal"] * result["depth"], 150)

    def test_submarineDestinationWithAim(self):
        result = submarineDestinationWithAim(exampledata)
        self.assertEqual(result["horizontal"], 15)
        self.assertEqual(result["depth"], 60)
        self.assertEqual(result["horizontal"] * result["depth"], 900)


if __name__ == "__main__":
    unittest.main()
