import unittest

from day10 import extractCorruptInput, corruptLineScore, day10a


# fmt:off
exampleInput = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>','(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{','<{([{{}}[<[[[<>{}]]]>[]]']
exampleCorruptLines = ['{([(<{}[<>[]}>{[]{[(<()>','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{']
# fmt:on


class TestDay10(unittest.TestCase):
    def test_extractCorruptInput(self):
        good, corrupt = extractCorruptInput(exampleInput)
        self.assertEqual(corrupt, exampleCorruptLines)

    # @unittest.skip("unimplemented")
    def test_corruptLineScore(self):
        score, expectedChar, badChar = corruptLineScore("{([(<{}[<>[]}>{[]{[(<()>")
        self.assertEqual(score, 1197)
        self.assertEqual(expectedChar, "]")
        self.assertEqual(badChar, "}")
        score, expectedChar, badChar = corruptLineScore("[[<[([]))<([[{}[[()]]]")
        self.assertEqual(score, 3)
        self.assertEqual(expectedChar, "]")
        self.assertEqual(badChar, ")")
        score, expectedChar, badChar = corruptLineScore("[{[{({}]{}}([{[{{{}}([]")
        self.assertEqual(score, 57)
        self.assertEqual(expectedChar, ")")
        self.assertEqual(badChar, "]")
        score, expectedChar, badChar = corruptLineScore("[<(<(<(<{}))><([]([]()")
        self.assertEqual(score, 3)
        self.assertEqual(expectedChar, ">")
        self.assertEqual(badChar, ")")
        score, expectedChar, badChar = corruptLineScore("<{([([[(<>()){}]>(<<{{")
        self.assertEqual(score, 25137)
        self.assertEqual(expectedChar, "]")
        self.assertEqual(badChar, ">")

    def test_day10a(self):
        self.assertEqual(day10a(exampleInput), 26397)


if __name__ == "__main__":
    unittest.main()
