import unittest

from day10 import (
    extractCorruptInput,
    corruptLineScore,
    day10a,
    closingCharacters,
    autoCompleteScore,
    day10b,
)


# fmt:off
exampleInput = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>','(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{','<{([{{}}[<[[[<>{}]]]>[]]']
exampleCorruptLines = ['{([(<{}[<>[]}>{[]{[(<()>','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{']
exampleIncompleteLines = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','(((({<>}<{<{<>}{[]{[]{}','{<[[]]>}<{[{[{[]{()[[[]','<{([{{}}[<[[[<>{}]]]>[]]']
# fmt:on


class TestDay10(unittest.TestCase):
    def test_extractCorruptInput(self):
        incomplete, corrupt = extractCorruptInput(exampleInput)
        self.assertEqual(incomplete, exampleIncompleteLines)
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

    def test_closingCharacters(self):
        self.assertEqual(closingCharacters("[({(<(())[]>[[{[]{<()<>>"), "}}]])})]")
        self.assertEqual(closingCharacters("[(()[<>])]({[<{<<[]>>("), ")}>]})")
        self.assertEqual(closingCharacters("(((({<>}<{<{<>}{[]{[]{}"), "}}>}>))))")
        self.assertEqual(closingCharacters("{<[[]]>}<{[{[{[]{()[[[]"), "]]}}]}]}>")
        self.assertEqual(closingCharacters("<{([{{}}[<[[[<>{}]]]>[]]"), "])}>")

    def test_autoCompleteScore(self):
        self.assertEqual(autoCompleteScore("])}>"), 294)
        self.assertEqual(autoCompleteScore("}}]])})]"), 288957)
        self.assertEqual(autoCompleteScore(")}>]})"), 5566)
        self.assertEqual(autoCompleteScore("}}>}>))))"), 1480781)
        self.assertEqual(autoCompleteScore("]]}}]}]}>"), 995444)
        self.assertEqual(autoCompleteScore("])}>"), 294)

    # @unittest.skip("unimplemented")
    def test_day10b(self):
        self.assertEqual(day10b(exampleInput), 288957)


if __name__ == "__main__":
    unittest.main()
