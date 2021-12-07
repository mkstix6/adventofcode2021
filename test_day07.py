import unittest

from day07 import leastFuel

# fmt:off
exampledata = [16,1,2,0,4,2,7,1,2,14]
# fmt:on
class TestDay07(unittest.TestCase):
    def test_leastFuel(self):
        self.assertEqual(leastFuel(exampledata), 37)


if __name__ == "__main__":
    unittest.main()
