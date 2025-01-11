import unittest
import day5

class TestDay5(unittest.TestCase):

    def test_part1(self):
        r = day5.solution(True, "input-test.txt")
        self.assertEqual(r, 143, "result is incorrect")
    
    def test_part2(self):
        r = day5.solution(False, "input-test.txt")
        self.assertEqual(r, 123, "result is incorrect")

if __name__ == '__main__':
    unittest.main()