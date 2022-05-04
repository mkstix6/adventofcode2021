import unittest

from day13 import countDots, fold, day13a, day13b


# fmt:off
# fmt:on


class TestDay13(unittest.TestCase):
    def test_day13a(self):
        self.assertEqual(day13a(exampleInput01), len(examplePaths01))

    def test_fold(self):
        # fmt:off
        coordinates = [(6,10),(0,14),(9,10),(0,3),(10,4),(4,11),(6,0),(6,12),(4,1),(0,13),(10,12),(3,4),(3,0),(8,4),(1,10),(2,14),(8,10),(9,0)]
        inputField = ['...#..#..#.','....#......','...........','#..........','...#....#.#','...........','...........','...........','...........','...........','.#....#.##.','....#......','......#...#','#..........','#.#........']
        expected = ['#.##..#..#.','#...#......','......#...#','#...#......','.#.#..#.###','...........','...........']
        # fmt:on
        instruction = ("y", 7)
        result = fold(coordinates, instruction)
        self.assertEqual(result, expected)

    # @unittest.skip("unimplemented")
    # def test_day13b(self):
    #     self.assertEqual(day13b(exampleInput), ???)


if __name__ == "__main__":
    unittest.main()
