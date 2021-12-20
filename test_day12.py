import unittest

from day12 import day12a, day12b


# fmt:off
exampleInput01 = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']
examplePaths01 = ['start,A,b,A,c,A,end','start,A,b,A,end','start,A,b,end','start,A,c,A,b,A,end','start,A,c,A,b,end','start,A,c,A,end','start,A,end','start,b,A,c,A,end','start,b,A,end','start,b,end']
exampleInput02 = ['dc-end','HN-start','start-kj','dc-start','dc-HN','LN-dc','HN-end','kj-sa','kj-HN','kj-dc']
examplePaths02 = ['start,HN,dc,HN,end','start,HN,dc,HN,kj,HN,end','start,HN,dc,end','start,HN,dc,kj,HN,end','start,HN,end','start,HN,kj,HN,dc,HN,end','start,HN,kj,HN,dc,end','start,HN,kj,HN,end','start,HN,kj,dc,HN,end','start,HN,kj,dc,end','start,dc,HN,end','start,dc,HN,kj,HN,end','start,dc,end','start,dc,kj,HN,end','start,kj,HN,dc,HN,end','start,kj,HN,dc,end','start,kj,HN,end','start,kj,dc,HN,end','start,kj,dc,end']
exampleInput03 = ['fs-end','he-DX','fs-he','start-DX','pj-DX','end-zg','zg-sl','zg-pj','pj-he','RW-he','fs-DX','pj-RW','zg-RW','start-pj','he-WI','zg-he','pj-fs','start-RW']
examplePathCount03 = 226
# fmt:on


class TestDay12(unittest.TestCase):
    def test_day12a(self):
        self.assertEqual(day12a(exampleInput01), len(examplePaths01))
        self.assertEqual(day12a(exampleInput02), len(examplePaths02))
        self.assertEqual(day12a(exampleInput03), examplePathCount03)

    # @unittest.skip("unimplemented")
    # def test_day12b(self):
    #     self.assertEqual(day12b(exampleInput), ???)


if __name__ == "__main__":
    unittest.main()
